import re
value=input("Enter Value : ")
split_value=re.split(r'[()+-]',value)
if value.find('+')>0:
    sum_value=(int(split_value[1])+int(split_value[2]))*int(split_value[3])
    print(f"Answer: <{sum_value}>")
if value.find('-')>0:
    sum_value=(int(split_value[1])-int(split_value[2]))*int(split_value[3])
    print(f"Answer: <{sum_value}>")
