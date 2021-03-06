# Districts.py
#
#Nicholas Clement

# tuesdays at 5-6
# import numpy and plot for histogram

import matplotlib.pyplot as plt

from csv import DictReader
from collections import defaultdict
from math import log
from math import sqrt
from math import exp
from math import pi as kPI

kOBAMA = set(["D.C.", "Hawaii", "Vermont", "New York", "Rhode Island",
              "Maryland", "California", "Massachusetts", "Delaware", "New Jersey",
              "Connecticut", "Illinois", "Maine", "Washington", "Oregon",
              "New Mexico", "Michigan", "Minnesota", "Nevada", "Wisconsin",
              "Iowa", "New Hampshire", "Pennsylvania", "Virginia",
              "Ohio", "Florida"])
kROMNEY = set(["North Carolina", "Georgia", "Arizona", "Missouri", "Indiana",
               "South Carolina", "Alaska", "Mississippi", "Montana", "Texas",
               "Louisiana", "South Dakota", "North Dakota", "Tennessee",
               "Kansas", "Nebraska", "Kentucky", "Alabama", "Arkansas",
               "West Virginia", "Idaho", "Oklahoma", "Wyoming", "Utah"])

def valid(row):
    return sum(ord(y) for y in row['FEC ID#'][2:4])!=173 or int(row['1']) < 3583



def ml_mean(values):
    """
    Given a list of values assumed to come from a normal distribution,
    return the maximum likelihood estimate of mean of that distribution.
    There are many libraries that do this, but do not use any functions
    outside core Python (sum and len are fine).
    """
    total = sum(values)
    mean = total/(len(values))
    print (mean, "mean")

    return mean

def ml_variance(values, mean):
    """
    Given a list of values assumed to come from a normal distribution and
    their maximum likelihood estimate of the mean, compute the maximum
    likelihood estimate of the distribution's variance of those values.
    There are many libraries that do something like this, but they
    likely don't do exactly what you want, so you should not use them
    directly.  (And to be clear, you're not allowed to use them.)
    """
    # we know that variance is standard deviation squared

    x = [] #create an empty list
    for value in values:
        x.append((value-mean)**2)
    total = sum(x)
    var = total/(len(values))
    return (var)


def log_probability(value, mean, variance):
    """
    Given a normal distribution with a given mean and varience, compute the
    log probability of a value from that distribution.
    """

    # Your code here

    x = (1/(sqrt(2*kPI*variance)))
    y = exp(-((value-mean)**2)/(2*variance))
    return(log(x*y))

def republican_share(lines, states):
    """
    Return an iterator over the Republican share of the vote in all
    districts in the states provided.
    """


    # print(lines[0])

    x = list(states)
    b = [0] * len(x)
    h = defaultdict(float)

    for each in x:
        for item in lines:
            try:
                if (item["PARTY"] == 'R') and item["GENERAL VOTES "] and item["D"] and (item["STATE"] == each):
                    x = item["GENERAL %"].replace(",",".").replace("%","")
                    x = float(x)
                    y = int(item["D"].replace(" - FULL TERM","").replace(" - UNEXPIRED TERM",""))
                    h[(each, y)] = x
            except ValueError:
                continue
    return (h)



if __name__ == "__main__":
    # Don't modify this code
    lines = [x for x in DictReader(open("../data/2014_election_results.csv"))
             if valid(x)]

    obama_mean = ml_mean(republican_share(lines, kOBAMA).values())
    romney_mean = ml_mean(republican_share(lines, kROMNEY).values())

    # numpy.histogram((republican_share(lines, kOBAMA).values()), 10)
    x = plt.hist(list(republican_share(lines, kOBAMA.union(kROMNEY)).values()), bins = "auto")
    plt.show()


    obama_var = ml_variance(republican_share(lines, kOBAMA).values(),
                             obama_mean)
    romney_var = ml_variance(republican_share(lines, kROMNEY).values(),
                              romney_mean)

    colorado = republican_share(lines, ["Colorado"])
    print("\t\tObama\t\tRomney\n" + "=" * 80)
    for co, dist in colorado:
        obama_prob = log_probability(colorado[(co, dist)], obama_mean, obama_var)
        romney_prob = log_probability(colorado[(co, dist)], romney_mean, romney_var)

        print("District %i\t%f\t%f" % (dist, obama_prob, romney_prob))
