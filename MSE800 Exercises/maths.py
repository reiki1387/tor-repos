# def add(a1, a2):
#     return a1 + a2



# s1 = "my name is Alice"
# s2 = "my name is Alice"

# print(s1 is s2)

# s3 = "hello world"
# s4 = "hello world"

# print(s3 is s4)

# x = 9999
# y = 9999

# print (x is y)

# for i in range(0, 10, -1):  # Decrement by 2
#     print(i)

pictures = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]
print(len(pictures))
for list in pictures:
    for element in list:
        print(element,end= " ")
    print ()