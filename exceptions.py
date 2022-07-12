#exception handling
try:
 file = open("testfile", "r")
 file.write("This is my test file for exception handling!!")
except IOError:
 print ("Error: can\'t find file or read data")
else:
 print ("Written content in the file successfully")


#finnally
try:
 file = open("testfile", "w")
 file.write("This is my test file for exception handling!!")
finally:
 print ("Error: can\'t find file or read data")
 file.close()

#try,finnally,clause
try:
    file = open("testfile", "w")
    try:
        file.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
    file.close()
except IOError:
    print("Error: can\'t find file or read data")
    
# Define a function here.
def temp_convert(var):
    try:
        returnint(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n",Argument)

#user defined exceptions
class Networkerror(RuntimeError):
def __init__(self, arg):
    self.args = arg


