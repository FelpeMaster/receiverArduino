import serial
import json
import os
import glob
import pandas as pd
import sys
import time

class receiver:
    def __init__(self):
        with open('configuration.json','r') as file:
            self.deviceConf = json.load(file)
        self.connectToDevice()
        self.variablesNumber = len(self.deviceConf['deviceSelection']['variables'])
        while True:
            msg = self.readDevice().rstrip()
            self.processSaveData(msg)

    def connectToDevice(self):
        self.baudrate = self.deviceConf['deviceType']['arduino']['baudrate']
        self.device = self.checkSerialPort()[0]
        self.s = serial.Serial(self.device, self.baudrate)

    def processSaveData(self, msg):
        self.parsingProcessing(msg)

    def parsingProcessing(self, msg):
        dataString = msg.split(":")
        if self.variablesNumber == len(dataString):

    def readDevice(self):
        msg = self.s.readline()
        return  msg.decode()

    def checkSerialPort(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
if __name__ == "__main__":
    r = receiver()
