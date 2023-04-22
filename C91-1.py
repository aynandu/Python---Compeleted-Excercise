while True:
    try:
        start_number = int(input("Enter the start point number : "))
        ending_number = int(input("Enter the end point number : "))
        if ending_number > start_number:
            for i in range(start_number,ending_number+1):
                print(f'{start_number} - {ending_number}\n',)
                start_number+=1
                ending_number-=1
            break   
        elif ending_number < start_number:
            print("Start point should a less value than end point.")
        else:
            print("Start point and end point can't be equal.")
     
    except:
        print("Please enter a number!")
    