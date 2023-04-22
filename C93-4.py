#1234-4534-4355-9090
#9090-4567-2345-6109
#6767-6763-8989-3409

flag=0
while True:
    card_num=input("Enter Your Card Number: ")
    split_cdnum=(card_num.rstrip()).split("-")
    if split_cdnum[0]=="1234":
        print(f"This is VISA({split_cdnum[0]}) Card")
        break
    elif split_cdnum[0]=="9090":
        print(f"This is RuPay({split_cdnum[0]}) Card")
        break
    else:
        flag+=1
        print("Invalid Card !")
        if flag==3:
            break

