# ops start math500 sft cka only v4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_start_math500_sft_cka_only_v4_20260518T170634_result.json`
- **Structured JSON:** [`dffbd407c0b68eff88c9.json`](../../sessions/df/dffbd407c0b68eff88c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，汇总：

- **任务**: `eval_math500_sft_cka_only_20_v4`
- **服务器**: westd-29022, cuda:2 (12.5 GB 已占用，模型加载中)
- **tmux session**: `eval_math500_v4`
- **命令**: `CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py --model_path .../sft_cka_only_20 --output_path .../math500_sft_cka_only_20_v4.json --max_new_tokens 2048`
- **无 timeout 包装**
- **不支持 resume**，从头跑全部 500 题
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_v4.log`
- **Registry 状态**: RUNNING

---
