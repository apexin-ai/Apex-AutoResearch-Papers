# ssh harvest eval gsm8k grpo random 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_eval_gsm8k_grpo_random_20_20260521T044849_result.json`
- **Structured JSON:** [`7ddaf6925104d77e5dea.json`](../../sessions/7d/7ddaf6925104d77e5dea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_gsm8k_grpo_random_20 失败**，没有产出任何 eval 结果。

- **原因**：`nohup: failed to run command 'python': No such file or directory` — 启动命令用了 `python` 而非 `python3`（或未激活 conda 环境），导致进程直接退出。
- **输出**：无 eval 输出目录，无结果 JSON。
- **GRPO 训练本身已完成**：`grpo_random_20/checkpoint-100/` 存在，模型文件齐全。

需要修正 eval 启动脚本中的 python 路径（改用 `python3` 或先 `source conda activate`）后重新提交 eval 任务。是否现在重跑？

---
