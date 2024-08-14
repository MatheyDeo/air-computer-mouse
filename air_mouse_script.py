import serial, pyautogui, pydirectinput, serial
from serial import Serial

#=========================CONFIG========================================#

speed = 20 #speed of mouse (higher = faster)

# COM port of the esp32 should look like "COM1" , "COM3", "COM12" etc.
# COM port of the esp32 can be seen trough Device Manager
COMport = "COM3" 

# PyAutoGUI failsafe stops the script when the cursor touches any corner of the screen.
# However, this can make clicking on objects near them troublesome.
# False = OFF | True = ON
pyautogui.FAILSAFE = False

# inverts up and down motion of the cursor.
invert_Y_Axis = True

#========================END OF CONFIG==================================#

pydirectinput.PAUSE = 0

keysDown = {}
pressed0= pressed1= pressed2= pressed3= Lmousedown= Rmousedown= Mmousedown= False

def keyDown(key):
    keysDown[key] = True
    pydirectinput.keyDown(key)

def keyUp(key):
    if key in keysDown:
        del (keysDown[key])
        pydirectinput.keyUp(key)


ser = serial.Serial(COMport, 115200)
data = []
pyautogui.PAUSE = 0
button_pressed = False

print("air Script Init. complete")
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().rstrip()
        if data.startswith("S"):
            elements = data[1:].split(",")
            print(f"{elements[0]},{elements[1]},{elements[2]},{elements[3]},{elements[4]},{elements[5]}")
            button1,button2,button3,button4,button5 = elements[0],elements[1],elements[2],elements[3],elements[4],

            if(invert_Y_Axis): ymovement = int(elements[5])*2
            else: ymovement = -int(elements[5])*2

            if button4 == "1": pyautogui.move(-int(elements[4])*2, ymovement)


            if (button1 == "1") and (Lmousedown == False): # left button
                pyautogui.mouseDown(button='left')
                Lmousedown = True
            elif (button1 == "0") and (Lmousedown == True):
                pyautogui.mouseUp(button='left')
                Lmousedown = False

            if (button2 == "1") and (Rmousedown == False): # right button
                pyautogui.mouseDown(button='right')
                Rmousedown = True
            elif (button2 == "0") and (Rmousedown == True):
                pyautogui.mouseUp(button='right')
                Rmousedown = False

            if (button3 == "1") and (Mmousedown == False): # middle button
                pyautogui.mouseDown(button='middle')
                Mmousedown = True
            elif (button3 == "0") and (Mmousedown == True):
                pyautogui.mouseUp(button='middle')
                Mmousedown = False
