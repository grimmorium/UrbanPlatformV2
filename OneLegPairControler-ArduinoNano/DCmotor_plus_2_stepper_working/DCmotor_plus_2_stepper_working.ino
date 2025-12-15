#include <TMCStepper.h>         // TMCstepper - https://github.com/teemuatlut/TMCStepper
#include <SoftwareSerial.h>     // Software serial for the UART to TMC2209 - https://www.arduino.cc/en/Reference/softwareSerial
#include <AccelStepper.h>

/*Common*/
int microsteps = 8;

/*
Stepper 1
*/
#define S1_EN_PIN           2      // Enable - PURPLE
#define S1_dir_PIN          3      // direction - WHITE
#define S1_STEP_PIN         4      // Step - ORANGE
#define S1_SW_SCK           8      // Software Slave Clock (SCK) - BLUE
#define S1_SW_TX            12      // SoftwareSerial receive pin - BROWN
#define S1_SW_RX            13      // SoftwareSerial transmit pin - YELLOW
#define S1_DRIVER_ADDRESS   0b00   // TMC2209 Driver address according to MS1 and MS2
#define S1_R_SENSE 0.11f           // SilentStepStick series use 0.11 ...and so does my fysetc TMC2209 (?)

SoftwareSerial S1_SoftSerial(S1_SW_TX, S1_SW_RX);                          // Be sure to connect RX to TX and TX to RX between both devices
TMC2209Stepper S1_TMCdriver(&S1_SoftSerial, S1_R_SENSE, S1_DRIVER_ADDRESS);   // Create TMC driver
AccelStepper S1_stepper = AccelStepper(S1_stepper.DRIVER, S1_STEP_PIN, S1_dir_PIN);
bool S1_dir = true;

/*
Stepper 2
*/
#define S2_EN_PIN           A3      // Enable - PURPLE
#define S2_dir_PIN          A2      // direction - WHITE
#define S2_STEP_PIN         10      // Step - ORANGE
#define S2_SW_SCK           11      // Software Slave Clock (SCK) - BLUE
#define S2_SW_TX            6      // SoftwareSerial receive pin - BROWN
#define S2_SW_RX            7      // SoftwareSerial transmit pin - YELLOW
#define S2_DRIVER_ADDRESS   0b00   // TMC2209 Driver address according to MS1 and MS2
#define S2_R_SENSE 0.11f           // SilentStepStick series use 0.11 ...and so does my fysetc TMC2209 (?)

SoftwareSerial S2_SoftSerial(S2_SW_TX, S2_SW_RX);                          // Be sure to connect RX to TX and TX to RX between both devices
TMC2209Stepper S2_TMCdriver(&S2_SoftSerial, S2_R_SENSE, S2_DRIVER_ADDRESS);   // Create TMC driver
AccelStepper S2_stepper = AccelStepper(S2_stepper.DRIVER, S2_STEP_PIN, S2_dir_PIN);
bool S2_dir = true;

/*DC Motor*/
int DC_IA1 = 9;
int DC_IA2 = 5;



void setup() {
  // put your setup code here, to run once:
  pinMode(DC_IA1, OUTPUT);
  pinMode(DC_IA2, OUTPUT);

  /*
  Stepper 1 config
  */
  S1_SoftSerial.begin(115200);           // initialize software serial for UART motor control
  S1_TMCdriver.beginSerial(115200);      // Initialize UART

  pinMode(S1_EN_PIN, OUTPUT);           // Set pinmodes
  pinMode(S1_STEP_PIN, OUTPUT);
  pinMode(S1_dir_PIN, OUTPUT);
  digitalWrite(S1_EN_PIN, LOW);         // Enable TMC2209 board  

  S1_TMCdriver.begin();                                                                                                                                                                                                                                                                                                                            // UART: Init SW UART (if selected) with default 115200 baudrate
  S1_TMCdriver.toff();                 // Enables driver in software
  S1_TMCdriver.rms_current(1500);        // Set motor RMS current
  S1_TMCdriver.microsteps(microsteps);         // Set microsteps

  S1_TMCdriver.en_spreadCycle(false);
  S1_TMCdriver.pwm_autoscale(true);     // Needed for stealthChop
  
  S1_stepper.setMaxSpeed(80000); // 100mm/s @ 80 steps/mm
  S1_stepper.setAcceleration(50000); // 2000mm/s^2
  S1_stepper.setEnablePin(S1_EN_PIN);
  S1_stepper.setPinsInverted(false, false, true);
  S1_stepper.enableOutputs();

  S1_TMCdriver.shaft(S1_dir);

  /*
  Stepper 2 config
  */
  S2_SoftSerial.begin(115200);           // initialize software serial for UART motor control
  S2_TMCdriver.beginSerial(115200);      // Initialize UART

  pinMode(S2_EN_PIN, OUTPUT);           // Set pinmodes
  pinMode(S2_STEP_PIN, OUTPUT);
  pinMode(S2_dir_PIN, OUTPUT);
  digitalWrite(S2_EN_PIN, LOW);         // Enable TMC2209 board  

  S2_TMCdriver.begin();                                                                                                                                                                                                                                                                                                                            // UART: Init SW UART (if selected) with default 115200 baudrate
  S2_TMCdriver.toff();                 // Enables driver in software
  S2_TMCdriver.rms_current(1500);        // Set motor RMS current
  S2_TMCdriver.microsteps(microsteps);         // Set microsteps

  S2_TMCdriver.en_spreadCycle(false);
  S2_TMCdriver.pwm_autoscale(true);     // Needed for stealthChop
  
  S2_stepper.setMaxSpeed(80000); // 100mm/s @ 80 steps/mm
  S2_stepper.setAcceleration(50000); // 2000mm/s^2
  S2_stepper.setEnablePin(S2_EN_PIN);
  S2_stepper.setPinsInverted(false, false, true);
  S2_stepper.enableOutputs();

  S2_TMCdriver.shaft(S2_dir);
}

void loop() {

  /*move stepper 1*/
  if (S1_stepper.distanceToGo() == 0) {
      S1_stepper.disableOutputs();
      //delay(10);
      S1_stepper.move(16000); // Move 100mm
      S1_dir = !S1_dir;
      S1_TMCdriver.shaft(S1_dir);
      S1_stepper.enableOutputs();
    }
  S1_stepper.run();

  /*move stepper 2*/
  if (S2_stepper.distanceToGo() == 0) {
      S2_stepper.disableOutputs();
      //delay(10);
      S2_stepper.move(16000); // Move 100mm
      S2_dir = !S2_dir;
      S2_TMCdriver.shaft(S2_dir);
      S2_stepper.enableOutputs();
    }
  S2_stepper.run();

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

