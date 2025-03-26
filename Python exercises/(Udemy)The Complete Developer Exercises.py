#Section 4 
# Exercise: GUI
pictures = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

#printing same structure
for list in pictures:
    for element in list:
        print(element,end= " ")
    print ("")

#printing christmas tree
for list in pictures:
    for element in list:
        if element == 0:  
            print("_", end=" ")
        else:
            print ("*", end=" ")
    print ('')

#Cleaning up the code for best practice
fill= "*"
empty= "_"
for list in pictures:
    for element in list:
        if element:
            print(fill, end=" ")
        else:
            print (empty, end=" ")
    print ('')


#Exercise: Find duplicates
some_list = ['a','b','c','d','b','m','n','n','a']
duplicate = []

for letter in some_list:
    if some_list.count(letter) >= 2:
        if letter not in duplicate:
            duplicate.append(letter)
  
print(duplicate)


#Exercise: Tesla
age = input("What is your age?: ")

if int(age) < 18:
	print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
	print("Powering On. Enjoy the ride!");
elif int(age) == 18:
	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


#ANSWER
def checkDriverAge(age=0):  
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

age = input("What is your age?: ")
checkDriverAge(age)