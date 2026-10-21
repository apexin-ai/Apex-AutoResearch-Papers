# analysis nve threshold v3 reviewer fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_threshold_v3_reviewer_fix_20260515T170034_result.json`
- **Structured JSON:** [`596caf3af6a4f3c0c6b1.json`](../../sessions/59/596caf3af6a4f3c0c6b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已生成。关键发现：

### Per-Experiment max_nve (35K+)
| Experiment | max_nve | 分类 |
|---|---|---|
| exp_006_fixed_dt2 | **4.8362** | CIVO collapse |
| exp_008d_subsample_on_h8 | **4.1292** | CIVO collapse |
| exp_008e_v3_walker_s2 | **3.7801** | late collapse |
| exp_009b_008d_walker_s2 | **1.6190** | self-corrected |
| exp_001_baseline | 1.0000 | healthy |
| exp_008f | 0.9701 | healthy |
| exp_008e_v3_walker_s1 | 0.9411 | healthy (stable) |
| exp_008a | 0.9322 | healthy |

### Task A (检测 trained dt_emb)
- **AUROC = 0.867**，CI [0.5, 1.0]
- threshold 1.3 和 1.5 最优：Acc=87.5%, P=100%, R=80%, F1=88.9%
- FN 是 exp_008e_v3_walker_s1（有 trained dt_emb 但 NVE=0.94，行为完全 healthy）

### Task B1 (预测 CIVO 崩溃，009b=negative)
- **AUROC = 1.0**，完美分离
- threshold ≥ 1.7 时完美分类：Acc=100%, F1=1.0
- 009b 的 max_nve=1.62 刚好落在 collapse 和 stable 之间

### Task B2 (预测 CIVO 崩溃，009b=positive)
- **AUROC = 1.0**
- threshold 1.5 完美：Acc=100%, F1=1.0
- threshold ≥ 1.7 时 009b 被漏掉（FN=1）

JSON 已保存到 `artifacts/nve_threshold_v3.json`，脚本在 `scripts/nve_threshold_analysis_v3.py`。

---
