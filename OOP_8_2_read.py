import array
import os.path


filename = "bin.bin"
filesize = os.path.getsize(filename)
count = filesize // array.array('i').itemsize
numbers = array.array('i', (0 for _ in range(count)))

with open(filename, 'rb') as binary:
    binary.readinto(numbers)
    list_1 = numbers.tolist()

print("Список элементов: ", list_1)
print('Сумма всех элементов: ', sum(list_1))