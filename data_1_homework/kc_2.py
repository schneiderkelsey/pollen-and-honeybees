import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

dataframe = pd.read_csv("assets/deadbees.csv")

dead = dataframe["dead"]
year = pd.to_datetime(dataframe["year"], errors = "coerce")


plt.plot(dead, year, marker="^")

plt.show()