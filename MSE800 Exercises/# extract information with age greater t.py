# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def speak(self):
#         print(f"my name is {self._name}, and i'm {self._age} y/old ")

# # #Answers:
# # 1 Instantiate the Cat object with 3 cats.
# cat1 = Cat('cat1', 5)
# cat2 = Cat('Cat2', 7)
# cat3 = Cat('Cat3', 3)


# # 2 Create a function that finds the oldest cat.
# def oldest_cat(*args):
#     return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
# print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
# cat = Cat("jojo", 100)
# cat.speak = "asdlaksf"
# cat.name = "alll"

# print(cat.speak)
# print(cat.name)



# data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]

# # for age in data:
# #     if age["age"] > 25:
# #         print(age["age"])

# age_above_25 = [age["age"]  for age in data if age["age"]>25 ]
# print(age_above_25)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_matrix = [num for rows in matrix for num in rows]
# print(flattened_matrix)

# grades = [88, 92, 78, 65, 50, 94]

# extra_grades = extra_grades = [num +5 if i < len(grades) - 1 else num + 10 for i, num in enumerate(grades) ]
# print(extra_grades)

# # filter out elements depend on their index: 
# # use list comprehension and enumerate() to get elements with even index
# data = [100, 200, 300, 400, 500]
# even_index = [num for i, num in enumerate(data) if i % 2== 0]
# print(even_index)


# create a dictionary from lists using zip()
# keys = ['name', 'age', 'grade']
# values = ['Alice', 25, 'A']

# zipped = zip(keys, values)
# print(type(zipped))   #class zip
# print(zipped)  # prints an object zip
# print(list(zipped))

# sort the dictionary based on the ages using lambda
# students = [
#     {'name': "John", 'grade': "A", 'age': 20}, 
#     {'name': "Jane", 'grade': "B", 'age': 21}, 
#     {'name': "Joss", 'grade': "A+", 'age': 19}, 
#     {'name': "Jack", 'grade': "A-", 'age': 16}, 
#     {'name': "Dave", 'grade': "C", 'age': 25}, 
# ]

# #arranged dictionary by age(ascending)
# sorted_pairs = sorted(students, key=lambda x: x["age"])
# print(sorted_pairs)

# grades = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 88, 92, 78, 65, 50, 94,]
# prime_grades = [num for num in grades  if num != 1 and num % 2 != 0 and num % 3 !=0 and num% 5 != 0]
# print(prime_grades)

# grades = [88, 92, 78, 65, 50, 94]

# # Function to check if a number is prime
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# prime_grades = [num for num in grades if is_prime(num)]
# print(prime_grades)


# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
 
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# df= df.iloc[[1]]



# Sort by age, then by salary if ages are the same
# use lambda
# employees = [
#     {'name': 'Alice', 'age': 30, 'salary': 80000},
#     {'name': 'Bob', 'age': 25, 'salary': 50000},
#     {'name': 'Charlie', 'age': 35, 'salary': 120000},
# ]



# for employee in employees:
#     holder = employee["age"]
#     print(holder)
#     if employee["age"] == employee["age"]:
#         sorted_pairs = sorted(employees, key=lambda x: x["age"] )
#     else:
#         sorted_pairs = sorted(employees, key=lambda x: x["salary"] )

# print(sorted_pairs)

print(4E2)
print(4**2)