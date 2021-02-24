import serial
from time import sleep

class Motor:
    def __init__(self):
        try:
            self.usb = serial.Serial('/dev/ttyACM0', 9600)
            sleep(2)
        except:
            print("Can't connect too arduino.")

    def forward(self):
        self.usb.write(b'F')

    def reverse(self):
        self.usb.write(b'B')

    def stop(self):
        self.usb.write(b'S')

    def right(self):
        self.usb.write(b'R')

    def left(self):
        self.usb.write(b'L')

    def close(self):
        self.usb.close()

if __name__ == "__main__":
    motor = Motor()
    motor.forward()
    print("1")
    sleep(2)
    motor.reverse()
    print("2")
    sleep(2)
    motor.right()
    print("3")
    sleep(2)
    motor.left()
    print("4")
    sleep(2)
    motor.stop()
    print("5")
    sleep(2)
    motor.close()
