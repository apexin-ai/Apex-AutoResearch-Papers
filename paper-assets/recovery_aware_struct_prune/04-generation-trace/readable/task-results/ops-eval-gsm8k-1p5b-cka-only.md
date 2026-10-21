# ops eval gsm8k 1p5b cka only

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_gsm8k_1p5b_cka_only_20260518T163600_result.json`
- **Structured JSON:** [`abf030187f7ec5d1100d.json`](../../sessions/ab/abf030187f7ec5d1100d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已启动，状态汇总：

- **实验**: `eval_gsm8k_grpo_cka_only_20_1p5b`
- **PID**: 822503
- **tmux session**: `eval_gsm8k_cka_only`
- **GPU**: westb-23072 cuda:1（模型加载中，GPU 显存尚未占用）
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_cka_only_20_1p5b.log`
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_1p5b.json`
- **Registry**: RUNNING

注意到有一个旧的 `eval_unstructured_20` tmux session (PID 680597) 仍存在于 cuda:1，但其 python 进程可能已结束（GPU 显存仅 3 MiB）。如需清理可告知。

---
