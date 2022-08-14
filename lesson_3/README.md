# Lesson 3 #

**<ins> Question 1:</ins>**

>Write the following code:\
a = 1/0\
&nbsp;&nbsp;&nbsp;&nbsp;a. Build a corresponding try-except block to avoid exception

Method written in .py file and called in main. Because I know
that the error will be a ZeroDivisionError, I am only creating an 
exception for that error. Should other errors occur, I will want the
error thrown.

**<ins> Question 2:</ins>**

>Is the following code legal?\
```python
try:
    x = 1
finally:
    print("finally")
```
The code is legal (albeit useless), because when there is a try statement
without an except, it won't catch any errors, so essentially it's
the same as writing
```python
x=1
print("finally")
```
**<ins> Question 3:</ins>**

>What exception types can be caught by the following handler?
```python
except:
    print("found an error")
```
Since the exception type is not specified, this handler will catch
all exceptions. If you want to ignore only specific exceptions, this needs
to be specified. 

**<ins> Question 4:</ins>**

>What is wrong with using the above type of exception handler?

General catch/except statements should be used with
caution, as this can make your code run without warning while not actually
working properly. Since the exception type is not specified, your code will not only
ignore exceptions that you know about, but it will ignore ALL exceptions, even ones that
you possibly will want to be notified about.

**<ins> Question 5:</ins>**

>What exceptions can be caught by the following handlers?\
&nbsp;&nbsp;&nbsp;&nbsp;a. except IOError\
&nbsp;&nbsp;&nbsp;&nbsp;b. except ZeroDivisionError

Only IOError and ZeroDivisionError will be caught respectively, as they are stated.

**<ins> Questions 6,7,8:</ins>**

>6. Create a text file named “words.txt” programmatically\
>a. Write your name into the file
>7. Read your file content and print it
>8. Write Hebrew content into your text file and print its content programmatically.

Called in main.

**<ins> Questions 9:</ins>**
