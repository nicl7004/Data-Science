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
    # print(list(rows["D"] for rows in lines))
    # district= []
    # state = []
    # for x in lines:
    #      if x["D"] and x["D"] != "H":
    #          district.append(x["D"])
    #          state.append(x["STATE"])
    #
    #
    # districtState = dict(zip(district,state))
    # # print (districtState['STATE'])
    # # print(districtState)
    # if 'Colorado' in districtState:
    #     print(key, "that is the key fam")
        # print(rows["DISTRICT"])

    #

    # Complete this function

    percentages = defaultdict(list)
    print(lines)
    return dict((int(x["D"]), 25.0) for x in lines if x["D"] and x["D"] != "H")

def all_states(lines):
    """
    Return all of the states (column "STATE") in list created from a
    CsvReader object.  Don't think too hard on this; it can be written
    in one line of Python.
    """
    return set(list(rows["STATE"] for rows in lines if rows["STATE"]))
    # return list(["Alabama"])

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
