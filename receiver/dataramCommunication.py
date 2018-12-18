import serial

class dr4000:
    def __init__(self):
        self.device = '/dev/ttyUSB0'
        self.baudrate = 9600
        dr = serial.Serial(self.device, self.baudrate)
        self.getMeasurements()

    def getMeasurements(self):
        dr.write('output\r')
        while True:
            print (dr.readline())

if __name__ == "__main__":
    dram = dr4000()
