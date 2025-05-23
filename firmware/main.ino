/*
 * IX-T Ambient Energy Harvesting System
 * Main firmware for Arduino Nano
 * Reads voltage/current from INA219 sensors and logs checkpoint power data.
 */

#include <Wire.h>
#include <Adafruit_INA219.h>

// Create INA219 sensor instances with addresses
Adafruit_INA219 sensor1(0x40);
Adafruit_INA219 sensor2(0x41);
Adafruit_INA219 sensor3(0x44);

void setup() {
  Serial.begin(115200);
  Wire.begin();
  
  // Initialize sensors
  sensor1.begin();
  sensor2.begin();
  sensor3.begin();
  
  Serial.println("Starting IX-T Ambient Energy Harvesting Monitor...");
}

void logPower(Adafruit_INA219 &sensor, int checkpoint) {
  float voltage = sensor.getBusVoltage_V();
  float current = sensor.getCurrent_mA();
  float power = voltage * current / 1000.0; // mW
  
  Serial.print("Checkpoint ");
  Serial.print(checkpoint);
  Serial.print(": ");
  Serial.print(voltage, 2);
  Serial.print(" V, ");
  Serial.print(current, 2);
  Serial.print(" mA, ");
  Serial.print(power, 2);
  Serial.println(" mW");
}

void loop() {
  logPower(sensor1, 1);
  logPower(sensor2, 2);
  logPower(sensor3, 3);
  Serial.println("------------------------");
  delay(5000);
}
