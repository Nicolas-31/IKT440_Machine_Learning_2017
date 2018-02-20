from Filereader import Filereader
from os import listdir
from os.path import isfile, join
from Bayesianlib import calculateProbability, findGroupWithMaxP

# Vocabulary contains ALL words in ALL files (except stop words which are stripped away).
# Is a dictionary with word as its key, and the wordcount as its value
_vocabulary = dict()
_fr = Filereader()


def getTrainingData(path):
    if not path.endswith("/"):
        path += "/"
    wordsInGroup = dict()
    groups = listdir(path)

    for g in groups:
        if g.startswith("."):
            groups.remove(g)

    for groupName in groups:
        newsgroupPath = path + groupName
        wordsInGroup[groupName] = dict()
        files = [f for f in listdir(newsgroupPath) if isfile(join(newsgroupPath, f))]
        for file in files:
            counts = _fr.getWords(newsgroupPath + "/" + file)
            _fr.mergeDict(wordsInGroup[groupName], counts)
        _fr.mergeDict(_vocabulary, wordsInGroup[groupName])

    return wordsInGroup

def getVerificationData(path):
    verificationData = dict()
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        #print(file)
        counts = _fr.getWords(path + "/" + file)
        verificationData[file] = counts
        #print(len(counts))
    return verificationData


def probabilityCalc(wordsInGroup):
    problist = dict()
    for groupName, words in wordsInGroup.items():
        problist[groupName] = calculateProbability(_vocabulary, words)
    return problist


def classify_documents(trainingdata_folder, verificationdata_folder):
    # Dictionary containing list of filenames by newsgroup as key, for trainingdata
    wordsInGroup = getTrainingData(trainingdata_folder)
    p_word_given_group = probabilityCalc(wordsInGroup)

    # Dictionary containing list of filenames by newsgroup as key, for verificationdata
    verificationData =  getVerificationData(verificationdata_folder)

    result = dict()
    for filename, words in verificationData.items():
        estimatedGroup = findGroupWithMaxP(_vocabulary, p_word_given_group, words)
        result[filename] = estimatedGroup
        # Comment out when running in bamboo !!!
        print("Filename", filename, "Estimated", estimatedGroup)

    return result


# Comment out for running in bambo !!!