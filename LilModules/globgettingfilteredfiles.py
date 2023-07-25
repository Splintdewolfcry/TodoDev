import glob

myfiles = glob.glob('')
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as f:
        print(f.read())