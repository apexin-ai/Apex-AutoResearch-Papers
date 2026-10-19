# code exp r3 mlp probe

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_r3_mlp_probe_20260517T125418_result.json`
- **Structured JSON:** [`3aee9d418c05dc3b1ab4.json`](../../sessions/3a/3aee9d418c05dc3b1ab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registration isn't working with remote paths. That's fine - the results are saved on the server. Here's the final summary:

## Results: MLP Probe (dim→128→1, ReLU+Sigmoid, BCE)

| Model | W | Bal Acc | Precision | Pre-CP FPR | Coverage | Lead (steps) | LR Acc | Delta |
|-------|---|---------|-----------|------------|----------|--------------|--------|-------|
| R1-8B | 3 | 0.799 | 0.703 | 0.098 | 1.000 | 9.8 | 0.817 | -0.018 |
| R1-32B | 10 | 0.677 | 0.512 | 0.343 | 1.000 | 6.5 | 0.737 | -0.060 |
| QwQ-32B | 5 | 0.686 | 0.425 | 0.423 | 1.000 | 12.9 | 0.761 | -0.076 |
| OT-7B | 3 | 0.704 | 0.515 | 0.107 | 1.000 | 10.4 | 0.688 | +0.016 |

**Key observations:**
- The simple MLP achieves 100% coverage across all models (every jailbreak trace is detected post-CP)
- Balanced accuracy is slightly below LR for 3/4 models (R1-8B -1.8%, R1-32B -6.0%, QwQ-32B -7.6%), but slightly above for OT-7B (+1.6%)
- The MLP trades off balanced accuracy for perfect coverage and competitive precision, especially for R1-8B (0.703 precision, 9.8% FPR)
- Without pos_weight or dropout, the simpler MLP tends to predict more positives (hence perfect coverage but higher FPR on some models)

Results saved to `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_mlp_probe/results.json`. Script at `src/experiments/exp_r3_mlp_probe_v2.py`.

---
