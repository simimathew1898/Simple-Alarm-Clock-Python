# Simple Alarm Clock
This is a simple alarm clock program written in Python using the **pygame** library. It can be used to set an alarm for a specific time and plays a sound when the alarm time is reached. There is also an option to snooze the alarm for a specified duration.

# Prerequisites
Before running the program, make sure to install pygame library. It can be installed by running the following command:

```python
pip install pygame
```

# Usage
1. Run the script in your Python environment.
2. Enter the desired alarm time in the format HH:MM when prompted.
3. The program will continuously check the current time and compare it with the alarm time.
4. When the alarm time is reached, the program will print "It's time to wake up" and play the alarm sound repeatedly until you choose to snooze or turn off the alarm.
5. If you choose to snooze the alarm, enter "yes" when prompted and specify the duration for snoozing in minutes.
6. The program will update the alarm time based on the snooze duration and continue checking for the new alarm time.
7. If you choose not to snooze the alarm, enter any other input when prompted to turn off the alarm and exit the program.
   
Note: Make sure you have an audio file named "Alarm.mp3" in the same directory as the script. You can replace it with your own alarm sound in MP3 format.
