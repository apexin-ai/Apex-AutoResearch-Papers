# code cross seed transfer

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_seed_transfer_20260517T052138_result.json`
- **Structured JSON:** [`0cf6749ae2c04b946bb8.json`](../../sessions/0c/0cf6749ae2c04b946bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Hypothesis PASS.** 结果：

| Metric | Accuracy | 95% CI |
|--------|----------|--------|
| Within-seed CV (seed=42) | 78.68% | ±0.44% |
| Within-seed CV (seed=43) | 77.45% | ±1.18% |
| **Within-seed avg** | **78.07%** | — |
| train=42 → test=43 | 77.85% | [76.10%, 79.65%] |
| train=43 → test=42 | 75.68% | [75.07%, 76.25%] |
| **Cross-seed avg** | **76.76%** | — |
| **Delta (cross - within)** | **-1.30pp** | — |

Cross-seed avg = 76.76% ≥ 75% threshold, delta = -1.30pp (within the ≤3pp tolerance).

注意：seed=43 数据集只有 2000 samples（vs seed=42 的 20000），所以 train=43→test=42 方向略低属于预期（训练数据少 10x）。train=42→test=43 方向几乎无损（77.85% vs within 78.07%），进一步确认 feature space 跨 seed 一致性。

结果已保存至 `/root/autodl-tmp/recursive_gen_depth_est/results/cross_seed_transfer/summary.json`。

---
