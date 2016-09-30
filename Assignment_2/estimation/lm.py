from math import log, exp
import random
# Nicholas Clement
from collections import defaultdict, Counter
from zipfile import ZipFile
import re

kNEG_INF = -1e6

kSTART = "<s>"
kEND = "</s>"

kWORDS = re.compile("[a-z]{1,}")
kREP = set(["Bush", "GWBush", "Eisenhower", "Ford", "Nixon", "Reagan"])
kDEM = set(["Carter", "Clinton", "Truman", "Johnson", "Kennedy"])

class OutOfVocab(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def sentences_from_zipfile(zip_file, filter_presidents):
    """
    Given a zip file, yield an iterator over the lines in each file in the
    zip file.
    """
    with ZipFile(zip_file) as z:
        for ii in z.namelist():
            try:
                pres = ii.replace(".txt", "").replace("state_union/", "").split("-")[1]
            except IndexError:
                continue

            if pres in filter_presidents:
                for jj in z.read(ii).decode(errors='replace').split("\n")[3:]:
                    yield jj.lower()

def tokenize(sentence):
    """
    Given a sentence, return a list of all the words in the sentence.
    """

    return kWORDS.findall(sentence.lower())

def bigrams(sentence):
    """
    Given a sentence, generate all bigrams in the sentence.
    """

    for ii, ww in enumerate(sentence[:-1]):
        yield ww, sentence[ii + 1]




class BigramLanguageModel:

    def __init__(self):
        self._vocab = set([kSTART, kEND])
        self._everything = {}
        self._bigramEverything = {}
        self._vocab_final = False

    def train_seen(self, word):
        """
        Tells the language model that a word has been seen.  This
        will be used to build the final vocabulary.
        """
        assert not self._vocab_final, \
            "Trying to add new words to finalized vocab"
        self._vocab.add(word)
        try:
            self._everything[word] +=1
        except KeyError:
            self._everything[word] = 1

    def generate(self, context):
        """
        Given the previous word of a context, generate a next word from its
        conditional language model probability.
        """

        # Add your code here.  Make sure to the account for the case
        # of a context you haven't seen before and Don't forget the
        # smoothing "+1" term while sampling.
        # fetch words related to context
        # generate random number as threshold
        # between 0 and 1
        # divide probability of that word with that context
        # check if normalized value crosses threshold of random value

        number = random.uniform(0,1)

        occurances = 0


        for context, word in self._bigramEverything:
            # print (-self.laplace(context,word))
            prob = exp(-self.laplace(context, word))
            # print(prob)
            if (prob > number):
                return word
            else: #increment prob
                prob += prob

    def sample(self, sample_size):
        """
        Generate an English-like string from a language model of a specified
        length (plus start and end tags).
        """

        # You should not need to modify this function
        yield kSTART
        next = kSTART
        for ii in range(sample_size):
            next = self.generate(next)
            if next == kEND:
                break
            else:
                yield next
        yield kEND

    def finalize(self):
        """
        Fixes the vocabulary as static, prevents keeping additional vocab from
        being added
        """

        # you should not need to modify this function

        self._vocab_final = True

    def tokenize_and_censor(self, sentence):
        """
        Given a sentence, yields a sentence suitable for training or testing.
        Prefix the sentence with <s>, generate the words in the
        sentence, and end the sentence with </s>.
        """
        # you should not need to modify this function

        yield kSTART
        for ii in tokenize(sentence):
            if ii not in self._vocab:
                raise OutOfVocab(ii)
            yield ii
        yield kEND

    def vocab(self):
        """
        Returns the language model's vocabulary
        """

        assert self._vocab_final, "Vocab not finalized"
        return list(sorted(self._vocab))

    def laplace(self, context, word):
        """
        Return the log probability (base e) of a word given its context
        """
        try:
            self._bigramEverything[context,word]
        except KeyError:
            self._bigramEverything[context,word] = 0
        try:
            self._everything[context]
        except KeyError:
            self._everything[context] = 0
            # above is for the edge case of there not existing the given context or word meaning it hasnt occured (possible empty sentence)
        numerator = self._bigramEverything[context,word]+1
        denom = (self._everything[context]+len(self._vocab))
        prob = numerator/denom
        return log(prob)


    def add_train(self, sentence):
        # print("in add train")
        for context, word in bigrams(list(self.tokenize_and_censor(sentence))):
            if context == "<s>" or word == "<s>":
                try:
                    self._everything['<s>'] +=1
                except KeyError:
                    self._everything['<s>'] = 1
            elif context == "</s>" or word == "</s>":
                try:
                    self._everything['</s>'] +=1
                except KeyError:
                    self._everything['</s>'] = 1

            try:
                # print("in the try for add train")
                self._bigramEverything[context, word] +=1
            except KeyError:
                # print("Key error in add_train fam whats this about")
                self._bigramEverything[context, word] = 1

    def log_likelihood(self, sentence):
        """
        Compute the log likelihood of a sentence, divided by the number of
        tokens in the sentence.
        """
        j =1
        i = total = 0
        sentence = list(sentence)
        while j < len(sentence):
            lap = self.laplace(sentence[i],sentence[j])
            total = total + lap
            i += 1
            j += 1
        # print(total/len(sentence))
        return (total/(len(sentence)))





if __name__ == "__main__":
    dem_lm = BigramLanguageModel()
    rep_lm = BigramLanguageModel()

    for target, pres, name in [(dem_lm, kDEM, "D"), (rep_lm, kREP, "R")]:
        for sent in sentences_from_zipfile("../data/state_union.zip", pres):
            for ww in tokenize(sent):
                target.train_seen(ww)

        print("Done looking at %s words, finalizing vocabulary" % name)
        target.finalize()

        for sent in sentences_from_zipfile("../data/state_union.zip", pres):
            target.add_train(sent)
# Nicholas Clement
        print("Trained language model for %s" % name)

    with open("../data/2016-obama.txt") as infile:
        print("REP\t\tDEM\t\tSentence\n" + "=" * 80)
        for ii in infile:
            if len(ii) < 15: # Ignore short sentences
                continue
            try:
                dem_score = dem_lm.log_likelihood(ii)
                rep_score = rep_lm.log_likelihood(ii)

                print("%f\t%f\t%s" % (dem_score, rep_score, ii.strip()))
            except OutOfVocab:
                None
