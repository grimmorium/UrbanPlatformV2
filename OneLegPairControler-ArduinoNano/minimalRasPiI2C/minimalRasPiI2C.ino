/**
This is a minimal Arduino soft to let the board be seen by RPi via I2C
*/


#include <Wire.h>

#define SLAVE_ADDRESS 0x0a       // I2C address for Arduino x0A leg 1; x0B leg 2; x0C-front leg 3; x0D-front leg 4

void setup(){
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

}

// Handle request to send I2C data
void sendData() { 

}