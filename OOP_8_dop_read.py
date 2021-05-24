import pickle

with open('data.json', 'rb') as file:
    my_list = pickle.load(file)

    print(my_list)