limit=int(input("Enter Limit: "))
skip=input("Skip : ")
split_skip=list(skip.split(","))

for lmt in range(1,limit+1):
    if str(lmt) in split_skip:
        continue
    else:
        print(f"\n{lmt}")