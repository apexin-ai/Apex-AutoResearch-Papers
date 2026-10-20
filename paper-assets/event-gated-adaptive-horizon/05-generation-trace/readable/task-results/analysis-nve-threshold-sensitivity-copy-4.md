# analysis nve threshold sensitivity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve-threshold-sensitivity_20260517T115238_result.json`
- **Structured JSON:** [`4630319d7a08743806c8.json`](../../sessions/46/4630319d7a08743806c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果保存在 `artifacts/analysis/nve_threshold_sensitivity.json`。

## 结果摘要

| Threshold | Accuracy | Precision | Recall | F1 |
|-----------|----------|-----------|--------|------|
| **1.3×** | 0.818 | 0.600 | 1.000 | 0.750 |
| **1.5×** | **1.000** | **1.000** | **1.000** | **1.000** |
| **1.7×** | 0.818 | 1.000 | 0.333 | 0.500 |
| **2.0×** | 0.818 | 1.000 | 0.333 | 0.500 |

**AUROC = 1.0**（正负类完全可分）

**推荐最优阈值：1.5×**

- 在 11 个实验上实现完美分类
- 最近的负例是 `exp_015b_frozen_dt_emb`（peak NVE = 1.454），最近的正例是 `exp_008d_civo_trigger_s3`（peak NVE = 1.528）
- 分离间隙仅 0.074，虽窄但干净
- 1.3× 太松（frozen_dt_emb 和 baseline_walker_s2 被误判为 positive）；1.7×/2.0× 太严（只能抓住 full collapse 的极端 case，漏掉温和 CIVO）

---
