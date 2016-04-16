/*
  sensor_Interrupt.ino
  Created by Kenny from www.iotbreaks.vn, April 16, 2016.
  Released into the public domain.
  Tutorial: 
*/
const byte ledOutPin = 13; // LED connected to digital pin 13
const byte sensorInPin = 2;  // Sensor DOUT connected to interrupt pin 2 (Int.0)
volatile byte val = HIGH; // variable to store the read value from sensor sensor. 
                          // Default is HIGH for inactive state of sensor sensor
void setup() {
  pinMode(ledOutPin, OUTPUT);
  pinMode(sensorInPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(sensorInPin), doutSensorDidChange, CHANGE);
  digitalWrite(ledOutPin,1);
}

void loop() {
  // Do nothing here
}

void doutSensorDidChange() {
  val = digitalRead(sensorInPin);
  digitalWrite(ledOutPin, val);
}
