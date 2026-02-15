import serial
import winsound

PORT = "COM3"
BAUD_RATE = 9600

arduino = serial.Serial(PORT, BAUD_RATE)
print("Connected")

current_state = "OFF"

while True:
    data = arduino.readline().decode().strip()
    print(data)

    if data == "Pump ON" and current_state == "OFF":
        print("ALARM START")
        winsound.PlaySound("alarm.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        current_state = "ON"

    elif data == "Pump OFF" and current_state == "ON":
        print("ALARM STOP")
        winsound.PlaySound(None, winsound.SND_PURGE)
        current_state = "OFF"
