# analysis exp 019 trained verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_019_trained_verifier_20260516T112741_result.json`
- **Structured JSON:** [`d19e7de55b8f983d1174.json`](../../sessions/d1/d19e7de55b8f983d1174.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Selection F1

| Method | seed42 | seed123 | seed789 | Mean ± σ |
|--------|--------|---------|---------|----------|
| Greedy | 0.6439 | 0.6457 | 0.6511 | 0.6469 ± 0.0037 |
| LP (best unsup) | 0.6501 | 0.6436 | 0.6478 | 0.6472 ± 0.0033 |
| **LR (supervised)** | 0.6484 | 0.6467 | 0.6490 | **0.6480 ± 0.0012** |
| Oracle | 0.7758 | 0.7805 | 0.7885 | 0.7816 ± 0.0064 |

LR vs best unsupervised (LP): **+0.0009**. Gap closure: **0.8%**.

### Instance-level AUROC

| Method | Mean ± σ |
|--------|----------|
| VC (best single) | 0.7064 ± 0.0173 |
| SJ | 0.6842 ± 0.0111 |
| **LR (5 signals)** | **0.6973 ± 0.0161** |

LR AUROC *underperforms* VC alone by -0.0090.

### Feature Importance

VC dominates massively (coef 0.65–0.92 across seeds). SJ has negative coefficients (-0.08 to -0.17), meaning it *hurts* when combined with VC in a linear model.

### Key Takeaway

Supervised LR on 5 signals provides negligible improvement over unsupervised baselines. The oracle gap (13.5 F1 points) is **not closable** with these features — it stems from irreducible per-sample variance that instance-level signals cannot capture, confirming the paper's position that the remaining gap requires fundamentally different approaches (e.g., task-specific reward models, not linear combinations of existing signals).

---
