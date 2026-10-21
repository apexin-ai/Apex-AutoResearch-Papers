# ops check gpu1 cwm s42 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu1-cwm-s42-status_20260519T023215_result.json`
- **Structured JSON:** [`01b1cea2f7e811adc1cb.json`](../../sessions/01/01b1cea2f7e811adc1cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**CWM s42 best @4096 — 已完成**

- **目录**: `deepseek_cwm_repo_s42_test`
- **Checkpoint**: `checkpoints_deepseek_cwm_repo/best/`，`max_seq_length=4096`
- **GPU 1 状态**: 空闲（0% 利用率，0 MiB 显存），进程已退出

| 指标 | 值 |
|---|---|
| Total | 9784 |
| Overall accuracy | 5548/9784 = **56.70%** |
| Unparseable | 4992/9784 = **51.0%** |
| Parseable accuracy | 1855/4792 = **38.71%** |
| F1 macro | 51.16 |
| F1 pass / F1 fail | 67.61 / 34.71 |

注意：unparseable 率极高（51%），导致 overall accuracy 低于 majority baseline（72.96%）。另外 `deepseek_cwm_repo_s42_epoch2`（同 checkpoint-8844 但可能 seq=8192 default）在 3050/9784 处中断，进程已死，无错误日志。

---
