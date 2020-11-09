import serial, time
arduino = serial.Serial('COM4', 9600)
time.sleep(2)
rawString = "2"
arduino.write(rawString.encode())
#arduino.close()