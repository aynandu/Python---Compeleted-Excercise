number = input("Enter Numbers: ")
character =input("Enter Join Character: ")

split_data=number.split(" ")

for i in split_data:
    print(f"{i}{character}",end="")