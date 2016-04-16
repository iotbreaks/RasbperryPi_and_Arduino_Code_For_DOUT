/*
  Sensor_Polling.ino
  Created by Kenny from www.iotbreaks.vn, April 16, 2016.
  Released into the public domain.
  Tutorial: 
*/
const byte ledOutPin = 13; // LED connected to digital pin 13
const byte sensorInPin = 12;  // Sensor DOUT connected to digital pin 12
volatile byte val = HIGH; // variable to store the read value from sensor dout.

void setup() {
  pinMode(ledOutPin, OUTPUT);
  pinMode(sensorInPin, INPUT);
}

void loop() {
  val = digitalRead(sensorInPin);
  digitalWrite(ledOutPin, val);
  delay(200);
}
