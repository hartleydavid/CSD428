#Create a my_filter function that will exclude all odd numbers from our dataset

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

#Filters out all the values in the my_list object by the boolean case of my_function
def my_filter(my_list, my_function):

    #Size of the list
    list_size = len(my_list)

    #Split the overall list into two halfs for two "computers" to computate
    my_list1 = my_list[: list_size // 2]
    my_list2 = my_list[list_size // 2 :]    

    #Filter out the odds for each computers lists
    result1 =  [num for num in my_list1 if my_function(num)]
    result2 =  [num for num in my_list2 if my_function(num)]


    

    #Return the combination of both lists
    return result1 + result2

#Not working
def my_filter_n_computers(my_list, my_function, num_computers = 2):
    #Size of the list
    list_size = len(my_list)
    
    overall_result = []

    for computer in range(num_computers):
        sublist = my_list[(computer) * (list_size // num_computers): (computer + 1) * (list_size // num_computers)]
        result = [item for item in sublist if my_function(item)]
        overall_result += result
    
    return overall_result
#Range of numbers
nums = range(5)

#Filter out all the odd numbers from our list of numbers
# Computer the sum of the squares of the values (evens)
#Print the running total to the console
print(my_reduce(my_map(my_filter(nums, lambda x: x % 2 == 0), lambda x: x * x), lambda x, y: x + y, 0))

#Not currently functioning for n computers
#print(my_reduce(my_map(my_filter_n_computers(nums, lambda x: x % 2 == 0), lambda x: x * x), lambda x, y: x + y, 0))