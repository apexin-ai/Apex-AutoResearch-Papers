# analysis random reweight seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random_reweight_seed123_20260522T005350_result.json`
- **Structured JSON:** [`7233bcd421c16913e375.json`](../../sessions/72/7233bcd421c16913e375.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。总结：

---

## 实验 random_reweight_seed123 结果

**Holdout PPL = 17.945**（loss=2.887，6103步，4h23m，train_loss=8.042）

### 对比分析

| 实验 | Holdout PPL | Δ vs adaptive_seed123 |
|------|------------|----------------------|
| **random_reweight_seed123** | **17.945** | **+0.329** |
| random_reweight_v2_seed42 (参考) | 17.830 | +0.214 |
| adaptive_fix_seed123 (bs16_r2) | 17.616 | baseline |
| uniform_seed123 | 17.686 | +0.070 |

### 跨 seed 一致性
- seed42 random reweight: 17.830
- seed123 random reweight: 17.945
- 两者都明显差于对应的 adaptive（~17.62-17.65），差值 Δ ≈ +0.21~0.33

### 结论：Detector signal 跨 seed 一致地 load-bearing

打乱 q_scores 后 PPL 退化到 17.945，比真实 detector adaptive（17.616）高 **0.33**，甚至差于 uniform baseline（17.686）。这表明 adaptive weighting 的收益不是来自于权重分布的形状本身，而是来自 detector 对 contamination 的正确定位。两个 seed 结果一致，结论稳健。

---
