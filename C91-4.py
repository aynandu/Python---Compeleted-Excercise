while True:
    try:
        symbol = input("Enter a symbol : ")
        limit = int(input("Enter limit: "))

        for i in range(1,limit+1):
            print(f'{symbol*i}{i}')
        break
    
    except:
        print("please provide limit a numeric value.")