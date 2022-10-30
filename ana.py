import pandas as pd
import numpy as np


def patates():
    print("Hello world!!")

    domates = {
        "1": "1",
        "2": "2",
    }

    population_dict = {
        "California": 38332521,
        "Texas": 2644,
        "New York": 19,
        "Florida": 19552860,
        "Illinois": 12882135,
    }
    population = pd.Series(population_dict)
    population


if __name__ == "__main__":
    patates()
