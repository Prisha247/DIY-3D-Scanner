 #include <Servo.h>

Servo pan; //Servo controlling panning
Servo tilt; // Servo controlling tilting

// pan angle range: 0-180, interval = 10
// tilt angle range: 30-120, interval = 10
int pan_pos = 0;    // variable to store the servo position
int tilt_pos =30;
int sensorPin = A0;


uint16_t LOOP_INTERVAL = 20;
uint32_t loop_time;
bool it_is_time(uint32_t t, uint32_t t0, uint16_t dt) {
  return ((t >= t0) && (t - t0 >= dt)) ||         // The first disjunct handles the normal case
            ((t < t0) && (t + (~t0) + 1 >= dt));  //   while the second handles the overflow case
}

void setup() {
  Serial.begin(9600);
  pan.attach(13);
  tilt.attach(12);
  pan.write(pan_pos);
  tilt.write(tilt_pos);
  loop_time = millis();
}

void loop() {  
  // Pan left-to-right
  while(tilt_pos < 120) {
      for (pan_pos = 0; pan_pos <= 180; pan_pos += 10) {
        pan.write(pan_pos);
        delay(100);
        Serial.print(pan_pos);
        Serial.print(" ");
        Serial.print(tilt_pos);
        Serial.print(" ");
        Serial.println(read_sharp_IR(sensorPin));
      }
      tilt_pos += 10;
      tilt.write(tilt_pos);
      delay(50);
      for (pan_pos = 180; pan_pos >= 0; pan_pos -= 10) {
        pan.write(pan_pos);             
        delay(100);
        Serial.print(pan_pos);
        Serial.print(" ");
        Serial.print(tilt_pos);
        Serial.print(" ");
        Serial.println(read_sharp_IR(sensorPin));
      }
      tilt_pos += 10;
      tilt.write(tilt_pos);
      delay(50);
  }
  
  Serial.println("Completed Data Gathering");
  
  // Return to original spot
  pan.write(90);
  tilt.write(90);
}

int read_sharp_IR(int sensorPin) // clean read of r
{
  uint32_t t;
  uint16_t x, y, z, w, res;

  t = millis();
  if (it_is_time(t, loop_time, LOOP_INTERVAL)) 
  {
    x = analogRead(sensorPin);
    y = analogRead(sensorPin);
    z = analogRead(sensorPin);
    w = analogRead(sensorPin);
    res = min(min(min(x, y), z), w);

//    res = min(min(x, y), z);
    loop_time = t;
    return res;
  }
}
