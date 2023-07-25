from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import schedule

running = True
upgrade_count = 1
upgrade_limit = 10
print('Program has STARTED!!')

#Y corr is 64 difference between each button
#[Name, x-Corr, y-Corr]

click_location = [
    ['Cursor', 1177, 310],
    ['Grandma',1177, 374],
    ['Farm', 1177, 438],
    ['Mine', 1177, 502],
    ['Factory', 1177, 566],
    ['Bank', 1177, 630],
    ['Temple', 1177, 694],
    ['Wizard Tower', 1177, 758],
    ['Shipment', 1177, 822],
    ['Alchemy Lab', 1177, 886],
    ['Q1', 1177, 950],
    ['Q2', 1177, 1014],
    ['index', 991, 197]
]
 
#Clicking function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This is the pause in between clicks
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
#Upgrade function
def upgrade():
    for location in click_location[::-1]:
            click(location[1], location[2])
            time.sleep(.03)

schedule.every(10).seconds.do(upgrade)

#Main Program    
while running:
    
    #random clicks on screen
    click(random.randint(150,230), random.randint(600,650))
    
    schedule.run_pending()
    
    #Fail Safe
    if keyboard.is_pressed('down'):
        running = False
        print('The program has ENDED...')
        
upgrade_count += 1
time.sleep(.0001)