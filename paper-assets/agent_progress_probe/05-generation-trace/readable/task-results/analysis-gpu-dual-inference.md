# analysis gpu dual inference

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu-dual-inference_20260514T221738_result.json`
- **Structured JSON:** [`a8e8a4d3d1182e397bc2.json`](../../sessions/a8/a8e8a4d3d1182e397bc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成，产出已注册。

## 结果摘要

### Task A: 跨 Encoder 预测一致性

| 指标 | 值 |
|---|---|
| 交集 test windows | 269 (STE:2206, E5:1824, BGE:1824) |
| 3/3 一致 | 85.87% (231/269) |
| 2/3 一致 | 14.13% (38/269) |
| 完全不一致 | 0% |
| Fleiss' Kappa | **0.6449** (substantial) |

**Pairwise 相关系数：**
| Pair | Pearson r | Spearman r |
|---|---|---|
| STE vs E5-large | 0.629 | 0.655 |
| STE vs BGE-M3 | 0.700 | 0.620 |
| E5 vs BGE-M3 | **0.874** | **0.811** |

**不一致样本特征：** 38 个不一致 window 全部 conf=2，STE 平均概率 0.74（偏高），E5/BGE 平均 0.35/0.37（偏低）。位置分布 early:15 / mid:8 / late:15，early 和 late 阶段不一致更多。

### Task B: Probe 校准分析

| 指标 | 原始 | Temperature Scaling (T=2.06) |
|---|---|---|
| ECE | 0.0606 | **0.0451** |
| Brier Score | 0.0632 | **0.0586** |
| MCE | 0.4965 | — |

模型输出高度 bimodal：64.4% 的 window 概率 >0.9，21.7% <0.1。中间区间（0.4-0.7）严重过置信——置信度 45-63%，实际准确率仅 12-23%。Temperature scaling (T=2.06, val set 拟合) 将 ECE 降低 25%。

---
