#Find the sum of the ascii values of all the characters in the string

#hash("abc") = 97 + 98 + 99 = 294 

#We want to end up using this in the end
#print(my_reduce(my_map(list, lambda x: x*x), lambda a,b: a+b, 0, 2))

#Splits the my_list object to two computers and performs a computation on each computer
#Returns the combined list of both computed result list
def my_map(my_list, my_function, n =2):

    #Size of the list
    list_size = len(my_list)

    #Split the overall list into two halfs for two "computers" to computate
    my_list1 = my_list[: list_size // n]
    my_list2 = my_list[list_size // n :]

    #my_list1 -> computer 1
    result1 = []

    for n in my_list1:
        result1.append(my_function(n))

    #my_list2 -> computer 2
    result2 = []

    for n in my_list2:
        result2.append(my_function(n))

    #The combination of both lists
    return result1 + result2

#Splits the list into two computers and performs a computation on each computer
def my_reduce(my_list, my_function, seed, n = 2):

    #Size of the list
    list_size = len(my_list)

    #Split the overall list into two halfs for two "computers" to computate
    my_list1 = my_list[: list_size // n]
    my_list2 = my_list[list_size // n :]

    #Computer 1 computations
    result1 = seed
    for i1 in my_list1:
        result1 = my_function(result1, i1)

    #Computer 2 computations
    result2 = seed
    for i2 in my_list2:
        result2 = my_function(result2, i2)

    return my_function(result1, result2)

#Send a string to the my_map with converting each char to a numerical value (ord())
#Sum all the values on each char to a running total and print to console
print(my_reduce(my_map("abc", lambda x: ord(x)), lambda a,b: a+b, 0, 2))