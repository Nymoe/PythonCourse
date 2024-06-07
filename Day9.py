#Dictionary
# a list of keys and values assigned to them

age = {"X": 55,
       "Y": 74,
       "Z": 23
}

#To fetch an element or a value, you need the key
# print(age["X"])

#To add an element to the dictionary
age["B"] = 99

# print(age)

#To edit a dictionary

age["B"] = 20

#To loop in a dictionary - It allows the user to get all the keys not the values

# for key in age:
#     print(key)

#To empty a dictionary
age = {}

#Exemple

# travel_log = [
#     {
#         "country" : "France",
#         "cities_visited" : ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# ]
#
# for country in travel_log:
#     print(country["cities_visited"])

country = input("Country\n")  # Add country name
visits = int(input("Visits\n"))  # Number of visits
list_of_cities = eval(input("Cities\n"))  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(country, visits, list_of_cities):
  travel_log.append({'country': country, 'visits': visits, 'cities':list_of_cities}) #The method append is used because travel_log is a list/For a dictionary, update could be used instead

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['cities']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")
