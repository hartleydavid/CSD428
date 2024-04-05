#List to compute the sum of all the squares
list = [1, 4, 2, 3, 1, 1, 2, 3, 3, 5, 1]

#Running total
sqrSum = 0

#First Method
for num in list:
    sqrSum += num**2
print(sqrSum)

#Method 2
squareList = [x ** 2 for x in list]
sqrSum = sum(squareList)
print(sqrSum)

#Method 3
print(sum([x ** 2 for x in list]))
print(sum([x ** 2 for x in [1, 4, 2, 3, 1, 1, 2, 3, 3, 5, 1]]))

#Method 4
def my_square(n):
    return n *n

def my_sum(a,b):
    return a+b

#Method 5
def sum_squares():
    l = [1, 4, 2, 3, 1, 1, 2, 3, 3, 5, 1]

    result = 0

    for num in l:
        result + my_square(num)

    print(result)

#Method 6

#Splits the list into two computers and squares of all the values (based on my_function)
def my_map(my_list, my_function, n =2):

    list_size = len(my_list)

    my_list1 = my_list[: list_size // n]
    my_list2 = my_list[list_size // n :]

    #my_list1 -> comp 1
    result1 = []

    for n in my_list1:
        result1.append(my_function(n))

    #my_list2 -> comp 2
    result2 = []

    for n in my_list2:
        result2.append(my_function(n))

    
    return result1 + result2

#Splits the list into two computers and will calculate the sum of the values (based on my_function)
def my_reduce(my_list, my_function, seed, n = 2):

    list_size = len(my_list)

    my_list1 = my_list[: list_size // n]
    my_list2 = my_list[list_size // n :]

    result1 = seed
    for i1 in my_list1:
        result1 = my_function(result1, i1)

    result2 = seed
    for i2 in my_list2:
        result2 = my_function(result2, i2)

    return my_function(result1, result2)

#squared_numbers = my_map(list, my_square)
#summed_numbers = my_reduce(squared_numbers, my_sum, 0, 2)
#print(summed_numbers)

#Uses user defined functions
#print(my_reduce(my_map(list, my_square), my_sum, 0, 2))

#Uses lambda functions 
print(my_reduce(my_map(list, lambda x: x*x), lambda a,b: a+b, 0, 2))