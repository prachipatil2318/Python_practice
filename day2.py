# Dynamically Typed Language :- We don't need to mention the name of what type of data is been store in particular variable, python automatically identifies and save the data in respective variable
'''
n=10
print("n:",n)
print("Datatype of n:",type(n))
print("*********************")
n='Python'
print("n:",n)
print("Datatype of n:",type(n))
print("*********************")
n=10.77
print("n:",n)
print("Datatype of n:",type(n))
print("*********************")
'''
# Intrepreted Langauage :- Execute line to line code
'''
n=10
print("n:",n)
print("Datatype of n:",type(n))
print("*********************")
n='Python'
print("n:",n)
print("Datatype of n:",type(n))
print("*********************") #will execute till here
n=10.77
prin("n:",n) #will give error on this line
print("Datatype of n:",type(n))
print("*********************")
'''
# Identifiers :- It is a user defined name given to a variable, class, functions.
'''
1. Identifiers can be alpha numeric but should not start with number.
2. Identifiers Can not be keywords.
3. Identifiers are case sensitive.
4. The only special character allow while declaring identifier is underscore(_).
'''
# Keywords :- Reserved Words. There are 35 Keywords in python and 32 in C. First we need to import it as "import keyword print(kwlist)"
'''
import keyword
print(keyword.kwlist)
=> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
# Indentation :- One tab space is use to declare the block for any function. This One Tab space is called Indentation.
'''
n=1
if n>5:
    print(n,"is greater that 5")
else:
    print(n,"is not greater that 5")
print("Byee")
'''
# Comments :- The Unexecutable line are called as comments and we declare 1 line comment by '#' where as multi line comment is declare by ''' line of info ''' OR """ Line of info """.

#Data Type
"""
1. Integer - Whole number and can be store in - Decimal, Binary, Octal, Hexa Decimal
"""
# Base Conversion
'''
a=5
print(a)
print(bin(a))
print(oct(a))
print(hex(a))
'''


