import json
import sqlite3
import sys
import paho.mqtt.client as mqtt

#this script subscribes to an MQTT topic and inserts the received data 
#into an SQLlite databse

# Configuration constants
MQTT_SERVER = "localhost"                   # MQTT broker address
MQTT_TOPIC = "SDET101/endurance_data"      # Topic to subscribe to
DB_NAME = "sdet101_test.db"          # SQLite database file or path
VALID_TABLES = {"endurance_data"}           # Check to make sure the we are usign the correct databse


def connect_db(db_name):
    # Connect to an SQLite database and return the connection.
    # Exits on failure with an error message.
    try:
        conn = sqlite3.connect(db_name)
        print("Connected to database '{}'".format(db_name))
        return conn
    except sqlite3.Error as err:
        print("Error connecting to database '{}': {}".format(db_name, err))
        sys.exit(1)


def insert_db_data(conn, table, data):
    # Insert non-None values from `data` dict into `table`.
    # Builds a parameterized INSERT statement dynamically.
    # Prepare column names, placeholders, and values
    columns = []
    placeholders = []
    values = []
    for key, val in data.items():
        if val is not None:
            columns.append(key)
            placeholders.append("?")
            values.append(val)

    # Construct the SQL INSERT statement
    sql = "INSERT INTO {} ({}) VALUES ({})".format(
        table,
        ", ".join(columns),
        ", ".join(placeholders)
    )
    print("Executing SQL: {}\nWith values: {}".format(sql, values))

    try:
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
    except sqlite3.Error as err:
        print("Error inserting into '{}': {}".format(table, err))
    finally:
        cursor.close()


def on_message(client, userdata, msg):
    # Callback for MQTT messages: parse JSON and insert into DB if table valid.
    payload = msg.payload.decode('utf-8')
    table = msg.topic.rpartition('/')[-1]

    # Attempt to parse JSON payload
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as err:
        print("Invalid JSON payload: {}".format(err))
        return

    # Only process known tables
    if table in VALID_TABLES:
        print("Received data for '{}': {}".format(table, data))
        insert_db_data(userdata['db_conn'], table, data)
    else:
        print("Ignoring message for invalid table '{}'".format(table))


# Connect to SQLite database
conn = connect_db(DB_NAME)

# Set up MQTT client; store DB connection in userdata for callbacks
client = mqtt.Client(userdata={'db_conn': conn})
client.on_message = on_message

# Connect to broker and subscribe to topic
print("Connecting to MQTT broker '{}'...".format(MQTT_SERVER))
client.connect(MQTT_SERVER)
client.subscribe(MQTT_TOPIC, qos=2)
print("Subscribed to topic '{}'. Waiting for messages...\n".format(MQTT_TOPIC))

# Start the blocking loop and listen indefinitely for messages
client.loop_forever()



