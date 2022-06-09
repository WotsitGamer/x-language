import os

def run(f):
    print(f)
files = os.listdir(os.getcwd())
for file in files:
    if ".x" in file:
        run(file)
    else:
        continue
