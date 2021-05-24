import json
import pickle

def goods():

    shop_goods = {
        "PC" : "Asus",
        "CPU" : "Intel I9",
        "GPU" : "NVIDIA",
        "RAM" : "64 Gb",
        "SSD": "1 Tb",
    }

    with open('data.json', 'wb') as file:
        a = pickle.dump((shop_goods), file)
        # json.dump(a, file)

goods()
