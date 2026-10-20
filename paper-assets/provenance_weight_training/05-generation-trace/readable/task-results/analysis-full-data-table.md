# analysis full data table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full_data_table_20260515T154608_result.json`
- **Structured JSON:** [`8482e31077278343668f.json`](../../sessions/84/8482e31077278343668f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件：`artifacts/experiment_summary_table.md`（已注册为 `art_20260515_3671c5`）。

包含 8 张表：

| 表 | 内容 |
|---|------|
| Table 1 | Grid-b sweep (b=0.5–5.0, 3 seeds, seed456 b≥2.0 标注 D026 artifact) |
| Table 2 | Method comparison (adaptive_fix / uniform / grid-best / golden_ratio / ess_only) + capture ratio + b* 分布 |
| Table 3 | τ sensitivity (τ=0.6 negative 已标注, 0.5/0.7/0.9/0.95 RUNNING) |
| Table 4 | n_min ablation (1/2/3/4) + cross-seed variance 对比 |
| Table 5 | Detector 性能 |
| Table 6 | Data generation |
| Table 7 | 非成功实验 (1 negative + 1 failed + 6 killed) |
| Table 8 | 当前 RUNNING/PREPARING |

核心数字：adaptive_fix 3-seed mean PPL=17.651, vs uniform 17.693 (ΔPPL=+0.042), vs grid-best 17.646 (capture ~87%), 零调参成本。

---
