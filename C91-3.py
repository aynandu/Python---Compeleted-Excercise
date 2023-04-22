while True:
    try:
        user_name=input("Enter Name : ")
        physics_mark = int(input("Enter Physics : "))
        chemistry_mark = int(input("Enter Chemistry : "))
        maths_mark = int(input("Enter Mathamatics : "))

        split_name=user_name.split(" ")
        total_mark=int(physics_mark)+int(chemistry_mark)+int(maths_mark)
        average=total_mark/3
        deci_num=round(average,2)

        print(f'\nFirst Name : {split_name[0]}\nSecond Name: {split_name[1]}')

        def mark_secured(mark):
            if 90<=mark<100:
                return 'A'
            elif 80<=mark<=89:
                return 'B'
            elif 70<=mark<=79:
                return 'C'
            elif 50<=mark<=69:
                return 'D'
            else:
                return 'Fail'

        if average>=50:
            print(f'Exam Status:Pass ({deci_num}%)')
        else:
            print(f'Exam Status:Failed ({deci_num}%)')

        print(f"Physics({mark_secured(physics_mark)})")
        print(f"Physics({mark_secured(chemistry_mark)})")
        print(f"Physics({mark_secured(maths_mark)})")
        print(f'Total: {total_mark}/300')
        
        break
    except:
        print("Please choose marks as numeric number")