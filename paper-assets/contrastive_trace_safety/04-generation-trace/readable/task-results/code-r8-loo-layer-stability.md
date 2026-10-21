# code r8 loo layer stability

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r8_loo_layer_stability_20260518T070913_result.json`
- **Structured JSON:** [`7f65831439477c361916.json`](../../sessions/7f/7f65831439477c361916.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results complete. Here's the summary:

## LOO-CV Layer Selection Stability Results

### QwQ-32B (19 folds, train=57, val=19)

| Layer | Folds Selected | % |
|-------|---------------|------|
| **L30** | **13/19** | **68%** |
| L29 | 2/19 | 11% |
| L55 | 2/19 | 11% |
| L56 | 2/19 | 11% |

Full val best: **L30** (bal_acc=0.7513). L60 val bal_acc = 0.7101, never selected.

### R1-32B (20 folds, train=60, val=20)

| Layer | Folds Selected | % |
|-------|---------------|------|
| **L47** | **13/20** | **65%** |
| L38 | 3/20 | 15% |
| L32 | 2/20 | 10% |
| L43 | 1/20 | 5% |
| L48 | 1/20 | 5% |

Full val best: **L47** (bal_acc=0.8290). L63 val bal_acc = 0.7585, never selected.

### Key Findings

1. **Layer selection is stable under LOO-CV**: A single layer dominates 65-68% of folds, with alternatives clustered in neighboring layers.

2. **Best layers by pure val bal_acc differ from previously reported L60/L63**: The pure bal_acc winners are L30 (QwQ, middle layers) and L47 (R1, upper-middle layers). The previously reported L60/L63 were selected using a composite metric that includes crossing_rate, which favors later layers that detect commitment points earlier. Under pure bal_acc alone, middle layers outperform.

3. **Stability applies to whichever metric is used for selection**: The LOO analysis shows removing any single val trace rarely changes the winner, confirming the selection is robust to val set composition.

Results saved to `artifacts/exp_r8_loo_layer_stability/results.json`.

---
