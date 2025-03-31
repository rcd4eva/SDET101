import json
import requests
from datetime import datetime
import os,csv


p_data ={"timestamp":"", 
         "temp": 0, "humidity": 0,
         "condition": "",
         "city": "", "country": "",
         "lat":0,"lon":0
         }
dataFile = "weather_data.txt"    
# latitude = 40.74
# longitude = -74.18
t_unit = "imperial"
filename = "weather_data.txt"
apiKey="cd0fba18398a88f25a610b165d6eee59"

p_data["lat"] = 40.74
p_data["lon"] = -74.18

#apiURL = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code&hourly=temperature_2m&temperature_unit={t_unit}&timezone=America%2FNew_York'
apiURL=f'http://api.openweathermap.org/data/2.5/forecast?lat={p_data["lat"]}&lon={p_data["lon"]}&appid={apiKey}&units={t_unit}&cnt=1'
print (apiURL)

weatherData = requests.get(apiURL).json()

if weatherData["cod"] != "200":
    print("Error in API call, please try again later!")
    os.exit(1) #exit gracefully with error code 1

p_data["timestamp"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
p_data["temp"] = weatherData["list"][0]["main"]["temp"]
p_data["humidity"] = weatherData["list"][0]["main"]["humidity"]
p_data["condition"] = weatherData["list"][0]["weather"][0]["description"]
p_data["city"] = weatherData["city"]["name"]
p_data["country"] = weatherData["city"]["country"]

print(p_data)

#if file does not exist, add a header to it 
if not os.path.exists(dataFile):
    with open(dataFile, 'w') as f:
        f.write("Timestamp, Temperature, Humidity, Condition, City, Country\n")

#now append the data to the file
with open(dataFile, 'a') as f:
    #f.write(f"{p_data['timestamp']}, {p_data['temp']}, {p_data['humidity']}, {p_data['condition']}, {p_data['city']}, {p_data['country']}\n")
    f = csv.writer(f)
    f.writerows(p_data)



# with open(filename ="weather_data.txt", 'a') as f:
#     f.write(f"{now:%d-%m-%Y %H:%M:%S} : {weatherData['list'][0]['main']['temp']} : {weatherData['list'][0]['main']['humidity']} : {weatherData['list'][0]['weather'][0]['description']} : {weatherData['city']['name']} : {weatherData['city']['country']}\n")
#     print("Weather data saved")

# currentTemp = str(weatherData["current"]["temperature_2m"])
# timeStamp = str(weatherData["current"]["time"])

# print(f"Testing{currentTemp}")
# # data = {weatherData["current"]["temperature_2m"], weatherData["current"]["time"]}
# # print(data)


# with open(filename, 'a') as f:
#     # Convert json to string and write to file
#     f.write(currentTemp + ":" + timeStamp + '\n')
#     #json.dump(data, f, indent=4) # indent for readability
#     print("Weather data saved")


