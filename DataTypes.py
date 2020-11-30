"""
1) A Python program to count the number of characters (character
frequency) in a string. Sample String : google.com
"""
my_string_Q1 = str(input("Enter a string:"))
my_dict_Q1 = {}
for i in my_string_Q1:
    keys = my_dict_Q1.keys()
    if i in keys:
        my_dict_Q1[i] += 1
    else:
        my_dict_Q1[i] = 1
print("Count of characters in given string = ", my_dict_Q1)

"""
2) A Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
"""
my_string_Q2 = str(input("Enter a string:"))
string_length_Q2 = len(my_string_Q2)
new_string_Q2 = ""
if string_length_Q2 >= 2:
    first_letters_Q2 = my_string_Q2[0:2]
    last_letters_Q2 = my_string_Q2[-2:]
    new_string_Q2 = first_letters_Q2 + last_letters_Q2
else:
    new_string_Q2 = "Empty String"
print(new_string_Q2)

"""
3) A Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
"""
my_string_Q3 = str(input("Enter a string:"))
first_letter_Q3 = my_string_Q3[0]
print(first_letter_Q3 + my_string_Q3[1:].replace(first_letter_Q3, "$", ))

"""
4) A Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
"""
my_string_1_Q4 = str(input("Enter a string:"))
my_string_2_Q4 = str(input("Enter another string:"))
output_string_1_Q4 = my_string_2_Q4[:2] + my_string_1_Q4[2:]
output_string_2_Q4 = my_string_1_Q4[:2] + my_string_2_Q4[2:]
print(output_string_1_Q4 + " " + output_string_2_Q4)

"""
5) A Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
"""
my_string_Q5 = str(input("Enter a string:"))
string_length_Q5 = len(my_string_Q5)
if string_length_Q5 >= 3:
    if my_string_Q5[-3:] == 'ing':
        print(my_string_Q5 + "ly")
    else:
        print(my_string_Q5 + "ing")
else:
    print(my_string_Q5)

"""
6) A Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
"""
my_string_Q6 = str(input("Enter any string:"))
word_one_Q6 = "not"
word_two_Q6 = "poor"
if word_one_Q6 in my_string_Q6:
    not_index_Q6 = my_string_Q6.index(word_one_Q6, 1)
    if word_two_Q6 in my_string_Q6:
        poor_index_Q6 = my_string_Q6.index(word_two_Q6, 1)
        if not_index_Q6 < poor_index_Q6:
            print(my_string_Q6[:not_index_Q6] + "good" + my_string_Q6[poor_index_Q6 + 4:])
    else:
        print("The string was not changed:", my_string_Q6)
else:
    print("The string was not changed:", my_string_Q6)

"""
7) A Python function that takes a list of words and returns the length of the
longest one.
"""


def longest_word_q7(word_list_q7):
    largest_q7 = 0
    for i in word_list_q7:
        word_length_q7 = len(i)
        if word_length_q7 > largest_q7:
            largest_q7 = word_length_q7
    return largest_q7


my_list_Q7 = ['Learning', 'python', 'is', 'awesome']
print("Longest length in the list is:", longest_word_q7(my_list_Q7))

"""
8) A Python program to remove the n th index character from a nonempty string.
"""
my_string_Q8 = str(input("Enter a string:"))
index_to_remove_Q8 = int(input("Enter the index to be removed:"))
print(my_string_Q8[:index_to_remove_Q8] + my_string_Q8[index_to_remove_Q8 + 1:])

"""
9) A Python program to change a given string to a new string where the first
and last chars have been exchanged.
"""
my_string_Q9 = str(input("Enter a string:"))
new_string_Q9 = my_string_Q9[-1].upper() + my_string_Q9[1:-1] + my_string_Q9[0].lower()
print(new_string_Q9)

"""
10) A Python program to remove the characters which have odd index
values of a given string.
"""
my_string_Q10 = str(input("Enter a string:"))
even_string = ""
for i in my_string_Q10:
    index = my_string_Q10.find(i)
    if index % 2 == 0:
        even_string += i
