# SDET101
  This page you can find all the work I did for the Spring 2025 SDET101 class. 
  But the main attraction is the final project "Alexandri Data Monitring System" Below
## Alexandria Data Monitoring App

### Prerequisites
    
- **Mosquitto Broker:**  
    The app requires an MQTT broker. You can use the public broker at [mosquitto.org](https://test.mosquitto.org/).

- **Database:**  
    The app uses SQLite for portability, but it can be adapted to other databases if needed.

### Setup Instructions

1. **Directory Structure:**  
    Download all the files from the `finalProject` folder. Ensure all files, including the `assets` directory (used by dash-bootstrap-components for custom CSS), are in the same directory.

2. **Create the Database:**  
    Run the `createDB.py` script to set up the necessary tables in the SQLite database:
    Alternatively you can use the already populated "sdet101_test.db"
    make sure to change the 
3. **Start the  MQTT broker:**  
    The app is ocnfigure to use the default port number 1883

3. **Run the MQTT to Databse translator App:** 
    Check that the script's MQTT_SERVER is using the correct ip address.
    Default value is "localhost".
    Also make sure that the "DB_NAME" variable matches the name of sqlite dabase filename that is being used.
    When you are ready, run tbe `serverMQTT2DB.py` script.

3. **Simulate an IoT client and crearte some data:** 
    Check the 'host' variable to match the desired target, default is 'localhost'
    Run tbe `MQTTclient.py` script and follow the terminal isntructions.
    You can also run the client once the system is runnign and watch the real time graph is new data coems on.

3. **Run the App:**  
     Start the Alexandria Data Monitoring App by running the `animeEndurance2.py`.
     The default tcp port is 18080, but you can easily configure it to run at any other.
     Go to `http://localhost:18080`

### Notes

- Update the database configuration if you wish to use a different database type.
- Make sure the Mosquitto broker is accessible before starting the app.
- For more information on Mosquitto, visit [https://mosquitto.org/](https://mosquitto.org/).