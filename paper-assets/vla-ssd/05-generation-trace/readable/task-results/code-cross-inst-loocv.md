# code cross inst loocv

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_inst_loocv_20260517T000038_result.json`
- **Structured JSON:** [`3c18b4e8e818d2cd2cdc.json`](../../sessions/3c/3c18b4e8e818d2cd2cdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Complete. Here are the full results:

## 10-Fold Leave-One-Task-Out CV Results

**Task:** Classify instruction identity (10-class) from cross-instruction features, generalizing across tasks.

### Summary Table (mean ± std accuracy across 10 folds)

| Layer | Trained image_mean | Trained last_preaction | Untrained image_mean | Untrained last_preaction |
|-------|-------------------|----------------------|---------------------|--------------------------|
| L0  | 10.00 ± 0.00 | 10.00 ± 0.00 | 10.00 ± 0.00 | 10.00 ± 0.00 |
| L8  | 10.00 ± 0.00 | **100.00 ± 0.00** | 10.00 ± 0.09 | 96.64 ± 7.07 |
| L16 | 10.00 ± 0.00 | **100.00 ± 0.00** | 10.02 ± 0.06 | 93.50 ± 7.19 |
| L24 | 10.06 ± 0.09 | **100.00 ± 0.00** | 10.04 ± 0.08 | 88.60 ± 10.88 |
| L31 | 10.00 ± 0.20 | **100.00 ± 0.00** | 10.02 ± 0.06 | 84.76 ± 11.59 |

### Key findings:

1. **Trained last_preaction: perfect 100% on all 10 folds, all layers L8-L31.** Instruction identity perfectly generalizes across unseen tasks.

2. **Untrained last_preaction: high but imperfect** — peaks at L8 (96.6%), monotonically degrades deeper (L31 = 84.8%). Higher variance across folds (fold 1 is consistently hardest at 55-76%).

3. **image_mean: chance level everywhere** (both trained and untrained). Instruction information is not encoded at the image mean token position — expected since the same image is shown regardless of instruction.

4. **L0 always chance** — embedding layer doesn't yet integrate instruction content into these positions.

Results saved to `/root/autodl-tmp/vla-ssd/results/cross_instruction/loocv_results.json`.

---
