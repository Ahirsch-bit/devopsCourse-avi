# Lesson 1 Homework Answers:

### All questions which require me to write code or build a function will be done in a separate class and will be called in main for that lesson.

**<ins> Question 1:</ins>**
Method called in Main

**<ins> Question 2:</ins>**

>2. What will be the values of a, b, c at the end?\
a = 8\
a = 17\
a = 9\
b = 6\
c = a+b\
b = c+a\
b = 8
>
 The final value of the variable will always be the last value stated. So if at the end of
 this code I were to print the results, they would be as follows:\
 a=9\
 b=8\
 c=15\
Since we have defined 'c' before we changed the value of 'b', the value of 'c' will not
change.

**<ins> Question 3:</ins>**

>3. is there a difference between the two lines below? Why?\
a. name = “john”\
b. name = ‘john’

In Python, there would be no difference, because both a single and double quote are
both acceptable for strings. The only issue is that if one were to start with a single or 
double quote, the string must be closed using the same format as was used to open the string.

**<ins> Question 4:</ins>**
>4. What is the issue with the code below? Suggest an edit.\
my_number = 5+5\
print("result is: "+my_number)

Because Python does not require one to define the variable type, they will not allow you
to concat a string and a number without first casting both to the same data type. Most languages
which require explicit data types to be defined will allow printing a string and number like this.
The code fix is in the lesson1 class, and it will be called by main.


**<ins> Question 5:</ins>**
>5. What will be the output?\
x = 5\
y = 2.36\
print(x+int(y))

The output would be 7, as 'y' is being cast to an int, which means that it will drop
anything after the decimal. This will **NOT** round the number, so if you were to cast 2.8 to
an int, the result would still be 2 and not 3.
