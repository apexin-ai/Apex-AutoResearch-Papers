# analysis exp 006 full metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_006_full_metrics_20260514T004608_result.json`
- **Structured JSON:** [`63965f1c23b64586ced6.json`](../../sessions/63/63965f1c23b64586ced6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已保存。以下是 summary：

---

## exp_006 (fixed_dt2) 状态

**进程**: 仍在运行 (PID 85029)，当前 ~65K / 150K 步
**gate_dt_mean**: 始终 2.0（符合预期）

## eval_return 轨迹

| Step | fixed_dt2 | Baseline | 差距 |
|------|-----------|----------|------|
| 5K   | 31.0      | 31.8     | -0.8 |
| 15K  | 256.9     | 206.6    | +50.3 |
| 25K  | 321.4     | 395.3    | -73.9 |
| 35K  | **485.3** (peak) | 388.5 | +96.9 |
| 45K  | 477.0     | 513.8    | -36.8 |
| 55K  | 360.4     | 625.7    | **-265.3 (-42.4%)** |

Baseline 后续持续攀升至 932.2 @ 145K。

## 趋势判断

1. **存在明显崩塌**：35K peak 后连续两个 eval 点下降，55K 时较 peak 跌 25.7%，且下降加速（-8 → -117）
2. **世界模型正常，策略端出问题**：model_loss 持续下降（20.7→4.9），但 eval_return 反向走低，说明 fixed dt=2 的 imagination horizon 导致策略优化不稳定
3. **与 baseline 差距急剧扩大**：前 35K 交替领先，55K 后已落后 42%，且 baseline 后续还会升至 900+
4. **趋势不乐观**：虽然实验还在跑，但倒V形曲线没有回升迹象

---
