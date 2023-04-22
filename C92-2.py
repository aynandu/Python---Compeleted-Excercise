import re

value = input("Enter two value along with '#' : ")
split_value = re.split(r'[#+-/x ]', value.rstrip())
val = value.find("x")

if value.find("+") > 0:
    Total = int(split_value[1]) + int(split_value[3])
    print(f'Answer : #{Total}')

if value.find("x") > 0:
    Total = int(split_value[1]) * int(split_value[3])
    print(f'Answer : #{Total}')
    
if value.find("-") > 0:
    Total = int(split_value[1]) - int(split_value[3])
    print(f'Answer : #{Total}')

