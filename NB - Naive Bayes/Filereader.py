import string
from Stopwords import getStopWords


class Filereader:

    def __init__(self):
        self.stopwords = getStopWords()

    def removeStopwords(self, wordlist):
        return [w for w in wordlist if w not in self.stopwords]

    #
    # Merge the newWords into the vocabulary dictionary
    #
    def mergeDict(self, vocabulary, newWords):
        for word, count in newWords.items():
            if word not in vocabulary:
                vocabulary[word] = count
            else:
                vocabulary[word] += count

    def getWords(self, filename):

        fhandle = open(filename, "r", encoding = "iso-8859-1")


        counts = dict()
        inHeader = True
        for line in fhandle:
            if line.startswith("\n"):
                inHeader = False
            if inHeader: continue
            # https://stackoverflow.com/questions/16050952/how-to-remove-all-the-punctuation-in-a-string-python
            line = "".join(l for l in line if l not in string.punctuation)
            line = line.rstrip().lower()
            if len(line) < 3: continue
            words = line.split()
            words = self.removeStopwords(words)
            for word in words:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
        return counts