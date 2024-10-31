# Many Values to Multiple Variables
# x , y, z = "Orange" , "Banana" , "Mango"
# print(x)
# print(y)
# print(z)


# One Value to Multiple Variables

# x=y=z= "Mango"
# print(x)
# print(y)
# print(z)

fruits = ["Orange" , "Mango" , "Banana" , "Cherry"]
# x , y , z , z1 = fruits
# print(x)
# print(y)
# print(z)
# print(z1)




# Global Variables

# import asyncio
# x = "Awesome"

# async def my_function():
#     print("Python is " , x)
#     await asyncio.sleep(5)
#     print("Yes Python is" , x)
# asyncio.run(my_function())


# If you use the global keyword, the variable belongs to the global scope:

def my_Function():
    global x
    x = "Fantastic"
    print("Python is " , x , "langauge")
    
my_Function()

print(x)