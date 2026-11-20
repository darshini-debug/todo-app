filenames=["1.raw Data.txt","2.raw Data.txt","3.raw Data.txt"]

for filename in filenames:
    filename=filename.replace('.','-',1)
    print(filename)