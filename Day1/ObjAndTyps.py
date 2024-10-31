#int
# x = 10
# print(type(x))

#Str
# x = 'Hello World! Here You will learn About Python'
# print(type(x))

#float
# x=2.2
# print(type(x))

#Boolen
# x = True
# print(type(x))


# 1. Objects in Python
# In Python, everything is an object, whether it's a number, string, or even a function. Each object has a type, value, and unique ID in memory.


# x = 10
# y=20
# print(type(x))
# print(x)
# print(id(x))
# print(id(y))


# pi = 3.14
# temperature = -0.001
# print(type(pi))
# print(pi + temperature)

# greeting = "Hello"
# name = "World"
# combined = greeting + " " + name
# print(combined)
# print(name * 3)

# text = "My Name is"
# name = "Talha!"
# print(text+" "+name)
# print(name * 5)

# is_raning = True
# is_sunny = False
# print(type(is_raning))
# print(is_raning and is_sunny)
# print(is_raning or is_sunny)
# print(not is_raning)


# result = None
# print(type(result))
# print(result)




#List
# my_list = [1,2,3,4,5]
# my_list.append(200)
# my_list[0] = 100
# print(my_list)

# my_list = [1,2,3,4,5,6]
# my_list.insert(1 , 100)
# print(my_list)

# my_marvel_list=["Spider-Man" , "Iron Man" , "Captain America " , "Thor"  , "Hulk"] 
# my_marvel_list.append("Doctor Strange ")
# my_marvel_list.insert(3 , "Black Panther")
# # my_marvel_list.remove("Hulk")
# my_marvel_list.pop(0)
# print(my_marvel_list)
# for index , Heros in enumerate(my_marvel_list):
#     print("The Marvel Hero:" , Heros , "is at Index No:" , index )
    
     
     
# Tuple 
# A tuple in Python is an ordered, immutable collection of items, typically used to group related data that shouldn’t change, like coordinates or database records.
# since tuples are immutable We cant change
# cordinate = (10,20)
# cordinate[0] = 200
# print('X =' , cordinate[0]  , 'Y =' , cordinate[1] )


# Dictionaries
# my_dict = { "Luke Cage" , "Deadpool" , "Groot"  , "Gamora"}
# my_dict = {
#     "Luke Cage": "Hero 1",
#     "Deadpool": "Hero 2",
#     "Groot": "Hero 3",
#     "Gamora": "Hero 4"
# }
# print(my_dict.get("Luke Cage"))
# print(my_dict)



# Membership Testing 
#In (in)
# #Returns True if the value is found in the collection.

# my_dict = {
#     "Luke Cage",
#     "Deadpool",
#     "Groot",
#     "Gamora"
# }

# result = "Gamora" in my_dict
# print(result)
# result = "Gamora" not in my_dict
# print(result)


# x = 10 
# if x > 5:
#     print("Greater than 5")
    
# else:
#     print("less than 5")


# x = [1,2,3,4,5,6,7,8,9,10]
# for item in x:
#     y = item*2
#     print(y)


# x = 2
# if(x > 5):
#     print("Greater than 5")
# else:
#     print("Less than 5")


# x = 9
# if(x > 10):
#     print("Greater than 10")
# elif(x == 10):
#     print("Equal to 10")
# else:
#     print("Less than 10")




#In Python, an f-string (formatted string literal) is used for string interpolation, allowing you to easily embed expressions inside string literals. Here are some key points about why and how we use f-strings:



# my_dict = { "Luke Cage" , "Deadpool" , "Groot"  , "Gamora"}
# x = "Groot"
# if  x in my_dict :
#     print(f"  {x}:is Included in your list")
# else:
#     print(f" {x}: isnt included in your list")
    
    
    
# name = "Talha"
# age = 22
# print(f"{name} age is {age}")



# counting = [22,33,11,44,66,55,77,99,88]
# for number in range(4):
#     print(counting[number])


counting = [9,8,7,6,5,4,3,2,1]
for result in range(4):
    print(counting[result])