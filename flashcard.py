import pandas
import random

dataframe = pandas.read_csv("data/french_words.csv")
dictionary = dataframe.to_dict(orient="records")


def get_random_term():
    return random.choice(dictionary)
