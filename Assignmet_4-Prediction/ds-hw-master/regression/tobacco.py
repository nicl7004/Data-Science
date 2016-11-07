import pandas
from math import isnan

def filterTobacco(fileA):
    tobacco = pandas.read_csv(fileA)
    dictTob = {}

    for intEach, each in enumerate(tobacco["STATE"]):
        each = str(each)
        each = each.replace(" ", "")

        if each == "US": #filter out US because its not a state
            continue

        try:
            print(each, (tobacco["STATE"][intEach+1]))
            if each != str(tobacco["STATE"][intEach+1].replace(" ", "")) and intEach >=1:
                print(each, (tobacco["STATE"][intEach+1]), "hererehrehrherhe")

                dictTob[each] = tobacco["MEAN"][intEach]




        except KeyError:
            continue
        except AttributeError:
            continue

    #remove the first element because it is nan




    return dictTob



if __name__ == '__main__':
    y = filterTobacco('tobacco_sales.csv')
