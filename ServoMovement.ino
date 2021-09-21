#include <Servo.h>

const int servo1 = 13;       // first servo
//const int servo2 = 10;       // second servo
const int PotInput1 = A1;   // first potentiometer
//const int PotInput2 = A1;   // second potentiometer

int PotValue1 = 0;           //set both potentiometer values to be 0 initially
//int PotValue2 = 0;

int servoVal;           // variable to read the value from the analog pin

Servo myservo1;  // create servo object to control a servo
//Servo myservo2;  // create servo object to control a servo



void setup() {

  // Servo  
  myservo1.attach(servo1);  // attaches the servo
//  myservo2.attach(servo2);  // attaches the servo

  // Inizialize Serial
  Serial.begin(9600);
}


void loop(){

    // Display Joystick values using the serial monitor
    PotValue1 = analogRead(PotInput1);

    // Read the first pot value  (value between 0 and 1023)
    servoVal = analogRead(PotValue1);          
    servoVal = map(servoVal, 0, 1023, 0, 180);     // scale it to use it with the servo (result  between 0 and 180)

//    myservo2.write(servoVal);                         // sets the servo position according to the scaled value    
//
//    // Read the second pot value  (value between 0 and 1023)
//    servoVal = analogRead(PotValue2);           
//    servoVal = map(servoVal, 0, 1023, 70, 180);     // scale it to use it with the servo (result between 70 and 180)

    myservo1.write(servoVal);                           // sets the servo position according to the scaled value

    delay(15);                                       // waits for the servo to get there

    Serial.println(analogRead(PotValue1));
//    Serial.print(analogRead(PotValue2));
//    Serial.println ("----------------");
}


/**
* Display joystick values
*/
//void outputJoystick(){
//
//    Serial.print(analogRead(PotValue1));
//    Serial.print ("---"); 
//    Serial.print(analogRead(PotValue2));
//    Serial.println ("----------------");
//}
