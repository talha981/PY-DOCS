# text = "***************"
# for index in range(len(text)):
#     print(*text[:index + 10])


# def my_function():
#     print("Hello from a function")
    
# my_function()


# def my_function(fname):
#     print(fname +" " + "Refsnes")
# my_function("Email")
    
    
    
# def my_function(*name ):
#     print("My Name is :" + name[0] )
    
# my_function("Talha" , "Safdar")


# def my_fun(fname , lname):
#     print(fname , lname)
# my_fun("Talha " , "Safdar")


# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)


# import asyncio
# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(5)
#     print("World")
# asyncio.run(say_hello())


# import asyncio
# async def my_name():
#     print("Talha")
#     print("Talha")
#     print("Talha")
#     print("Talha")
#     print("Talha")
#     print("Talha")
#     await asyncio.sleep(5)
#     print("Safdar")
# asyncio.run(my_name())



import asyncio
async def my_function():
    print("Hello World!")
    await asyncio.sleep(5)
    print("How Are You!")
asyncio.run(my_function())
    