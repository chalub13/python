# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print("My one line:", myFile.readline())
myFile.seek(0)
print("My one line:", myFile.readline())

# Iterate through each line of a file
for line in myFile:
    newHighScore = line.replace("BBB", "PDJ")
    print(newHighScore)

myFile.close()
