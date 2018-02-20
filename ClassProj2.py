import pprint

target = open("reviews_sample.txt")

myList = []

for line in target:
    tempList = line.split()
    myList.append(tempList)

def find_bigrams(input_list):
  bigram_list = []
  for i in range(len(input_list)-1):
      bigram_list.append((input_list[i], input_list[i+1]))
  return bigram_list

def find_trigrams(input_list):
    trigram_list = []
    for i in range(len(input_list)-2):
        trigram_list.append((input_list[i], input_list[i+1], input_list[i+2]))
    return trigram_list


minSupport = 0.01
support = int(minSupport*len(myList))

biList = []
for smallList in myList:
    bigrams = find_bigrams(smallList)
    biList.append(bigrams)

triList = []
for smallList in myList:
    trigrams = find_trigrams(smallList)
    triList.append(trigrams)

biDict = {}

def addToDictionary(list):
    tempDict = {}
    for items in list:
        for item in items:
            tempDict.setdefault(item, 0)
            tempDict[item] = tempDict[item] + 1
    return tempDict

biDict = addToDictionary(biList)
triDict = addToDictionary(triList)

#print(masterDict)

bigramDict = {}
bigramDict = { k:v for k, v in biDict.items() if v > 100 }

trigramDict = {}
trigramDict = { k:v for k, v in triDict.items() if v > 10 }


#def printDict(dictionary):
#    for key, value in dictionary.items():
#        print(str(value)+":"+str(key))

def printDictBi(dictionary):
    for key, value in dictionary.items():
            print(str(value)+":"+str(key[0])+";"+str(key[1]))

def printDictTri(dictionary):
    for key, value in dictionary.items():
            print(str(value)+":"+str(key[0])+";"+str(key[1]+";"+str(key[2])))


#printDictBi(bigramDict)
printDictTri(trigramDict)

def writeDictBi(dictionary,fileName):
    file = open(fileName, 'w')
    for key, value in dictionary.items():
        file.write(str(value)+":"+str(key[0])+";"+str(key[1])+"\n")
    file.close()

writeDictBi(bigramDict,'output.txt')


