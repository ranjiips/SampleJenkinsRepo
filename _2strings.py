#strings in python

a="Ranjith"
b='Kumar'
print(a)
print(b)
c="string with 'single quotes'"
d='string with "double quotes"'
print(c)
print(d)
e="string with \"double quotes\""
f='string with \'single quotes\''
print(f)
g="string with single quote's"
print(g)
h="string written in multiple lines\
 but displaying in single line\
 continuing the line"
print(h)
print(50*"*")
print("string manipulation")
name="Ranjith"
n=name[3]
print("print 3rd index character: "+n)

lname="Kumar"
# print("print last 2nd character: "+lname)

length=len(name)
print("Name length: "+str(length))
print("2nd character from reverse: "+name[length-2])
print("Name in upper case: "+name.upper())
print("Last name in lower case: "+lname.lower())
print("Concatenation: "+name+" "+lname)

#replace string
text="xdfghbgfhxdftfght"
print("Replace string: "+text.replace("xdf","AAAA"))
print("Replace string given instance: "+text.replace("xdf","AAAA",1))

#substring - slicing
text="xdfghbgfhxdftfght"
sub=text[2]
print(sub)
sub=text[2:8]
print(sub)  #fghbgfh   fbh
sub=text[2:9:3]     #last number is skip the alternate value
print(sub)

#slicing  and Indexing
name="Ranjith"
print(name[:])      #Ranjith
print(name[2:])     #njith
print(name[:3])     #Ran
print(name[2:5])    #nji
print(name[3])      #j
print(name[-3])     #i
print(name[:-2])    #Ranji
print(name[::])     #Ranjith
print(name[::2])    #Rnih

#Reverse the string
print(name[::-1])   #htijnaR
print(name[::-2])   #hinR
print(name[::-3])   #hjR

#string formatting
country="India"
content="Enjoy well"
a=10
b=True
string1="Welcome to Incredible "+country+"! "+content
string2="Welcome to Incredible %s! %s %r %r"%(country,content,bool(a),b)
print(string1)
print(string2)
print("I am from %s"%(country))
print("I am from %s"%country)

print(bool(a))

# from typing import List

# fname='Ranjith'
# lname : str='Kumar'
# fname=fname.upper()
# print(fname)
# print(lname.lower())
# print(type(fname))
# print(type(lname))

# number = 1
# num1: int=5
# print(number)
# print(num1)

