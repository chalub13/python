# Least to Greatest
pointsInAGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInAGame)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "Jerry", "Linda"]))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInAGame, reverse=True))

leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

students = [("alice", "B", 12), ("eliza", "A", 16), ("tae", "C", 15)]
print(sorted(students, key=lambda student: student[0]))
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[2]))
