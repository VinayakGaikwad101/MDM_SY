# V11

"""print("Hello, World!")"""

"""my_list = [1,2,99, 65, 77, 12, 12, 89, 45]
print(len(my_list))
print(type(my_list))
print(sum(my_list))
print(sorted(my_list))"""

"""s = "Hey"
print(len(s))
print(type(s))"""

# -----------------------------------------

# V12

"""def my_function():
    print("Hello World")
my_function()"""

"""def fun(age):
    print("Your age is: ", age)
age=123
fun(age)"""

"""def two_args(A, B):
    print(f"{A} and {B}")
two_args("Hi", 1234)"""

"""def add(A, B):
    print(f"Addition of {A} and {B} = {A+B}")
add(123, 542)"""

"""def subtract(A, B):
    print(f"Subtraction of {A} and {B} = {A-B}")
subtract(54, 100)"""

"""print("Welcome to calculator (without function)")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4): "))
if choice == 1:
    res = num1+num2
    print(f"Addition of {num1} and {num2} is: {res}")
elif choice == 2:
    res = num1-num2
    print(f"Subtraction of {num1} and {num2} is: {res}")
elif choice == 3:
    res = num1*num2
    print(f"Multiplication of {num1} and {num2} is: {res}")
elif choice == 4:
    if num2 != 0:
        res = num1/num2
        print(f"Division of {num1} and {num2} is: {res}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice. Please try again.")"""


"""print("Welcome to calculator with function")
def calculator(num1, num2, operation):
    if operation == "add":
        print(f"Addition: {num1+num2}")
    elif operation == "subtract":
        print(f"Subtraction: {num1-num2}")
    elif operation == "multiply":
        print(f"Multiplication: {num1*num2}")
    elif operation == "divide":
        if num2 != 0:
            print(f"Division: {num1/num2}")
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
operation = ""
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4): "))
if choice == 1:
   operation="add"
elif choice == 2:
   operation="subtract"
elif choice == 3:
    operation="multiply"
elif choice == 4:
    operation="divide"
calculator(num1, num2, operation)"""

# -----------------------------------

# V12-A and V12-B
# marksheet function

"""def marksheet():
    name = input(f"Enter name for student {i}: ")
    phy = int(input(f"Enter physics marks for student {i}: "))
    chem = int(input(f"Enter chemistry marks for student {i}: "))
    math = int(input(f"Enter math marks for student {i} : "))
    total = phy + chem + math
    avg = total/3
    print(f"Marksheet for {name}: ")
    print(f"Total for student {i}: {total}")
    print(f"Average for student {i} : {avg}")
n = int(input("Enter total number of students: "))
for i in range(1, n+1): 
    marksheet()"""

"""def marksheet():
  name = input("Enter name for student: ")
  phy = int(input("Enter physics marks: "))
  chem = int(input("Enter chemistry marks: "))
  math = int(input("Enter math marks: "))
  total = phy + chem + math
  avg = total / 3
  return name, total, avg
n = int(input("Enter total number of students: "))
for i in range(1, n+1):
  name, total, avg = marksheet()
  print(f"Marksheet for {name}:")
  print(f"Total: {total}")
  print(f"Average: {avg}")"""

# ----------------------------------------

# V12-C  and v13

"""def total(a, b, c):
    t = a+b+c
    avg = t/3
    return t, a
total, a = total(123,32,11)
print(f"Total: {total}")
print(f"Average: {a}")"""

# --------------------------------------

# v14
"""def add_two_numbers(num1, num2):
  return num1 + num2
result = add_two_numbers(5, 3)
print(result)"""

"""def add_two_numbers(num1, num2):
  return num1 + num2
for i in range(5):
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  result = add_two_numbers(num1, num2)
  print(f"The sum of {num1} and {num2} is {result}")"""

# ------------------------

# v16

"""def add_two_exponential_numbers(num1, num2):
  return num1+num2
result = add_two_exponential_numbers(1e5, 2e12)
# 2e7 = 2 x 10^7
print(result)"""

"""def sum_of_list_elements(lst):
  return sum(lst)
numbers = [1, 2, 3, 4, 5]
result = sum_of_list_elements(numbers)
print(result)"""

# -----------------------------

# v17

"""def marksheet(name, marks):
  total = sum(marks)
  average = total / len(marks)
  return total, average
student_name = input("Enter ur name: ")
student_marks = []
n = int(input("Enter total subjects: "))
for i in range(1,n+1):
    marks = int(input(f"Enter marks of subject no {i}: "))
    student_marks.append(marks)
total, average = marksheet(student_name, student_marks)
print(f"Marksheet for {student_name}:")
print(f"Total: {total}")
print(f"Average: {average}")"""

