import random

def write_to_file():
    my_list = [random.randint(1, 100)
                for element in range(10000)]
    with open('my_file.txt', 'w') as num_files:
        for number in my_list:
            num_files.write('{}\n'.format(number))

write_to_file()