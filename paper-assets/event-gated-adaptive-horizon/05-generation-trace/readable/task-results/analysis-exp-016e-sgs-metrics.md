# analysis exp 016e sgs metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_016e_sgs_metrics_20260515T221814_result.json`
- **Structured JSON:** [`b27585c867aad7888cd8.json`](../../sessions/b2/b27585c867aad7888cd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。完整 v/e ratio 分析如下：

## exp_016e SGS v/e Ratio 完整数据

| Step | eval_return | value_mean | v/e ratio | baseline_ve | **NVE** |
|------|------------|------------|-----------|-------------|---------|
| 5K   | 31.0       | 0.001      | 0.00      | —           | —       |
| 15K  | 140.3      | 3.1        | 0.022     | —           | —       |
| 25K  | 141.8      | 23.0       | 0.162     | 0.087       | **1.86** |
| 35K  | 173.0      | 53.5       | 0.309     | 0.241       | **1.28** |
| 45K  | 184.0      | 85.3       | 0.464     | 0.331       | **1.40** |
| 55K  | 153.8      | 115.6      | 0.752     | 0.404       | **1.86** |
| 65K  | 324.3      | 152.3      | 0.469     | 0.563       | 0.83   |
| 75K  | 326.7      | 190.0      | 0.582     | 0.719       | 0.81   |
| 85K  | 256.2      | 215.4      | 0.841     | 0.701       | **1.20** |
| 95K  | **31.7**   | 208.9      | **6.583** | 0.632       | **10.42** |

## 诊断结论

**CIVO: 确认存在，灾难性崩溃 @95K**
- NVE 在 25-55K 持续偏高（1.3-1.9x），65-75K 短暂压制（eval 跳升时），85K 回升到 1.2x，95K 爆发到 **10.42x**
- actor_loss 在 95K 翻正（0.014），确认 value 过度膨胀驱动 actor 崩溃
- eval 从 327@75K → 31.7@95K（回到随机策略水平）
- train_return@96K = 41-101（已全面崩溃）

**vs 008d 对比**: 008d 在 55K 就出现 NVE 峰值 4.12x 但随后自愈；016e 的 SGS 干预**推迟了崩溃**（55K→95K）但使最终崩溃**严重得多**（NVE 10.42x vs 4.12x，eval 完全归零）。

**SGS 结论**: `reward_dt_emb_detach=True` 未能阻止 CIVO。CIVO 的传导路径不仅通过 reward head 的 dt_emb 梯度。

实验当前 96K，还在跑向 105K，但已全面崩溃。

---
