# ssh kill math500 and fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_math500_and_fix_20260521T024823_result.json`
- **Structured JSON:** [`a6387df00756ab57df74.json`](../../sessions/a6/a6387df00756ab57df74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

第一题完成：**90.96s/it**，ETA **12.6h**。

对比之前：320s/it → 91s/it，**提速 3.5x**。ETA 从 31h 降到 ~12.6h。

汇总：

| 项目 | 结果 |
|------|------|
| **Kill** | PID 59502 + 子进程 59509 已杀，GPU 已释放 |
| **原因** | `max_new_tokens` 默认 4096，模型带 `&lt;think>` reasoning 打满上限，~320s/题 |
| **修复** | `--max_new_tokens 2048` 重跑 |
| **新进程** | PID 62714，cuda:0 (15GB)，99% 利用率 |
| **新速度** | 91s/it，ETA ~12.6h（原 31h，提速 3.5x） |
| **输出** | `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json` |
| **日志** | `/tmp/eval_math500_sft_standard_25.log` |

---
