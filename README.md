# receiverArduino
Program written in python 3 that receive arduino string with sensors data

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
```console
foo@bar:~$ python receiver.py
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
