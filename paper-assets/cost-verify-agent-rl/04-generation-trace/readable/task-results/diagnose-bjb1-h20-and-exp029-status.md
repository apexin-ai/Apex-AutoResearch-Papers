# diagnose bjb1 h20 and exp029 status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-h20-and-exp029-status_20260519T020834_result.json`
- **Structured JSON:** [`bf59db6a3980da949297.json`](../../sessions/bf/bf59db6a3980da949297.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-17606 h=20

| 项目 | 状态 |
|------|------|
| PID 77613 | **存活**, 运行 6h58m, 状态 Ss+ |
| GPU 0 | 45% util, 44067/97887 MiB |
| GPU 1 | 54% util, 44389/97887 MiB |
| 当前 step | **2/15** (13%), ~50 min/step |
| 日志时间戳 | 2026-05-19 09:31:15 (活跃) |
| train success | 13.28%, pass@8=43.75% |

进程正常运行，GPU 双卡活跃。当前在 rollout 阶段（日志输出 ALFWorld 交互 warning 是正常的）。

## westd-47453 exp029_seed2

| 项目 | 值 |
|------|------|
| 当前 step | **39** |
| train success | 35.9%, pass@8=87.5% |
| 最新 val (step 35) | **success=28.125%**, pass@1=28.125% |
| 前次 val (step 15) | success=25.0%, pass@1=25.0% |

val success 从 25.0% → 28.125%，有提升但幅度不大。train success 35.9% 且 manager_invalid_action 飙升到 47.7%（step 39），response_length 大幅缩短（mean=7516），模型可能在学习 shortcut（少做 action 但靠部分成功拿分）。

---
