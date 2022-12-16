# Below function runs a for loop for given list and finds if the given parameter number is present in the list, if its present, it will return true, else it will return false

def find_num(number_list:list, number:int):
 for iterate_number in number_list:
    if iterate_number == number:
        return True
    else:
        return False # this line was changed from pass to return False for the function to return False instead of None
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

#It returns None because, by default python Function has a return value, if you don't return anything it will return None.
