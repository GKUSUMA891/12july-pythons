#regex
#two strings are equal or not

line1="we are in thundersoft company"
line2="we are in thundersoft company"
if line1==line2:
    print("same")
else:
    print("different")

line1="we are in thundersoft company"
line2="thundersoft company"
if line2 in line1:
    print("present")
else:
    print("not present")

line1="we are in microsoft company"
line2="microsoft company"
if line1.find(line2):
    print("string is find:")
else:
    print("string is not find:")

line1="we are in microsoft company"
line2="microsoft"
print(line1.index(line2))

#match()
import re
line="python and java gives jython"

result=re.match(r'java',line)
print("on failure:",result)
result1=re.match(r'python',line)
print("on success:",result1)
#match
import re

line1="my favorate location is bangalore"
result=re.match(r'my favorate',line1)
if result:
    print("yes! match found")
else:
    print("match Not found")

#search
import re
txt="the rain in hyderabad"
x=re.search("the rain",txt)
if x:
    print("Yes search found")
else:
    print(" search not found")

#findall()
import re
txt="my situation is not gud"
result=re.findall("t",txt)
print(result)

line2="the rain in the spain"
result=re.findall("ai",line2)
print(result)
if result:
    print("yes! 'ai' present two times")
else:
    print("no 'ai' not present in line2")

#split
    import re
txt="Hello! jijju how are you gal"
result=re.split("\s",txt)
print(result)
if result:
    print("split the string")
else:
    print("not split the string")

      #split
import re
txt1="the rain in spain"
xx=re.split("\s",txt1,1)
print(xx)

#sub()
import re
txxt="the rain in spain was goody"
result=re.sub("\s","9",txxt)
print(result)
if result:
    print("Yes replace the digit with whitespace")
else:
    print("not replace the digit iwth whitespace")
     #sub
import re
txxt="the rain in spain was goody"
result=re.sub("\s","9",txxt,2)
print(result)

#fullmatch()
import re
line="we are in python"
res=re.fullmatch("we are in python",line,flags=re.IGNORECASE)
print(res)

import re
line="we are in python"
res=re.fullmatch("are in python",line,flags=re.IGNORECASE)
print(res)

#finditer()
import re
text="abcdefghijklabcmnopqrsabctuvwxyz"
res=re.compile("abc")
result=re.finditer(res,text)
for i in result:
    print(i)

#compile,finditer
import re
text1="123defghijkl123mnopqrs123tuvwxyz"
res1=re.compile("123")
result1=re.finditer(res1,text1)
#print(result1)
for i in result1:
    print(i)

#subn()
import re
text1="abc defghijkl abc mnopqrs abc tuvwxyz"
res3=re.compile("123")
result3=re.subn(res3,"xyz",text1)
print(result3)

#start(),end(),span()
import re
string="39801 356,2101 1111"
res="(\d{3}) (\d{2})"
match=re.search(res,string)
if match:
    print("group:",match.group())
    print("start:",match.start())
    print("end:",match.end())
    print("span:",match.span())
else:
    print("pattern not found")


#escape()
import re
print(re.escape("hello 123.?!@ world"))

