while True:
    try:
        name=input("Enter Name : ")
        dob=input("Enter DOB: ")
        place=input("Enter Place: ")

        split_dob=dob.split("/")
        age=2021 -int(split_dob[2])
        print(f'Hai,I am {name}(Age {age}) from {place}.')
        break
    except:
        print("Enter DOB a numeric value and seperate using '/' Symbol")

