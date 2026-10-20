# code grpo v6 dual submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-v6-dual-submit_20260515T124250_result.json`
- **Structured JSON:** [`b84be4bb96604748b67e.json`](../../sessions/b8/b84be4bb96604748b67e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 未空闲**，当前有 4 个 python 进程在运行：

| PID | GPU | 运行时间 | 命令 |
|-----|-----|---------|------|
| 498479 | cuda:0 | 3h10m | train_grpo_v5.py RASP v5 (max_completion_length=512) |
| 518416 | cuda:0 | 6m | train_grpo_v5.py Standard v5 (max_completion_length=512) |
| 517379 | cuda:1 | 11m | eval_gsm8k.py sft_standard_20 |
| 518908 | cuda:1 | 5m | train_grpo_v5.py Standard v5 (旧 output_dir) |

需要先 kill 这 4 个进程才能提交 v6。是否 kill 全部？

---

CLI 参数已确认完毕，flag 名称如下：`--beta`, `--temperature`, `--repetition_penalty`, `--format_reward_weight`, `--gradient_checkpointing`, `--num_train_epochs`, `--max_samples`, `--learning_rate`, `--loss_type`, `--max_completion_length`。v6 命令已就绪，等你确认 kill 后立即提交。

---
