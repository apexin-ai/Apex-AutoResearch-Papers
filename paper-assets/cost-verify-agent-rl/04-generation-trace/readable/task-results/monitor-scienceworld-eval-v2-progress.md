# monitor scienceworld eval v2 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_scienceworld_eval_v2_progress_20260519T201136_result.json`
- **Structured JSON:** [`04ce81037eeb10ba7124.json`](../../sessions/04/04ce81037eeb10ba7124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_v2 进度报告

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE (PID 187796, 运行 1h25m) |
| **进度** | **159/1796** (8.9%) |
| **GPU** | cuda:0,1 各占用 84GB, 利用率 46% |
| **当前任务** | `find-living-thing` 系列 (v154–v193) |

### 初步指标 (159 episodes)

| 指标 | 值 |
|------|-----|
| **Success (OK)** | 74/159 (**46.5%**) |
| **Fail** | 86/159 (注: OK+FAIL=160, 日志含1行非episode行) |

### 速度估算

- 159 episodes / 85 min ≈ **1.87 ep/min**
- 剩余 1637 episodes ≈ **875 min (~14.6h)**
- 预计完成时间: 约 **5月20日 19:00**

### 观察

- FAIL episodes 多数跑满 100 steps (40-95s)，OK episodes 通常 10-20 steps (4-8s)
- FAIL 的 valid_action_rate 普遍很低 (0%-46%)，OK 的普遍 60%-90%
- 结果文件 `eval_results_dev_v2.json` 尚未生成（应是全部完成后才写入）

---
