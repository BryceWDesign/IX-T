# Checkpoint Charging Circuit Pinout

This document provides detailed pinout information for key components in the checkpoint charging circuit.

## Energy Harvesting Antenna Array
| Pin | Description             | Notes                         |
|------|-------------------------|-------------------------------|
| RF+  | Positive RF signal input | Connect to antenna terminals  |
| RF-  | Negative RF signal input | Connect to antenna ground     |

## Rectifier Circuit (Schottky Diode Bridge)
| Pin   | Description         | Notes                       |
|--------|---------------------|-----------------------------|
| AC1    | AC input 1          | Connect to antenna RF+      |
| AC2    | AC input 2          | Connect to antenna RF-      |
| DC+    | Positive DC output  | Connect to Boost Converter +|
| DC-    | Negative DC output  | Connect to Boost Converter -|

## Boost Converter Module (e.g., XL6009)
| Pin       | Description            | Notes                      |
|------------|------------------------|----------------------------|
| VIN+       | DC input positive      | From rectifier DC+ output  |
| VIN-       | DC input negative      | From rectifier DC- output  |
| VOUT+      | Boosted DC output +    | To energy storage capacitor|
| VOUT-      | Boosted DC output -    | To energy storage capacitor|

## Energy Storage Capacitor
| Terminal  | Description            | Notes                      |
|------------|------------------------|----------------------------|
| +          | Positive terminal      | Connect to boost converter output +|
| -          | Negative terminal      | Connect to boost converter output -|

## MOSFET (e.g., IRFZ44N)
| Pin    | Description           | Notes                      |
|---------|-----------------------|----------------------------|
| Gate    | Control input         | Connected to microcontroller PWM output|
| Drain   | Load output           | Connects to energy loop injection point|
| Source  | Ground                | Connect to common ground   |

## Voltage Sensor (e.g., Voltage Divider Circuit)
| Pin     | Description           | Notes                      |
|---------|-----------------------|----------------------------|
| Input   | Voltage measurement point | Connects to injection point|
| Output  | Sensor output          | Connects to microcontroller ADC input|

## Current Sensor (e.g., ACS712)
| Pin     | Description           | Notes                      |
|---------|-----------------------|----------------------------|
| Input   | Current measurement point | Connects to injection point|
| Output  | Sensor output          | Connects to microcontroller ADC input|

