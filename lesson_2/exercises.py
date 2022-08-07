def question_1(x, y):
    if x > y:
        print("BIG")
    if x < y:
        print("small")


def question_2():
    for i in range(0, 5):
        print(i)


def question_3(x):
    match x:
        case 1:
            print("Summer")
        case 2:
            print("Winter")
        case 3:
            print("fall")
        case 4:
            print("spring")
        case _:
            print("Sorry, but there are only 4 seasons.")


from forex_python.converter import CurrencyRates


class Question5:
    c = CurrencyRates()

    def __init__(self, age, last_initial, traveled_abroad, street_number):
        self.age = age
        self.last_initial = last_initial
        self.shekel_amount = 1 / self.c.get_rate('ILS', 'USD')
        self.traveled_abroad = traveled_abroad
        self.street_number = street_number

    def print_variables(self):
        print(
            f"age: {self.age}, last initial: {self.last_initial}, current USD/ILS rate: {self.shekel_amount}, "
            f"traveled abroad: {str(self.traveled_abroad)}, street number: {self.street_number}")

    def age_plus_currency(self):
        print(f"My age plus the current shekel rate is {self.shekel_amount + self.age}")


def question_6():
    x = input("Please enter your phone number.")
    print(f"Phone number: {x}")


# Question 7
def print_hello():
    print("Hello")


def calculate():
    print(5 + 3.2)


def question_7():
    print_hello()
    calculate()


def question_8():
    name = input("Please enter your name.")
    number = int(input("Enter a number."))
    print(name)
    print(number / 2)


def question_9(num1, num2, str1, str2):
    print(num1 + num2)
    print(f'{str1} {str2}')


def question_10():
    for i in range(1, 5):
        print("#")
        for j in range(0, i):
            print("#", end=" ")
    print("#")


def question_11():
    num = 7

    for i in range(num):
        for j in range(num):
            if (i == j) or ((num - j - 1) == i):
                print('#', end='')
            else:
                print(' ', end='')
        print('')


def question_12():
    x = int(input("Enter a number which is 2 digits or more."))
    nums = [int(a) for a in str(x)]
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    print(sum)
