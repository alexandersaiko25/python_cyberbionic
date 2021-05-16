import os
from decimal import Decimal

def read_file():
    with open("/home/alexander/PycharmProjects/pythonProject/venv/random.txt", "r", encoding='UTF-8') as the_file:
        content = the_file.readlines()
        print(content)

read_file()