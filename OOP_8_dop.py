import pickle

def goods():
    shop_goods = {
        "PC" : "Asus",
        "CPU" : "Intel I9",
        "GPU" : "NVIDIA",
        "RAM" : "64 Gb",
        "SSD": "1 Tb",
    }
    with open('data.pic', "wb") as file:
        pickle.dump(shop_goods, file)

    # with open('data.pic', 'rb') as file:
    #     new_file = pickle.load(file)
    #
    # print(new_file)

goods()
