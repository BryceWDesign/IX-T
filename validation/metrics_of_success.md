# IX-T Metrics of Success

This document outlines the measurable criteria used to evaluate the feasibility and simulated performance of the IX-T ambient energy loop system. These metrics allow both developers and external reviewers to determine whether the system demonstrates practical potential based on logged and analyzed data.

---

## 1. **Power Consistency**
- **Definition**: Stability of power output at each checkpoint over time.
- **Target**: Variance within ±5% of mean power value at each checkpoint.
- **Evaluation**: Visualized using power trend plots; quantified with standard deviation and coefficient of variation.

---

## 2. **Net Power Differential**
- **Definition**: Total power observed across checkpoints versus initial input.
- **Target**: Ideally close to zero for validation of lossless simulation; any net gain must be accompanied by explanation of energy sourcing (e.g., ambient input).
- **Evaluation**: Compare summed power across all checkpoints using data analysis script (`analysis.py`).

---

## 3. **Simulated Ambient Harvesting Effect**
- **Definition**: Implied increase in available power attributed to the model's checkpoints acting as passive ambient energy harvesting nodes.
- **Target**: Observable trend showing power "boost" at mid-loop checkpoints.
- **Evaluation**:
  - Use voltage/current trends from `data_logging.py`.
  - Confirm via consistent checkpoint power increases not explainable by circuit delay or artifacts.

---

## 4. **Sensor Integrity**
- **Definition**: Validation that sensor readings are reliable and not due to noise, aliasing, or drift.
- **Target**: No anomalous spikes/drops in current/voltage unless clearly documented as external changes.
- **Evaluation**: Cross-check raw values; compare to expected values based on resistor calibration and expected range.

---

## 5. **Repeatability**
- **Definition**: Ability to reproduce results with same simulated configuration.
- **Target**: <10% variation across multiple simulation logs.
- **Evaluation**: Repeat logging 3+ times and compare results using `analysis.py`.

---

## Conclusion

These success metrics are designed to evaluate IX-T purely in a simulation context. While they do not provide irrefutable physical proof of perpetual operation or net energy creation, they allow structured testing of feasibility claims in a way that meets engineering expectations for early conceptual models.

For reviewers: Please refer to `hardware_build.md` and `/validation/` scripts to run and analyze simulations.

