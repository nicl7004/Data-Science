from csv import DictReader #dictreader is nice because you can reference by name and not just index
import csv


votes = list(DictReader(open("2012pres.csv"), delimiter=";"))
#
# for each in votes:
#     if votes["FIRST"]["Total State Votes:"]:
#         x = x + votes["PARTY"]
# print(x)

total_votes = sum(int(x["TOTAL VOTES #"].replace(".", "")) \
for x in votes if x["TOTAL VOTES #"])

print(total_votes)
# Look up list comprehensions
# better way to write a for loop

#find the largest margin between parties in each state
a=0
with open('2012pres.csv', 'rt') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        # print(row)
        if row[9] == "R":
            print ("in if")
            print(row[11])
            print(row)
            print(row[9])
            x = row[10].replace(".", "").replace("[","").replace("]","")
            row = next(spamreader)
            y = row[10].replace(".", "").replace("[","").replace("]","")
            x = float(x)
            y = float(y)
            print("R =", x, "D =", y)
            diff = abs(x-y)
            if diff > a:
                a = diff
                print(a)
print(a)