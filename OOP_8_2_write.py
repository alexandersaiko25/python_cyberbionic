import array
import random

def write_bin():
    my_list = [random.randint(-100, 100) for element in range(10000)]
    numbers_array = array.array('i', my_list)
    with open("bin.bin", 'wb') as bin_file:
        bin_file.write(numbers_array)

write_bin()

