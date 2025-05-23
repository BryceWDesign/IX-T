# IX-T Measurement and Validation Plan

## Objective

To establish scientific credibility, IX-T defines specific, measurable criteria to evaluate the simulated performance and feasibility of its ambient energy loop system.

## Key Metrics

### 1. **Ambient Energy Harvest Efficiency**
- **Definition:** Percentage of ambient energy successfully harvested at each checkpoint.
- **Measurement Tool:** Simulated antenna efficiency curves, modeled based on frequency response and known field strengths (e.g., from Wi-Fi, Bluetooth, or thermal gradients).
- **Target:** ≥ 30% capture efficiency under moderate EM conditions.

### 2. **Circuit Retention Efficiency**
- **Definition:** Percentage of original signal energy retained as it completes one full loop through the system.
- **Tool:** Simulated charge counters at entry/exit points of the loop.
- **Target:** ≥ 90% retention with checkpoint amplification.

### 3. **Net Positive Loop Operation**
- **Definition:** Whether energy added at checkpoints exceeds energy lost to resistance or leakage over time.
- **Tool:** Power-in vs. power-out simulation ledger.
- **Target:** Stable or growing loop power over ≥ 100 cycles.

### 4. **Sustainability Without External Recharge**
- **Definition:** Duration the system can remain active without an external power source, assuming environmental field presence.
- **Tool:** Continuous loop simulation over extended time (e.g., 24 hours).
- **Target:** 12+ hours sustained with background EM sources.

## Methodology

- Use Python-based simulation scripts provided in `simulations/` to run models with various antenna gain, loop resistance, and energy field parameters.
- Log all iterations and visualize results via `results/` output plots.
- Document anomalies and edge cases.

## Assumptions

- Environmental EM energy is present at low levels throughout the simulation.
- Checkpoints operate ideally without hardware faults or thermal inefficiencies.
- All components are simulated with real-world material properties as referenced in `docs/materials_reference.md`.

## Output Examples

- `.csv` logs of loop energy retention
- Line plots of harvested vs. lost energy per checkpoint
- Histograms of loop survivability duration under variable input conditions

---

This plan serves to ground IX-T in scientific rigor by tying each claim to quantifiable parameters. Real-world prototypes can be compared against these simulations in future phases.
