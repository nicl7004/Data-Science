from collections import Counter
from zipfile import ZipFile
import re
import os

kWORDS = re.compile("[a-z]{4,}")

def text_from_zipfile(zip_file):
    """
    Given a zip file, yield an iterator over the text in each file in the
    zip file.
    """
    print(zip_file)
    with ZipFile(zip_file, 'r') as myzip:
        info=myzip.infolist()
        # print (info)
        for each in info:
            data = each.read()
            print(each)
        # with ZipFile(myzip, 'r')as myNewZip:
        #     print(myNewZip)


        # for each in myzip.namelist():
        #     if each != "state_union/":
        #         # y = ZipFile(each)
        #         remove = re.sub("^.{12,}", '', each)
        #         print(remove)
        #         print (each)
                # ZipFile.read(each)
                # x = ZipFile.read(each)
            #     while True:
            #         # yield(x.readline())
            # else:
            #     break
	  #  yield(each)
        # print(myzip.namelist())
    # for fn in os.listdir(/home/user/Desktop/Data_Sci/Data-Science/HW 1/ds-hw-master/wrangling/data/state_union.zip):
    #     if os.path.isfile(fn):
    #         print (fn)



    # Modify this function


def words(text):
    """
    Return all words in a string, where a word is four or more contiguous
    characters in the range a-z or A-Z.  The resulting words should be
    lower case.
    """
    # Modify this function
    return text.lower().split()

def accumulate_counts(words, total=Counter()):
    """
    Take an iterator over words, add the sum to the total, and return the
    total.

    @words An iterable object that contains the words in a document
    @total The total counter we should add the counts to
    """
    assert isinstance(total, Counter)

    # Modify this function
    return total

if __name__ == "__main__":
    # You should not need to modify this part of the code
    total = Counter()
    for tt in text_from_zipfile("data/state_union.zip"):
        total = accumulate_counts(words(tt), total)

    for ii, cc in total.most_common(100):
        print("%s\t%i" % (ii, cc))
