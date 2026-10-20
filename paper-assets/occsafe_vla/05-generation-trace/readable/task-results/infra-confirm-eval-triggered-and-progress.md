# infra confirm eval triggered and progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_confirm_eval_triggered_and_progress_20260520T224900_result.json`
- **Structured JSON:** [`055256519dd4381cd28b.json`](../../sessions/05/055256519dd4381cd28b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Eval 触发状态：已自动触发，无需手动启动

| seed | .launched 时间 | 进度（截至 06:50） |
|------|---------------|-------------------|
| s0 | 06:43 | Task 3 完成，继续中 |
| s1 | 06:48 | Task 0 完成，继续中 |

两个 eval 都在运行，无 `.done_*` 文件。每 task ~80-90s，10 tasks × 20 rollouts，预计 s0 约 06:55 完成，s1 约 07:02 完成。

### 2. 使用的 checkpoint

- s0: `vanilla_s0/...--50000_chkpt` ✓
- s1: `vanilla_s1/...--50000_chkpt` ✓

### 3. s2 训练进度

- 从 `35000_chkpt` 恢复（04:40:46 启动）
- tqdm: **8269/50005**，elapsed 2h08m，速度 **~1.08 it/s**
- 实际 step: 35000 + 8269 = **43269**
- tqdm total=50005 但训练在 actual step 50005 停止 → 即 tqdm 到 **15005** 时结束
- 剩余: 15005 - 8269 = **6736 步 ≈ 1h 44min**
- 最新 checkpoint: **40000_chkpt**，下个 checkpoint 在 45000（tqdm ~10000）
- **ETA ≈ ~08:33 UTC**

### 4. s0/s1 训练完成确认

- s0: 最终 checkpoint **50000_chkpt** ✓（checkpoints: 35000→40000→45000→50000）
- s1: 最终 checkpoint **50000_chkpt** ✓（checkpoints: 35000→40000→45000→50000）

---
