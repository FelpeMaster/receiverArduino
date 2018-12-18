import serial
from serial import Serial
import json
import os
import glob
import pandas as pd
import sys
import time
import csv
import numpy as np

class receiver:
    def __init__(self):
        with open('configuration.json','r') as file:
            self.deviceConf = json.load(file)
        self.connectToDevice()
        self.variablesNumber = len(self.deviceConf['deviceSelection']['variables'])
        self.createCsvfile()
        while True:
            msg = self.readDevice().rstrip()
            self.processSaveData(msg)

    def createDatabaseDirectory(self):
        path = self.deviceConf['deviceSelection']['databaseFolder']
        os.makedirs(path, exist_ok=True)
        os.chdir(path)

    def connectToDevice(self):
        self.baudrate = self.deviceConf['deviceType']['arduino']['baudrate']
        self.device = self.checkSerialPort()[0]
        self.s = serial.Serial(self.device, self.baudrate)

    def createCsvfile(self):
        self.createDatabaseDirectory()
        csvfile = self.deviceConf['deviceSelection']['databaseFile']
        if not os.path.isfile(csvfile):
            variables = self.deviceConf['deviceSelection']['variables']
            arrayOfVariableNames = ['time']
            for v, value in variables.items():
                arrayOfVariableNames.append(value)
            with open(csvfile, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=arrayOfVariableNames)
                writer.writeheader()
            print ("fichero de base de datos creado")

    def processSaveData(self, msg):
        data = self.parsingProcessing(msg)
        data = [float(i) for i in data]
        data[0] = int(data[0])
        csvfile = self.deviceConf['deviceSelection']['databaseFile']
        print (data)
        if data:
            with open(csvfile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(data)

    def parsingProcessing(self, msg):
        dataString = msg.split(":")
        [float(i) for i in dataString]
        data = [int(time.time())]
        if self.variablesNumber == len(dataString):
            return data + dataString
        else:
            return None

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
            except:
                pass
        return result
if __name__ == "__main__":
    r = receiver()
