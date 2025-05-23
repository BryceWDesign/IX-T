# IX-T Experimental Test Plan

## Purpose

This document provides a detailed step-by-step experimental plan to validate the IX-T Ambient Energy Harvesting System in a controlled physical environment. The goal is to generate empirical data to prove or disprove the energy checkpoint amplification hypothesis.

---

## Equipment Needed

- Assembled IX-T circuit prototype with all checkpoints and ambient energy harvesters
- INA219 power sensors or equivalent voltage/current sensors at each checkpoint
- Microcontroller with data logging capabilities (Arduino Nano / Raspberry Pi Pico)
- Data acquisition PC or SD card logger
- Multimeter and oscilloscope for spot checks
- Stable ambient energy sources (e.g., RF signal generators, WiFi sources)
- Power supply for initial system startup (if needed)

---

## Test Setup

1. Verify wiring and sensor connections match hardware schematics.  
2. Calibrate all sensors for accuracy using known voltage/current sources.  
3. Connect microcontroller and set up serial logging or SD card logging.  
4. Position ambient energy sources around the prototype.  
5. Ensure stable environmental conditions (temperature, interference).

---

## Test Procedure

### Step 1: Baseline Measurement

- Power on the system with no ambient energy source active.  
- Record voltage, current, and power at each checkpoint for 10 minutes.  
- This establishes baseline noise and leakage levels.

### Step 2: Ambient Energy Activation

- Activate ambient energy sources sequentially (WiFi, RF, etc.).  
- Record power sensor readings continuously for at least 1 hour per source.  
- Note environmental conditions and any anomalies.

### Step 3: Loop Amplification Check

- Observe if power at downstream checkpoints shows measurable increase or sustained levels over baseline.  
- Monitor stability over time (at least 4-24 hours).

### Step 4: Stress Testing

- Vary ambient energy source intensity and distance.  
- Test system response to sudden drop or increase in input energy.

---

## Data Collection

- Log sensor readings every 5 seconds minimum.  
- Capture timestamped CSV files for voltage, current, and power per checkpoint.  
- Note all external factors and test conditions in a lab notebook.

---

## Success Criteria

Refer to `/validation/metrics_of_success.md` for detailed metrics. Focus on:

- Voltage and power stability or growth  
- Correlation with ambient energy source activity  
- Consistency and repeatability of results

---

## Safety Notes

- Avoid short circuits and overheating.  
- Handle RF sources with proper shielding and compliance.

---

## Next Steps After Testing

- Analyze collected data with scripts provided in `/validation/data_analysis/`.  
- Generate reports summarizing findings.  
- Update repo with test results and recommendations.

---

*End of Test Plan*
