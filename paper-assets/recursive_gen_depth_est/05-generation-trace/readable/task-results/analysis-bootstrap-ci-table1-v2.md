# analysis bootstrap ci table1 v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_table1_v2_20260518T160028_result.json`
- **Structured JSON:** [`3775ff186a9b0c449c6e.json`](../../sessions/37/3775ff186a9b0c449c6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全 9 cells 完成。4-class accuracy 点估计与之前 B=10000 的结果完全一致，数据可靠。

JSON 已保存到 `results/reviewer_metrics/bootstrap_ci_table1_v2.json`。

## Table 1 Bootstrap 95% CI (B=1000, seed=42)

| Model | Strategy | 4-class Acc [95% CI] | d1-d3 Bal Acc [95% CI] |
|---|---|---|---|
| Pythia-1.4B | nucleus | 78.7% [78.1, 79.2] | 71.8% [71.0, 72.5] |
| Pythia-1.4B | temp0.9 | 76.7% [76.2, 77.4] | 69.3% [68.5, 70.0] |
| Pythia-1.4B | top-k50 | 68.8% [68.2, 69.4] | 58.9% [58.1, 59.6] |
| GPT-2 XL | nucleus | 84.1% [83.6, 84.6] | 79.4% [78.7, 80.0] |
| GPT-2 XL | temp0.9 | 85.9% [85.4, 86.3] | 81.4% [80.8, 82.1] |
| GPT-2 XL | top-k50 | 75.9% [75.3, 76.5] | 68.4% [67.6, 69.1] |
| OLMo-1B | nucleus | 78.9% [78.4, 79.5] | 72.6% [72.0, 73.3] |
| OLMo-1B | temp0.9 | 82.1% [81.6, 82.7] | 76.4% [75.7, 77.0] |
| OLMo-1B | top-k50 | 74.5% [73.9, 75.1] | 66.2% [65.5, 67.0] |

所有 CI 宽度约 1.0-1.5 个百分点，表明结果稳定。GPT-2 XL temp0.9 最强 (85.9%/81.4%)，Pythia top-k50 最弱 (68.8%/58.9%)。

---
