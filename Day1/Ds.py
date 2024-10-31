# 1. Strings
#Description: Strings are sequences of characters enclosed in quotes (single, double, or triple). They are immutable, meaning that once created, their contents cannot be changed. 

# Characteristics:
# Immutable
# Can contain letters, numbers, symbols, etc.
# Support various operations (e.g., concatenation, slicing).


# my_String ="Hello, World!"
# print(my_String[0:13])
# new_String = my_String +" "+ "Welcome to Python"
# print(new_String.upper())

single_Quote_String = 'Hello World!'
double_Quotes_String = "Hello World"
multi_Quote_String = """This is a
multi-line string."""


orginal_String = "Hello World!"
new_String = orginal_String.replace("H" , "J").replace( "W" , "Z")
# print(new_String)


repeated_String = "HA"
result = repeated_String * 2
# print(result)

my_String = "Hello World!"
sub_String = my_String[0:3]
# print(sub_String)

# STRING METHODS
# print(my_String.lower())
# print(my_String.upper())


whitespace_String = "     HELLO WORLD!      "
# print(whitespace_String.strip())


sentence = "Hello Worlds!"
words = sentence.split(',')
# print (words)

fname = "John Alice"
greet = "Hello"
result = f"{greet}, {fname}! How are You? "
print(result)