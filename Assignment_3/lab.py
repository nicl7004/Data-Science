# read in csv list

import pandas as pd
from numpy import mean
from numpy import var

mpg = pd.read_csv("data/jp-us-mpg.dat", delim_whitespace=True)
print(mpg.head())

japan = mean(mpg["Japan"].dropna())
us = mean(mpg["US"].dropna())

japanList = mpg["Japan"].dropna()
usList = mpg["US"].dropna()

print("Japs =", japan, "US =", us) #print means

japan_varience = var(japanList) * len(japanList)/ float(len(japanList)-1)
us_varience = var(usList) * len(usList) / float(len(usList)-1)

print("Japs varience =", japan_varience, "US varience =", us_varience)
