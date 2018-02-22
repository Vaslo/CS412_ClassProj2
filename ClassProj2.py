import pprint

target = open("reviews_sample.txt")

myList = []

for line in target:
    tempList = line.split()
    myList.append(tempList)

def find_unigrams(input_list):
    unigram_list = []
    unigram_list = (set(input_list))
    return unigram_list
 
def find_bigrams(input_list):
  bigram_list = []
  for i in range(len(input_list)-1):
      bigram_list.append((input_list[i], input_list[i+1]))
      bigram_list = list(set(bigram_list))
  return bigram_list

def find_trigrams(input_list):
    trigram_list = []
    for i in range(len(input_list)-2):
        trigram_list.append((input_list[i], input_list[i+1], input_list[i+2]))
    return trigram_list

minSupport = 0.01
support = int(minSupport*len(myList))

uniList = []
for smallList in myList:
    unigrams = find_unigrams(smallList)
    uniList.append(unigrams)

biList = []
for smallList in myList:
    bigrams = find_bigrams(smallList)
    biList.append(bigrams)

triList = []
for smallList in myList:
    trigrams = find_trigrams(smallList)
    triList.append(trigrams)

#print(unigrams)

uniDict = {}
biDict = {}
triDict = {}

def addToDictionary(list):
    tempDict = {}
    for items in list:
        for item in items:
            tempDict.setdefault(item, 0)
            tempDict[item] = tempDict[item] + 1
    return tempDict

uniDict = addToDictionary(uniList)
biDict = addToDictionary(biList)
# triDict = addToDictionary(triList)

#print(masterDict)

unigramDict = {}
unigramDict = { k:v for k, v in uniDict.items() if v > 100 }

bigramDict = {}
bigramDict = { k:v for k, v in biDict.items() if v > 100 }

trigramDict = {}
trigramDict = { k:v for k, v in triDict.items() if v > 10 }


#def printDict(dictionary):
#    for key, value in dictionary.items():
#        print(str(value)+":"+str(key))


def printDictUni(dictionary):
    for key, value in dictionary.items():
            print(str(value)+":"+str(key))


def printDictBi(dictionary):
    for key, value in dictionary.items():
            print(str(value)+":"+str(key[0])+";"+str(key[1]))

def printDictTri(dictionary):
    for key, value in dictionary.items():
            print(str(value)+":"+str(key[0])+";"+str(key[1]+";"+str(key[2])))

printDictUni(unigramDict)
printDictBi(bigramDict)
# printDictTri(trigramDict)

# def writeDictBi(dictionary,fileName):
#     file = open(fileName, 'w')
#     for key, value in dictionary.items():
#         file.write(str(value)+":"+str(key[0])+";"+str(key[1])+"\n")
#     file.close()

#writeDictBi(bigramDict,'output.txt')

def writeDictBi(dictionary,fileName):
    file = open(fileName, 'w')
    for key, value in dictionary.items():
        file.write(str(value)+":"+str(key[0])+";"+str(key[1])+"\n")
    file.close()

def writeDict(dict1, dict2,fileName):
    uniCounter = 0
    biCounter = 0
    file = open(fileName, 'w')
    for key, value in dict1.items():
        file.write(str(value)+":"+str(key)+"\n")
        uniCounter += 1
    for key, value in dict2.items():
        file.write(str(value)+":"+str(key[0])+";"+str(key[1])+"\n")
        biCounter += 1
    file.close()
    print("Total unigram lines printed: "+str(uniCounter))
    print("Total bigram lines printed: "+str(biCounter))

writeDict(unigramDict,bigramDict,"patterns.txt")