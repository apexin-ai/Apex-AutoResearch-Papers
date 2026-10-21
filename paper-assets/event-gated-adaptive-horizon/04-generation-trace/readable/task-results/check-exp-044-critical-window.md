# check exp 044 critical window

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_044_critical_window_20260522T121523_result.json`
- **Structured JSON:** [`25d93d4d1178d0b4d38e.json`](../../sessions/25/25d93d4d1178d0b4d38e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_044 Gradient Stop Walker — CIVO 已确认发生

| 指标 | 85K | 95K | 变化 |
|------|-----|-----|------|
| **eval_return** | 269.7 | **44.3** | -84% (峰值 75K 约 545) |
| **ve_ratio** | 0.89 | **4.45** | 5× 爆发，远超 1.5 阈值 |
| **delta_ve** | 0.44 | **3.56** | 加速恶化 |
| **civo_alert** | 0 | **1** | 已触发 |
| **value_mean** | 240.1 | 197.0 | value 仍高估 (vs eval 44) |
| **EMA_005 / EMA_095** | 216.7 / 274.5 | 168.8 / 244.4 | 缓慢下调但远不够 |

**当前 step**: ~104K（训练中，下次 eval 在 105K）

**CIVO 判断**: **Gradient stopping 失败，CIVO 完全发生。**

- 95K 时 CIVO 检测器已明确告警：`ve_ratio=4.448, delta_ve=3.558, accel=True, eval_decline=2/3`
- eval_return 从峰值 545 → 270 → 44，跌幅 92%
- 95K 后 train_return 大部分塌缩至 ~30（96K 的四个 episode: 28, 30, 30, 277；100K: 121, 172, 31, 30；104K: 31, 154, 80, 33）
- Value 网络估值 ~197 vs 实际 eval 44，过度高估 4.5 倍
- Gate 固定 dt=2，entropy=0（符合预期的 fixed_dt 配置）

**结论**: `reward_dt_emb_detach=True` 未能阻止 CIVO。梯度阻断仅切断了 reward 对 dt embedding 的反传，但 value function 的过度高估仍通过 actor-critic 回路放大，策略已全面崩溃。实验可以考虑提前终止。

---
