
def seven_boom():
    print("Let's play a game. It's called 7 boom.")
    counter = 0
    while counter < 10:
        counter = counter +1
        x = int(input("Enter a number."))
        if (x%7 == 0) or str(x).find("7")!=-1:
            print("boom")
        else:
            print(x)
    print("That was fun. Let's do this again sometime.")
