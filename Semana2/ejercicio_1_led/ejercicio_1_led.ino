#include "DHT.h"
#define DHTTYPE DHT11   // DHT 11

//#define dht_dpin 4 // D2
#define dht_dpin 0 // D3 
DHT dht(dht_dpin, DHTTYPE);

//#define LED D1 // LED
#define LED D4 // LED
int ValueRead=2;
int myflag=0;

void setup()
{
 //Serial.begin(9600);
 Serial.begin(115200);
 pinMode(LED, OUTPUT);
 digitalWrite(LED, LOW); //LED comienza apagado
}

void loop()
{
 if (Serial.available()){
   ValueRead=Serial.parseInt();
 }
   if (((ValueRead==1 && myflag==0)|| myflag==1)&!(ValueRead==2 && myflag==1)){
     digitalWrite(LED, HIGH);  // Se prende el LED
     Serial.println("Prendido");
     myflag=1;
   }
   else{
     digitalWrite(LED, LOW);   // Se apaga el LED
     Serial.println("Apagado");
     myflag=0;
   }
 float h = dht.readHumidity();
 float t = dht.readTemperature();
 Serial.print("Current humidity = ");
 Serial.print(h);
 Serial.print("%  ");
 Serial.print("temperature = ");
 Serial.print(t);
 Serial.println("C  ");
}