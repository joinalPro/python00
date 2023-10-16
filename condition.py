letter = ["A", "B", "C"]

inputLetter = input("Enter the letter: ")
if inputLetter in letter:
    print(inputLetter, "is correct")
else: 
    print(inputLetter, "is not correct letter")
    
print("program terminated")