"""name = input("Enter your name: ")
reg_no = input("Enter your registration number: ")
phy = int(input("Enter physics marks: "))
chem = int(input("Enter chemistry marks: "))
math = int(input("Enter math marks: "))
student_data = (name, reg_no, phy, chem, math)
total = sum(student_data[2:])
average = total / 3
print(f"Marksheet for {student_data[0]} (Reg No: {student_data[1]}):")
print(f"Total: {total:.5f}")
print(f"Average: {average:.5f}")"""

"""name = input("Enter your name: ")
reg_no = input("Enter your registration number: ")
phy = int(input("Enter physics marks: "))
chem = int(input("Enter chemistry marks: "))
math = int(input("Enter math marks: "))
student_data = {
    "name": name,
    "reg_no": reg_no,
    "phy": phy,
    "chem": chem,
    "math": math
}
total = student_data["phy"]+student_data["chem"]+student_data["math"]
average = total / 3
print(f"Marksheet for {student_data['name']} (Reg No: {student_data['reg_no']}):")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")"""

# ------------------------------------------

# v17-A 

"""phy = int(input("Enter physics marks: "))
chem = int(input("Enter chemistry marks: "))
math = int(input("Enter math marks: "))
student_dict = {
    "phy": phy,
    "chem": chem,
    "math": math
}
student_tuple = (phy, chem, math)
student_list = [phy, chem, math]
list_total = sum(student_list)
dict_total = sum(student_dict.values())
tuple_total = sum(student_tuple)
print("List Total:", list_total)
print("Dictionary Total:", dict_total)
print("Tuple Total:", tuple_total)"""

# -------------------------------------

# v18

# collection data types: 
# list(ordered, mutable, redundant)
# tuple(ordered, immutable, redundant)
# dictionary(ordered[in new python versions], mutable, non-redundant)
# set(un-ordered, immutable, non-redundant) 

# list methods: 

"""my_list=["apple", "banana", "cherry"]
print(my_list)
print(my_list[1])"""

"""my_list=["apple", "banana", "cherry", 123, True]
print(my_list)"""

"""my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  """

"""my_list = [1, 2, 3]
my_list.clear()
print(my_list)"""  

"""original_list = [1, 2, [3, 4]]
copied_list = original_list.copy()
# Modifying the original list/ copied list both will change if either is modified
copied_list[2][0] = 5
print("Original list:", original_list)  
print("Copied list:", copied_list)  """

"""my_list = [1, 2, 3, 2, 4, 2]
count = my_list.count(2)
print(count)  # Output: 3"""

"""my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  """

"""my_list = [1, 2, 3, 2, 4]
index = my_list.index(2)
print(index)  # Output: 1"""

"""my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]"""

"""my_list = [1, 2, 3]
removed_element = my_list.pop(1)
print(removed_element)  # Output: 2
print(my_list)  # Output: [1, 3]"""

"""my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2, 4]"""

"""my_list = [1, 2, 3, 2, 4]
my_list.reverse()
print(my_list)  # Output: [4, 2, 3, 2, 1]"""

"""my_list = [1, 2, 3, 2, 4]
my_list.sort()
print(my_list)  # Output: [1, 2, 2, 3, 4]"""

"""my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]"""

"""my_list = [1, 2, 3, 4, 5]
# Extract elements from index 1 to 3 (excluding index 3)
sliced_list1 = my_list[1:3]
print(sliced_list1)  # Output: [2, 3]"""

# tuple: 

"""# tuple methods: 
tuple_example = (1, 2, 3)
a, b, c = tuple_example
print(a, b, c)"""

"""my_tuple = (1, 2, 3, 4, 5)
for element in my_tuple:
    print(element)"""

"""my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print(length)  # Output: 5"""

"""tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)"""

"""my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)"""

"""my_tuple = (1, 2, 3, 4, 5)
element_to_check = 10
if element_to_check in my_tuple:
    print("Element found in the tuple")
else:
    print("Element not found in the tuple")"""

"""my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)"""

"""my_tuple = (1, 2, 3, 2, 4)
count = my_tuple.count(2)
print(count)  # Output: 2"""

"""my_tuple = (1, 2, 3, 2, 4)
index = my_tuple.index(2)
print(index)  # Output: 1"""

# ------------------------------------

# V20

# Program using lists

"""student_names = []
phy_marks = []
chem_marks = []
math_marks = []
num_students = int(input("Enter the total number of students: "))
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    phy = int(input(f"Enter physics marks for student {i+1}: "))
    chem = int(input(f"Enter chemistry marks for student {i+1}: "))
    math = int(input(f"Enter math marks for student {i+1}: "))
    student_names.append(name)
    phy_marks.append(phy)
    chem_marks.append(chem)
    math_marks.append(math)
print("\nStudent Data (Lists):")
for i in range(num_students):
    print(f"Student {i+1}: Name: {student_names[i]}, Physics: {phy_marks[i]}, Chemistry: {chem_marks[i]}, Math: {math_marks[i]}")"""


# Program using tuples

