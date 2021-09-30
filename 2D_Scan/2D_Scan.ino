/* This script performs a 2D scan (horizonal line) and outputs in the form [pan_angle, tilt_angle, sensor_reading_in_inches] */

#include <Servo.h>

Servo pan; //Servo controlling panning
Servo tilt; // Servo controlling tilting

// Initial servo positions
int pan_pos = 90;
int tilt_pos = 90;
int sensorPin = A0;

bool run_complete = false;
uint16_t LOOP_INTERVAL = 20;
uint32_t loop_time;

void setup() {
  Serial.begin(9600);
  pan.attach(13);
  tilt.attach(12);
  pan.write(pan_pos);
  tilt.write(tilt_pos);
  loop_time = millis();
}

void loop() {  
  // Pan left-to-right once
  while (run_complete == false){
      for (pan_pos = 40; pan_pos <= 130; pan_pos += 5) {
        pan.write(pan_pos);
        delay(500);
        Serial.print(pan_pos);
        Serial.print(" ");
        Serial.print(tilt_pos);
        Serial.print(" ");
        Serial.println(read_sharp_IR(sensorPin));
      }
      run_complete = true;
  }
 
  // Return to original spot
  pan.write(90);
  tilt.write(90);
}

bool it_is_time(uint32_t t, uint32_t t0, uint16_t dt) {
  return ((t >= t0) && (t - t0 >= dt)) ||         // The first disjunct handles the normal case
            ((t < t0) && (t + (~t0) + 1 >= dt));  //   while the second handles the overflow case
}

int read_sharp_IR(int sensorPin) // clean read of IR values, returns distance in inches
{
  uint32_t t;
  uint16_t x, y, z, res;

  t = millis();
  if (it_is_time(t, loop_time, LOOP_INTERVAL)) 
  {
    x = analogRead(sensorPin);
    y = analogRead(sensorPin);
    z = analogRead(sensorPin);

    res = min(min(x, y), z);
    float e=2.71828;

    // convert to distance in inches
    res = 54.692*pow(e, -0.004*res);
    
    loop_time = t;
    return res;
  }
}
