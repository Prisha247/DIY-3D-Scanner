#include <Servo.h>

Servo pan; //Servo controlling panning
Servo tilt; // Servo controlling tilting

int pan_pos = 0;    // variable to store the servo position
int pos_tilt = 0;
int sensorPin = A0;

void setup() {
  Serial.begin(9600);
  pan.attach(13);
  tilt.attach(12);
  
  // attaches the servo on pin 13 to the servo object
}

void loop() {
  // Pan left-to-right
  while(pos_tilt < 180) {
      for (pan_pos = 0; pan_pos <= 180; pan_pos += 1) {
        pan.write(pan_pos);
        delay(15);
        Serial.print(pan_pos);
        Serial.print(" ");
        Serial.print(pos_tilt);
        Serial.print(" ");
        Serial.println(analogRead(sensorPin));
      }
      pos_tilt += 10;
      tilt.write(pos_tilt);
      delay(50);
      for (pan_pos = 180; pan_pos >= 0; pan_pos -= 1) {
        pan.write(pan_pos);             
        delay(15);
        Serial.print(pan_pos);
        Serial.print(" ");
        Serial.print(pos_tilt);
        Serial.print(" ");
        Serial.println(analogRead(sensorPin));
      }
      pos_tilt += 10;
      tilt.write(pos_tilt);
      delay(50);
  }
  Serial.println("Completed Data Gathering");
}