print(even_string)

"""
11) A Python program to count the occurrences of each word in a given
sentence.
"""
my_sentence_Q11 = str(input("Enter a sentence:"))
sentence_words_Q11 = my_sentence_Q11.split(" ")
count_dict_Q11 = {}
print(sentence_words_Q11)
for word in sentence_words_Q11:
    keys = count_dict_Q11.keys()
    if word in keys:
        count_dict_Q11[word] += 1
    else:
        count_dict_Q11[word] = 1
print(count_dict_Q11)

"""
12) A Python script that takes input from the user and displays that input
back in upper and lower cases.
"""
my_input_Q12 = str(input("Input String:"))
print("Upper Case:", my_input_Q12.upper())
print("Lower Case:", my_input_Q12.lower())

"""
13) A Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
"""
my_words_Q13 = str(input("Enter a sequence of words separated by commas: "))
my_words_Q13 = my_words_Q13.split(',')
my_words_Q13 = list(set(my_words_Q13))
print(",".join(sorted(my_words_Q13)))

"""
14) A Python function to create the HTML string with tags around the
word(s).
"""


def add_html_tags_q14(html_tag_q14, my_string_q14):
    return "<" + html_tag_q14 + ">" + my_string_q14 + "</" + html_tag_q14 + ">"


my_string_Q14 = str(input("Enter text to be included in HTML tags:"))
html_tag_Q14 = str(input("Enter the tag you want:"))
print(add_html_tags_q14(html_tag_Q14, my_string_Q14))

"""
15) A Python function to insert a string in the middle of a string.
"""


def middle_string_q15(first_str_q15, second_str_q15):
    string_length_q15 = len(first_str_q15)
    middle_text_q15 = int(string_length_q15 / 2)
    new_string_q15 = first_str_q15[:middle_text_q15] + second_str_q15 + first_str_q15[middle_text_q15:]
    return new_string_q15


first_string_Q15 = str(input("Enter first string:"))
second_string_Q15 = str(input("Enter second string:"))
print(middle_string_q15(first_string_Q15, second_string_Q15))

"""
16) A Python program to sum all the items in a list.
"""
my_list_Q16 = []
list_size_Q16 = int(input("Enter the total number of items in the list:"))
for i in range(0, list_size_Q16):
    print("Enter item no.", i, ":")
    input_list_Q16 = int(input())
    my_list_Q16.append(input_list_Q16)
print("Given List:", my_list_Q16)
print("Sum of the given list:", sum(my_list_Q16))

"""
17) Python program to multiplies all the items in a list
"""
my_list_Q17 = []
list_product_Q17 = 1
list_size_Q17 = int(input("Enter the total number of items in the list:"))
for i in range(0, list_size_Q17):
    print("Enter item no.", i, ":")
    input_list_Q17 = int(input())
    my_list_Q17.append(input_list_Q17)
    list_product_Q17 *= input_list_Q17
print("Given List:", my_list_Q17)
print("Product of the given list:", list_product_Q17)

"""
18) A Python program to get the largest number from a list.
"""
my_list_Q18 = []
list_size_Q18 = int(input("Enter the total number of items in the list:"))
for i in range(0, list_size_Q18):
    print("Enter item no.", i, ":")
    input_list_Q18 = int(input())
    my_list_Q18.append(input_list_Q18)
list_largest_Q18 = my_list_Q18[0]
for i in my_list_Q18:
    if list_largest_Q18 < i:
        list_largest_Q18 = i

print("Given List:", my_list_Q18)
print("Largest number in the list:", list_largest_Q18)

"""
19) A Python program to get the smallest number from a list.
"""
my_list_Q19 = []
list_size_Q19 = int(input("Enter the total number of items in the list:"))
for i in range(0, list_size_Q19):
    print("Enter item no.", i, ":")
    input_list_Q19 = int(input())
    my_list_Q19.append(input_list_Q19)
list_smallest_Q19 = my_list_Q19[0]
for i in my_list_Q19:
    if list_smallest_Q19 > i:
        list_smallest_Q19 = i

