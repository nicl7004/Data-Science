from collections import Counter
from zipfile import ZipFile
import re

kWORDS = re.compile("[a-z]{4,}")

def text_from_zipfile(zip_file):
    # Modify this function
    tex = list()
    with ZipFile(zip_file) as z:
        for name in z.namelist():
            with z.open(name) as f:
                for line in f:
                    linestr = line.decode("ISO-8859-1")
                    line_split = linestr.split()
                    for word in line_split:
                        tex.append(word)
    return tex

def words(text):
    text = text.replace(",","")
    text = text.replace(".","")
    text = text.replace("?","")
    text = text.replace(";","")
    text = text.replace(":","")
    text = text.replace("-","")
    text = text.lower()
    if(len(text) > 3):
        return (text)
    else:
        return 0

def accumulate_counts(words, total=Counter()):
    assert isinstance(total, Counter)
    #newList = dict()
    if (words != 0):
        if words in total:
            total[words] += 1
        else:
            total[words] = 1

    # Modify this function
    return total

if __name__ == "__main__":
    # You should not need to modify this part of the code
    total = Counter()
    for tt in text_from_zipfile("./data/state_union.zip"):
        total = accumulate_counts(words(tt), total)

    for ii, cc in total.most_common(100):
        print("%s\t%i" % (ii, cc))
