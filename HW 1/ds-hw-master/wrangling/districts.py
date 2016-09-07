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

    # Complete this function
    x = []
    y = []
    for rows in state_lines:
        if rows["D"] and rows["GENERAL %"] and rows["D"] != "H" and rows["D"] != " - ":
            x.append(rows["D"])
            y.append(rows["GENERAL %"])
    # print(x, y)
    new_dict={}
    for each in range(len(x)):
         new_dict[x[each]] = y[each]
    print (new_dict)

    return dict((int(x["D"]), 25.0) for x in state_lines if x["D"] and
                not (x["D"] == "H" or " - " in x["D"]))

def all_states(lines):
    """
    Return all of the states (column "STATE") in list created from a
    CsvReader object.  Don't think too hard on this; it can be written
    in one line of Python.
    """

    # Complete this function

    return set(list(rows["STATE"] for rows in lines if rows["STATE"]))

def all_state_rows(lines, state):
    """
    Given a list of output from DictReader, filter to the rows from a single state.
    @state Only return lines from this state
    @lines Only return lines from this larger list
    """

    # Complete/correct this function
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
