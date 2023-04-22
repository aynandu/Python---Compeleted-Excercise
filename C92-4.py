import re
value=input("Enter Value : ") 
split_value=re.split(r'[-@#*]',value.rstrip())
print(split_value)
print(f'Roll No: {split_value[0]}\nName: {split_value[1]}\nPhone: {split_value[2]}\nPlace: {split_value[3]}\nEmail: {split_value[4]}@{split_value[5]}')