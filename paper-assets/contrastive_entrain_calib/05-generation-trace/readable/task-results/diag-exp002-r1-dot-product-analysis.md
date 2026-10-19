# diag exp002 r1 dot product analysis

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp002-r1-dot-product-analysis_20260518T233004_result.json`
- **Structured JSON:** [`f86b188e22946449862c.json`](../../sessions/f8/f86b188e22946449862c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## 诊断结果

### 1. Activation Norms — 远超预期

| Layer | Mean ||h|| | Min | Max |
|-------|-----------|-----|-----|
| 19 | 108.6 | 106.9 | 111.1 |
| 20 | 120.7 | 118.6 | 123.4 |
| 24 | 268.5 | 263.1 | 274.0 |
| 27 | 420.2 | 411.8 | 426.1 |
| 32 | 856.8 | 838.9 | 875.0 |
| 33 | 1001.9 | 980.8 | 1023.8 |
| **35** | **1182.6** | 1117.9 | 1275.4 |

深层 activation norm 达到 **1000+**，d_syc 是单位向量，所以 dot product 的量级完全由 ||h|| 决定。

### 2. Raw Dot Products — 深层严重饱和

| Layer | Mean | Std | Min | Max | \|val\|>20 |
|-------|------|-----|-----|-----|-----------|
| 19 | 9.92 | 3.94 | 2.61 | 17.54 | 0/20 |
| 20 | 11.02 | 5.97 | -2.27 | 20.46 | 1/20 |
| 24 | -5.16 | 18.58 | -46.17 | 14.98 | 3/20 |
| 27 | 12.16 | 34.60 | -55.86 | 54.68 | **15/20** |
| 32 | 107.82 | 56.06 | -9.68 | 176.08 | **17/20** |
| 33 | 70.40 | 58.96 | -53.64 | 142.95 | **19/20** |
| 35 | 43.89 | 66.16 | -92.71 | 127.65 | **16/20** |

Layer 32 的 dot product 最大值达 **176**，除以 scale=20 后是 8.8，tanh(8.8) ≈ 1.0000。

### 3. tanh(dot/20) — 深层完全饱和

| Layer | Mean | |val|>0.9 |
|-------|------|-----------|
| 19 | 0.4464 | 0/20 |
| 20 | 0.4742 | 0/20 |
| 24 | -0.0843 | 3/20 |
| 27 | 0.3439 | **13/20** |
| 32 | 0.8832 | **17/20** |
| 33 | 0.6764 | **17/20** |
| 35 | 0.4667 | **16/20** |

Layer 27-35 的 R1 基本是 {-1, +1} 二值信号。

### 4. Cosine Similarity — 数值合理但区分度有限

Cosine 值在 [-0.17, +0.21] 范围内，不饱和，但两组的 mean 差异小（valid=0.044 vs invalid=0.078），std 也大。AUROC: dot=0.69, cosine=0.67，几乎无差。

### 5. 诊断结论

**CONFIRMED: tanh 饱和是 R1 震荡的根因。**

- 平均 activation norm = **565.6**
- **50.7%** 的 dot product 绝对值 > 20（tanh 饱和阈值）
- 深层（L27-35）几乎全部饱和，R1 退化为 ±1 噪声
- 浅层（L19-20）还在 tanh 线性区，但信号本身也弱

**但 cosine similarity 直接替换也不够**：AUROC 仅 0.67-0.69，说明单靠 asst_first 位置的方向投影区分 valid/invalid 的能力本身就弱。问题不止是 scale，方向信号本身也需要增强。

---
