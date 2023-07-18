
## Day 6 Coding Exercise 6
# new_user = input('Add a new member:  ')

# with open('members.txt', 'a') as f:
#     print(new_user, file=f)
#     f.close

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for name in filenames:
#     file = open(f'{name}', 'w')
#     writing = file.write('Hello')
#     file.close()

# from pathlib import Path
# import os
# for file in os.listdir("./CodingExercises"):
#     if file.endswith(".txt"):
#         print('I am', Path(f'./CodingExercises/{file}').stem + '.')


# Path('/root/dir/sub/file.ext').stem

# file = open("a.txt", 'w')

# file.write("100.12 \n")
# file.write("111.23 \n")

# file.close()        

# with open("D:/AUIVVII/Udemy/PratikPython/CodingExercises/NotNeededRN/file.txt", 'r') as file:
#     content = file.read()
#     # print(content+ '\n' + len(content))
#     print(f'{content}\n{len(content)}')

# ids = ["XF345_89", "XER76849", "XA454_55"]
    
# x = 0
    
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

# try:
#     waiting_list = ["john", "marry"]
#     name = input("Enter name: ")
        
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
# except ValueError:
#     print(f'{name} is not in the list')

def get_average():
    x = "hello"
    return x.capitalize()
    
average = get_average()

print(average)