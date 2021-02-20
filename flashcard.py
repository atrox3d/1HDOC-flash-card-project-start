import pandas
import random

FR = "French"
EN = "English"

dataframe = pandas.read_csv("data/french_words.csv")
cards = dataframe.to_dict(orient="records")


def next_card():
    return random.choice(cards)
