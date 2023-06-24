'''
Alarm Clock
'''

#Import Required libraries
from datetime import datetime,timedelta #Basic date and time types
import time
import pygame #To play alarm sounds

# Initialize Pygame to ensure modules are properly set up and ready to be used in the program
pygame.init()

#Get the time to set alarm
time_for_alarm = input('Enter the time to set the alarm: ')
alarm_time = datetime.strptime(time_for_alarm, '%H:%M').time()

while True:
  #Checking whether its alarm time
  if datetime.now().time().hour >= alarm_time.hour and datetime.now().time().minute >= alarm_time.minute:
    print('Its time to wake up')
    # Initialize mixer module
    pygame.mixer.init()
    # Load the alarm sound and play it
    pygame.mixer.music.load("Alarm.mp3")
    pygame.mixer.music.play(-1) #Play the music until alarm switched off
    
    snooze_input = input('Do you want to snooze the alarm: ')
    # Checking whether snooze needs to be applied
    if snooze_input == 'yes':
      pygame.mixer.quit()
      snooze_duration = int(input('Enter the snooze duration: '))
      alarm_time = (datetime.now() + timedelta(minutes = snooze_duration)).time()

    else:
      pygame.mixer.quit()
      break

  time.sleep(1)
  
pygame.quit()
