import requests
import json
import sqlite3

# Define the URL for the api you want to hit
useless_facts_url = "https://uselessfacts.jsph.pl/api/v2/facts/random"


# Function to fetch data from url
def get_api_data(url):

    # Make the HTTP request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the JSON response
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None


# Function to write data to text file
def write_data_to_file(data, filename):

    # Open the file in write mode
    with open(filename, 'w') as f:

        # Convert json to string and write to file
        json.dump(data, f, indent=4) # indent for readability
        print("Random fact written to",filename)


# Example usage
random_fact = get_api_data(useless_facts_url)
write_data_to_file(random_fact, "random_fact.txt")

# Function to read response from text file and parse as dictionary
def read_data_from_file(filename):

    # Open the file in read mode
    with open(filename, "r") as f:

        # Read the file content
        data = json.load(f)
        return data

# Example usage
fact_data = read_data_from_file('random_fact.txt')

# Print all the fields from the dictionary
print("Fact ID:", fact_data["id"])
print("Fact Text:", fact_data["text"])
print("Source:", fact_data["source"])
print("Source URL:", fact_data["source_url"])
print("Language:", fact_data["language"])
print("Permalink:", fact_data["permalink"])