from Filereader import Filereader
from os import listdir
from os.path import isfile, join
from Bayesianlib import calculateProbability, findGroupWithMaxP


p_word_given_group = dict()


# Set relative path to the trainingdata
path = "./training_data/"
# Create the Filereader instance
fr = Filereader()

#Dictionary containing list of filenames by newsgroup as key, for trainingdata
trainingFiles = dict()
#Dictionary containing list of filenames by newsgroup as key, for verificationdata
verificationFiles = dict()


# Vocabulary contains ALL words in ALL files (except stop words which are stripped away).
# Is a dictionary with word as its key, and the wordcount as its value
vocabulary = dict()
# This is a container for keeping all words for all groups.
# Is a dictionary where each newsgroups wordcount is an entry
wordsInGroup = dict()

#Find all directories in the trainingdata, and exclude hidden directories (git)
def getDatafiles(dataPath, traingdataFraction):
    groups = listdir(dataPath)
    for g in groups:
        if g.startswith("."):
            groups.remove(g)

    for g in groups:
        newsgroupPath = path + g
        trainingArr = []
        verificationArr = []
        print(newsgroupPath)
        i = 0
        files = [f for f in listdir(newsgroupPath) if isfile(join(newsgroupPath, f))]
        ntraining = int(len(files) * traingdataFraction)
        #print(g, len(files))

        for file in files:
            if i < ntraining:
                trainingArr.append(file)
            else:
                verificationArr.append(file)
            i += 1
        trainingFiles[g] = trainingArr
        verificationFiles[g] = verificationArr


#Gather the trainingdata. Loop through all directories, and all files in given directory
#Build the vocabulary and the wordcounts for each newsgroup
def readTrainingData(dataPath):
    print("Load trainingdata")
    for groupName, fileArr in trainingFiles.items():
        wordsInGroup[groupName] = dict()
        newsgroupPath = dataPath + groupName
        print(newsgroupPath)

        for file in fileArr:
            #print(file)
            counts = fr.getWords(newsgroupPath + "/" + file)
            fr.mergeDict(wordsInGroup[groupName], counts)
            #print("File:", counts)

        fr.mergeDict(vocabulary, wordsInGroup[groupName])
    # include break here for testing only ONE group
    #break


#
# Iterate through all groups, and create the probability dictionary
#
def probabilityCalc():
    for groupName, words in wordsInGroup.items():
        #print("Calculate word probabilities")

        p_group = calculateProbability(vocabulary, words)
        p_word_given_group[groupName] = p_group
'''
    for groupName, words in wordsInGroup.items():
        plist = p_word_given_group[groupName]
        i=0
        print(groupName)
        for w in sorted(plist, key=plist.get, reverse=True):
            print(w, plist[w])
            i += 1
            if i > 5:
                break
'''



def classify(dataPath):
    print("Start classifying...")
    correctCount = 0
    totalCount = 0
    for groupName, fileArr in verificationFiles.items():
        wordsInGroup[groupName] = dict()
        newsgroupPath = dataPath + groupName
        #print("Classify:", groupName)
        groupCorrectCount = 0
        for file in fileArr:
            sample = fr.getWords(newsgroupPath + "/" + file)
            estimatedGroup = findGroupWithMaxP(vocabulary, p_word_given_group, sample)
            if estimatedGroup == groupName:
                correctCount += 1
                groupCorrectCount += 1
            else:
                print("Failed:", estimatedGroup)
            totalCount += 1
            #print("Total:", totalCount, "Correct: ", correctCount)
        #print(groupCorrectCount, len(fileArr))
        #print(groupName, groupCorrectCount, len(fileArr))
    print("Total: " , correctCount, totalCount, correctCount / totalCount)

# Training data fraction, the rest is used for verification (classiy)
traingdataFraction = 0.7
getDatafiles(path, traingdataFraction)
readTrainingData(path)
probabilityCalc()
classify(path)