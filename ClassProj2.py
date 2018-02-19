

target = open("small_sample.txt")

myList = []

for line in target:
    tempList = line.split()
    myList.append(tempList)

def find_bigrams(input_list):
  bigram_list = []
  for i in range(len(input_list)-1):
      bigram_list.append((input_list[i], input_list[i+1]))
  return bigram_list

#print(myList)

minSupport = 0.01
support = int(minSupport*len(myList))

newList = []
for smallList in myList:
    bigrams = find_bigrams(smallList)
    newList.append(bigrams)
    
print(newList)

#zipped = zip(myList, myList[1:])

#print(list(zipped))

input_list = ['all', 'this', 'happened', 'more', 'or', 'less']


#bigrams = find_bigrams(input_list)
#print(bigrams)

find_bigrams(input_list)

#def find_trigrams(input_list):
#  bigram_list = []
#  for i in range(len(input_list)-2):
#      bigram_list.append((input_list[i], input_list[i+1],input_list[i+2]))
#  return bigram_list

#trigrams = find_trigrams(input_list)
#print(trigrams)

find_bigrams(input_list)
#def find_bigrams(input_list):
#    for item in list:
#        print(list(zip(input_list, input_list[1:])))

#def find_bigrams(input_list):
#    for item in list:
#        print(list(item))
     
  


#for list in myList:
    #bigramList = zip(list,list[1:])

#print(list(bigramList))


    
#ngram = zip(input_list, input_list[1:], input_list[2:])

#x = [1,2,3]
#y = [4,5,6]

#zipped = zip(x,y)
#zipped


#phrase1 = 'hoagie institution walking doe seem like throwback year ago old fashioned menu board booth large selection food speciality italian hoagie voted best area year year usually order burger patty obviously cooked frozen ingredient fresh overall good alternative subway road'
#phrase2 = 'excellent food superb customer service miss mario machine used still great place steeped tradition'

#fixedPhrase = phrase1.split()
#print(fixedPhrase)

#bigram = find_bigrams(myList)
#find_bigrams(myList)
#unigram = find_unigrams(fixedPhrase)
#print(list(bigram))
#print(list(unigram))


