#include <TMCStepper.h>         // TMCstepper - https://github.com/teemuatlut/TMCStepper
#include <SoftwareSerial.h>     // Software serial for the UART to TMC2209 - https://www.arduino.cc/en/Reference/softwareSerial
#include <AccelStepper.h>

/*
Stepper 1
*/
#define EN_PIN           2      // Enable - PURPLE
#define DIR_PIN          3      // Direction - WHITE
#define STEP_PIN         4      // Step - ORANGE
#define SW_SCK           8      // Software Slave Clock (SCK) - BLUE
#define SW_TX            12      // SoftwareSerial receive pin - BROWN
#define SW_RX            13      // SoftwareSerial transmit pin - YELLOW
#define DRIVER_ADDRESS   0b00   // TMC2209 Driver address according to MS1 and MS2
#define R_SENSE 0.11f           // SilentStepStick series use 0.11 ...and so does my fysetc TMC2209 (?)

SoftwareSerial SoftSerial(SW_TX, SW_RX);                          // Be sure to connect RX to TX and TX to RX between both devices

TMC2209Stepper TMCdriver(&SoftSerial, R_SENSE, DRIVER_ADDRESS);   // Create TMC driver

AccelStepper stepper = AccelStepper(stepper.DRIVER, STEP_PIN, DIR_PIN);

int DC_IA1 = 9;
int DC_IA2 = 5;


bool dir = true;

void setup() {
  // put your setup code here, to run once:
  pinMode(DC_IA1, OUTPUT);
  pinMode(DC_IA2, OUTPUT);

  SoftSerial.begin(115200);           // initialize software serial for UART motor control
  TMCdriver.beginSerial(115200);      // Initialize UART

  pinMode(EN_PIN, OUTPUT);           // Set pinmodes
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  digitalWrite(EN_PIN, LOW);         // Enable TMC2209 board  

  TMCdriver.begin();                                                                                                                                                                                                                                                                                                                            // UART: Init SW UART (if selected) with default 115200 baudrate
  TMCdriver.toff();                 // Enables driver in software
  TMCdriver.rms_current(1500);        // Set motor RMS current
  TMCdriver.microsteps(8);         // Set microsteps

  TMCdriver.en_spreadCycle(false);
  TMCdriver.pwm_autoscale(true);     // Needed for stealthChop
  
  stepper.setMaxSpeed(80000); // 100mm/s @ 80 steps/mm
  stepper.setAcceleration(50000); // 2000mm/s^2
  stepper.setEnablePin(EN_PIN);
  stepper.setPinsInverted(false, false, true);
  stepper.enableOutputs();

  TMCdriver.shaft(dir);
}

void loop() {

  /*move stepper 1*/
  if (stepper.distanceToGo() == 0) {
      stepper.disableOutputs();
      //delay(10);
      stepper.move(16000); // Move 100mm
      dir = !dir;
      TMCdriver.shaft(dir);
      stepper.enableOutputs();
    }
  stepper.run();

  /*move DC motor*/
   //  DC_Forward_slow_decay(200);//Motor MA1 forward; PWM speed control

     DC_Backward_slow_decay(200);//Motor MA2 backward; PWM speed control

}

void DC_Forward_slow_decay(int Speed1)
{
     digitalWrite(DC_IA1,HIGH);
     analogWrite(DC_IA2,Speed1);
}

void DC_Backward_slow_decay(int Speed1)
{
     analogWrite(DC_IA1,Speed1);
     digitalWrite(DC_IA2,HIGH);
}

