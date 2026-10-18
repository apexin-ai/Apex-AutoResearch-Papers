# ops instruct phase45 results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_instruct_phase45_results_20260517T191522_result.json`
- **Structured JSON:** [`f93dda4bbbd6a020184e.json`](../../sessions/f9/f93dda4bbbd6a020184e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

002 的结果和 001 完全相同（同一份 features 数据，产出写入同一个路径）。两个 run 收敛到同一个结果文件。

## qwen25-1p5b-instruct Phase 4+5 结果

| Metric | Value |
|---|---|
| **RF 4-class acc** | 0.4742 [0.467, 0.4811] |
| **LR 4-class acc** | 0.4256 [0.4184, 0.4321] |
| **RF 3-class (no d0)** | 0.4987 [0.4905, 0.5064] |

### Pairwise AUC (RF)

| Pair | AUC |
|---|---|
| d0v1 | 0.653 |
| d0v2 | 0.819 |
| d0v3 | 0.902 |
| d1v2 | 0.620 |
| d1v3 | 0.807 |
| d2v3 | 0.664 |

### Pairwise AUC (LR)

| Pair | AUC |
|---|---|
| d0v1 | 0.619 |
| d0v2 | 0.773 |
| d0v3 | 0.838 |
| d1v2 | 0.594 |
| d1v3 | 0.734 |
| d2v3 | 0.621 |

### Top-10 Feature Importance (RF)

| Feature | Importance |
|---|---|
| surprisal_range | 0.0708 |
| surprisal_position_corr | 0.0700 |
| prob_std | 0.0687 |
| surprisal_first_half_minus_second | 0.0640 |
| surprisal_std | 0.0563 |
| surprisal_diff_std | 0.0545 |
| surprisal_iqr_10_90 | 0.0520 |
| surprisal_skew | 0.0507 |
| surprisal_frac_above_2std | 0.0496 |
| surprisal_p90 | 0.0490 |

### 关键观察

- 样本量: 19,992 (d0=5000, d1=5000, d2=4996, d3=4996)
- AUC 随 depth gap 单调递增（d0v1=0.653 → d0v3=0.902），符合预期
- 相邻 depth 区分最难：d1v2 AUC=0.620 是最低的
- Top features 全部是 surprisal 统计量，prob_std 是唯一非 surprisal 命名的 feature
- 001 和 002 两个 run 产出完全相同（共用同一个 summary.json 和 features.npz）

---
