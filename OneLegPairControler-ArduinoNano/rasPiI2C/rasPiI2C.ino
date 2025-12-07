#include <Wire.h>
#include <Servo.h>

//Servos
volatile Servo s1 ,s2, s3, s4, s5, s6;

#define SLAVE_ADDRESS 0x0a       // I2C address for Arduino x0A-rear; x0B-middle; x0C-front
int i2cData = 0;                 // the I2C data received

char charAr[11];

short charCnt = 0;

short msgType = -1;

short S1=-1;
short S2=-1;
short S3=-1;
short S4=-1;
short S5=-1;
short S6=-1;
short DC1=-1;
short DC2=-1;

void setup(){
  Serial.begin(115200);

  s1.attach(14);
  s2.attach(15);
  s3.attach(16);
  s4.attach(17);
  s5.attach(7);
  s6.attach(8);

  Wire.begin(SLAVE_ADDRESS);
  Wire.setWireTimeout(200,false);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
}
void loop() {
  // Everything happens in the interrupts
}
// Handle reception of incoming I2C data
void receiveData(int byteCount) {

  
  while (Wire.available()) {
    i2cData = Wire.read();

    if(char(i2cData) == '>'){charCnt = 0;}
    if(charCnt == 1){
      if(DC2<0 && DC1>=0)    {DC2 = i2cData;}
      if(DC1<0 && S6>=0)     {DC1 = i2cData;}
      if(S6<0  && S5>=0)     {S6 = i2cData;}
      if(S5<0  && S4>=0)     {S5 = i2cData;}
      if(S4<0  && S3>=0)     {S4 = i2cData;}
      if(S3<0  && S2>=0)     {S3 = i2cData;}
      if(S2<0  && S1>=0)     {S2 = i2cData;}
      if(S1<0  && msgType>0){S1 = i2cData;}
      if(msgType<0)         {msgType = i2cData;}
    }
    if(char(i2cData) == '<'){charCnt = 1;}

    if(charCnt == 0){
      msgType = -1;
      S1 = -1;
      S2 = -1;
      S3 = -1;
      S4 = -1;
      S5 = -1;
      S6 = -1;
      DC1= -1;
      DC2= -1;
    }

    if(S1>=0 && S2>=0 && S3>=0 && S4>=0 && S5>=0 && S6>=0){
      s1.write(S1);
      s2.write(S2);
      s3.write(S3);
      s4.write(S4);
      s5.write(S5);
      s6.write(S6);
    }

    Serial.print(i2cData);
    Serial.print('/');
    Serial.print(charCnt);
    Serial.print('/');
    Serial.print(msgType);
    Serial.print('/');
    Serial.print(S1);
    Serial.print('/');
    Serial.print(S2);
    Serial.print('/');
    Serial.print(S3);
    Serial.print('/');
    Serial.print(S4);
    Serial.print('/');
    Serial.print(S5);
    Serial.print('/');
    Serial.print(S6);
    Serial.print('/');
    Serial.print(DC1);
    Serial.print('/');
    Serial.print(DC2);
    Serial.println('/');
  }
}

// Handle request to send I2C data
void sendData() { 

}