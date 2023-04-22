while True:
    try:
        limit = int(input("Enter Limit : "))
        table_value =int(input("Enter Table : "))
        for limit in range(1,limit+1):
            value = limit*table_value
            print(f'{limit:02d} x {table_value} = {value:02d}')
        print('.'*limit,end="End")
        break
    except:
        print("Please enter a Number !")