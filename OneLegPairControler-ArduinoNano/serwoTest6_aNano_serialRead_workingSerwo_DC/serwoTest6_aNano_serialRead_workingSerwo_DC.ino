#include <Servo.h>

//Servos
Servo s1 ,s2, s3, s4, s5, s6;
int s1Ordered, s2Ordered, s3Ordered, s4Ordered, s5Ordered, s6Ordered;
int s1Actual, s2Actual, s3Actual, s4Actual, s5Actual, s6Actual = -1;
int s1Cal, s2Cal, s3Cal, s4Cal, s5Cal, s6Cal;
int stepFraction = 3;
int stepInterval = 1200;
int stepIntervalCnt = 0; 

//DC motors
const int IA1=3;//?
const int IA2=5;//?
const int IB1=6;//?
const int IB2=9;//?
int mot1v = 0;
int mot2v = 0;
bool mot1dir = false;
bool mot2dir = false;

//read values from external source
int partPos;
int pos = 90;
char c;
int rChar = 1;

void setup() {
  Serial.begin(9600);
  s1.attach(14);
  s2.attach(15);
  s3.attach(16);
  s4.attach(17);
  s5.attach(7);
  s6.attach(8);

  pinMode(IA1, OUTPUT);
  pinMode(IA2, OUTPUT);
  pinMode(IB1, OUTPUT);
  pinMode(IB2, OUTPUT);
}

void loop() {
  
  //read values from external source (Serial)
  {
    if(Serial.available()>0){

      c = Serial.read();

      if(rChar==1){
        partPos = 0;
      }
      if(rChar==1){
        partPos = partPos + (c - '0') * 100;
      }

      if(rChar==2){
        partPos = partPos + (c - '0') * 10;
      }

      if(rChar==3){
        partPos = partPos + (c - '0') * 1;
        pos = partPos;
      }

      rChar++;

      if(rChar>3){
        rChar = 1;
      }
    }
  }

  //TODO
  //read values from external source (I2C)
  {

  }

  //set PWM values for DC motors
  {
    if(pos > 90){//forward: dir=true
      mot1v = pos - 90;
      mot2v = pos - 90;
      mot1dir = true;
      mot2dir = true;
    }
    else{ //reverse: dir=false
      mot1v = pos;
      mot2v = pos;
      mot1dir = false;
      mot2dir = false;
    }
  }

  //handle DC motors
  {
    if(mot1dir){
      MA1_Forward(mot1v);
    }
    else{
      MA2_Backward(mot1v);
    }

    if(mot2dir){
      MB1_Forward(mot2v);
    }
    else{
      MB2_Backward(mot2v);
    }
  }

  //set ordered position for servos (and other steering parameters)
  s1Ordered = pos;
  s2Ordered = pos;
  s3Ordered = pos;
  s4Ordered = pos;
  s5Ordered = pos;
  s6Ordered = pos;
  stepFraction = 3;
  stepInterval = 1200;

  //handle serwo
  stepIntervalCnt = stepIntervalCnt + 1;
  if(stepIntervalCnt == stepInterval){
    s1Actual = calculateChange(s1Ordered,  s1Actual, stepFraction);
    s1.write(s1Actual);
    s2Actual = calculateChange(s2Ordered,  s2Actual, stepFraction);
    s2.write(s2Actual);
    s3Actual = calculateChange(s3Ordered,  s3Actual, stepFraction);
    s3.write(s3Actual);
    s4Actual = calculateChange(s4Ordered,  s4Actual, stepFraction);
    s4.write(s4Actual);
    s5Actual = calculateChange(s5Ordered,  s5Actual, stepFraction);
    s5.write(s5Actual);
    s6Actual = calculateChange(s6Ordered,  s6Actual, stepFraction);
    s6.write(s6Actual);

    stepIntervalCnt = 0;
  }

}

//Supporting functions
int minimal(int val1, int val2){
  if(val1 < val2){
    return val1;
  }
  return val2;
}

int maximal(int val1, int val2){
  if(val1 > val2){
    return val1;
  }
  return val2;
}

int max180(int val){
  if(val > 180){
    return 180;
  }
  return val;
}

int min0(int val){
  if(val < 0){
    return 0;
  }
  return val;
}

int calculateChange(int _orderedState, int _actualState, int _stepFraction){
  int out = 0;
    if(_orderedState != _actualState){

      if(_orderedState > _actualState){
        out = max180(_actualState + minimal(_orderedState - _actualState, _stepFraction));
      }

      if(_orderedState < _actualState){
        out = min0(_actualState - minimal(_actualState - _orderedState, _stepFraction));
      }
    }
    else
    {
      out = _actualState;
    }
  return out;
}

//DC motor functions
void MA1_Forward(int Speed1)  //fast decay; Speed = High duty-cycle
{
     analogWrite(IA1,Speed1);
     digitalWrite(IA2,LOW);
}

void MA2_Backward(int Speed1)  //slow decay; Speed = Low duty-cycle
{
    int Speed2=255-Speed1;
    analogWrite(IA1,Speed2);
    digitalWrite(IA2,HIGH);
}

void MB1_Forward(int Speed1)
{
     analogWrite(IB1,Speed1);
     digitalWrite(IB2,LOW);
}

void MB2_Backward(int Speed1)
{
    int Speed2=255-Speed1;
    analogWrite(IB1,Speed2);
    digitalWrite(IB2,HIGH);
}
 