# analysis qwen15b median ppl

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_median_ppl_20260524T044540_result.json`
- **Structured JSON:** [`7d354e96330850503a22.json`](../../sessions/7d/7d354e96330850503a22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## PPL

| β | Model | mean | median | trimmed99 | max | outliers(>100) |
|---|-------|------|--------|-----------|-----|----------------|
| 0.0 | Base | 1.8816 | 1.9092 | 1.8707 | 2.41 | 0 |
| 0.0 | TG | 1.8711 | 1.8965 | 1.8621 | 2.31 | 0 |
| 3.0 | **Base** | **5,707,632.79** | **2.2162** | **2.2985** | **279,673,896** | **1 (conv[10])** |
| 3.0 | TG | 1.9918 | 1.9745 | 1.9769 | 2.73 | 0 |
| 5.0 | Base | 2.8476 | 2.8042 | 2.7933 | 5.51 | 0 |
| 5.0 | TG | 2.6879 | 2.6244 | 2.6658 | 3.77 | 0 |

## GAR

| β | Model | mean | median |
|---|-------|------|--------|
| 0.0 | Base | 0.0167 | 0.0114 |
| 0.0 | TG | 0.0233 | 0.0158 |
| 3.0 | Base | 0.1202 | 0.0924 |
| 3.0 | TG | 0.1143 | 0.1030 |
| 5.0 | Base | 0.6571 | 0.6512 |
| 5.0 | TG | 0.7150 | 0.7104 |

**关键发现：**

- β=3 Base 有 1 个 catastrophic outlier：conv[10] PPL = **2.8 亿**，导致 mean PPL 完全不可用。Median PPL = 2.22 是合理的。
- TG 在所有 β 下都没有 outlier，说明 TG 训练后模型更稳定。
- 用 median 后，β=3 的 Base vs TG PPL 对比变为 2.22 vs 1.97（TG 更低，更好），而不是原来 mean 显示的 570 万 vs 1.99。
- β=5 Base median PPL (2.80) 也高于 TG (2.62)，TG 在高 β 下保持更低 PPL。
- GAR 的 median 和 mean 差异不大，没有极端 outlier。

---
