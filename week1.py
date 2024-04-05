list = [1, 4, 2, 3, 1, 1, 2, 3, 3, 5, 1]

sqrSum = 0

for num in list:
    sqrSum = sqrSum + num**2
print(sqrSum)

squareList = [x ** 2 for x in list]
sqrSum = sum(squareList)
print(sqrSum)

print(sum([x ** 2 for x in list]))

print(sum([x ** 2 for x in [1, 4, 2, 3, 1, 1, 2, 3, 3, 5, 1]]))