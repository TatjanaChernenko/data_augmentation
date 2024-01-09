import pickle

import nltk
from nltk.corpus import wordnet as wn

def thesarius(our_input):
    translation = ""
    punctuation = [".",",","?","!",":",";","...","\"","\'","\'\''","(",")","[","]","{","}"]
    for word in our_input.split(" "):
        clean_word = ""
        for el in word:
            if el not in punctuation:
                clean_word+=el
        synon = wn.synsets(clean_word)
        alle = []
        for el in synon:
            a = el.lemma_names()
            alle.append(a[0])
        if len(alle) > 0:
            a = alle[0]
            if a.split("_"):
                x = ""
                a = a.split("_")
                for el in a:
                    x+=el
                    x+=" "
                x.strip()
                a = x
            translation+=a
            translation+=" "
        else:
            translation+=clean_word 
            translation+=" "
    if translation != our_input: 
        return translation
  

f = open("./data/contract_data.pkl","rb")
data = pickle.load(f)

print("Original data length: ", len(data))

new_data = []

for el in data:
    new = thesarius(el["text"])
    new_el = el.copy()
    new_el["text"] = new
    new_el["id"]+="-thesarius"
    new_data.append(new_el)
    print("...",len(new_data))

for el in new_data:
    data.append(el)

print("New data length: ",len(data)) 

with open("./data/contract_data_thesarius.pkl", 'wb') as fp:
    pickle.dump(data, fp)

# Check the new IDs:
#x = open('./data/contract_data_thesarius.pkl', "rb")

#data_r = pickle.load(x)
#for el in data_r:
#    print(el["id"])
#print("Done. Check the new IDs above.")