print("Given List:", my_list_Q19)
print("Smallest number in the given list:", list_smallest_Q19)

"""
20) A Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
"""
my_string_list_Q20 = []
match_count_Q20 = 0
list_size_Q20 = int(input("Enter the total number of items in the list:"))
for i in range(0, list_size_Q20):
    print("Enter item no.", i, ":")
    input_list_Q20 = str(input())
    my_string_list_Q20.append(input_list_Q20)
for i in my_string_list_Q20:
    if len(i) >= 2 and i[0] == i[-1]:
        match_count_Q20 += 1
print("Given list:", my_string_list_Q20)
print("Number of string in list with same first and last character:", match_count_Q20)

"""
21) A Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples
"""
tuple_list_Q21 = []
list_size_Q21 = int(input("Enter the total number of items in the list:"))
print("Note: If you want tuple as (1,2), enter '12' without anything in middle.")
for i in range(0, list_size_Q21):
    print("Enter tuple no.", i, ":")
    input_tuple_Q21 = tuple(input())
    tuple_list_Q21.append(input_tuple_Q21)


def last(n):
    return n[-1]


print("Given list:", tuple_list_Q21)
new_list_Q21 = sorted(tuple_list_Q21, key=last)
print(new_list_Q21)

"""
22) A Python program to remove duplicates from a list.
"""
my_list_Q22 = []
list_size_Q22 = int(input("Enter the total number of items in the list:"))
while list_size_Q22 <= 0:
    list_size_Q22 = int(input("Invalid Input.Please enter again:"))
for i in range(0, list_size_Q22):
    print("Enter item no.", i, ":")
    input_item_Q22 = input()
    my_list_Q22.append(input_item_Q22)
new_list_Q22 = list(set(my_list_Q22))
print("Given List:", my_list_Q22)
print("List with unique elements:", new_list_Q22)

"""
23) A Python program to check a list is empty or not.
"""
my_list_Q23 = []
list_size_Q23 = int(input("Enter the total number of items in the list:"))
for i in range(0, list_size_Q23):
    print("Enter item no.", i, ":")
    input_item_Q23 = input()
    my_list_Q22.append(input_item_Q23)
if not my_list_Q23:
    print("List is empty.")
else:
    print("List is not empty.")

"""
24) A Python program to clone or copy a list.
"""
my_list_Q24 = []
list_size_Q24 = int(input("Enter the total number of items in the list:"))
for i in range(0, list_size_Q24):
    print("Enter item no.", i, ":")
    input_item_Q23 = input()
    my_list_Q24.append(input_item_Q23)
new_list_Q21 = my_list_Q24.copy()
print("Given List:", my_list_Q24)
print("Copied List:", new_list_Q21)

"""
25) A Python program to check whether all dictionaries in a list are empty or not.
"""
dict_list_empty_Q25 = [{}, {}, {}]
dict_list_Q25 = [{}, {2, 8}, {}]


def empty_dict_check_q25(dict_list_q25):
    list_length_q25 = len(dict_list_q25)
    empty_count_q25 = 0
    for i in dict_list_q25:
        if not i:
            empty_count_q25 += 1
    if empty_count_q25 == list_length_q25:
        print(True)
    else:
        print(False)


empty_dict_check_q25(dict_list_empty_Q25)
empty_dict_check_q25(dict_list_Q25)

"""
26) A Python program to insert a given string at the beginning of all items in
a list.
"""
my_list_Q26 = []
new_list_Q26 = []
list_size_Q26 = int(input("Enter the total number of items in the list:"))
while list_size_Q26 <= 0:
    list_size_Q26 = int(input("Invalid Input.Please enter again:"))
for i in range(0, list_size_Q26):
    print("Enter item no.", i, ":")
    input_item_Q26 = int(input())
    my_list_Q26.append(input_item_Q26)
add_string_Q26 = str(input("Enter string to be added in front of the list:"))
for num in my_list_Q26:
    num = add_string_Q26 + str(num)
    new_list_Q26.append(num)
