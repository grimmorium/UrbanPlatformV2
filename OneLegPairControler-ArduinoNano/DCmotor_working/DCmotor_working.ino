
int DC_IA1 = 9;
int DC_IA2 = 5;


bool dir = true;

void setup() {
  // put your setup code here, to run once:
  pinMode(DC_IA1, OUTPUT);
  pinMode(DC_IA2, OUTPUT);
}

void loop() {
     Forward_slow_decay(200);//Motor MA1 forward; PWM speed control
     delay(1000);
     /*
     digitalWrite(DC_IA1, HIGH);
     digitalWrite(DC_IA2, HIGH);
     delay(1000);
     */
     Backward_slow_decay(200);//Motor MA2 backward; PWM speed control
     delay(1000);
     /*
     digitalWrite(DC_IA1, HIGH);
     digitalWrite(DC_IA2, HIGH);
     delay(1000);
     */
}

void Forward_slow_decay(int Speed1)
{
     digitalWrite(DC_IA1,HIGH);
     analogWrite(DC_IA2,Speed1);
}

void Backward_slow_decay(int Speed1)
{
     analogWrite(DC_IA1,Speed1);
     digitalWrite(DC_IA2,HIGH);
}

