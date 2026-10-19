# ops exp026 step3 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_step3_check_20260515T125557_result.json`
- **Structured JSON:** [`24cd64390f9dd340ecc7.json`](../../sessions/24/24cd64390f9dd340ecc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 训练进度报告

### 状态
- **进程**：PID 778562 存活，状态正常
- **GPU**：双卡 100% 利用率，各 ~49GB/97GB — 正常满载
- **当前位置**：Step 3 训练中（actor update 阶段），尚未完成

### 已完成指标汇总

| Step | 阶段 | success | entropy | grad_norm | kl_loss | ppo_kl | action_is_valid |
|------|------|---------|---------|-----------|---------|--------|-----------------|
| 0 | val | 6.25% | - | - | - | - | 63.1% |
| 1 | train | 21.88% | 0.267 | 14.43 | 0.18 | - | - |
| 2 | train | 32.81% | 0.317 | 15.62 | 0.097 | 0.027 | 60.3% |

Worker log 文件 1496 行，最后一条是 step 2 完整指标。Step 3 尚无输出行。

### 异常监控（三项均无异常）
1. **Entropy 突降 >30%**：Step 1→2 从 0.267 升至 0.317（+18.7%），趋势健康，无突降
2. **Success 连续 2 步下降**：0→1→2 为 6.25%→21.88%→32.81%，持续上升
3. **GPU 利用率骤降**：双卡均 100%，正常

### 时间估算
- Step 2 耗时 ~2561s（42.7 min），stderr 最后时间戳 20:21:39
- Step 3 预计完成时间：**~21:05**（约 8 分钟后）
- Step 4 预计完成：~21:47
- **Step 5 val 预计出结果：~21:55**（约 1 小时后）

### Checkpoint
exp026 目录为空（save_freq=25，test_freq=5，还没到保存点）。

---
