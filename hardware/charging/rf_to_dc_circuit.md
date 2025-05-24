# RF-to-DC Converter Circuit – Design Explanation

This document explains the operation of the RF-to-DC converter circuit shown in `rf_to_dc_circuit.svg`. This subsystem allows the IX-T drone to harvest ambient RF energy (e.g., from checkpoint beacons or strong field emitters) and convert it into stored DC power for the battery system.

---

## 🧩 Block Overview

| Block                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Antenna (ANT)       | Captures RF energy from environment or checkpoint signal                    |
| Matching Network     | Matches antenna impedance to input of rectifier to minimize energy loss     |
| Schottky Rectifier   | High-frequency SMS7630 Schottky diodes rectify AC to DC                    |
| Capacitor (C1)       | Smooths DC signal from rectifier                                            |
| Voltage Multiplier   | Cascaded Cockcroft-Walton stage doubles/triples voltage to usable range    |
| BQ25570 IC           | Manages energy harvesting and outputs stable regulated DC voltage           |
| Supercapacitor       | Buffers energy in storage for immediate use                                 |
| Output               | Supplies stable DC output to drone battery charge controller                |

---

## 🔌 Key Components and Specs

| Component           | Suggested Part #      | Notes                                              |
|--------------------|-----------------------|----------------------------------------------------|
| Schottky Diodes     | SMS7630-079LF         | Fast-switching, low forward-voltage drop          |
| Capacitor C1        | 10 µF, ceramic, 25V    | Helps filter and stabilize DC                      |
| Voltage Multiplier  | 2–4 stage Cockcroft-Walton | Multiplies voltage, built using diodes & caps |
| Energy IC           | Texas Instruments BQ25570 | Ultra-low power boost + battery management       |
| Supercapacitor      | 1F, 2.7V (Maxwell or Eaton) | High-speed charge/discharge buffer              |

---

## 🔋 Expected Output

- Input RF power: -10 dBm to +10 dBm (typical in near field)
- Output Voltage (after BQ25570): ~3.3V DC regulated
- Charge Current: ~10–50 mA depending on signal strength and antenna gain

---

## 🛠️ Integration Tips

- The antenna must be tuned for the expected RF band (e.g. 915 MHz ISM).
- Keep traces short and impedance-matched at RF stages.
- Use shielded compartments for high-sensitivity sections.
- Place BQ25570 close to the output of the rectifier for minimal loss.
- Use ground pours and proper decoupling caps.

---

## 📎 References

- [TI BQ25570 Datasheet](https://www.ti.com/product/BQ25570)
- [SMS7630 Diode Datasheet](https://www.skyworksinc.com/products/detail/sms7630)
- [Ambient RF Harvesting Techniques – IEEE](https://ieeexplore.ieee.org/document/XXXXXX)

---

This module is one of several interchangeable charging interfaces for IX-T. For solar and kinetic converters, see `/hardware/charging/`.

