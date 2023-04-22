first_word=input("Enter Word 1 : ")
second_word=input("Enter Word 2 : ")
New_Word=""
print(f"Length of the Word One and Word Two is {len(first_word)+len(second_word)}\nFirst Word Length is {len(first_word)}\nSecond Word Length is {len(second_word)}")

for i in range(max(len(first_word),len(second_word))):
    if i < len(first_word):
        New_Word+=first_word[i]
    if i < len(second_word):
        New_Word+=second_word[i]
print(f"Mix: {New_Word}")
