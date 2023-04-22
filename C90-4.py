import  random 
collection_list=[]
while True:
    try:
        names = int(input("Enter collection limit = "))
        if 2< names <=10:
            for limit in range(1,names+1):
                collection_list.append(input(f"Enter Name {limit}: "))
            selection = random.choice(collection_list)
            print(f'Hai {selection}({int(collection_list.index(selection))+1})')
            break
        elif names >10 :
            print("Sorry ! Only 10 names are allowed")
        else :
            print("Minimum 3 names required")
    except:
        print(" Please enter a number ! ")
