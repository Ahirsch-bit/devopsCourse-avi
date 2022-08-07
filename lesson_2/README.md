# Lesson 2 #

**<ins> Question 1:</ins>**\
Method called in Main.\
The first problem is simply to create a method which accepts
two variables, which checks if the first number is bigger or 
smaller than the second. This is a simple "if" function.

Ideally there would be an option if they were equal, but this 
wasn't specifically requested in the exercise, so if the
numbers are equal, the method will do nothing.

**<ins> Question 2:</ins>**\
Method called in main. Simple for loop in range.

**<ins> Question 3:</ins>**\
The question asked for a variable to be initialized with a number 
between 1 and 4, and assign them seasons with "if" function.
Generally if I have to use "if" more than twice, I use a switch
case, or in Python, it's called match case. I added a default 
value just in case the user doesn't know how to count to 4.

**<ins> Question 4:</ins>**\

>While loop:\
a. how many times will the following loop run?\
b. what will be printed last?
```python
count =1
while count <11:
    print(count)
    count = count + 1
```

In this scenario, the loop will run 10 times, and the last 
printed number will be 10, as the first iteration starts with 
1 and when the counter reaches 11, the program will exit the loop.

**<ins> Question 5:</ins>**\
Since these are all attributes of a person, it makes the most sense
to create a class and initialize the object before calling the methods.
