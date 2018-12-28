import serial
import binascii
import datetime
import time
import json
import os
import csv

class dr4000:
    def __init__(self):
        with open('/home/pi/Documentos/receiverArduino/receiver/configuration.json','r') as file:
            self.deviceConf = json.load(file)
        self.device = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_D-if00-port0'
        self.baudrate = 38400
        self.dr = serial.Serial(
                    self.device,
                    self.baudrate,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE,
                       bytesize=serial.EIGHTBITS,
                       xonxoff=True,
                       rtscts = False,
                       timeout = 4)
        self.createDatabaseDirectory()
        self.createCsvfile()
        while True:
            data = self.getMeasurements()
            if len(data) == 2:
                self.saveMesurements(data)
                time.sleep(5)

    def saveMesurements(self,d):
        #data = {'Time':int(time.time()), 'Concentracion':d[0], 'TWA':d[1]}# data: {timestamp, concentration, twa}
        data = [int(time.time()), d[0], d[1]]
        csvfile = self.deviceConf['deviceSelection']['databaseFileDR']
        with open(csvfile, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            print (data)

    def createDatabaseDirectory(self):
        path = self.deviceConf['deviceSelection']['databaseFolder']
        os.makedirs(path, exist_ok=True)
        os.chdir(path)

    def createCsvfile(self):
        self.createDatabaseDirectory()
        csvfile = self.deviceConf['deviceSelection']['databaseFileDR']
        if not os.path.isfile(csvfile):
            variables = self.deviceConf['deviceSelection']['variablesDR4000']
            arrayOfVariableNames = ['time']
            for v, value in variables.items():
                arrayOfVariableNames.append(value)
            with open(csvfile, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=arrayOfVariableNames)
                writer.writeheader()

    def sendRequestToInstrument(self,m):
        self.dr.write(m)

    # this function works only if Rx of dr4000 works fine
    def setDate(self):
        today = datetime.datetime.now()
        m = bytearray(b'1 date 10 5 2018\r')
        self.sendRequestToInstrument(m)

    def getMeasurements(self):
        msg  = bytearray(b'1 d\r')
        self.sendRequestToInstrument(msg)
        fromdr4000 = self.dr.readline()
        try:
            aux = []
            aux = fromdr4000.decode('ascii').split('"')
            print (len(aux))
            if len(aux) == 9:
                conc = aux[3].split()[1]
                twa = aux[5].split()[1]
                return [conc, twa]
            else:
                return []
        except:
            return []

if __name__ == "__main__":
    dram = dr4000()
