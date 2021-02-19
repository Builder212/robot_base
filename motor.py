import serial
from time import sleep

class Motor:
    def __init__(self):
        try:
            self.usb = serial.Serial('/dev/ttyACM0', 9600)
        except:
            print("Can't connect too arduino.")

    def forward(self):
        self.usb.write(b'Forward')

    def reverse(self):
        self.usb.write(b'Reverse')

    def stop(self):
        self.usb.write(b'Stop')

    def right(self):
        self.usb.write(b'Right')

    def left(self):
        self.usb.write(b'Left')

if __name__ == "__main__":
    motor = Motor()
    motor.forward()
    sleep(2)
    motor.reverse()
    sleep(2)
    motor.right()
    sleep(2)
    motor.left()
    sleep(2)
    motor.stop()
