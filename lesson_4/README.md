# Lesson 4 #

**<ins> Overview:</ins>**

The automation framework that I built uses the 
Page Object Model using page factory. In addition, I used the Bonigarcia Webdriver Manager
to automatically download and set up the driver based on the current browser version.

All the answers are written and called in the 'tests.py' file. Ideally I would have separated
the functions into different files and classes in order to make my code look cleaner and
more maintainable, but since this is simply an exercise, this is sufficient. 

Whenever I created a driver instance, I added it to a list. At the end, I created a method 
to close all driver instances. If this was a work project, I probably would have made a 
singleton class in order to use the same driver instance throughout the project and only
close the driver instance at the very end. 

**<ins>Question 3:</ins>**

All webelement locaters should be the same in all browsers, as this is a requirement 
of the W3C.

**<ins>Question 6:</ins>**

By xpath: 
```
//*[@aria-label='Source text']
```
By css: 
```
[aria-label='Source text']
```
By css - different locator: 
```
[aria-autocomplete='list']
```

**<ins>Question 10,11:</ins>**
Extensions can only be disabled before the driver instance is created and not during 
runtime. Regarding Firefox, from what I have read,a new profile will automatically contain
no extensions, so creating a new profile will have the same effect. 
Edge works with Chromium, so it should work the same as Chrome. I didn't have the opportunity
to further investigate this due to time constraints. 