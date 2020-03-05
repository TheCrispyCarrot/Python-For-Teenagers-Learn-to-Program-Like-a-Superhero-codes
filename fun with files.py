

#code is used in order to open a new file, but it does not exist so it creates it
newFile = open("CreatedFile.txt", 'w')

#code simmilar bit it writes to the text file
newFile.write("Look, we created a brand new file using python code!\n")
newFile.write("Look, a second line in the file!\n")

# saves and closes the new file
newFile.close()

# opens the file CreatedFile.txt
read_me_seymour = open("CreatedFile.txt", 'r')

print("THIS IS THO ORIGINAL TEXT IN THE FILE")
print(read_me_seymour.readline())
print(read_me_seymour.readline())

#close the file again
read_me_seymour.close()

#opens the file again to add some text to it
addingToFile = open("CreatedFile.txt", 'a')

addingToFile.write("this is some additonal added text")

#closes the file again
addingToFile.close()

############################################

#opens file to read it
print("THIS IS THE ADDED TEXT IN THE FILE")
appendedFile = open("CreatedFile.txt", 'r')

#using a loop to print the lines in the file
for line in appendedFile:
    print(line)

#closes the file agian
appendedFile.close()
