# ssh kill duplicate eval cuda1

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_duplicate_eval_cuda1_20260515T133118_result.json`
- **Structured JSON:** [`f6d007f978586c31ee57.json`](../../sessions/f6/f6d007f978586c31ee57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇报：**

| 项目 | 状态 |
|------|------|
| PID 108843 (eval) | 已 kill |
| PID 109289 (eval) | 已 kill |
| PID 107198 (exception_only 训练) | 正常运行中，step 69/444 |
| cuda:1 显存 | 22423 MiB（从 ~56730 MiB 降回，释放 ~34 GB） |

训练速度在 step 58 前约 12-15s/it，step 59 起恶化到 19→27→31→35→39→45→49s/it（eval 进程抢显存）。kill 后最后一条日志是 step 69 @ 38s/it，速度正在恢复中，后续 step 应回到正常水平。

---
