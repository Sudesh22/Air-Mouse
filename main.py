import serial, time, pyautogui

# # print(pyautogui.size())
# # pyautogui.moveTo(100,100,duration=1.3)
# while 1:
#     # try:    
#         ser = serial.Serial("COM6", 9600)
#         time.sleep(0.1)
#         value = ser.readline().decode()
#         print(value)
#     # except serial.serialutil.SerialException:
#         print("Arduino not connected....")

# # ser = serial.Serial('COM3', 9600)
# # if not ser.isOpen():
# #     ser.open()
# # print('com3 is open', ser.isOpen())

# import serial

ser = serial.Serial(
    port='/COM6',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

while(True):
    x,y,z = str(ser.readline().decode()).split("\t")
    print("x:",x,"y:",y,"z:",z)
    if float(x)<1:
        x=="1"
    if float(y)<1:
        y=="1"
    if float(z)<1:
        z=="1"
    pyautogui.moveTo(x=float(y)*50,y=float(z)*50,duration=1.3)

ser.close()