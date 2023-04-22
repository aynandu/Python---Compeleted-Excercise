name= input("Enter Name : ")
print(name)
for i in name:
    if i == ' ':
        print(" ",end="")
    else:
        print("=",end="")
