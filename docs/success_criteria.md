# IX-T Success Criteria

This document defines the measurable, testable outcomes that demonstrate the IX-T simulation is functioning as intended — and that its conceptual approach to ambient energy checkpoints is technically plausible.

---

## ✔ Primary Success Criteria

These are the core indicators that the system logic is sound and valid:

### 1. **Loop Sustainability**
- **Goal**: System must maintain non-zero energy for at least 1,000 iterations.
- **Constraint**: Without any checkpoints, system energy should decay to zero within a predictable time window.
- **With Checkpoints**: Energy should remain above 10% of the original injection after 1,000 steps.

### 2. **Ambient Boost Realism**
- Checkpoint boosts should not exceed plausible ambient harvesting values:
  - Max 5–10% of the decayed energy per step.
  - No spike behavior or unrealistic self-sustaining spikes.
  - Energy levels remain bounded and recover predictably.

### 3. **Loss-Driven Behavior**
- System must **fail** if:
  - Checkpoints are disabled.
  - Boost values are set to zero.
- This confirms decay logic is dominant, and boosts are required.

---

## ✔ Secondary Criteria

These reinforce feasibility and simulation integrity:

### 4. **Parameter Sensitivity**
- Minor config changes should not cause simulation instability.
- System should be tunable for short-lived or long-sustained loops based on decay/boost ratio.

### 5. **Output Predictability**
- Energy output trends must show predictable decay and recovery curves (no random spikes).
- Exported logs from the simulation match expected behavior within ±5% error tolerance.

### 6. **Test Coverage**
- All modules are tested for:
  - Initialization
  - Boost calculation
  - Loop termination conditions
  - Edge cases (e.g., zero decay or max boost)

---

## ❓ Experimental Success (Future)
For future physical validation:
- Harvesting circuits must provide actual measured output in μW to mW range.
- Loop must demonstrate closed flow with ambient recharge input from environment or controlled emitters.

---

These criteria establish that IX-T behaves as a plausible simulation of real-world energy loop dynamics — one grounded in science, not fantasy.

