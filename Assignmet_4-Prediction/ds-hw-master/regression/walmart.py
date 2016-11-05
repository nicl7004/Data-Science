import pandas


def replaceState(dictA, fileA):
    walmart_data = pandas.read_csv(fileA)
    statedict = {}

    for k,v in dictA.items():
        statedict[v] = k

#get rid of words after the int
    for intEach, each in enumerate(walmart_data['NUMBER']):
        walmart_data['NUMBER'][intEach] = each.replace("per 1 million people", "")

#change state names to symbols
    for intEach, each in enumerate(walmart_data['STATE']):
        walmart_data['STATE'][intEach] = each = each.replace(":","")

        if each in statedict:
            walmart_data['STATE'][intEach] = statedict[each]

    return(walmart_data)






if __name__ == "__main__":

    replaceState(states, "walmart.csv")
