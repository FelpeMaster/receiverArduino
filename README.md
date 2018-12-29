# Overview

This is a repository development to communicate sensors to raspberry pi or GNU/Linux pc, using usb port and arduino uno as interface.

In this project sensors are:

PM analyzer Dataram 4000 by Thermo Thermo Scientific
CSS811 TVOC, eCO2 and temperature sensor.

For this sensors two python scripts was developmented, and two services to systemd was created to get automatilly data from this sensores were both are connected to raspberry pi.

# receiverArduino
Program written in python 3 that receive arduino string with sensors data

# dataramCommunication
Program written in python 3 that receive measurements from DR 4000.

## dust_humidity.ino
Dependencies: stht1x, source: https://github.com/practicalarduino/SHT1x

## receiver.py
python dependencies:<br /> 
  pyserial<br />
  pandas<br />
  standard libraries
json file:
  configuration.json
  
## To run program

### receiver.py
```console
foo@bar:~$ python3 receiver.py
```

### dataramCommunication.py
```console
foo@bar:~$ python3 dataramCommunication.py
```

## Database
  Data will save in csv file for later processing

## To do
  Update data into cloud<br />
  Realtime receiver visualization

## Acknowledgments
To all people that share information in the world. <br />
special to:<br />
Thomas for reply how detect all serial ports in differents os machines in that thread<br/>
https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python <br />
Best regards!!
