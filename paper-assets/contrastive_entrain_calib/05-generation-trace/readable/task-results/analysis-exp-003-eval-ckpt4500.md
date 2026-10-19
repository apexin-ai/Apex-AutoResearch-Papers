# analysis exp 003 eval ckpt4500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-ckpt4500_20260520T190452_result.json`
- **Structured JSON:** [`6653d53687fd345c9981.json`](../../sessions/66/6653d53687fd345c9981.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

## 分析摘要

### 指标

| Checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| vanilla baseline | 0.072 | 0.945 | 0.134 |
| ckpt-1000 | — | — | 0.074 |
| ckpt-2000 | — | — | 0.085 |
| ckpt-3000 | 0.050 | 0.972 | 0.095 |
| **ckpt-4000** | 0.061 | 0.967 | **0.114** |
| **ckpt-4500** | **0.072** | **0.961** | **0.134** |
| **ckpt-5000** | — | — | **0.114** |
| **ckpt-5500** | 0.061 | 0.972 | **0.114** |

### 关键发现：非单调轨迹，假设被推翻

原假设预设了两种可能：ckpt-4500 = 0.114（plateau 始于 4000）或更低（plateau 始于 4500-5000 之间）。**实际结果两者都不是**——ckpt-4500 SYCONScore = 0.1337，**显著高于** ckpt-4000/5000/5500 的 0.114，几乎追平 vanilla baseline（0.1335）。

轨迹是**非单调的**：
- step 1000→4500：持续上升（0.074 → 0.085 → 0.095 → 0.114 → **0.134**）
- step 4500→5000：**骤降**回 0.114（跌幅 -17%）
- step 5000→5500：锁定在 0.114

### Plateau onset 判定

**不存在从 step 4000 开始的简单 plateau。** 实际模式是：
- R3-only 训练在 step 4500 达到峰值（≈vanilla baseline）
- 随后发生性能退化（可能是过拟合或 reward hacking）
- Step 5000-5500 才是真正的 plateau/退化区间

### Conclusion = negative

ckpt-4500 SYCONScore (0.1337) ≈ vanilla baseline (0.1335)，本质上只是恢复到了未训练水平，未实现改进。R3-only 训练的最佳 checkpoint 也仅能追平 baseline，进一步证实单独使用 behavioral reward (R3) 不足以超越 vanilla。

---