"""student_names = ()
phy_marks = ()
chem_marks = ()
math_marks = ()
num_students = int(input("Enter the total number of students: "))
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    phy = int(input(f"Enter physics marks for student {i+1}: "))
    chem = int(input(f"Enter chemistry marks for student {i+1}: "))
    math = int(input(f"Enter math marks for student {i+1}: "))
    student_names += (name,)
    phy_marks += (phy,)
    chem_marks += (chem,)
    math_marks += (math,)
print("\nStudent Data (Tuples):")
for i in range(num_students):
    print(f"Student {i+1}: Name: {student_names[i]}, Physics: {phy_marks[i]}, Chemistry: {chem_marks[i]}, Math: {math_marks[i]}")"""

# Program using Dictionary (dictionaries also have indices)
"""students = {}
num_students = int(input("Enter the total number of students: "))
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    phy = int(input(f"Enter physics marks for student {i+1}: "))
    chem = int(input(f"Enter chemistry marks for student {i+1}: "))
    math = int(input(f"Enter math marks for student {i+1}: "))
    students[i] = {
        "name": name,
        "physics": phy,
        "chemistry": chem,
        "math": math
    }
for i in range(num_students):
    print(f"Student {i+1}:\nName: {students[i]['name']}\nPhysics: {students[i]['physics']}\nChemistry: {students[i]['chemistry']}\nMath: {students[i]['math']}")"""

# ----------------------------------

# V21 and V22
"""def calculate_total(marks):
  return sum(marks)
math_marks = int(input("Enter math marks: "))
chem_marks = int(input("Enter chemistry marks: "))
phy_marks = int(input("Enter physics marks: "))
marks_tuple = (math_marks, chem_marks, phy_marks)
total_marks = calculate_total(marks_tuple)
print("Total marks:", total_marks)"""

"""def calculate_total(marks_dict):
  return sum(marks_dict.values())
math_marks = int(input("Enter math marks: "))
chem_marks = int(input("Enter chemistry marks: "))
phy_marks = int(input("Enter physics marks: "))
marks_dict = {"math": math_marks, "chem": chem_marks, "phy": phy_marks}
total_marks = calculate_total(marks_dict)
print("Total marks:", total_marks)"""

# ---------------------------------------

# V23
"""def greet(name, age):
    print("Hello,", name, "!")
    print("You are", age, "years old.")
greet("Alice", 30)  # Output: Hello, Alice! You are 30 years old."""

"""def greet(name, age):
    print("Hello,", name, "!")
    print("You are", age, "years old.")
greet(age=30, name="Alice")  # Output: Hello, Alice! You are 30 years old."""

"""def greet(name, age=30):
    print("Hello,", name, "!")
    print("You are", age, "years old.")
greet("Bob")  # Output: Hello, Bob! You are 30 years old."""

"""def add_numbers(*args):
    return sum(args)
total = add_numbers(1, 2, 3, 4, 5)
print(total)  # Output: 15"""

"""def marksheet(**kwargs):
    total = sum(kwargs.values())
    return total
total_marks = marksheet(phy=30, chem=99, math=999, eng=101, prog=123)
print(total_marks)"""

# -----------------------------------------

# V24 (OPTIONAL)

"""# clear() - Removes all elements from the dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.clear()
print(my_dict)  # Output: {}"""

"""# copy() - Returns a shallow copy of the dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}"""

"""# fromkeys() - Creates a new dictionary with the specified keys and a default value
keys = ["a", "b", "c"]
my_dict = dict.fromkeys(keys, 0)
print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}"""

"""# get() - Returns the value of the specified key, or a default value if the key doesn't exist
my_dict = {"a": 1, "b": 2, "c": 3}
value = my_dict.get("a")
print(value)  # Output: 1
value = my_dict.get("d", "Key not found")
print(value)  # Output: Key not found"""

"""# items() - Returns a list of key-value pairs
my_dict = {"a": 1, "b": 2, "c": 3}
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])"""

"""# keys() - Returns a list of all keys in the dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])"""

"""# pop() - Removes the specified key-value pair and returns the value
my_dict = {"a": 1, "b": 2, "c": 3}
value = my_dict.pop("b")
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}"""

"""# popitem() - Removes and returns the last inserted key-value pair
my_dict = {"a": 1, "b": 2, "c": 3}
item = my_dict.popitem()
print(item)  # Output: ('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2}"""

"""# setdefault() - Returns the value of the specified key. If the key doesn't exist, inserts it with the specified value
my_dict = {"a": 1, "b": 2}
value = my_dict.setdefault("c", 3)
print(value)  # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}"""

"""# update() - Updates the dictionary with the specified key-value pairs
my_dict = {"a": 1, "b": 2}
other_dict = {"c": 3, "d": 4}
my_dict.update(other_dict)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}"""

"""# values() - Returns a list of all values in the dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])"""