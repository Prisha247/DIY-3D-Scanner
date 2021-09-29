
#include <Servo.h>

Servo pan; //Servo controlling panning
Servo tilt; // Servo controlling tilting

// pan angle range: 0-180
// tilt angle range: 60-130
int pan_pos = 90;    // variable to store the servo position
int tilt_pos = 130;
int sensorPin = A0;

void setup() {
  Serial.begin(9600);
  pan.attach(13);
  tilt.attach(12);

  pan.write(pan_pos);
  tilt.write(tilt_pos);
}

void loop() {
  // put your main code here, to run repeatedly:

}
