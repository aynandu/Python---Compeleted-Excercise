while True:
    try:
        dob=input("Enter Your DOB: ")
        age=input("Enter Age Limit : ")

        split_dob=dob.split("/")
        find_age=2021-int(split_dob[2])
        if find_age>=int(age):
            print("You are selected ☺")
            break
        else:
            print("You are not selected")
            break
    except:
        print("Please provide date in DD/MM/YY")