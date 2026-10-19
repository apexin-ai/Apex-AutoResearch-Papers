# analysis exp002v3 collapse

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp002v3-collapse_20260520T033746_result.json`
- **Structured JSON:** [`b6fd444f73337661667d.json`](../../sessions/b6/b6fd444f73337661667d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data collection complete. Here's the analysis:

---

## exp-002v3 Collapse 分析报告

### Collapse 时间线：两阶段崩溃

**Phase 1 — 长度坍缩 (step 100-300)**
| Step | Entropy | mean_len | grad_norm |
|------|---------|----------|-----------|
| 0 | 0.451 | 247.3 | 0.043 |
| 100 | 0.380 | 240.3 | 0.054 |
| 200 | 0.288 | **80.5** | 0.044 |
| 300 | 0.164 | 81.8 | 0.014 |
| 360 | **0.098** | 78.8 | 0.007 |

模型在 step 200 前就完成了长度坍缩（247→80 tokens），entropy 同步降至 0.1 以下。

**Phase 2 — 终末坍缩 (step 2150-2250)**
| Step | Entropy | grad_norm | frac_zero_std | mean_len |
|------|---------|-----------|---------------|----------|
| 2100 | 0.069 | 0.002505 | 0.087 | 97.7 |
| 2150 | 0.056 | 0.001540 | 0.125 | 96.8 |
| 2160 | **0.043** | 0.000589 | **0.269** | 97.4 |
| 2170 | **0.026** | 0.000293 | **0.419** | 95.7 |
| 2180 | 0.018 | 0.000548 | 0.550 | 94.9 |
| 2200 | 0.013 | 0.000330 | 0.631 | 94.4 |
| 2310 | 0.005 | 0.000000 | 0.850 | 93.1 |
| 2340 | 0.002 | 0.000077 | **0.963** | 93.0 |
| 2460 | 0.006 | 0.000062 | 0.825 | 93.1 |

**临界点在 step ~2160**：entropy 急速从 0.056→0.026（50 步内腰斩），frac_zero_std 从 0.125 跳到 0.419。之后 grad_norm → 0，模型完全停止学习。

### R1/R3 Reward 分析

- **R3 (format)**: 从 step ~100 起饱和在 0.9998 (std=0.0000)，**提供零学习信号**。模型很快学会了满足格式要求。
- **R1 (cosine contrastive)**: mean 始终在 0 附近剧烈波动（-0.46 to +0.41），**从未出现持续正向趋势**。5x scaling 没有帮助 R1 提供有效优化方向。
- **R2**: 全程为 0（被关闭）。

### 可用 Checkpoint

| Checkpoint | 保存时间 | 估计 entropy | 状态 |
|-----------|---------|-------------|------|
| checkpoint-500 | 05:23 | ~0.11 | Phase 1 后，低 entropy 平台期 |
| checkpoint-1000 | 07:14 | ~0.08 | 平台期中段 |
| checkpoint-1500 | 08:53 | ~0.07 | 平台期后段 |
| **checkpoint-2000** | **10:18** | **~0.062** | **Phase 2 前最后可用 checkpoint** |

所有 checkpoint 均在 Phase 1 长度坍缩之后（mean_len 已降至 ~93-105），没有任何 checkpoint 保留了健康状态（entropy > 0.3）。

### 结论与建议

**建议 Kill。** 理由：

1. **数据充分**：两阶段坍缩模式清晰——length collapse (step 200) → low-entropy plateau (300-2150) → terminal collapse (2160+)
2. **"scaled cosine R1 also fails" 结论已得到充分支持**：5x scaling 未能阻止坍缩，R1 mean 全程无正向趋势
3. **不可恢复**：grad_norm ≈ 0，frac_zero_std > 80%，模型输出近确定性
4. **根因明确**：R3 过早饱和（step 100），combined reward 退化为只有 R1 信号，而 cosine R1 的高方差无法提供稳定优化方向。即使 5x 放大也不够——问题不是 R1 太弱，而是 R1 信号本身噪声太大

---
