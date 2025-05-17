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
    Download all the entire **`finalProject`** folder. Ensure all files, including the **`assets`** directory (used by dash to load custom .css), are in the same directory.

2. **Install Python Dependencies:**  
    The **`requirements.txt`** inside the project's folder contains the required python libraries.

2. **Create the Database:**  
    Run the **`createDB.py`** script to create the sqlite database file and populate it with the necessary tables.
    Alternatively you can use the already populated "sdet101_test.db" that comes with the project.

3. **Start the  MQTT broker:**  
    The broker should be configured to use the default port number 1883 and allow anonymous login or use sockets for authentication.

4. **Run the MQTT to Databse translator App:** 
    Check that the script's **MQTT_SERVER** variable is using the correct ip address.
    Default value is "localhost".
    Also make sure that the **DB_NAME** variable matches the name of sqlite dabase filename that is being used.
    When you are ready, run tbe **`serverMQTT2DB.py`** script.

5. **Simulate an IoT client and crearte some data:** 
    Check the **'host'** variable to match the desired target, default is 'localhost'
    Run tbe **`MQTTclient.py`** script and follow the terminal isntructions.
    You can also run the client once the system is runnign and watch the real time graph is new data coems on.

6. **Run the App:**  
     Start the Alexandria Data Monitoring App by running the **`animeEndurance2.py`**.
     The default tcp port is **18080**, but you can easily configure it to run at any other.
     Finally, go to **`http://localhost:18080`**

### Notes

- A report on the challenges of creating the system can be found [here](./finalProject/A_guide_to_Alexandria.docx)
- An overview video of features and how to use is [here](https://www.youtube.com/watch?v=IrPf0yzfNSg)
- Update the database configuration if you wish to use a different database type.
- Make sure the Mosquitto broker is accessible before starting the app.
- For more information on Mosquitto, visit [https://mosquitto.org/](https://mosquitto.org/).