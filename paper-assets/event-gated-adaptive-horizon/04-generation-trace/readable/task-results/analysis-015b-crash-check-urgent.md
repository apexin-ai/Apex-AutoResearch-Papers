# analysis 015b crash check urgent

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_015b_crash_check_urgent_20260515T150616_result.json`
- **Structured JSON:** [`3451374d6fb3cab7ac20.json`](../../sessions/34/3451374d6fb3cab7ac20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。整理结果。

---

## 015b 状态报告

### 1. 进程状态
- **PID 149991 存活**，运行 2h41m，当前在 **52K step**
- **55K eval 尚未到达**，无法直接确认/否认崩溃

### 2. 015b Eval Checkpoints

| Step | eval_return | value_mean | v/e | actor_entropy | actor_loss |
|------|-------------|------------|-----|---------------|------------|
| 5K | 31.0 | 0.00 | 0.0 | 8.159 | -0.109 |
| 15K | 167.9 | 3.29 | 0.02 | 1.550 | -0.222 |
| 25K | 171.8 | 21.48 | 0.125 | -0.311 | -0.060 |
| **35K** | **201.6** | 39.28 | 0.195 | -1.182 | -0.026 |
| **45K** | **122.3** | 51.09 | **0.418** | -3.344 | **-0.014** |

### 3. 015b Train Returns (36K-52K)

| Step | Episode 1 | Episode 2 | Episode 3 | Episode 4 | Avg |
|------|-----------|-----------|-----------|-----------|-----|
| 36K | 187.5 | 86.6 | 163.5 | 230.0 | 166.9 |
| 40K | 171.6 | 105.0 | 221.6 | 93.8 | 148.0 |
| 44K | 138.3 | 215.9 | 67.7 | 218.5 | 160.1 |
| 48K | 179.9 | 186.8 | 106.9 | 208.6 | 170.6 |
| **52K** | **33.1** | **30.5** | **260.8** | **39.1** | **90.9** |

52K 确认崩溃信号：**3/4 episode 跌至 30-40（随机策略水平）**，1 个异常高 260.8。

### 4. 015b vs 008d 对比

| Step | 015b eval | 015b v/e | 008d eval | 008d v/e | 差异 |
|------|-----------|----------|-----------|----------|------|
| 5K | 31.0 | 0.0 | 31.0 | 0.0 | 0 |
| 15K | 167.9 | 0.02 | 153.7 | 0.022 | +14.2 |
| 25K | 171.8 | 0.125 | 167.2 | 0.155 | +4.6 |
| 35K | **201.6** | 0.195 | 146.3 | 0.411 | **+55.3** |
| 45K | 122.3 | 0.418 | 140.8 | 0.693 | -18.5 |
| 55K | *TBD* | *TBD* | **82.7** | **1.666** | — |

### 5. 崩溃机制分析

**015b 不是 CIVO。是 policy collapse via gradient starvation。**

关键证据：

| 指标 | 015b@45K | 008d@45K | 解读 |
|------|----------|----------|------|
| v/e | **0.418** | 0.693 | 015b 价值低估，非高估 |
| value_mean | 51 | 98 | 015b critic 保守 |
| actor_entropy | -3.34 | -4.58 | 015b 熵更高（还没完全坍缩） |
| **actor_loss** | **-0.014** | -0.106 | **015b 梯度信号接近零** |

**两种完全不同的崩溃路径：**

- **008d = 经典 CIVO**：v/e 单调上升 0→1.67，value 膨胀到 138，actor 被过高估值误导到窄策略，最终崩溃
- **015b = 梯度饥饿 (gradient starvation)**：actor_loss 从 -0.22 持续萎缩到 -0.014（接近零），策略梯度信号消失，actor 停止学习

**根因推测：frozen dt_emb。** 世界模型在持续训练中改变内部表示，但时间嵌入被冻结无法跟随。随着表示漂移，actor 的梯度信号在冻结嵌入附近变得平坦。到 48-52K，漂移超过临界点，策略突然崩溃。

佐证：
- 015b 在 35K 一度达到 201.6（远超 008d 的 146.3），说明早期冻结嵌入反而稳定了训练
- 崩溃发生在 48K→52K 之间，非常突然（train_return avg 从 170.6 骤降到 90.9）
- 52K 的 3/4 episode 退化到随机水平（~30-40），但 1 个仍有 260.8 → 策略双峰化，偶尔命中旧策略

### 6. 结论

- **55K eval 尚未到达**，大约还需 ~20min
- **崩溃已高度确定**（52K train return 3/4 归零），等 55K eval 做最终确认
- **不是 CIVO**，是 frozen dt_emb 导致的 gradient starvation → policy collapse
- **不 kill**，继续跑到 65K 收集完整崩溃轨迹

---
