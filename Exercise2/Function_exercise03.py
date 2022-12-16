
numbers = input("Enter a list of numbers: ")
number_list = numbers.split()
print(number_list)
def find_even_number():
 for number in number_list:
    if int(number) %2 == 0:
        print(True)
    else:
        print(False)
        pass
find_even_number()

#The above program finds even numbers in a given list of numbers
