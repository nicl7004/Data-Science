from collections import defaultdict
from csv import DictReader, DictWriter
import heapq

kHEADER = ["STATE", "DISTRICT", "MARGIN"]

def district_margins(state_lines):
    """
    Return a dictionary with districts as keys, and the difference in
    percentage between the winner and the second-place as values.
    @lines The csv rows that correspond to the districts of a single state
    """


    percentages = {}
    districts = set(x["D"] for x in lines if x["D"] and x["D"] != "H")
    for dicts in districts:
        newList = []
        for each in lines:
            if (each["D"] == dicts):
                each["D"] = each["D"].split("-")[0]
# parse the percent column and throw values in a list
#then take list values and throw them in a dict
                if (each["GENERAL %"]):
                    par = each["GENERAL %"].replace(",", '.') #parse and replace
                    par = float(par.replace("%",'')) #parse and replace again
                    newList.append(par)
                    percentages[int(each["D"])] = newList
# find the top percentages by iterating through the districts
#find and remove the largest percent and repeat the process to find the next largest percent
# subtract secondplace from first and get the margin
    for dicts in percentages:
        if (percentages[dicts]):
            if (len(percentages[dicts]) > 1):
                biggest = max(percentages[dicts])
                percentages[dicts].remove(biggest)
                secondBiggest = max(percentages[dicts])
                percentages[dicts] = biggest - secondBiggest
            else:
                percentages[dicts] = float(percentages[dicts][0])

    return percentages


def all_states(lines):
    """
    Return all of the states (column "STATE") in list created from a
    CsvReader object.  Don't think too hard on this; it can be written
    in one line of Python.
    """

    #  Complete this function
    # iterate through lines and return a set (no repeats) of all states

    return set(list(rows["STATE"] for rows in lines if rows["STATE"]))

def all_state_rows(lines, state):
    """
    Given a list of output from DictReader, filter to the rows from a single state.
    @state Only return lines from this state
    @lines Only return lines from this larger list
    """

    #  Complete/correct this function

    for ii in lines:
        yield ii

if __name__ == "__main__":
    # You shouldn't need to modify this part of the code
    lines = list(DictReader(open("./data/2014_election_results.csv")))
    output = DictWriter(open("district_margins.csv", 'w'), fieldnames=kHEADER)
    output.writeheader()

    summary = {}
    for state in all_states(lines):
        margins = district_margins(all_state_rows(lines, state))

        for ii in margins:
            summary[(state, ii)] = margins[ii]

    for ii, mm in sorted(summary.items(), key=lambda x: x[1]):
        output.writerow({"STATE": ii[0], "DISTRICT": ii[1], "MARGIN": mm})
