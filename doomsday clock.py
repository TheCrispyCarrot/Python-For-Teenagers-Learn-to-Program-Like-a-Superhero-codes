import time 

print("Sinister loop stands before you.")
print("He says: \"You are doomed wonder boy!\"")
print("")

for i in range (10, 0, -1):
    print(i, "Mississippi")

    if i == 5:
 #      time.sleep(1)  
       print("Any last words Wonder Boy?")
       continue
  

    time.sleep(1)

print("Nothing happens! Foiled again wonder boy!!!")
