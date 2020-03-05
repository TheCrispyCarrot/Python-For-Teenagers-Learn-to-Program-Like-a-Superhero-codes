# import the module os (a directory that allows us to work with the operating system)
import os

#use the getcwd() method of the os module
#to see what directory we are in
os.getcwd()

"""
this is commented out because the directory has already been created
and running the program and recreating it will create an error   """
# creates a new directory
os.mkdir("newDirectory")


#using the chdir() mehtod in order to change directories
#dont forget to change all the back slashes to forward slashes

#changing to a new directory
print("changing to a new directory")
os.chdir("C:/Users/Garrett/AppData/Local/Programs/Python/Python38/learningPythonBook/newDirectory")
print(os.getcwd())

# changing back to the original directiory
print("changing back to the original directiory")
os.chdir("C:/Users/Garrett/AppData/Local/Programs/Python/Python38/learningPythonBook")
print(os.getcwd())


# deleting the newDirectory folder with the rmdir() mehtod
os.rmdir('newDirectory')
