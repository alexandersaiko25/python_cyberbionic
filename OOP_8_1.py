import random
import sys
import os
import re

def write_to_file():
    sys.stdout = open("random.txt", "w")
    total = 0
    for element in range(10000):
        k = random.randrange(100)
        print(k, end=" ")
        total += k
    print("\nСумма всех элементов списка: ", total)
    sys.stdout.close()


write_to_file()