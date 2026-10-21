# code e1c kill eval and sft 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1c_kill_eval_and_sft_1p5b_20260518T112451_result.json`
- **Structured JSON:** [`53758af8e331aa20c602.json`](../../sessions/53/53758af8e331aa20c602.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成：

- **Killed**: PID 796502 (1.5B post-prune eval on cuda:0)
- **Launched**: `sft_cka_only_20_1p5b` — PID 797860, tmux session `sft_cka_only_20_1p5b`
  - 服务器: westb-23072 cuda:0, 显存 28524 MiB
  - 配置: 2 epochs, lr=2e-5, batch_size=4, grad_accum=2 (effective batch 8), GSM8K 7473 samples, 1870 total steps
  - 速度: ~3.5 it/s
  - **预计 ~9 分钟完成** (~19:37 UTC)
- **Registry**: `sft_cka_only_20_1p5b` → RUNNING

---
