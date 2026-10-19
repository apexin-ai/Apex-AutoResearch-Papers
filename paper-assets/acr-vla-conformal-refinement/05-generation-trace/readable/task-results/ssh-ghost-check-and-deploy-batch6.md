# ssh ghost check and deploy batch6

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ghost-check-and-deploy-batch6_20260517T111811_result.json`
- **Structured JSON:** [`26aafab77ee259aef4b1.json`](../../sessions/26/26aafab77ee259aef4b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况严峻：**所有 4 台服务器的所有 GPU 都被占用，没有空闲 GPU 可以部署。**

### Ghost 实验诊断

| 实验 | 服务器 | GPU | 状态 | 详情 |
|------|--------|-----|------|------|
| eval-perdof-object-norm02-seed45 | bjb2-28827 | cuda:1 | **ALIVE** | PID 222830 在跑，1923MiB，17% util |
| eval-obs-only-object-norm01-seed45 | bjb1-18228 | cuda:0 | **ALIVE** | PID 474319 在跑，1923MiB，20% util |

两个都不是 ghost，是正常运行的实验。Registry 的 RUNNING 状态正确，无需更新。

### GPU 实际占用情况

**bjb1-18228** (4 GPU) — 全满：
- cuda:0: PID 474319 (ghost 2，在跑)
- cuda:1: PID 612853 (5645MiB)
- cuda:2: PID 587763 (4250MiB)
- cuda:3: PID 588037 (4717MiB)

**bjb1-32546** (6 GPU) — 全满：
- cuda:0~5 全部被占用 (PIDs: 421086, 414824, 416568, 422357, 393646, 423767)

**bjb2-28827** (6 GPU) — 全满：
- cuda:0: PID 224628 (1923MiB)
- cuda:1: PID 222830 (ghost 1，在跑)
- cuda:2: PID 392856+394435 (11324MiB, 99% util)
- cuda:3: PID 242264 (2392MiB)
- cuda:4: PID 389051 (5645MiB)
- cuda:5: PID 326081 (2856MiB)

**bjb2-40593** (1 GPU) — 全满：
- cuda:0: PID 388460 (5609MiB)

### 部署结果

| # | Exp ID | 计划 GPU | 结果 | 原因 |
|---|--------|----------|------|------|
| 1 | eval-obs-only-object-norm003-seed43 | bjb1-18228 cuda:0 | **跳过** | ghost 2 仍在运行 |
| 2 | eval-perdof-object-norm003-seed43 | bjb1-18228 cuda:1 | **跳过** | PID 612853 占用 |
| 3 | eval-obs-only-object-norm005-seed43 | bjb1-32546 cuda:0 | **跳过** | PID 421086 占用 |
| 4 | eval-perdof-object-norm005-seed43 | bjb1-32546 cuda:3 | **跳过** | PID 422357 占用 |
| 5 | eval-obs-only-object-default-seed43 | bjb1-32546 cuda:5 | **跳过** | PID 423767 占用 |
| 6 | eval-perdof-object-norm03-seed46 | bjb2-28827 cuda:1 | **跳过** | ghost 1 仍在运行 |
| 7 | eval-perdof-object-default-seed45 | bjb2-28827 cuda:2 | **跳过** | 2 进程占用，99% util |
| 8 | eval-obs-only-object-norm003-seed44 | bjb2-40593 cuda:0 | **跳过** | PID 388460 占用 |

**0/8 实验成功部署。** 所有目标 GPU 均被占用。需要等现有实验完成释放 GPU 后再部署。

---
