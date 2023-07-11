
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

file = open("a.txt", 'w')

file.write("100.12 \n")
file.write("111.23 \n")

file.close()        