# analysis threshold report verify

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_threshold-report-verify_20260515T102203_result.json`
- **Structured JSON:** [`6f0ab516848ca04b7f81.json`](../../sessions/6f/6f0ab516848ca04b7f81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Verification complete. Here are the results:

## 逐项验证结果

### 1. NVE 值 vs Registry — **PASS**

所有 9 个实验的 NVE 值与 registry 精确匹配：

| 实验 | Report max NVE | Registry 验证 |
|------|---------------|--------------|
| 006 | 4.83 | 2.722/0.563=4.83 ✓ |
| 008d | 4.12 | 1.666/0.404=4.12 ✓ |
| 008e_v3 s2 | 3.78 | ve_ratio_trajectory nve=3.78 ✓ |
| 009b | 1.62 | normalized_ve@45K=1.62 ✓ |
| 008e_v3 s1 | 0.94 | normalized_ve@35K=0.94 ✓ |
| 009c | 1.14 | normalized_ve@105K=1.14 ✓ |
| 008f | 0.97 | normalized_ve@55K=0.97 ✓ |
| 008a | 0.93 | normalized_ve@55K=0.93 ✓ |
| 008c | 0.90 | 0.218/0.241=0.90 ✓ |

全部轨迹点也逐一匹配（已验证所有 checkpoint NVE）。

### 2. 分组 — **PASS**
- Trained dt_emb (5): 006, 008d, 008e_v3_s2, 009b, 008e_v3_s1 ✓
- Untrained/No dt_emb (4): 008a, 008c, 008f, 009c ✓

### 3. 1.5x Threshold Accuracy — **PASS**
- TP=4 (006, 008d, 008e_v3_s2, 009b), FN=1 (008e_v3_s1@0.94)
- TN=4 (all untrained < 1.5), FP=0
- TPR=80%, TNR=100%, Accuracy=8/9=88.9% ✓

Threshold sweep 全表也已验证（1.0x 到 2.0x 每行 TP/FN/TN/FP 均正确）。

### 4. §4 Time Window — **PASS**
- Early (35K-55K): TPR=60% (3/5), missed 008e_v3_s1 + s2 ✓
- Mid (55K-75K): TPR=40% (2/5), missed 008e_v3_s1 + s2 + 009b ✓
- Late (75K-105K): TPR=20% (1/5) ✓
- Full: TPR=80% (4/5) ✓

### 5. §6 Collapse Rate — **PASS**
- dt=2 trained: 1/2 (008d collapsed, 009b self-corrected) ✓
- dt=1 trained: 1/2 (008e_v3_s1 healthy, 008e_v3_s2 collapsed) ✓
- 两者均 50% ✓

### 6. 旧错误文字 — **PASS**
`analysis/` 版本中无 "~100%"、"~50%"、"perfect classification" 残留。

---

## 发现一个问题

**`_project/report/threshold_sensitivity_report.md` 是旧版本，未同步更新。** 它仍然包含：
- 分组 4 trained / 5 untrained（错误，008e_v3_s1 被放在 untrained 组）
- "100% accuracy"、"perfect classification"（旧错误文字）
- Threshold sweep 表使用旧数字（如 1.5x 显示 100% accuracy 而非 88.9%）

`analysis/` 版本是正确的修订版。需要将 `_project/report/` 副本同步为 `analysis/` 版本。

是否需要我同步更新 `_project/report/` 副本？

---
