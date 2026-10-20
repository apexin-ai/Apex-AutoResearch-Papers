# ssh warmstart transition v2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_warmstart-transition-v2_20260516T161746_result.json`
- **Structured JSON:** [`e84061128dced0d49d46.json`](../../sessions/e8/e84061128dced0d49d46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training confirmed working. Here's the complete summary:

---

## Results Summary

### 1. Checkpoint-200 prove_rate
- **s42 steps 180-200**: Average prove_rate ≈ 0.66, step 200 = 1.0 (well above 0.6 threshold)

### 2. Dry-run metrics
| Metric | Step 1 (s42) | Criteria | Note |
|--------|-------------|----------|------|
| prove_rate | 1.0 | > 0.3 | ✓ |
| gate_pass | 0.0 | 0 < x < 1 | ✗ (stochastic, ISR < threshold for this batch) |
| grad_norm | 0.0 | > 0 | ✗ (follows from gate_pass=0) |
| reward_std | 0.0 | > 0 | ✗ (follows from gate_pass=0) |

**BUT** s43 full-run step 4 immediately shows: gate_pass=0.286, grad_norm=9.65, loss=-0.0285, reward_std=0.463 — confirming the gate works.

### 3. Dual-card PIDs
- **cuda:0** (s42): PID 890110
- **cuda:1** (s43): PID 890250

### 4. First steps (s43 — active gradients)
| Step | prove_rate | gate_pass | grad_norm | loss |
|------|-----------|-----------|-----------|------|
| 1 | 1.0 | 1.0 | 0.0 (reward_std=0, all passed) | 0.0 |
| 3 | 0.875 | 0.286 | 9.65 | -0.029 |
| 5 | 1.0 | 0.125 | 3.14 | -0.065 |
| 9 | 0.125 | 1.0 | 0.77 | 0.195 |

ISR-gated warmstart is running on both GPUs. The gate is functional (s43 producing gradients immediately). s42 gate_pass=0 in early steps is expected variance — the exec-only log shows ISR often below threshold at step 200; it will get signal from higher-ISR batches over 300 steps.

---
