# diagnose 41312 cuda0 uniform1 7b

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_41312-cuda0-uniform1_7b_20260518T173331_result.json`
- **Structured JSON:** [`c95a75e07538f75b1f10.json`](../../sessions/c9/c95a75e07538f75b1f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**cuda:0 不空闲，uniform_1_7b Plan B 正在正常运行。**

| 项目 | 状态 |
|---|---|
| GPU | cuda:0 占用 61684MiB，GPU-Util 99% |
| 进程 | PID 229968，`pretrain_weighted.py --model_name .../checkpoint-3000 --output_dir .../uniform_1_7b_seed42_resumed` |
| 进度 | **step 2647 / 3051（87%）**，已跑 2h07m，预计剩余 ~19 min |
| Checkpoints | `uniform_1_7b_seed42_resumed/` 下已有 checkpoint-1500、2000、2500 |
| Log | `uniform_1_7b_seed42_r3.log`，持续更新中 |
| Loss | ~1.6-2.0 范围，正常 |

训练健康，约 20 分钟后完成。

---
