# analysis r16 shapiro wilk

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16-shapiro-wilk_20260523T164518_result.json`
- **Structured JSON:** [`11352bd38580cb7763b8.json`](../../sessions/11/11352bd38580cb7763b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。汇总如下：

---

## Shapiro-Wilk 正态性检验结果（340M, LAMBADA, h3-1 vs pure）

| Architecture | Group | n | W | p-value | Skewness | Kurtosis | Normal? |
|---|---|---|---|---|---|---|---|
| GatedDeltaNet | rescue | 422 | 0.8986 | 3.95e-16 | 1.406 | 2.616 | No |
| GatedDeltaNet | disruption | 678 | 0.9558 | 2.11e-13 | 0.768 | 0.344 | No |
| RetNet | rescue | 373 | 0.9089 | 3.37e-14 | 1.398 | 3.139 | No |
| RetNet | disruption | 479 | 0.9726 | 8.15e-08 | 0.639 | 0.386 | No |
| HGRN2 | rescue | 575 | 0.9196 | 6.14e-17 | 1.328 | 3.087 | No |
| HGRN2 | disruption | 337 | 0.9678 | 8.35e-07 | 0.528 | -0.373 | No |

**所有 6 个分组均在 α=0.05 下显著拒绝正态性。**

## 实际偏离程度

| Group | 实际偏离 | W 范围 | skew 范围 | 特征 |
|---|---|---|---|---|
| **Disruption** | 轻微偏离 | 0.955–0.973 | 0.53–0.77 | 温和右偏，IQR/std 接近理论值 1.35 |
| **Rescue** | 中度–强偏离 | 0.899–0.920 | 1.33–1.41 | 明显右偏 + 厚尾 (kurtosis 2.6–3.1) |

## 关键发现：Rescue 组接近对数正态

对 rescue 组做 log 变换后，W 从 ~0.90 跃升至 **>0.997**，skew 降至 ~0.1，几乎完美正态。说明 rescue 组的 |log p| 服从**对数正态分布**，而非正态分布。

| Architecture | Group | W (原始) | W (log变换) |
|---|---|---|---|
| GatedDeltaNet | rescue | 0.8986 | **0.9970** |
| RetNet | rescue | 0.9089 | **0.9975** |
| HGRN2 | rescue | 0.9196 | **0.9979** |

## 对论文 Appendix P.2 的影响

与预期（disruption 近似正态，rescue 轻微右偏）**部分一致但有偏差**：

1. **Disruption 组**：确实接近正态（轻微右偏），Shapiro-Wilk 拒绝主要因为 n=300–700 时检验功效过高，实际偏差不大
2. **Rescue 组**：偏离比预期更严重——不是"轻微右偏"，而是近似**对数正态**（skew~1.4，W~0.90）
3. 论文中 Φ(|d|/√2) 公式的正态性假设对 disruption 组大致成立，但对 rescue 组成立条件较弱。不过 AUC 公式的鲁棒性通常较好——即使底层分布偏离正态，只要两组分布形状相似（location-shift model），AUC 估计的偏差有限

---
