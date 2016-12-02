// OLED
#include <Wire.h>  //載入I2C函式庫
#include <SeeedOLED.h> //載入SeeedOLED函式庫

// Buffer to store incoming commands from serial port
String inData;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);  // open serial connection to USB Serial                           //port(connected to your computer)
  Serial1.begin(57600);  // open internal serial connection to MT7688
  
  // OLED
  Wire.begin();
  SeeedOled.init();  
  SeeedOled.clearDisplay();  //清除螢幕
  SeeedOled.setNormalDisplay(); //設定螢幕為正常模式(非反白)
  SeeedOled.setPageMode();  //設定尋址模式頁模式
  SeeedOled.setTextXY(0,0); //設定啟始坐標
}

void loop() {
  // put your main code here, to run repeatedly:

  while (Serial1.available() > 0){
    char recieved = Serial1.read();
    inData += recieved; 

    // Process message when new line character is recieved
    if (recieved == '\n')
    {
      Serial.print("Arduino Received: ");
      Serial.print(inData);
        
      // OLED
      char *p = const_cast<char*>(inData.c_str());
      SeeedOled.clearDisplay();  //清除螢幕
      SeeedOled.setTextXY(1,0); //設定啟始坐標
      SeeedOled.putString(p); 
      
      inData = ""; // Clear recieved buffer
    }
  } 
     
}
