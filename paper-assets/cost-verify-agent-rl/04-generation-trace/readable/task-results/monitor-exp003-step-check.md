# monitor exp003 step check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp003_step_check_20260513T230135_result.json`
- **Structured JSON:** [`5fe552cfa852af3bfc1a.json`](../../sessions/5f/5fe552cfa852af3bfc1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp003 训练状态报告

| 项目 | 状态 |
|------|------|
| **进程** | ✅ 存活 (PID 157852, 已运行 1h23m) |
| **当前 step** | **0 / 100** — 刚完成初始验证，尚未开始第一个训练 step |
| **Training Progress** | `0%｜0/100` |
| **pg_loss** | 无数据（尚未进入训练循环） |
| **错误** | 无 Traceback / OOM / killed |

### Step 0 验证指标（baseline）

| 指标 | 值 |
|------|-----|
| success | 0.0 |
| manager_invalid_action | **0.95** (95%) |
| action_is_valid | 0.00125 |
| action_is_effective | 0.05 |
| pass@1 | 0.0 |
| num_actions | 2.5 |
| response_length | 1922.75 |
| reward mean@16 | -4.75 |
| reward best@16 mean | -2.53 |

### GPU 状态

| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| cuda:0 | 100% | 17.1 GB / 95.6 GB |
| cuda:1 | 100% | 16.9 GB / 95.6 GB |

### 分析

训练已运行 ~1h23m，目前仍在 step 0 的数据收集/rollout 阶段。128 条轨迹（16 env_groups × 8 group_size）× 50 max_turns 的初始 rollout 比较耗时。GPU 满载运行中，无错误，预计很快进入第一个训练 step 的参数更新。95% invalid_action rate 是 base 模型预期的基线水平。

---
