import math

#
# Calculate probabilities for words in ONE group
# Takes the complete vocabulary, groups wordcount dictionary, and the number of posts (files) in the particular group
# Return a dictionary with words (all words in vocabulary) and the probability for showing up in the group.
#
def calculateProbability(vocabulary, wordsInGroup):
    p_group = dict()
    #vocabularyLen: the total number of words in vocabulary, not just distinct words
    numWordsInVocabulary = sum(vocabulary.values())
    #numWordsInVocabulary = len(vocabulary)
    numWordsInGroup = sum(wordsInGroup.values())
    denominator = numWordsInGroup + numWordsInVocabulary

    for word in vocabulary.keys():
        #ensure we have at least 1 word of each
        if word not in wordsInGroup:
            wordsInGroup[word] = 1
        t = (wordsInGroup[word])
        p_group[word] = t / denominator

    return p_group


# Finds group with max P(O | H)*P(H)
def findGroupWithMaxP(vocabulary, p_word_given_group, sample):
    max_group = "none"
    max_p = -1000000

    for groupName, groupProb in p_word_given_group.items():
        # Calculates P(O | H)*P(H) for candidate group
        #p = math.log(p_group[groupName])
        j = 0
        #print("Evaluating", groupName)
        p = 0
        q = groupProb.values()
        #s = sum(groupProb.values())
        for word in sample:
            if word in vocabulary:
                pWord = groupProb[word]
                p += math.log(pWord)

        if p > max_p:
            max_p = p
            max_group = groupName
           # print("Maxgroup", max_group, p, max_p)
        #print(groupName, p)
    return max_group