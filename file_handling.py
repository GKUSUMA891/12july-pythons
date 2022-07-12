#file handling
#open file
file=open("file_handling.py")
#read the file
file=open("file_handling.py","r")
print(file.read())
#read only perticular line
file=open("file_handling.py","r")
print(file.read(5))
#readline
file=open("file_handling.py","r")
print(file.readline())
 #we want to read two lines of data in file we call two times
print(file.readline())
print(file.readline())
print(file.readline())
   #using loop through line by line
file=("file_handling.py","r")
for i in file:
    print(i)

#close files
file=open("file_handling.py","r")
print(file.readline())
file.close()

#write to existing file
file=open("file_handling.py","a")
file.write("hello pythons learners!")
file.close()

file=open("file_handling.py","r")
print(file.read())

#create file
file=open("my_file.py","a")
file.write("hello!bannysha")
file.close()

file=open("my_file.py","r")
print(file.read())

#delete a file
import os
if os.path.exists("my_file.py"):
    os.remove("my_file.py")
else:
    print("not exist")

 #delete folder
    import os
os.rmdir("myfolder")







           
           


