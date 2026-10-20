# run analysis decay curve

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_analysis_decay_curve_20260512T161823_result.json`
- **Structured JSON:** [`8e42c02be5b88ff73440.json`](../../sessions/8e/8e42c02be5b88ff73440.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。总结：

## EMA Score 衰减曲线分析结果

**假说：EMA centroid 收敛到平均表示，导致 score 失去区分度 — 部分证实。**

### 关键发现

| 指标 | 数值 |
|------|------|
| CV 衰减范围 | 5-28%（gamma=0.9/L36 衰减最严重 24%，gamma=0.5/L0 最严重 28%） |
| 初始 CV | 0.10-0.17（**本身就很低**） |
| 最终 CV | 0.09-0.16 |
| Score 均值 | 0.54-0.68（窄带，token间区分度极低） |
| Centroid 稳定性 | cos > 0.998（500 tokens 后几乎不动） |

### 根因分析

EMA eviction 失败有**两层原因**：

1. **Centroid 快速收敛**：500 tokens 后 centroid 几乎不变（cos > 0.998），本质上变成了"平均 K/V 表示"
2. **初始区分度就低**：即使在序列开头（前 2000 tokens），CV 也只有 0.10-0.17，意味着所有 token 和 centroid 的 cosine similarity 都落在 0.5-0.7 的窄带内。CV 衰减只是雪上加霜

**结论**：EMA similarity 不是一个好的 eviction signal — 问题不仅是 centroid 衰减，更根本的是 cosine similarity 在高维空间中天然缺乏区分度（所有向量都"差不多相似"），无法有效区分"重要"和"冗余" token。

### 产出
- 图1: `analysis_decay_curve.png` — Score 分布演变 + CV 衰减（6 panel）
- 图2: `analysis_centroid_convergence.png` — Centroid 收敛速率
- 数据: `analysis_decay_curve_results.json`
- Registry: `analysis_decay_curve` (DONE)

---
