import requests
import sqlite3
import pprint
import sys

#### please enter yout api key in the apiKeys.py file
from apiKeys import apiKey

print("\nSDET101-102 HW2 Part 3, Ricardo DaSilveira, UCID:212-05-998, rcd4@njit.edu\n")
#######=======================#####
#######       Question 7      #####
#######=======================#####
print("\nQuestion 7")
print("a. Fetches a random joke using the requests package.")
print("b. Prints the joke setup and punchline.")
print("c. Saves the joke to a text file called jokes.txt.\n")

url="https://official-joke-api.appspot.com/random_joke"
joke = requests.get(url).json() #create joke dictionary
print("Joke :" + joke['setup']) 
print("Punchline :" + joke['punchline'])
try:#catch excpetions
    with open("jokes.txt", "a") as file: #using with to handlew file open and close
        file.write(joke['setup'] + "\n")
        file.write(joke['punchline'] + "\n")
except: #catch exceptions
    print("Error saving to jokes.txt file")


#######=======================#####
#######       Question 8      #####
#######=======================#####
print("\nQuestion 8")
print("a. Fetches data about the latest SpaceX launch.")
print("b. Prints the mission name, launch date, and rocket name.")
print("c. Handles any potential errors in data retrieval.\n")

url ="https://api.spacexdata.com/v5/launches/latest"

try: #error handling
    launch = requests.get(url).json()
except:
    print("Error retrieving SpaceX launch data, please try again later")
else: #only continue if there are no errors
    # The launch dictionary only contains the rocket id, not the name
    # To get the rocket name, we use a differeeent API url
    rocket_url = "https://api.spacexdata.com/v4/rockets/" + launch['rocket']
    try: #error handling
        rocket = requests.get(rocket_url).json() #get rocket data which includes the rocket name
    except:
        print("Error retrieving SpaceX rocket data")
    else:
        print("Mission Name: " + launch['name'])
        print("Launch Date: " + launch['date_local'][:10]) #print only the first 10 characters (only the date)
        print("Rocket Name: " + rocket['name']) #rocket name


#######=======================#####
#######       Question 9      #####
#######=======================#####
print("\nQuestion 9")
print("a. Prompts the user to enter a news topic (e.g., 'technology', 'sports').")
print("b. Retrieves the top 5 headlines related to the topic using the requests package.")
print("c. Stores the headlines, descriptions, and publication dates in an SQLite database.")
print("d. Reads back the data from the database and displays it to the user in a readable format.")
print("e. Ensures that duplicate headlines are not stored in the database.\n")

print("Welcoem to the \"U get what u paid for news\" !")
topics = ["technology", "sports"]
inputMsg = "Please choose between the following topics:\n"

for topic in topics: #use for loop to easily accomodate more topics
    inputMsg += topic + "\n"
inputMsg += "Please enter your choice: "

usrTopic = input(inputMsg) 
while usrTopic not in topics: #keep asking until a valid topic is entered
    print("\nInvalid topic, pleas try again!\n")
    usrTopic = input(inputMsg)

nbr_of_topics = 5 #limit to five articles

#create API url using user input, apiKey and number of topics
url = f"https://newsapi.org/v2/top-headlines?country=us&category={usrTopic}&pageSize={nbr_of_topics}&apiKey={apiKey}"
try:
    news = requests.get(url).json() #get news data   
except: #exit fgacefully if there is an error
    print("There was an error retrieving news data")
    sys.exit(2) #print a different error code to differentiate between the two errors
if news['status'] == "error": #check if there was an error in the API response
    print("News API error: ", news['code'], ": ", news['message'])
    sys.exit(3) #print a different error code to differentiate between the two errors

try:
    with sqlite3.connect("newsorg.db") as cx: #close database automatically when done
        #create table if it does not exist, otherwise do nothing
        cx.execute("CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, headlines TEXT, descriptions TEXT, pub_dates TEXT)")
        cx.commit()
        #check if the headline already exists in the database
        sql_check = "SELECT headlines FROM news WHERE headlines = ?"
        for article in news['articles']: #iterate through the articles
            if cx.execute(sql_check, (article['title'],)).fetchone() is None:
                sql_insert = "INSERT INTO news (headlines, descriptions, pub_dates) VALUES (?, ?, ?)"
                cx.execute(sql_insert,(article['title'], article['description'], article['publishedAt'][:10]))
                cx.commit()
except sqlite3.Error as err:
    print("Database error: ", err)
    sys.exit(4)
else: #read back the data only if there wero no errors
    sql_read = "SELECT * FROM news"
    data = cx.execute(sql_read)
    print("Top Headlines:\n")
    i=1 #counter for the articles
    news_string = "" #string to store the news
    for news in data.fetchall():
        print(f"{i})\tTitle: {news[1]}")
        print(f"\tPublished Date: {news[3]}")
        print(f"\tDescription: {news[2]}\n")
        i+=1
            
