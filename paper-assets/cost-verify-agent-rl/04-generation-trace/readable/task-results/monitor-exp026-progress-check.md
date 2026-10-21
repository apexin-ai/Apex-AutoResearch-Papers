# monitor exp026 progress check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp026_progress_check_20260515T135705_result.json`
- **Structured JSON:** [`c28bdad11bdec104e5ea.json`](../../sessions/c2/c28bdad11bdec104e5ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 训练进度汇总

**进程状态**: PID 781795 运行中，已运行 3h18m，当前正在执行 Step 5。

### 每步关键指标

| Step | Type | Success | Pass@16 | Entropy | KL Loss | Grad Norm | Action Valid | 耗时 |
|------|------|---------|---------|---------|---------|-----------|-------------|------|
| 0 | val | 6.25% | — | — | — | — | 63.1% | — |
| 1 | train | 21.88% | 1.0 | 0.267 | 0.180 | 14.43 | 68.6% | 38m |
| 2 | train | **32.81%** | 1.0 | 0.317 | 0.097 | 15.62 | 60.3% | 43m |
| 3 | train | 17.19% | 0.75 | 0.387 | 0.262 | 15.65 | 64.1% | 50m |
| 4 | train | **0.00%** | **0.0** | 0.387 | 0.054 | 13.81 | 71.7% | 55m |

### 异常信号：Step 4 完全崩溃

**严重问题**：train success 从 step 2 的 32.81% 峰值连续下跌，step 4 归零（success=0%, pass@16=0%）。

特征分析：
- **entropy 没有崩溃**（维持 0.387），说明不是典型的 policy collapse（策略仍有多样性）
- **KL loss 反而降低**（0.262→0.054），模型回到了接近 reference policy 的状态
- **action_is_valid 反而上升**（64.1%→71.7%），格式正确但内容无效
- 解读：模型可能被 step 3 的负梯度过度惩罚，退回到一个"格式正确但不解决问题"的保守策略

### Step 5 Val 结果

**尚无**。Step 5 正在进行中（已进入约 12 分钟），预计还需 ~40 分钟完成。且从日志看，val eval 仅在 step 0 执行过一次（初始 baseline），后续 train step 未触发 val eval。需要确认 eval_interval 配置——如果设为每 5 步 eval 一次，step 5 结束后才会触发第一次训练后 val eval。

### 时间预估

平均每步耗时在增长（38m→55m），以当前 ~50min/step 计算：
- 剩余 146 步 × 50min = **~121 小时 ≈ 5 天**
- 但鉴于 step 4 已经归零，继续跑 150 步大概率是无意义的

### 判断

Step 4 train success=0% + pass@16=0% 是明确的训练失败信号。建议等 step 5 完成后确认是否恢复，如果 step 5 仍为 0%，应终止实验并调整超参（降低学习率或增加 entropy bonus）。

---
