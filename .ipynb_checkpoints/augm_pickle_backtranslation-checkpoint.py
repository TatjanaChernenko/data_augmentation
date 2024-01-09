import pickle
from mtranslate import translate

f = open("./data/contract_data.pkl","rb")
data = pickle.load(f)

print("Original data length: ", len(data))

new_data = []

for el in data:
    ger_transl = translate(el["text"], "de")
    new = translate(ger_transl, "en")
    new_el = el.copy()
    new_el["text"] = new
    new_el["id"]+="-backtranslation"
    new_data.append(new_el)
    print("...",len(new_data))

for el in new_data:
    data.append(el)

print("New data length: ",len(data))    

with open('./data/contract_data_backtranslation.pkl', 'wb') as fp:
    pickle.dump(data, fp)

# Check the new IDs:
#x = open('./data/contract_data_backtranslation.pkl', "rb")

#data_r = pickle.load(x)
#for el in data_r:
#    print(el["id"])


