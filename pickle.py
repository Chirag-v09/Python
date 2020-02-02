import pickle

data = { "A" :[1, 2, 3], "B" : [4, 5 ,6] }

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    data = pickle.load(f)


example_dict = {1:"6",2:"2",3:"f"}


pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)