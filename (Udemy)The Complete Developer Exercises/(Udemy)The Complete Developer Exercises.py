#Section 4 
# Exercise: GUI
# pictures = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0],
# ]

#printing same structure
# for list in pictures:
#     for element in list:
#         print(element,end= " ")
#     print ("")

#printing christmas tree
# for list in pictures:
#     for element in list:
#         if element == 0:  
#             print("_", end=" ")
#         else:
#             print ("*", end=" ")
#     print ('')

#Cleaning up the code for best practice
# fill= "*"
# empty= "_"
# for list in pictures:
#     for element in list:
#         if element:
#             print(fill, end=" ")
#         else:
#             print (empty, end=" ")
#     print ('')


#Exercise: Find duplicates
# some_list = ['a','b','c','d','b','m','n','n','a']
# duplicate = []

# for letter in some_list:
#     if some_list.count(letter) >= 2:
#         if letter not in duplicate:
#             duplicate.append(letter)
  
# print(duplicate)


#Exercise: Tesla
# age = input("What is your age?: ")

# if int(age) < 18:
# 	print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
# 	print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
# 	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


#ANSWER
# def checkDriverAge(age=0):  
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")

# age = input("What is your age?: ")
# checkDriverAge(age)


#Exercise : Function
#create a function the prints the highest even number in a list

# def highest_even(li):
#     even_number_list=[] 
#     for num in li:
#         if num % 2 == 0 :
#              even_number_list.append(num)
    
#     holder=even_number_list[0]
#     for num in even_number_list:
#         if num > holder:
#             holder=num
#     return holder

#     #or simple use built in function
#     #return max(even_number_list)

# num_list = [10,1,3,14,4,20,5,6,9,18]
# print(highest_even(num_list))

# a = 'hellowassupman'

# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")

# while ((n := len(a)) > 1):
#     print(n) #prints 14 down to 2
#     a = a[:-1] #take out all the iterable except the last element

# print(a) #ouput = h




#Exercise: Cats Everywhere (02 April 2025)
#Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def oldest_cat(self, cats):
#         cat_dict = {}
#         for cat in cats:
#             cat_dict[cat.name] = cat.age

#         print (cat_dict)

#         oldest_cat_age = cat_dict[cat.name] #last pair
        
#         for key, value in cat_dict.items():
#             if oldest_cat_age < value:
#                 oldest_cat_age = value
#                 oldest_cat_name = key
#         return oldest_cat_name , oldest_cat_age

# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat("kathy", 8)
# cat2 = Cat("Molly", 9)
# cat3 = Cat("Jenny", 3)

# # 2 Create a function that finds the oldest cat
# cat_list =[cat1, cat2, cat3]
# name , age = cat1.oldest_cat(cat_list)

# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f"The oldest cat is {age} years old")

# # 4 What is the name of the oldest cat
# print (f"The name of the oldest cat is {name}")


print (not "hello".islower())