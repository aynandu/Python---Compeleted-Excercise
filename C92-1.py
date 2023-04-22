
temp = 0
add_temp=1
tmp_value=0
number = input("Enter Numbers : ")
character =input("Enter Sign : ")

split_number=(number.rstrip()).split(" ")
for i in split_number:
    if character=='+':
        temp = temp+int(i)
    if character=='-':
        temp = temp-int(i)
    if character=='x':
        tmp_value=add_temp
        add_temp=tmp_value*int(i)
        temp=add_temp
    if character=='/':
        temp = temp/int(i)
print("Answer: ",end="")
for j in range(len(split_number)):
    print(f'{split_number[j]} {character} ',end="")
print("\b\b=",temp,end="")
        