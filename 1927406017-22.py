import random
matrix = [[random.randint(1,10)for j in range(4)]for i in range(4)]
print(matrix)
turn = [[row[a] for row in matrix]for a in range(4)]
print(turn)

