# IX-T Hardware Build Instructions (Simulated Prototype)

> ⚠️ This guide is for conceptual and educational purposes. No real-world construction is assumed or required.

---

## 📦 Components Required

| Component                          | Quantity | Notes                                      |
|-----------------------------------|----------|--------------------------------------------|
| USB Power Source (5V 2A+)         | 1        | Represents initial energy input            |
| INA219 High-side Current Sensor   | 3        | One per checkpoint                         |
| ESP32 Dev Board                   | 1        | For I2C communication and data logging     |
| Resistors (1Ω, 10Ω, 100Ω)         | 6        | Load variation across checkpoints          |
| Breadboard + Jump Wires           | 1 set    | Temporary circuit layout                   |
| MicroSD Module (optional)         | 1        | For persistent logging                     |

---

## 🔧 Circuit Topology (Text Description)

1. The loop is constructed as a linear sequence of three energy “checkpoints”:
   - Each checkpoint includes a voltage divider, a sensor, and a simulated energy buffer.
   - Sensors (INA219) measure voltage and current at each checkpoint.
   - Loads (resistors) simulate energy being consumed/transferred.

2. The ESP32 communicates over I2C to each INA219 sensor, collecting:
   - Bus voltage
   - Shunt voltage
   - Current (in mA)

3. Optional: Insert external low-frequency noise source near checkpoint 2 to mimic ambient energy disturbance.

---

## ⚙️ Assembly Steps

1. **Power Bus Setup**  
   Connect 5V from USB supply to breadboard power rails. Include a decoupling capacitor (10 µF) near the first checkpoint.

2. **Checkpoint 1 Setup**  
   - Insert 1Ω shunt resistor.
   - Wire INA219 for shunt and bus voltage detection.
   - Attach 10Ω load resistor post-sensor.

3. **Checkpoint 2 Setup**  
   - Repeat with new INA219 and a 10Ω load.
   - Optional: Add antenna stub or random noise source (capacitor with nearby mobile RF interference).

4. **Checkpoint 3 Setup**  
   - Final INA219 sensor + 100Ω load.
   - Connect output to ground.

5. **ESP32 + I2C**  
   - Wire SDA/SCL to all INA219 sensors (addressed individually via solder jumper or software).
   - Run `data_logging.py` with correct I2C addresses.

6. **Power On & Simulate**  
   Begin data logging, track checkpoint values, export CSV for analysis.

---

## 🔬 Simulation Notes

- This setup mimics theoretical ambient boosts by interpreting mid-loop energy readings.
- **No free energy** is claimed — ambient interference is interpreted as simulated input.

---

## 📁 Related Files

- `src/data_logging.py`
- `validation/data_analysis/analysis.py`
- `hardware/pricing_list.csv` (next file)

