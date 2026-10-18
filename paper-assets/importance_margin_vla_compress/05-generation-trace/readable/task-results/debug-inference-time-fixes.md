# debug inference time fixes

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_inference_time_fixes_20260516T111944_result.json`
- **Structured JSON:** [`83eac128eb0513e99a03.json`](../../sessions/83/83eac128eb0513e99a03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tests complete. Here are the results:

```
=== cuda:0 Inference Fixes (baseline_v5 final) ===
Default solver: Euler, steps=10

Steps=3:   std=0.0074 [FAIL]
Steps=5:   std=0.0059 [FAIL]
Steps=10:  std=0.0057 [FAIL]
Steps=20:  std=0.0058 [FAIL]
Steps=50:  std=0.0060 [FAIL]
Steps=100: std=0.0066 [FAIL]

SDE sigma=0.01: std=0.0065 [FAIL]
SDE sigma=0.05: std=0.0163 [WARN]
SDE sigma=0.1:  std=0.0313 [WARN]

Temp=0.5:  std=0.2644 [PASS]
Temp=0.8:  std=0.0515 [PASS]
Temp=1.2:  std=0.0113 [WARN]

Early stop t=0.01: std=0.0053 [FAIL]
Early stop t=0.05: std=0.0056 [FAIL]
Early stop t=0.1:  std=0.0977 [PASS]

LoRA merge: std=0.0055 [FAIL]
```

**Key findings:**

1. **ODE steps**: All FAIL. Changing step count doesn't help — the velocity field itself is collapsed, not a numerical integration issue.

2. **SDE noise injection**: Marginal improvement. sigma=0.1 gets to 0.031 (WARN) but doesn't restore diversity. The added noise is fighting a strong attractor.

3. **Temperature scaling**: **Temp < 1.0 PASSES** (0.5→0.264, 0.8→0.052). This is the inverted direction — scaling DOWN the velocity field preserves diversity. This makes sense: the collapsed velocity field is too strong, pulling all trajectories to the same fixed point. Reducing its magnitude weakens the attractor.

4. **Early stop t=0.1**: PASS (std=0.098). Stopping the ODE at t=0.1 (only integrating 90% of the way) retains noise from the initial condition.

5. **LoRA merge**: FAIL. The collapse is baked into the learned weights, not a PeftModel inference artifact.

**Interpretation**: The LoRA fine-tuning made the velocity field too dominant — it learned a near-constant output that overwhelms the initial noise. Temperature < 1.0 and early stopping both work by limiting how far the ODE drives toward the fixed point.

---
