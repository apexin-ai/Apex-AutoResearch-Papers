# analysis nmin ablation prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nmin_ablation_prep_20260515T155255_result.json`
- **Structured JSON:** [`2ca0cb5afb3a1b1ddbc4.json`](../../sessions/2c/2ca0cb5afb3a1b1ddbc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

| 文件 | 说明 |
|------|------|
| `analysis/nmin_ablation_analysis.py` | 分析脚本 |
| `analysis/nmin_ablation_curve.pdf` / `.png` | n_min vs PPL 图（含 uniform baseline 水平线） |
| `analysis/nmin_ablation_summary.json` | 结构化 JSON 摘要 |

**结果概要（3/4 数据点）**：

| n_min | PPL | Δ vs uniform | 状态 |
|-------|-----|-------------|------|
| 1 | 17.789 | -0.095 (worse) | ✓ |
| 2 | 17.650 | +0.044 (better) | ✓ |
| 3 | 17.644 | +0.050 (better) | ✓ |
| 4 | pending | — | NOT_STARTED |

- n_min=2 与 n_min=3 基本持平（ΔPPL=0.006）
- n_min=1 过于激进，反而比 uniform 差
- n_min=4 待训练完成后重跑脚本即可自动纳入

---
