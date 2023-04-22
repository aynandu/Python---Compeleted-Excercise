import re
data=input("Enter Data(Example: Name, Phone, Address) : ")
split_data=re.split(r'[, ]',data.rstrip())
if data.find(" ")>0:
    print(f'Name: {split_data[0]}\nPhone: {split_data[2]}\nAddress: {split_data[4]}')
else:
    print(f'Name: {split_data[0]}\nPhone: {split_data[1]}\nAddress: {split_data[2]}')

