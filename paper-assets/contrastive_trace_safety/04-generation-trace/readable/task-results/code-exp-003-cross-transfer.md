# code exp 003 cross transfer

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_003_cross_transfer_20260516T222021_result.json`
- **Structured JSON:** [`e484e5333ef6fc2fefbc.json`](../../sessions/e4/e484e5333ef6fc2fefbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment exp-003 complete. Here's the summary:

---

## Results: Cross-Model Transfer Probing

### Same-Model Baselines (upper bounds)

| Model | Accuracy | Crossing Rate | Lead Mean |
|-------|----------|---------------|-----------|
| r1-8b | 0.8234 | 0.413 | -1.46 |
| R1-32B | 0.6516 | 0.633 | 11.74 |
| QwQ-32B | 0.7171 | 0.724 | 9.24 |

### Transfer Matrix (best accuracy per pair)

| Source\Target | r1-8b | R1-32B | QwQ-32B |
|---|---|---|---|
| **r1-8b** | 0.8234 | 0.5220 | 0.5948 |
| **R1-32B** | 0.5828 | 0.6516 | 0.5499 |
| **QwQ-32B** | N/A | 0.6726 | 0.7171 |

### Key Findings

1. **QwQ-32B → R1-32B (direct, same-dim 5120)**: acc=0.6726 exceeds R1-32B self-baseline (0.6516), BUT crossing_rate drops to 0.01 (probe almost never triggers the detection). High accuracy comes from correctly predicting the majority class, not from temporal detection.

2. **Cross-architecture PCA transfers** (8b↔32b): 51-59% accuracy (marginally above chance), with crossing rates of 15-46%. PCA alignment enables *some* signal transfer but far below baselines.

3. **Same-arch direct transfer fails directionally**: R1-32B→QwQ (direct) gets acc=0.38 with xr=1.0 (always triggers), while reverse QwQ→R1-32B gets 0.67 with xr=0.01 (never triggers). The weight vectors are not interchangeable despite same architecture.

4. **PCA dimension has minimal impact**: 512 vs 1024 vs 2048 components yield similar results (~1-2% difference).

### Conclusion: **Negative**

Simple dimension projection (PCA) is insufficient for reliable zero-shot cross-model transfer. The safety commitment signal appears model-specific in its geometric encoding rather than being a universal linear direction. Shared architecture helps accuracy but destroys temporal detection quality.

---
