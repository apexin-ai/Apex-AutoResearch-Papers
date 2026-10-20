# diagnose tcn rave status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_tcn_rave_status_20260520T030432_result.json`
- **Structured JSON:** [`8db432f53a59bede0c86.json`](../../sessions/8d/8db432f53a59bede0c86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 进程状态：两个实验都在正常运行

| 实验 | PID | 状态 | 运行时间 | GPU |
|------|-----|------|----------|-----|
| exp_027_tcn_walker_s0 | 879355 | `Ss+` (运行中) | 10m27s | cuda:0 (PID 879360, 3257 MiB) |
| exp_028_rave_walker_s0 | 879636 | `Ss+` (运行中) | 10m24s | cuda:1 (PID 879641, 2742 MiB) |

### GPU 使用情况

| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|----------|--------|
| 0 | RTX PRO 6000 Blackwell | 10871/97887 MiB | 86% |
| 1 | RTX PRO 6000 Blackwell | 5498/97887 MiB | 95% |

注意：GPU 0 上还有其他进程（PID 877969, 878374），共占用额外 ~6.5GB。

### 训练进度

- **exp_027 (TCN)**: 已完成第一轮 eval（step 5000, eval_return=37.4），正在训练中（step 5000 的训练 metrics 已输出）
- **exp_028 (RAVE)**: 进度更快，已到 step 8000（train_return ~31.7-39.8），说明训练正常推进

### TCN/RAVE 代码实现：已实现

- **TCN**: `networks.py:241` — `img_step()` 接收 `tcn_sigma` 参数，当 >0 时对 dt embedding 添加高斯噪声（L257-258）。`models.py:691` 调用时传入 config 中的 `tcn_sigma`。
- **RAVE**: `models.py:746-751` — 当 `rave_ceiling > 0` 时，用 `_rave_anchor * rave_ceiling` 做 ceiling 约束。

### 结论

两个实验都在正常运行，代码已正确实现 TCN/RAVE 功能。Registry 状态仍为 PREPARING 是 registry 更新滞后，不影响实际训练。

---
