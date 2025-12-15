
int IA1 = 9;
int IA2 = 5;


bool dir = true;

void setup() {
  // put your setup code here, to run once:
  pinMode(IA1, OUTPUT);
  pinMode(IA2, OUTPUT);
}

void loop() {
     Forward(200);//Motor MA1 forward; PWM speed control
     delay(1000);
     /*
     digitalWrite(IA1, HIGH);
     digitalWrite(IA2, HIGH);
     delay(1000);
     */
     Backward(200);//Motor MA2 backward; PWM speed control
     delay(1000);
     /*
     digitalWrite(IA1, HIGH);
     digitalWrite(IA2, HIGH);
     delay(1000);
     */
}




void Forward_slow_decay(int Speed1)
{
     digitalWrite(IA1,HIGH);
     analogWrite(IA2,Speed1);
}

void Backward_slow_decay(int Speed1)
{
     analogWrite(IA1,Speed1);
     digitalWrite(IA2,HIGH);
}

