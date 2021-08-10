import random
from fileparser import MultipleChoiceQuestion
from random import choice

country_capital_list = {
    "the USA": "Washington, D.C.",
    "Brazil": "Brazilia",
    "China": "Beijing",
    "India": "New Delhi",
    "United Kingdom": "London",
    "Russia": "Moscow",
    "France": "Paris",
    "South Korea": "Seoul",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Iran": "Tehran",
    "Australia": "Canberra",
    "Bosnia and Herzegovina": "Sarajevo",
    "Canada": "Ottawa",
    "Germany": "Berlin",
    "Mexico": "Mexico City",
    "Austria": "Vienna",
    "Philippines": "Manila",
    "Vietnam": "Hanoi",
    "Poland": "Warsaw",
    "Qatar": "Doha",
    "Afghanistan": "Kabul",
    "Thailand": "Bangkok",
    "Egypt": "Cairo",
    "Uruguay": "Montevideo",
    "Lebanon": "Beirut",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "Morocco": "Rabat",
    "Romania": "Bucharest",
    "Nigeria": "Abuja",
    "United Arab Emirates": "Abu Dhabi",
    "Kazakhstan": "Astana",
    "Netherlands": "Amsterdam",
    "Saudi Arabia": "Riyadh",
}


def get_capital_of_country(country_name):
    """Gets the capital of `country_name`."""
    return country_capital_list[country_name]


def capital_question(country):
    """Returns a question about the capital of `country`."""
    capital = get_capital_of_country(country)
    countries = []
    for country1 in country_capital_list.keys():
        if country1 != country:
            countries.append(country1)

    answers = [
        get_capital_of_country(country),
        country_capital_list[choice(countries)],
        country_capital_list[choice(countries)],
        country_capital_list[choice(countries)],
    ]
    return MultipleChoiceQuestion("What is the capital of {}?".format(country), answers)
