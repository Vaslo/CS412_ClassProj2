#input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

def convertStringToList(string):
    tempList = []
    tempList = string.split()
    return tempList

def find_unigrams(input_list):
    return input_list
    
    


def find_bigrams(input_list):
  return zip(input_list, input_list[1:])

#ngram = zip(input_list, input_list[1:], input_list[2:])

#x = [1,2,3]
#y = [4,5,6]

#zipped = zip(x,y)
#zipped


phrase1 = 'hoagie institution walking doe seem like throwback year ago old fashioned menu board booth large selection food speciality italian hoagie voted best area year year usually order burger patty obviously cooked frozen ingredient fresh overall good alternative subway road'
phrase2 = 'excellent food superb customer service miss mario machine used still great place steeped tradition'

fixedPhrase = phrase1.split()
#print(fixedPhrase)

bigram = find_bigrams(fixedPhrase)
unigram = find_unigrams(fixedPhrase)
print(list(bigram))
print(list(unigram))