print("Given List:", my_list_Q26)
print("Given String:", add_string_Q26)
print("New List:", new_list_Q26)

"""
27) A Python program to replace the last element in a list with another list.
"""
my_list_Q27 = []
my_second_list_Q27 = []
replaced_list_Q27 = []
list_size_Q27 = int(input("Enter the total number of items in the list:"))
while list_size_Q27 <= 0:
    list_size_Q27 = int(input("Invalid Input.Please enter again:"))
for i in range(0, list_size_Q27):
    print("Enter item no.", i, ":")
    input_item_Q27 = int(input())
    my_list_Q27.append(input_item_Q27)

# Input for 2nd list
second_list_size_Q27 = int(input("Enter the total number of items in the second list:"))
while second_list_size_Q27 <= 0:
    second_list_size_Q27 = int(input("Invalid Input.Please enter again:"))
for i in range(0, second_list_size_Q27):
    print("Enter item no.", i, ":")
    input_item_Q27 = int(input())
    my_second_list_Q27.append(input_item_Q27)

# Logic to replace the last element in a list with another list
for i in range(0, list_size_Q27 - 1):
    replaced_list_Q27.append(my_list_Q27[i])

for i in my_second_list_Q27:
    replaced_list_Q27.append(i)

print("First List:", my_list_Q27)
print("Second List:", my_second_list_Q27)
print("Replaced List:", replaced_list_Q27)

"""
28) A Python script to add a key to a dictionary.
"""
my_dict_Q28 = {0: 10, 1: 20}
print("Current dictionary:", my_dict_Q28)
choice = "Y"
while choice == "Y":
    key = int(input("Enter a dictionary key:"))
    value = int(input("Enter a dictionary value:"))
    my_dict_Q28.update({key: value})
    print("Updated dictionary:", my_dict_Q28)
    choice = str(input("Do you want to add an key value pair? Y/N:")).upper()

"""
29) A Python script to concatenate following dictionaries to create a new one.
"""
first_dict_Q29 = {1: 10, 2: 20}
second_dict_Q29 = {3: 30, 4: 40}
third_dict_Q29 = {5: 50, 6: 60}
new_dict_Q29 = {}
for i in first_dict_Q29:
    j = first_dict_Q29.get(i)
    new_dict_Q29.update({i: j})
for i in second_dict_Q29:
    j = second_dict_Q29.get(i)
    new_dict_Q29.update({i: j})
for i in third_dict_Q29:
    j = third_dict_Q29.get(i)
    new_dict_Q29.update({i: j})
print("Combined dictionary:", new_dict_Q29)

"""
30) A Python script to check whether a given key already exists in a dictionary.
"""
my_dict_Q30 = {0: 'a', 1: 'b', 2: 'c'}
key_check_Q30 = int(input("Enter key to check:"))
print("Existing Dictionary:", my_dict_Q30)
if key_check_Q30 in my_dict_Q30.keys():
    print("Key already exists.")
else:
    print("Key is unique and does not exist.")

"""
31) A Python program to iterate over dictionaries using for loops.
"""
my_dict_Q31 = {0: "Python", 1: "Django", 2: "Awesome"}
for i in my_dict_Q31.items():
    print("Key:", i[0], "Value:", i[1])

"""
32) A Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
"""
input_num_Q32 = int(input("Enter a number:"))
my_dict_Q32 = dict()
for i in range(1, input_num_Q32 + 1):
    my_dict_Q32[i] = i * i
print("Dictionary:", my_dict_Q32)

"""
33) A Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys.
"""
my_dict_Q33 = dict()
for i in range(1, 16):
    my_dict_Q33[i] = i * i
print("Dictionary:", my_dict_Q33)

"""
34) A Python script to merge two Python dictionaries.
"""
first_dict_Q34 = {0: 'a', 1: 'b', 2: 'c'}
second_dict_Q34 = {3: 'd', 4: 'e', 5: 'f'}
dict_merge_Q34 = first_dict_Q34.copy()
dict_merge_Q34 = dict_merge_Q34.update(second_dict_Q34)
print("First Dictionary:", first_dict_Q34)
print("Second Dictionary:", second_dict_Q34)
print("Merged Dictionary:", dict_merge_Q34)

