# ops exp026 step5 monitor

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_step5_monitor_20260515T123320_result.json`
- **Structured JSON:** [`d3d718c547f73a29570a.json`](../../sessions/d3/d3d718c547f73a29570a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 训练进度报告

### 状态
- **进程**: PID 778562 存活，运行 1h55m
- **当前 step**: Step 2 刚完成（日志写入 20:32），Step 3 刚开始
- **Step 5 val 尚未到达**

### 训练指标趋势（train success）

| Step | Success | Action Valid | Entropy | PG Loss | PPO KL | Grad Norm | Time/Step |
|------|---------|-------------|---------|---------|--------|-----------|-----------|
| 0 (val) | 6.25% | 63.1% | — | — | — | — | — |
| 1 (train) | 21.88% | 68.6% | 0.380 | 0.0098 | 0.0082 | 7.25 | 38.0 min |
| 2 (train) | **32.81%** | 60.3% | 0.317 | 0.0057 | 0.0267 | 15.6 | 42.7 min |

趋势良好：success 从 6.25% → 21.88% → 32.81%，两步增长 **+26.6pp**。

### 注意信号
- **action_is_valid 下降**: 68.6% → 60.3%（step 2 降了 8pp），模型可能为了提高 success 牺牲了合规性
- **entropy 下降**: 0.380 → 0.317，策略正在收敛
- **PPO KL 上升**: 0.0082 → 0.0267（3.3×），step 2 偏离 ref policy 更多
- **grad_norm 翻倍**: 7.25 → 15.6，梯度波动增大

### GPU & 磁盘
- **GPU 0/1**: 100% 利用率，各用 ~49GB / 98GB VRAM
- **根分区**: 15G/30G（50%）
- **数据盘**: 137G/250G（55%）

### 时间预估
- Step 3 完成: ~21:15
- **Step 5 val 到达**: ~22:40（约 2 小时后）
- 150 步总训练: ~110 小时（4.6 天），预计 5/20 完成

---
