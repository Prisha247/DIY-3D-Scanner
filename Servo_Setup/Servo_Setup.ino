#include <Servo.h>

// Set servo positions to center point. Run this before collecting data to make sure the sensor is aligned correctly. 

Servo pan; //Servo controlling panning
Servo tilt; // Servo controlling tilting

// Set positions to center point
int pan_pos = 90;
int tilt_pos = 90;

void setup() {
  Serial.begin(9600);
  pan.attach(13);
  tilt.attach(12);

  pan.write(pan_pos);
  tilt.write(tilt_pos);
}

void loop() {
  // n/a

}
