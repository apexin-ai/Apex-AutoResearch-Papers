# monitor exp015 step1 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp015-step1-check_20260514T130738_result.json`
- **Structured JSON:** [`f7f13e8d00d673e7192a.json`](../../sessions/f7/f7f13e8d00d673e7192a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp015 状态报告

| 项目 | 状态 |
|------|------|
| **进程** | PID 334692 存活，运行 10:35，状态 Ss+ |
| **GPU** | GPU 0: 57% 利用率, 48.3/97.9 GB; GPU 1: 61% 利用率, 48.3/97.9 GB |
| **训练进度** | **epoch 1/30 (3%)** 已完成，耗时 5:37/epoch，预计总时长 ~2h43m |
| **val→train 过渡** | **成功** ✓ — validation step 0 已完成，training step 1 已完成并进入 step 2 |

### Step 0 Validation Metrics（baseline）

| Metric | 值 |
|--------|-----|
| success | 0.0 |
| pass@1 | 0.0 |
| action_is_valid | 0.858 |
| action_is_effective | 1.0 |
| num_actions | 30.0 |
| episodic_return | 0.0 |
| response_length | 2797.5 |

Training step 1 正在执行 `compute_policy_loss`（两个 worker 都在跑），但尚未输出第一个 training step 的 metrics。按当前速度 ~5.6 min/epoch，30 epochs 预计还需约 2h40m 完成。

---
