import csv, math
import pickle


def buildData(dataq):
    tmp = []
    # 0:Gender, 1:Length, 2:Diam, 3:Height, 4:Whole, 5:Shucked, 6:Viscera, 7:Shell, 8:Rings
    for row in dataq:
        tmp.append( (
            row[0],
            (float(row[1])),
            (float(row[2])),
            (float(row[3])),
            (float(row[4])),
            (float(row[5])),
            (float(row[6])),
            (float(row[7])),
            (int(row[8]))
        ) )
    return tmp





def replaceValueWithGroup(value, thresholds, prefix):
    if value <= thresholds[0]:
        return prefix + "_Low"
    return prefix + "_High"


def createThresholds(meanVals):
    splits = []
    lowFactor = 0.5
    highFactor = 1.2
    for n in range(0, len(meanVals)):
        if n == 7:
            lowFactor = 0.6
            highFactor = 1.3
        splits.append( (meanVals[n]*lowFactor, meanVals[n]*highFactor) )
    return splits


def getColumnMean(data, index):
    sum=0
    for row in data:
        sum += row[index]
    return 1.0*sum / len(data)

def getColumnMeans(data):
    t = []
    for x in range(1, len(data[0])):
        t.append(getColumnMean(data, x))
    return t


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


def prepareData(dataq, threshold):
    tmp = []

    # Columns: 0:Gender, 1:Length, 2:Diam, 3:Height, 4:Whole, 5:Shucked, 6:Viscera, 7:Shell, 8:Rings
    for row in dataq:
        tmp.append( (
            row[0],
            (replaceValueWithGroup(row[1], threshold, "Length")),
            (replaceValueWithGroup(row[2], threshold, "Diam")),
            (replaceValueWithGroup(row[3], threshold, "Height")),
            (replaceValueWithGroup(row[4], threshold, "Whole")),
            (replaceValueWithGroup(row[5], threshold, "Shucked")),
            (replaceValueWithGroup(row[6], threshold, "Viscera")),
            (replaceValueWithGroup(row[7], threshold, "Shell")),
            (replaceValueWithGroup(row[8], threshold, "Rings")),
        ) )
    return tmp



def countGender(list, gender):
    return len([i for i in list if i[0] == gender])


def getMean(data, index):
    sum=0
    for row in data:
        sum += row[index]
    return 1.0*sum / len(data)

def showMeanTable(data):
    t = []
    for x in range(1, len(data[0])):
        t.append(getMean(data, x))
    return t

def makeSplits(meanVals):
    splits = []
    for n in range(0, len(meanVals)):
        splits.append( (meanVals[n]*0.8, meanVals[n]*1.2) )
    return splits

#***

# print(trainingdata)
def entropy(oneclass):
    # print('ONECLASS:',oneclass)
    ma = len([i for i in oneclass if i[0] == "M"]) * 1.0
    fe = len([i for i in oneclass if i[0] == "F"]) * 1.0
    inf = len([i for i in oneclass if i[0] == "I"]) * 1.0
    #print('MALE:', ma, '\nFEMALE:',fe,'\nINFANT:',inf)
    total = ma + fe + inf

    if(inf == 0 and fe == 0) or (inf == 0 and ma == 0) or (ma == 0 and fe == 0):
        return 0

    if (min(ma,fe,inf) != 0):
        return - (ma / total) * math.log(ma / total, 2) - (fe / total) * math.log(fe / total, 2) - (inf/ total) * math.log(inf / total, 2)

    if inf == 0:
        entropy = -(ma / total) * math.log(ma / total, 2) - (fe / total) * math.log(fe / total, 2)

    elif ma == 0:
        entropy = - (fe / total) * math.log(fe / total, 2) - (inf / total) * math.log(inf/ total, 2)

    else:
        entropy = - (ma / total) * math.log(ma / total, 2) - (inf / total)*math.log(inf / total, 2)

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


# Read file
csvfile = csv.reader(open("train2.csv", "r"))
columns = ["Gender", "Length", "Diam", "Height", "Whole", "Shucked", "Viscera", "Shell", "Rings"]

numericalData = buildData(csvfile)
numericalData = numericalData[int(len(numericalData)/2):]

means = getColumnMeans(numericalData)

prepared = prepareData(numericalData, means)

trainingdata = prepared[int(len(prepared)/2):]
verificationdata = prepared[:int(len(prepared)/2)]



actualClassifier = "def classify(data):"


def buildTree(oneclass, spaces="   "):
    global actualClassifier
    if (isEmpty(oneclass) or isPure(oneclass)):
        print(spaces, "then", mostCommon(oneclass))
        print(spaces, "#confidence", confidence(oneclass))
        actualClassifier += "\n" + spaces + "return ('" + mostCommon(oneclass) + "')"
        return
    highest = getHighestGain(oneclass)
    g = gain(oneclass, highest)
    d = split(oneclass, highest)
    for key, value in d.items():
        print(spaces, "if", key)
        actualClassifier += "\n" + spaces + "if(data[" + str(highest) + "]==\"" + str(key) + "\"):"
        if g == 0:
            spaces += "   "
            actualClassifier += "\n" + spaces + "return ('" + mostCommon(oneclass) + "')"
            return
        buildTree(value, spaces + "   ")


buildTree(trainingdata)
print(actualClassifier)
exec(actualClassifier)

def build_forest(trainingData):
    buildTree(trainingData)
    classifier ={'1':actualClassifier}
    pickle.dump(classifier,open('classifier.p','wb'))
    return 1

print(build_forest(trainingdata))

def predict(hiddenVerficationData):
    classifier = pickle.load(open('classifier.p','rb'))
    exec(classifier['1'],globals())
    a = []
    for d in hiddenVerficationData:
        a.append(classify(d))
   # print(a)
    return a

print(predict(verificationdata))

correct, wrong = 0, 0
for data in verificationdata:
    if (str(data[0]) == str(classify(data))):
        correct += 1
    else:
        wrong += 1
print("Correct classifications", correct)
print("Wrong classifications", wrong)
print("Accuracy", (1.0 * correct / (correct + wrong)))