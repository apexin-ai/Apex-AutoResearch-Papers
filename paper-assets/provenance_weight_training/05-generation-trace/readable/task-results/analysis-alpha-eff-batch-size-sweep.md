# analysis alpha eff batch size sweep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_eff_batch_size_sweep_20260518T071007_result.json`
- **Structured JSON:** [`bc6b1613adb3e7b6e1fb.json`](../../sessions/bc/bc6b1613adb3e7b6e1fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `/root/provenance_weight_training/alpha_eff_batch_size_sweep.json`。

关键发现：

| | bs=4 | bs=8 | bs=16 |
|---|---|---|---|
| **Pearson r** | 0.706 | 0.697 | 0.707 |
| **Spearman r** | 0.699 | 0.683 | 0.691 |
| **MAE** | 0.114 | 0.097 | 0.075 |
| **α_eff 离散值数** | 5 | 9 | 13 |

**Pearson r 在三个 batch size 下几乎不变**（0.697–0.707），bs=4 的离散化并未显著降低相关性。主要差异在 MAE：bs=4 的 MAE=0.114 是 bs=16 的 1.5 倍，因为离散化粒度粗导致逐 batch 近似误差更大。

bs=4 的 α_eff 分布：0→551(11%), 0.25→1706(34%), 0.5→1775(36%), 0.75→832(17%), 1.0→136(3%)。集中在 0.25 和 0.5，极端值（纯 real 或纯 synthetic batch）较少。

---
