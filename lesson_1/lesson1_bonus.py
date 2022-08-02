# 1. Write a python program to swap two numbers using a third variable
# 2. Write a python program to swap two numbers without using third variable
# 3. Write a python program to read two numbers and find the sum of their cubes
# 4. Write a python program to read three numbers and if any two variables are equal , print that number
# 5. Write a python program to read three numbers and find the smallest among them


def question1(a, b):
    print("Question 1:")
    print("Here is how we swap numbers using a third variable.")
    print(f"""
    a = {a}
    b = {b}
    c = a
    a = b
    b = c """)
    c = a
    a = b
    b = c
    print(f"So now a = {a}, and b = {b}")


def question2(a, b):
    print("Question 2:")
    print("Here is another way to switch the numbers.")
    a, b = b, a
    print(f"So now a = {a}, and b = {b}")


def question3(a, b):
    print("Question 3:")

    print("The sum of the cubes of both numbers are " + str(a ** 3 + b ** 3))


def question4(a, b):
    print("Question 4:")
    c = int(input("Enter a value for 'c'."))
    if a == b or a == c:
        print(a)
    elif b == c:
        print(b)
    else:
        print("None of those numbers are equal.")


def question5(a, b):
    print("Question 5:")
    c = int(input("Enter a value for c."))
    smallest = a
    if b < a and b < c:
        smallest = b
    elif c < b and c < a:
        smallest = c
    print(f"The smallest number out of the 3 is {smallest}.")
    print("Another way of finding the smallest number is to put them in a list and sort them.")
    number_list = [a, b, c]
    number_list.sort()
    print(f"The smallest number is {number_list[0]}")
