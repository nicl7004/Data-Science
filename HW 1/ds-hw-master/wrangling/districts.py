from collections import defaultdict
from csv import DictReader, DictWriter
import csv
import heapq

kHEADER = ["STATE", "DISTRICT", "MARGIN"]

def district_margins(lines):
    """
    Return a dictionary with keys as districts as keys and the difference in
    percentage between the winner and the second-place.
    """


    # Complete this function
    percentages = defaultdict(list)

    return dict((int(x["D"]), 25.0) for x in lines if x["D"] and x["D"] != "H")

def all_states(lines):
    """
    Return all of the states (column "STATE") in list created from a
    CsvReader object.  Don't think too hard on this; it can be written
    in one line of Python.
    """

<<<<<<< HEAD
    # print(lines["STATE"])

    x = [0]*len(lines)
    i = 0

    for row in lines:
        x[i] = row["STATE"]
        i+=1

    x = set(x)
    print (x)
    return set(["Alabama"])
=======
    with open('2014_election_results.csv', 'rb') as csvfile:


    # Complete this function
    # print(lines)
    # x = { lines[3] : lines[3] for each in lines }
    # for each in lines:
    #     x = {
    #     'STATES':
    #     }


    # for i in range(len(lines)):
    #     # if lines[i-1]["STATE"] != (lines[i]["STATE"]) and (lines[i]["STATE"]) != "":
    #     x.append(str(lines[i]["STATE"]))
    #
    #     i+=1

    print(set(x["Alabama"]))


    return set(x["Alabama"])
>>>>>>> ef7b9c03a6c11b734ed8009383061984ef8076a5

def all_state_rows(lines, state):
    """
    Given a list of output from DictReader, filter to the rows from a single state.

    @state Only return lines from this state
    @lines Only return lines from this larger list
    """

    # Complete this function
    for ii in lines:
        yield ii

if __name__ == "__main__":
    # You shouldn't need to modify this part of the code
    lines = list(DictReader(open("data/2014_election_results.csv")))
    output = DictWriter(open("district_margins.csv", 'w'), fieldnames=kHEADER)
    output.writeheader()

    summary = {}
    for state in all_states(lines):
        margins = district_margins([x for x in lines if x["STATE"]==state])

        for ii in margins:
            summary[(state, ii)] = margins[ii]

    for ii, mm in sorted(summary.items(), key=lambda x: x[1]):
        output.writerow({"STATE": ii[0], "DISTRICT": ii[1], "MARGIN": mm})