"""
35) A Python program to iterate over dictionaries using for loops
"""
my_dict_Q35 = {0: "Python", 1: "Django", 2: "Awesome"}
for i in my_dict_Q35:
    print("Key:", i, "Value:", my_dict_Q35.get(i))

"""
36) A Python program to sum all the items in a dictionary.
"""
my_dict_Q36 = {0: 100, 2: 200, 3: 300}
print("Existing Dictionary:", my_dict_Q36)
print("Sum of the dictionary:", sum(my_dict_Q36.values()))

"""
37) A Python program to multiply all the items in a dictionary
"""
my_dict_Q37 = {0: 400, 2: 500, 3: 600}
print("Existing Dictionary:", my_dict_Q37)
dict_product_Q37 = 1
for i in my_dict_Q30.values():
    dict_product_Q37 *= i
print("Product of the list:%d" % dict_product_Q37)

"""
38) A Python program to remove a key from a dictionary.
"""
my_dict_Q38 = {0: 10, 1: 20, 2: 30, 3: 40}
print("Current dictionary:", my_dict_Q38)
choice = "Y"
while choice == "Y":
    key = int(input("Enter a dictionary key to be deleted:"))
    my_dict_Q38.pop(key)
    print("Updated dictionary:", my_dict_Q38)
    choice = str(input("Do you want to delete more keys? Y/N:")).upper()

"""
39) A Python program to unpack a tuple in several variables.
"""
my_tuple_Q39 = ("This", "is", "a", "tuple")
var_one, var_two, var_three, var_four = my_tuple_Q39
print(var_one, var_two, var_three, var_four)

"""
40) A Python program to add an item in a tuple
"""
my_tuple_Q40 = ("This", "is", "my", "tuple")
add_word_Q40 = str(input("Enter the word you want to add:"))
print("Before addition:", my_tuple_Q40)
my_tuple_Q40 = my_tuple_Q40 + (add_word_Q40,)
print("After addition:", my_tuple_Q40)

"""
41) A Python program to convert a tuple to a string
"""
my_tuple_Q41 = ("This", "is", "a", "tuple")
print("Tuple:", my_tuple_Q41)
tuple_string_Q41 = ''.join(my_tuple_Q41)
print("As a string:", tuple_string_Q41)

"""
42) A Python program to convert a list to a tuple
"""
my_list_Q42 = ["This", "is", "my", "list"]
tuple_list_Q42 = tuple(my_list_Q42)
print("List:", my_list_Q42)
print("Tuple:", tuple_list_Q42)

"""
43) A Python program to remove an item from a tuple
"""
my_tuple_Q43 = ("This", "is", "my", "tuple")
print("Existing Tuple:", my_tuple_Q43)
remove_word_Q43 = str(input("Enter the word you want to remove:"))
my_list_Q43 = list(my_tuple_Q43)
my_list_Q43.remove(remove_word_Q43)
my_tuple_Q43 = tuple(my_list_Q43)
print("Updated tuple:", my_tuple_Q43)

"""
44) A Python program to slice a tuple.
"""
my_tuple_Q44 = ("This", "is", "my", "tuple")
print("Original tuple:", my_tuple_Q44)
print("Sliced tuple:", my_tuple_Q44[2:])

"""
45) A Python program to find the index of an item of a tuple
"""
my_tuple_Q45 = ("This", "is", "my", "tuple")
print("Existing tuple:", my_tuple_Q45)
item_index_Q45 = str(input("Enter the item whose index is to be displayed:"))
print("Index:", my_tuple_Q45.index(item_index_Q45))

"""
46) A Python program to find the length of a tuple
"""
my_tuple_Q46 = ("This", "is", "my", "tuple")
print("Existing tuple:", my_tuple_Q46)
print("Tuple Length:", len(my_tuple_Q46))
