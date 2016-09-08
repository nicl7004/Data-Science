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
    x = []
    # print(zip_file)
    # extract zipfile
    with ZipFile(zip_file, 'r') as myzip:
        # use namelist to get an object we can read
        for each in myzip.namelist():
            # read data
            data=myzip.read(each)
            data = data.decode('utf-8', 'replace') #decode and yield
            for y in data.split(' '):
                yield(y)

def words(text):
    """
    Return all words in a string, where a word is four or more contiguous
    characters in the range a-z or A-Z.  The resulting words should be
    lower case.
    """
    # Modify this function
    # set pattern using regex compiler
    pattern = re.compile("[a-z]{4,}")
    text = text.lower()#lowercase everything
    result = (pattern.findall(text))
    # print (result)

    return result

def accumulate_counts(words, total=Counter()):
    """
    Take an iterator over words, add the sum to the total, and return the
    total.

    @words An iterable object that contains the words in a document
    @total The total counter we should add the counts to
    """
    assert isinstance(total, Counter)
    theList = {}
# iterate through words and increment the total associated with the word
    for word in words:
        if word in total:
            total[word] +=1
        else:
            total[word] = 1
    return total

if __name__ == "__main__":
    # You should not need to modify this part of the code
    total = Counter()
    for tt in text_from_zipfile("data/state_union.zip"):
        total = accumulate_counts(words(tt), total)

    for ii, cc in total.most_common(100):
        print("%s\t%i" % (ii, cc))
