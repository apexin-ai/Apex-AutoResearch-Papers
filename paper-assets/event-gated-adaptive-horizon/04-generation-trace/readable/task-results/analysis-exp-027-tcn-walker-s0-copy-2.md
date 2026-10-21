# analysis exp 027 tcn walker s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_027_tcn_walker_s0_20260520T062805_result.json`
- **Structured JSON:** [`0e07885cc4678f9f2889.json`](../../sessions/0e/0e07885cc4678f9f2889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the final analysis:

---

## exp_027_tcn_walker_s0 — **NEGATIVE**

**Hypothesis**: TCN (σ=0.5 Gaussian noise on dt_embedding) suppresses CIVO (NVE < 1.5×) while maintaining eval > 450.

### Results

| Metric | Target | Actual |
|--------|--------|--------|
| NVE < 1.5× | All checkpoints | 3 breaches: 55K(1.68×), 65K(1.54×), **85K(3.97×)** |
| eval_return > 450 | Sustained | Peak 240 (35K), avg 117 in latter half |
| Training extent | 210K | Stopped at 120K |

### Key Findings

1. **CIVO not suppressed** — Peak NVE 3.97× at 85K is *worse* than typical CIVO, suggesting TCN noise destabilizes rather than prevents value exploitation.
2. **CIVO signature confirmed** — 85K NVE spike (3.97×) coincides with eval collapse to 36, classic CIVO pattern.
3. **Gate behavior unchanged** — dt=2 fixed throughout, zero entropy. Noise on embedding didn't influence gate selection.
4. **σ=0.5 insufficient** — The critic can learn through this noise level. The dt conditioning signal-to-noise ratio remains high enough for value bias to develop.

### Implication

Both gradient-level (SGS, exp_025) and forward-pass noise (TCN, this experiment) fail to suppress CIVO. The critic's dt-specific value bias is robust to perturbation-based interventions — may need architectural separation (e.g., dt-agnostic critic) or value normalization approaches instead.

---
