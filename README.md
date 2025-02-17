University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    SOUMYA RANJAN DASH
        LinkedIn: https://www.linkedin.com/in/srd00/
    Tested on:DELL Inspiron 14 7420 2-in-1 (14-inch, 2022), Windows 11


4.4 Now that you can send any keyboard commands you want to a text display on your laptop, make your own custom real-time visualizer.Have fun with this! Use whatever sensor data you like, and display it however you like. The only requirement is that the display should update in “real time” along with your sensor.<br />
<br />
**Ans:**<br />
# **A Color - Based Keyboard Device for an Interactive Computer System**

## **Goal:**
    To draw patterns in text editor using light. We will be drawing a diamond using the Red, green and blue colour. Any pattern can be drawn using the code.
## **Description:**
For the project the major components used: RP2040, APDS 9960 & JST SH 4-Pin Cable. A diagram of connection & interaction.
![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%204.4/Chart.png)

**Code Description:**

1.	We have to import all the necessary libraries for using APDS 9960 for colour and brightness detection as well as for using RP2040 as an HID (Keyboard). 
2.	All necessary code for this project is provided.
3.	We use variable "a", "g", "b" & "c" for the Red, Green, Blue and Clear(Brightness) value, respectively.
4.	When Red color is detected, the RP2040 will press the "*" key on the keyboard.
5.	When a Green color is detected, the RP2040 will press the "SpaceBar" key on the keyboard.
6.	When a Blue color is detected, the RP204 will press the "Backspace" key on the keyboard.
7.	These three basic colors will help us draw any pattern in the text editor using *.
8.	Detection of green and blue colors is easy. We can recognise the green colour when the "g" variable is the largest and the blue colour when the "b" variable is the largest among the "r", "g" & "b" variables.
9.	However, it becomes tricky to recognise the red color. Red generally has the highest intensity hence the logic used in '8' won't be valid. If we use the same logic as '8' we will get the value of the "r" variable greater than the "g" & "b" variables for any color of light.
10.	So, we have derived a formula for the detection of red color. The "red" variable, whenever crosses the value 3. We can be sure it's a RED color.
11.	 The red value is defined by :"red" = ("r" - "g") / "g".
12.	Finally, we use the clear (Brightness) {we assign the "c" variable less than 150 to indicate darkness} to exit the main loop. Whenever we want to free our keyboard and stop the program.

So the major operations being:<br />

**RED LIGHT -> Print/Press "*"**<br />
**GREEN LIGHT -> Print/Press SPACEBAR** <br />
**RED LIGHT -> Print/Press BACKSPACE**<br />
**Darkness / Low Brightness -> QUITS Program**<br />

###**Some Images / Gifs from our projects:**<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%204.4/4.4%201-1.gif)<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%204.4/4.4%201-2.gif)<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%204.4/4.4%202-1.gif)<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%204.4/4.4%202-2n.gif)<br />

<br />

**We quit as their is darkness**<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%204.4/Quit%20Photo.jpg)<br />

**Printed Diamond**<br />
<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%204.4/Diamond.png)<br />

<br />
3.2 Load this video of an actual firefly on your laptop, go to the closeup of it flashing starting around 6:52, and make the video large. https://youtu.be/BtCGtaMrBXQ?t=413. Point your sensor at the screen, and your board should now flash in sync with the firefly!<br />

**Ans:**<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%203.2/3.2%20P-1.gif)<br />

![alt text](https://github.com/satyajeetburla/ese5190-2022-lab1-firefly/blob/main/Section%203.2/3.2%20P-2.gif)<br />

