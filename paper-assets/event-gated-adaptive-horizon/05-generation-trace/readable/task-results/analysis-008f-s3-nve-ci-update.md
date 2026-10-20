# analysis 008f s3 nve ci update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_008f_s3-nve-ci-update_20260516T201039_result.json`
- **Structured JSON:** [`217960c0c484f9d0283f.json`](../../sessions/21/217960c0c484f9d0283f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有文件已更新。总结:

**008f_s3 NVE 提取结果:**
- 35K+ 窗口 NVE peak: **0.8509** @ step 95K
- 全步数 NVE peak: **0.8667** @ step 25K
- 35K+ sustained avg: **0.5731**
- eval_return_peak: 594.18 @ step 85K
- eval_return_final: 420.71
- collapse: 0（无崩溃）

**已更新的文件（共 10 个）:**

| 文件 | 更新内容 |
|------|---------|
| `bootstrap_ci_results.json` × 2 | no_dt_emb n=3, peaks=[0.97, 0.82, 0.85], mean=0.88, CI=[0.82, 0.97] |
| `bootstrap_cis/bootstrap_cis.json` + `_project/data/bootstrap_cis.json` | no_dt_emb n=3, nve_peak mean=1.05 CI=[0.87, 1.26] |
| `artifacts/bootstrap_cis.json` | no_dt_emb n_seeds=3, mean=0.9879 CI=[0.8509, 1.1425] |
| `bootstrap_ci_summary.md` × 3 | no_dt_emb 行: n=3, status ⚠️→✓, 更新 effect sizes |
| `compute_bootstrap_cis.py` | 加入 008f_s3 原始数据 |

---
