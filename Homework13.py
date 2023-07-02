import os
import re

# TASK 1
print("TASK 1 \n")


def func(start, order):

    num_1 = 0
    num_2 = 1
    num_3 = num_1 + num_2

    while start < order:

        if start == 0:
            yield num_1
            start += 1
        elif start == 1:
            yield num_2
            start += 1
        elif start == 2:
            yield num_3
            start += 1
        else:
            num_1 = num_2
            num_2 = num_3
            num_3 = num_1 + num_2
            yield num_3
            start += 1


start = 0
order = int(input("Enter the number of sequence: "))
result = func(start, order)

for value in result:
    print(value, end=' ')
print("\n")


# TASK3
print("TASK3 \n")

print("Name of OS:", os.uname())
print("Current directory:", os.getcwd())
os.mkdir('file_folder')
os.makedirs(os.path.join('file_folder', 'txt'))
os.makedirs(os.path.join('file_folder', 'docx'))
os.makedirs(os.path.join('file_folder', 'pptx'))
os.replace("text.txt", "file_folder/txt/text.txt")
os.replace("oop.txt", "file_folder/txt/oop.txt")
os.replace("oop(1).txt", "file_folder/txt/oop(1).txt")
os.replace("Lesson10.pptx", "file_folder/pptx/Lesson10.pptx")
os.replace("Lesson11.pptx", "file_folder/pptx/Lesson11.pptx")
os.replace("Lesson12.pptx", "file_folder/pptx/Lesson12.pptx")
os.replace("Lesson13.pptx", "file_folder/pptx/Lesson13.pptx")
os.replace("prikaz_pr_4_zo.docx", "file_folder/docx/prikaz_pr_4_zo.docx")

folder_paths = ["file_folder/docx", "file_folder/pptx", "file_folder/txt"]

for folder_path in folder_paths:
    file_counts = {}
    file_sizes = {}
    total_size = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            file_path = os.path.join(root, file)

            if file_extension not in file_counts:
                file_counts[file_extension] = 0
                file_sizes[file_extension] = 0

            file_counts[file_extension] += 1
            file_sizes[file_extension] += os.path.getsize(file_path)
            total_size += os.path.getsize(file_path)

    print(f"Folder: {folder_path}")

    for extension, count in file_counts.items():
        size = file_sizes[extension]
        print(f"Extension: {extension}, An amount of files: {count}, Size of files: {size} bytes")

    print(f" An equal amount of files in the folder: {total_size} bytes")
    print()

os.rename("file_folder/txt/text.txt", "some_text.txt")
os.replace("some_text.txt", "file_folder/txt/some_text.txt")
print("File 'text.txt' was renamed in 'some_text.txt' ")
print("\n")


# TASK4
print("TASK4 \n")

text = """Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном 
заседании вину инкриминируемого правонарушения признала в полном
объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии
алкогольного опьянения от безысходности, в связи с состоянием здоровья
позвонила со своего стационарного телефона в полицию, сообщив о том,
что у неё в квартире якобы заложена бомба. После чего приехали
сотрудники полиции, скорая и пожарные, которым она сообщила, что
бомба — это она."""

new_text = re.sub(r'Эверт-Колокольцева Елизавета Александровна', 'N', text)

print(new_text)
print("\n")


# TASK2
print("TASK2 \n")


def seq(amount):

    value = 0
    while value < amount:
        yield value
        value += 1
        if value == amount:
            value = 0


amount = int(input("Enter an amount of numbers: "))
result = seq(amount)

for i in result:
    print(i, end='-')
print("\n")
