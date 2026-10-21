# analysis plan 034 nve threshold

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_034_nve_threshold_20260525T120442_result.json`
- **Structured JSON:** [`f7c017e404eae49e86dc.json`](../../sessions/f7/f7c017e404eae49e86dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_034 完成。核心结果：

- **56 个样本**（24 CIVO collapsed, 32 healthy），98 个实验因技术故障/无数据/baseline/模糊被排除
- **AUROC = 0.990**，NVE 是极好的 CIVO 判别器
- **推荐阈值 NVE ≥ 1.5**：F1=0.941, Precision=0.889, Recall=1.000, Accuracy=0.946
  - 零漏报（FN=0），3 个误报均为 frozen_dt_emb/mitigation 配置的瞬态 NVE 尖峰
- CIVO 组 NVE 中位数 4.12，Healthy 组中位数 0.80，重叠区间 [1.53, 1.93] 仅 6 个样本

---
