# ops disk cleanup restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-restart_20260517T084947_result.json`
- **Structured JSON:** [`99d1d857811110bc65e9.json`](../../sessions/99/99d1d857811110bc65e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已正常运行，step 1 和 step 2 通过。

---

## 最终汇报

### 1. 备份结果
`/root/autodl-tmp/eval_archive/` 下 7 个目录：

| 目录 | 备份文件 |
|---|---|
| plan001_exec_only_s43_1000_r2 | eval_results.json, reward_log.jsonl |
| plan001_exec_only_s46 | eval_results.json, reward_log.jsonl |
| plan002_additive_b01_s45 | eval_results.json, h7_classification.json, reward_log.jsonl |
| plan002_additive_b01_s46 | eval_results.json, h7_classification.json, reward_log.jsonl |
| plan018_random_b01_s45 | eval_results.json, h7_classification.json, reward_log.jsonl |
| plan018_random_b01_s46 | eval_results.json, h7_classification.json, reward_log.jsonl |
| sweep_random_b005_s42 | eval_results.json, h7_classification.json, reward_log.jsonl |

### 2. 磁盘状态
`/dev/md0  250G  40G  211G  16%` — 释放 210G

### 3. sweep-isr-b005-s43 状态
已崩溃（磁盘满时死亡，仅完成到 step 50），已重启

### 4. 训练重启状态

| 实验 | GPU | PID | tmux session | 状态 |
|---|---|---|---|---|
| sweep-random-b005-s43 | cuda:1 (83423 MiB) | 246587 | sweep-random-b005-s43 | step 2 通过，~15s/step，预计 ~2h |
| sweep-isr-b005-s43 | cuda:0 (83423 MiB) | 246667 | sweep-isr-b005-s43 | step 2 通过，~14.5s/step，预计 ~2h |

---
