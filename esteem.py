print("This program is an implementation of the Rosenberg")
print("Self-Esteem Scale. This program will show you ten")
print("statements that you could possibly apply to yourself.")
print("Please rate how much you agree with each of the")
print("statements by responding with one of these four letters:")

print("'D' means you strongly disagree with the statement.")
print("'d' means you disagree with the statement.")
print("'a' means you agree with the statement.")
print("'A' means you strongly agree with the statement.")

#Ask User for input on questions.\

def question_statement():

    List_Positive = []
    List_Negative = []

    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    List_Positive.append = input("Enter D, d, a, or A: ")
    print()
    print("2. I feel that I have a number of good qualities.")
    List_Positive.append = input("Enter D, d, a, or A: ")
    print()
    print("3. All in all, I am inclined to feel that I am a failure.")
    List_Negative.append = input("Enter D, d, a, or A: ")
    print()
    print("4. I am able to do things as well as most other people.")
    List_Positive.append = input("Enter D, d, a, or A: ")
    print()
    print("5. I feel I do not have much to be proud of.")
    input("Enter D, d, a, or A: ")
    print()
    print("6. I take a positive attitude toward myself.")
    input("Enter D, d, a, or A: ")
    print()
    print("7. On the whole, I am satisfied with myself.")
    input("Enter D, d, a, or A: ")
    print()
    print("8. I wish I could have more respect for myself.")
    input("Enter D, d, a, or A: ")
    print()
    print("9. I certainly feel useless at times.")
    input("Enter D, d, a, or A: ")
    print()
    print("10. At times I think I am no good at all.")
    input("Enter D, d, a, or A: ")

    print(List_Negative)
    print(List_Positive)