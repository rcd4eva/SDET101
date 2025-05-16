import json
import time
import random
from datetime import datetime, timedelta
import paho.mqtt.publish as publish

## MQTT Broker address, hostname or IP address
host = "localhost"  


# Default data template for endurance tests
DEFAULT_DATA = {
    "date": None,
    "fixture": 1,
    "project": 1,
    "eut_type": 1,
    "eut_name": "",
    "op_nbr": 0,
    "op_dir": 1,
    "hh": 0.0,
    "icoil": 0.0,
    "vsrc": 0.0,
    "status": 0,
}

def publish_table(host: str, topic: str, data: dict, client_id: str, retain: bool = False) -> None:
    # Publish a filtered JSON payload of `data` to the specified MQTT `topic` on `host`.
    payload = json.dumps({k: v for k, v in data.items() if v})
    print(f"Publishing to {host} -> {topic}: {payload}")
    try:
        publish.single(
            topic,
            payload,
            hostname=host,
            client_id=client_id,
            qos=2,
            retain=retain
        )
        print(json.dumps(data, indent=4))
        print("Message published successfully!\n")
    except Exception as e:
        print(f"Error publishing to MQTT: {e}\n")


def generate_test_data(host: str, base_current: float, base_voltage: float, base_hh: float, iterations: int = 1, day_offset = 0) :

    #Generate and publish data one art a time
    data = DEFAULT_DATA.copy()
    client_id = "myPC_SDET101"

    for i in range(iterations):
        # Convert curretn date and time to string
        now = datetime.now()
        # Offset the current day by the amount entered
        date_offset = now + timedelta(days=day_offset)
        # And add 30 seconds for each iteration so it is plotted correctly
        data["date"] = (date_offset + timedelta(minutes=i)).strftime('%Y-%m-%d %H:%M:%S')

        # Increment operation count and alternate direction
        data["op_nbr"] += 1
        # Operation Direction is 1 or 2
        data["op_dir"] = (i % 2) + 1

        # Simulate measurements
        data["hh"] = round(base_hh + random.uniform(-5, 5), 1)
        data["icoil"] = round(base_current* random.uniform(1.1, 0.9), 1)
        data["vsrc"] = round(base_voltage + random.uniform(2.1, 5.9), 1)
        data["status"] = 1

        # Debug output of all fields
        for key, value in data.items():
            print(f"{key}: {value}")

        # Publish to MQTT
        publish_table(host, "SDET101/endurance_data", data, client_id)
        # give the mqtt server time before sending the next payload
        time.sleep(0.05)



# Print usage instructions
print("\n---  ---\n")
print("This program simulates an IoT device by generating random endurance test data values and " \
"publishing it into the Alexandria Data Monitoring System using the MQTT protocol.")
# Print instructions and prompt user for base values

print("Please enter initial values without units")
print("values entered will be randomly varied around these base values\n")
print(f"Sending paylod to: {host}")
base_current = float(input("Enter base current (A): "))
base_voltage = float(input("Enter base voltage (V): "))
base_hh = float(input("Enter base transfer speed (ms): "))
iterations = int(input("Enter number of data points to generate: "))
date_offset = int(input("Enter number of days to offset from today (Ex: -10 or +2): "))
print("\nSending data...\n")

generate_test_data(
    host=host,
    base_current=base_current,
    base_voltage=base_voltage,
    base_hh=base_hh,
    iterations=iterations,
    day_offset=date_offset
)




