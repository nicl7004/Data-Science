import pandas
from math import isnan

def filterTobacco(fileA):
    tobacco = pandas.read_csv(fileA)

    ddict = {}

    for intEach, each in enumerate(tobacco["STATE"]):
        each = str(each)
        each = each.replace(" ", "")

        if each == "US": #filter out US because its not a state
            continue

        try:

            if each != str(tobacco["STATE"][intEach+1].replace(" ", "")) and intEach >=1:
                ddict[each] = tobacco["MEAN"][intEach]

        except KeyError:
            continue
        except AttributeError:
            continue

    dictTob = pandas.DataFrame(list(ddict.items()),columns =["STATE", "MEAN"])

    return dictTob



if __name__ == '__main__':
    y = filterTobacco('tobacco_sales.csv')
