# Lesson 5 #

**<ins> Overview:</ins>**

Since questions 1-4 and 6-7 are essentially script jobs, I took the liberty of 
creating one job where each of them are separate steps. The JenkinsFile is located in this 
package, and it builds exercises 1-4. 

For question 5, I prefer not to have a job running on my computer every day at 8am,
so for simplicity's sake, I have provided the screen shot of the necessary configuration
for a scheduled build every day at 8am GMT +2. 

![screenshot](jenkins_schedule.PNG?raw=true "Title")

For the challenge, this is the screenshot that shows how to trigger a build based on another 
build:

![screenshot](Jenkins_build_trigger.PNG?raw=true "Title")
