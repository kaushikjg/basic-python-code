
"This simple while loop code"

while True:

    v1 = int(input("Value = "))
    v2 = int(input("Value = "))
    print("Please select +,-,*,/...")
    operator = input()

    if operator=="+":
        print(f"sum of {v1} and {v2} = ",v1+v2)
    elif operator=="-":
        print(f"sub of {v1} and {v2} = ", v1 - v2)
    elif operator=="*":
        print(f"mul of {v1} and {v2} = ", v1 * v2)
    elif operator=="/":
        print(f"div of {v1} and {v2} = ", v1 / v2)
    else:
        print("Please enter valid input")
