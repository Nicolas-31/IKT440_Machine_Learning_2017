'morten goodwin, code during lecture, python 3'
import csv, math

data = csv.reader(open("titanic.csv", "r"))


def getOldYoung(age):
    try:
        if (int(age) < 18):
            return "Young"
    except:
        pass
    return "Old"


alldata = []
for d in data:
    # alldata.append((d[1],d[2],d[4],getOldYoung(d[5])))
    alldata.append((d[1], d[2], d[4], getOldYoung(d[5])))  # ,getOldYoung(d[5])))

alldata = alldata[1:]
trainingdata = alldata[int(len(alldata) / 2):]
verificationdata = alldata[:int(len(alldata) / 2)]


# print(trainingdata)

def entropy(oneclass):
    pos = len([i for i in oneclass if i[0] == "0"])
    neg = len([i for i in oneclass if i[0] == "1"])
    total = pos + neg
    if (min(neg, pos) == 0):
        return 0
    entropy = -(pos / total) * math.log(pos / total, 2) - (neg / total) * math.log(neg / total, 2)
    return entropy


# print(entropy(trainingdata))

def split(data, attribute, remove=False):
    retvals = {}
    # allattributes = set([i[attribute] for i in data])
    for d in data:
        c = d[attribute]
        aList = retvals.get(c, [])
        if (remove):
            d.pop(attribute)
        aList.append(d)
        retvals[c] = aList
    return retvals


# print(split(trainingdata,2).keys())

def gain(oneclass, attribute):
    d = [(entropy(i), len(i)) for i in split(oneclass, attribute).values()]
    nAll = sum([i[1] for i in d])
    gain = sum([(i[0] * i[1]) / nAll for i in d])
    return gain


# print(gain(trainingdata,2))

def getHighestGain(oneclass):
    before = entropy(oneclass)
    attributes = [i for i in range(1, len(oneclass[0]))]
    entropies = [gain(oneclass, a) for a in attributes]
    return entropies.index(min(entropies)) + 1


# print(getHighestGain(trainingdata))

def isPure(oneclass):
    attributes = [i for i in range(1, len(oneclass[0]))]
    for a in attributes:
        if (len(set(i[a] for i in oneclass)) > 1):
            return False
    return True


# print(isPure(trainingdata))

def isEmpty(oneclass):
    return len(oneclass[0]) <= 1


# print(isEmpty(trainingdata))

def mostCommon(oneclass):
    aList = [i[0] for i in oneclass]
    return max(set(aList), key=aList.count)


# print(mostCommon(trainingdata))

def confidence(oneclass):
    mostcommon = mostCommon(oneclass)
    return len([i[0] for i in oneclass if i[0] == mostcommon]) / len(oneclass)


# print(confidence(trainingdata))

actualClassifier = "def classify(data):"


def buildTree(oneclass, spaces="   "):
    global actualClassifier
    if (isEmpty(oneclass) or isPure(oneclass)):
        print(spaces, "then", mostCommon(oneclass))
        print(spaces, "#confidence", confidence(oneclass))
        actualClassifier += "\n" + spaces + "return (" + mostCommon(oneclass) + ")"
        return
    highest = getHighestGain(oneclass)
    d = split(oneclass, highest)
    for key, value in d.items():
        print(spaces, "if", key)
        actualClassifier += "\n" + spaces + "if(data[" + str(highest) + "]==\"" + str(key) + "\"):"
        buildTree(value, spaces + "   ")


buildTree(trainingdata)
print(actualClassifier)
exec(actualClassifier)

# print(classify(verificationdata[0]))
correct, wrong = 0, 0
for data in verificationdata:
    if (int(data[0]) == int(classify(data))):
        correct += 1
    else:
        wrong += 1
print("Correct classifications", correct)
print("Wrong classifications", wrong)
print("Accuracy", (correct / (correct + wrong)))