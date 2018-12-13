// Connect the Pin_3 of DSM501A to Arduino 5V
// Connect the Pin_5 of DSM501A to Arduino GND
// Connect the Pin_2 of DSM501A to Arduino D8
#include<string.h>
#include <SHT1x.h>//Se incluye la libreria SHT1X
#define dataPinSHT15 10 //Se define el pin 10 de Arduino para entrada de dato.
#define clockPinSHT15 11 //Se define el pin 11 de Arduino para sincronización reloj.
SHT1x sht1x(dataPinSHT15, clockPinSHT15); //Se inician los pines para utilizar el sensor.
float temp_c;
//float temp_f;
float humedad;


byte buff[2];
int pin = 8;//DSM501A input D8
unsigned long duration;
unsigned long starttime;
unsigned long endtime;
unsigned long sampletime_ms = 30000;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
 
int i=0;
void setup()
{
  Serial.begin(9600);
  pinMode(8,INPUT);
  starttime = millis(); 
}

void pm25DetectFunction(){
  duration = pulseIn(pin, LOW);
  lowpulseoccupancy += duration;
  endtime = millis();
  if ((endtime-starttime) > sampletime_ms)
  {
    ratio = (lowpulseoccupancy-endtime+starttime + sampletime_ms)/(sampletime_ms*10.0);  // Integer percentage 0=>100
    concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
    lowpulseoccupancy = 0;
    starttime = millis();
  }
}

void readSHT15(){
  temp_c = sht1x.readTemperatureC();
  humedad = sht1x.readHumidity();
}

void readSensors(){
  pm25DetectFunction();
  readSHT15();
}

void communicateWithReceiver(){
  Serial.print(ratio);
  Serial.print(":");
  Serial.print((int)concentration*100); // 100 veces, en receiver dividir por 100 para tener un decimal
  Serial.print(":");
  Serial.print(temp_c); 
  Serial.print(":");
  Serial.println(humedad);
}

void sendDummieMessege(){
  Serial.print("1.25");
  Serial.print(":");
  Serial.print("15.22"); // 100 veces, en receiver dividir por 100 para tener un decimal
  Serial.print(":");
  Serial.print("20.22");
  Serial.print(":");
  Serial.println("49.5");
}

void loop()
{
  readSensors();
  //communicateWithReceiver();
  sendDummieMessege();
}
