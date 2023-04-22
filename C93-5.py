import re
value=input("Enter values: ")
split_value=re.split(r'[<>{}+xX/-]',value)

if '+' in value:
    sum=int(split_value[1])+int(split_value[6])
    print(f"{split_value[1]} + {split_value[6]} = {sum}")
if 'x' in value:
    sum=int(split_value[1])*int(split_value[6])
    print(f"{split_value[1]} x {split_value[6]} = {sum}")
if 'X' in value:
    sum=int(split_value[1])*int(split_value[6])
    print(f"{split_value[1]} x {split_value[6]} = {sum}")
if '-' in value:
    sum=int(split_value[1])-int(split_value[6])
    print(f"{split_value[1]} - {split_value[6]} = {sum}")
if '/' in value:
    if int(split_value[1]) > int(split_value[6]):
        sum=int(split_value[1])/int(split_value[6])
        print(f"{split_value[1]} / {split_value[6]} = {sum}")
    else:
        sum=int(split_value[6])/int(split_value[1])
        print(f"{split_value[6]} / {split_value[1]} = {int(sum)}")