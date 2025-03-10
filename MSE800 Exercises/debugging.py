from random import randint
import maths 

# def my_function():
#     for i in range(1, 21):
#         if i == 20:             # result is false
#             print(f"You got it!")    # not printed

# Describe the problem - Write your answers as comments:
# 1. what is the loop doing?
# 2. When is the function meant to print "You got it!"?
# 3. What are your assumptions about the value of i?


# def print_dice():
#     dice_images = ["1", "2", "3", "4", "5", "6"]  
#     dice_num = randint(1, 5)                         # end index is out of range
#     print(dice_images[dice_num])


# def print_your_year_of_birth():
#     year = int(input("What is your year of birth?"))

#     if year > 1980 and year <= 1994:                   
#         print(f"You are a Millennial")
#     elif year > 1994:
#         print("You are a Gen Z")
#     else:                                         #added statement to handle all condition
#         print("You are not a Millenial")


# def tell_if_you_can_drive():
#     age = int(input("How old are you?"))
#     if age > 18:
#         print(f"You can drive at age {age}.")   #f string


# def count_total_words():
#     # word_per_page = 0                               # not used
#     pages = int(input("Number of pages: "))
#     word_per_page = int(input("Number of words per page: "))    # ==
#     total_words = pages * word_per_page

#     print(f"We have {total_words} in total.")



def mutate(a_list):
    b_list = []  
    # c_list = []
    for item in a_list:             
        new_item = item * 2
        random_number = randint(1, 3)   
        new_item += random_number
        # c_list.append(random_number)            #append in separate list
        b_list.append(random_number)             #append in one list
        new_item = maths.add(new_item, item)
        b_list.append(new_item)                             
    # return b_list, c_list                      #returns tuple                   
    return b_list     

          
if __name__ == "__main__":
    # example 1
    # my_function()

    # example 2
    # print_dice()

    # example 3
    # print_your_year_of_birth()

    # example 4
    # count_total_words()

    # example 5
    a_demo_list = [1, 2.7, 3.5, 4, 5, 6, 7]
    combined_numbers = mutate(a_demo_list)
    print(combined_numbers)