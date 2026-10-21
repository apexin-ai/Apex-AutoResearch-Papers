# diag eval norm005 seed75 and seed51r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-norm005-seed75-and-seed51r3_20260521T031121_result.json`
- **Structured JSON:** [`6b24065a0e900b78ff6d.json`](../../sessions/6b/6b24065a0e900b78ff6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 实验 1: eval-obs-only-object-norm005-seed75 (bjb2-28827)

**结论：正常完成，结果可信。**

- 脚本跑完全部 10 个 task × 10 rollouts = 100 episodes，无 error/traceback
- 日志最后输出 `Overall success rate (crm_obs_only): 15.0% (15/100)`，与 registry SR=0.15 一致
- JSON 结果文件存在，内容完整，`overall_success_rate: 0.15`，10 个 task 的 per-task 数据齐全
- 进程 return_code=0，正常退出

### 实验 2: eval-obs-only-object-norm01-seed51-r3 (bjb1-32546)

**结论：正常完成，结果可信。**

- 脚本跑完全部 10 个 task × 10 rollouts = 100 episodes，无 error/traceback
- 日志最后输出 `Overall success rate (crm_obs_only): 11.0% (11/100)`，与 registry SR=0.11 一致
- JSON 结果文件存在，内容完整，`overall_success_rate: 0.11`，10 个 task 的 per-task 数据齐全
- 进程 return_code=0，正常退出

### 误报原因

两个实验都是**正常完成后进程退出**，cron 监控系统检测到进程不存在且没有 W&B metrics / sentinel 文件，误判为异常退出。根本原因是 eval 脚本没有写 sentinel 标记文件也没有上报 W&B，只输出了 JSON 结果文件，导致 cron 的完成检测机制未被触发。

---
