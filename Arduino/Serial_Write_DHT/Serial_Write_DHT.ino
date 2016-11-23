// DHT
#include "DHT.h"
#define DHTPIN A0
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(115200);  // open serial connection to USB Serial //port(connected to your computer)
  Serial1.begin(57600);  // open internal serial connection to MT7688
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  String sensingData  = String(t) + ":" + String(h) + "\n";
  int str_len = sensingData.length() + 1; 
  char char_array[str_len];
  sensingData.toCharArray(char_array, str_len);
  
  Serial1.write(char_array); 
  delay(1000);
  
}
