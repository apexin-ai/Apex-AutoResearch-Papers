# ssh check bjb1 seed200 eval urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_bjb1_seed200_eval_urgent_20260523T030829_result.json`
- **Structured JSON:** [`f1c85fc3b11bb2adc068.json`](../../sessions/f1/f1c85fc3b11bb2adc068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：COMPLETED (EXIT_CODE=0)**

进程 477932 已退出，GPU 已释放（两张卡均 0 MiB）。wandb teardown 有个 BrokenPipe 警告，无影响。

### OOD Eval Metrics (seed200, step5, AlfworldSG_OOD, 134 episodes)

| 指标 | 值 |
|------|-----|
| **pass@1** | **10.45%** |
| action_is_valid | 61.06% |
| action_is_effective | 100% |
| num_actions (avg) | 45.5 |
| response_length (avg) | 6854.9 |

**Best@K reward (mean):**

| K | mean |
|---|------|
| 2 | 2.15 |
| 4 | 3.70 |
| 8 | 5.86 |
| 16 | 8.22 |
| 32 | 9.72 |
| 64 | 10.0 |
| 128 | 10.0 |
| 134 (all) | 10.0 |

---
