name= input("Enter Name : ")
print(name)
split_text= name.split(" ")
for length in split_text:
    if len(length)>1:
        print(">"+'='*(len(length)-2),end="< ",)
    elif len(length)==1:
        print("=",end=" ")
   