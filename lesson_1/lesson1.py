# 1. Create a program with the following:
# a. Create a variable name first with value 7.
# b. Create a variable name second with value 44.3.
# c. Print result of adding first to second.
# d. Print result of multiplying first by second
# e. Print result of dividing second by first

def exercise_1():
    print(exercise_1.__name__)
    x = 7
    y = 44.3
    print('Print result of adding first to second: ' + str(x + y))
    print(x * y)
    print('Print result of dividing second by first: ' + str(y / x))
    print()


# What is the issue with the code below? Suggest an edit.
# my_number = 5+5
# print("result is: "+my_number)

def exercise_4():
    print(exercise_4.__name__)
    my_number = 5 * 5
    print(f'using f and {{variable}}: result is:   {my_number}')
    print(f'using casting: result is:  ' + str(my_number))

# 6. Fix the following code, without changing a or b
# a = 8
# b = "123"
# print(a+b)

def exercise_6():
    a = 8
    b = "123"
    #if we want to print as a string
    print(str(a)+b)
    #if we want to add both numbers together
    print(a+int(b))
