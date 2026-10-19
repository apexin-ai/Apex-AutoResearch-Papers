# ops exp026 step5 val check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp026_step5_val_check_20260515T140425_result.json`
- **Structured JSON:** [`b1e23fc77706ac098571.json`](../../sessions/b1/b1e23fc77706ac098571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp026 状态报告

**进程**: PID 781795，ALIVE，已运行 3h26m

**已完成的 steps**:
- step 0: val eval (baseline) — success=6.25%, pass@1=6.25%
- step 1: train — success=21.875%, pass@16=6.25%
- step 2: train — success=6.25%, pass@16=0%
- step 3: train — success=0%, pass@16=0%
- step 4: train — success=0%, pass@16=0%

**Step 5**: 尚未完成。Step 4 在 total=11189s 时结束，进程已运行 ~12356s，说明 step 5 已运行约 19 分钟。按前几步每步 ~50-55 分钟估算，**step 5 train 预计还需 ~35 分钟完成**（约 22:40 左右），之后会触发 val eval（test_freq=5）。

**趋势问题**: 训练正在 collapse——success 从 step 1 的 21.875% 跌到 step 3-4 的 0%，pass@16 也归零。entropy 从 step 1 降到 0.387，response_length 从 ~60 涨到 ~930。模型看起来在退化。

---
