# ssh 5epoch entity construction w3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5epoch_entity_construction_w3_20260522T135921_result.json`
- **Structured JSON:** [`f1cfab8b8b1b893d9786.json`](../../sessions/f1/f1cfab8b8b1b893d9786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the complete results:

```
5-epoch Entity Construction (FewNERD, N=8, T=1.0, seed=42):
  n_instances:                  32565 (gold-nonempty subset)
  degeneracy_rate:              25.7% (8375/32565)
  
  greedy_f1:                    0.7979 (micro) / 0.7807 (macro)
  lp_weighted_construction_f1:  0.7893 (micro) / 0.7828 (macro)   [θ=0.25]
  uniform_construction_f1:      0.7771 (micro) / 0.7761 (macro)   [θ=0.25]
  Δ_lp_construction:            -0.87 pp (micro) / +0.20 pp (macro)
  Δ_uniform_construction:       -2.08 pp (micro) / -0.47 pp (macro)

  Best LP-weighted across θ sweep:
    macro: θ=0.25  F1=0.7828  Δ=+0.20pp
    micro: θ=0.50  F1=0.7980  Δ=+0.01pp

3-epoch cross-validation (exp021, seed=42):
  greedy_f1:                    0.7911 (micro) / 0.7478 (macro)  ← micro matches ref
  lp_weighted_construction_f1:  0.7766 (micro) / 0.7566 (macro)  [θ=0.25]
  Δ_lp_construction:            -1.45 pp (micro) / +0.88 pp (macro, single seed)
  
  Note: ref "+1.40pp" is the multi-seed AVERAGE (seeds 42/123/456/789)
  macro-F1 delta from multiseed_results.json: mean=+1.40pp, std=0.51pp
  Single-seed macro deltas: 42→+0.88, 123→+2.18, 456→+1.51, 789→+1.02
```

**Key findings for reviewer W3 response:**

1. 5-epoch construction gain is near-zero: **+0.20pp macro-F1** (best θ=0.25) vs 3-epoch **+1.40pp** (multi-seed avg). Construction essentially fails at 5 epochs.

2. Root cause: **degeneracy rate jumps from 10.0% → 25.7%**. The 5-epoch model is over-converged — 1 in 4 instances produce identical outputs across all 8 samples, eliminating the diversity construction needs.

3. Metric note: the paper's 3-epoch reference "greedy=0.7911, LP=0.8051 (+1.40pp)" mixes micro-F1 absolute values with multi-seed average macro-F1 deltas. The single-seed (42) macro delta is +0.88pp, not +1.40pp.

---
