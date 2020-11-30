"""1) A Python function to find the Max of three numbers."""


def max_of_three_q1(var1, var2, var3):
    return var1 + var2 + var3


print(max_of_three_q1(2, 4, 6))

""" 2) A Python function to sum all the numbers in a list."""


def sum_of_list_q2(my_list_q2):
    return sum(my_list_q2)


print(sum_of_list_q2([9, 8, 7, 6]))

""" 3) A Python function to multiply all the numbers in a list."""


def product_of_list_q3(my_list_q3):
    product_q3 = 1
    for i in my_list_q3:
        product_q3 *= i
    return product_q3


print(product_of_list_q3([2, 4, 6, 8]))

""" 4) A Python program to reverse a string."""


def reverse_string_q4(my_string_q4):
    string_reverse_q4 = my_string_q4[::-1]
    return string_reverse_q4


my_string_Q4 = str(input("Enter a string to be reversed:"))
print(reverse_string_q4(my_string_Q4))

""" 5) A Python function to calculate the factorial of a number (a non-negative
    integer). The function accepts the number as an argument."""


def factorial_number_q5(number_q5):

    factorial_q5 = 1
    for i in range(1, number_q5 + 1):
        factorial_q5 *= i
    return factorial_q5


input_num_q5 = int(input("Enter a number to calculate factorial for:"))
print("Factorial of", input_num_q5, "is:", factorial_number_q5(input_num_q5))

""" 6) A Python function to check whether a number is in a given range. """


def number_in_range_q6(number_q6):

    if number_q6 in range(1, 51):
        print("%d is in range 1-50." % number_q6)
    else:
        print("%d is not in range 1-50." % number_q6)


number_in_range_q6(46)

"""7) A Python function that accepts a string and calculate the number of
    upper case letters and lower case letters"""


def char_case_count_q7(my_text_q7):
    count_upper_q7 = 0
    count_lower_q7 = 0
    for i in my_text_q7:
        if i.isupper():
            count_upper_q7 += 1
        else:
            count_lower_q7 += 1
    return count_upper_q7, count_lower_q7


my_text_Q7 = str(input("Enter a string:"))
upper_count_Q7, lower_count_Q7 = char_case_count_q7(my_text_Q7)
print("No. of Upper case characters:", upper_count_Q7, "\nNo. of Lower case characters:", lower_count_Q7)

""" 8) A Python function that takes a list and returns a new list with unique
elements of the first list."""


def return_unique_list_q8(my_list_q8):
    my_list_q8 = list(set(my_list_q8))
    return my_list_q8


print(return_unique_list_q8([1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9]))

""" 9) A Python function that takes a number as a parameter and check the
    number is prime or not."""


def check_prime_num_q9(number_q9):
    if number_q9 > 1:
        for i in range(2, number_q9):
            if (number_q9 % i) == 0:
                print(number_q9, "is not a prime number")
                break
        else:
            print(number_q9, "is a prime number")
    else:
        print(number_q9, "is not a prime number")


input_num_q9 = int(input("Enter any number:"))
check_prime_num_q9(input_num_q9)

"""
10) A Python program to print the even numbers from a given list.
"""
my_list_q10 = [5, 10, 15, 20, 25, 30]
even_list_q10 = []
for i in my_list_q10:
    if i % 2 == 0:
        even_list_q10.append(i)
print("List with only even numbers:", even_list_q10)

"""
11) A Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
"""
num_fifteen_Q11 = lambda num: num + 15
multiply_numbers_Q11 = lambda num1, num2: num1 * num2

print(num_fifteen_Q11(15))
print(multiply_numbers_Q11(15, 15))

"""
12) A Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number.
"""


def multiply_random_q12(number_q12):
    return lambda random: random * number_q12


result_Q12 = multiply_random_q12(2)
print("Calling the function with random number:", result_Q12(12))

"""
13) A Python program to sort a list of tuples using Lambda.
"""
my_tuple_q13 = [(0, 'Python'), (1, 'Django'), (2, "Awesome")]
print("Tuple before sorting:", my_tuple_q13)
my_tuple_q13.sort(key=lambda x: x[1])
print("Tuple after sorting:", my_tuple_q13)

"""
14) A Python program to sort a list of dictionaries using Lambda
"""
my_dict_q14 = [{'alphabet': 'A', 'example': 'Apple'}, {'alphabet': 'B', 'example': 'Ball'},
               {'alphabet': 'C', 'example': 'Cat'}]
print("Existing list:", my_dict_q14)
my_dict_q14.sort(key=lambda x: x['example'])
print("After sorting:", my_dict_q14)

"""
15) A Python program to filter a list of integers using Lambda
"""
my_list_q15 = [0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
print("Original List: ", my_list_q15)
list_positive_q15 = list(filter(lambda x: x > 0, my_list_q15))
list_negative_q15 = list(filter(lambda x: x < 0, my_list_q15))
list_neutral_q15 = list(filter(lambda x: x == 0, my_list_q15))
print("Positive List: ", list_positive_q15)
print("Negative List: ", list_negative_q15)
print("Neutral List: ", list_neutral_q15)

"""
16) A Python program to square and cube every number in a given list of
integers using Lambda
"""
from functools import reduce

my_list_q16 = [1, 2, 3, 4, 5]
print("Original List: ", my_list_q16)
print("Squared List: ", list(map(lambda x: x ** 2, my_list_q16)))
print("Cubed List: ", list(map(lambda x: x ** 3, my_list_q16)))

"""
17) A Python program to find if a given string starts with a given character
using Lambda.
"""
my_string_q17 = str(input("Enter a string:"))
my_char_q17 = str(input("Enter character to test from:"))
check_string_q17 = lambda string, char: True if string[0] == char else False
print(check_string_q17(my_string_q17, my_char_q17))

"""
18) A Python program to find if a given string starts with a given character using Lambda.
"""
my_string_q18 = input("Enter any input:")
starts_with_q18 = lambda x: True if x.startswith('A') else False
print(starts_with_q18(my_string_q18))

"""
19) A Python program to create Fibonacci series up to n using Lambda
"""
input_num_q19 = int(input("Enter any number:"))
fibonacci_num_q19 = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                                     range(n - 2), [0, 1])
print(fibonacci_num_q19(input_num_q19))

"""
20) A Python program to find intersection of two given arrays using Lambda.
"""
my_array_one_q20 = ["Python", "Django", "Java", "Ruby"]
my_array_two_q20 = ["Python", "Django"]
print("Given arrays:")
print(my_array_one_q20)
print(my_array_two_q20)
common_items_q20 = list(filter(lambda x: x in my_array_one_q20, my_array_two_q20))
print("Common items ", common_items_q20)
