# monitor training progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260512T202310_result.json`
- **Structured JSON:** [`537edbf52e5c53fad86f.json`](../../sessions/53/537edbf52e5c53fad86f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果摘要：

| 实验 | 进度 | Loss | GPU | ETA |
|------|------|------|-----|-----|
| **cwm-v6** (seetacloud cuda:2) | 166/6633 (2.5%) | train 11.16, eval 0.433 | 97%, 22.4/32.6GB | ~42h |
| **cls-home** (home cuda:0) | 1577/6633 (23.8%) | 日志无输出 | 92%, 19.5/32.6GB | ~10h |

关键发现：cwm-v6 每 50 步跑一次全量 eval（9335 样本，~12.5 min），导致训练效率极低——eval 占总时间 65%。cls-home 无 inline eval，速度快很多但无 loss 可视性，建议确认 wandb 或其他 metrics 输出。

---
