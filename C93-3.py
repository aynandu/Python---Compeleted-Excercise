commands=[]
while True:
    command=input("Enter Command: ")
    
    if command.upper() == "START":
        
        if command in commands:
            print("Sorry car already started !")
        else:
            commands.append(command)
            print("Car started")
            if "STOP" in commands:
                commands.remove("STOP")
    if command.upper() == "STOP":
        
        if command in commands:
            print("Sorry car already stopped")
        else:
            commands.append(command)
            print("Car stopped")
            if "START" in commands:
                commands.remove("START")
    if command.upper() == "Exit":
        break
