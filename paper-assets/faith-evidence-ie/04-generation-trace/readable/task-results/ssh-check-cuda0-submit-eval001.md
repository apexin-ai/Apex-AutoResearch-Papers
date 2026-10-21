# ssh check cuda0 submit eval001

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_cuda0_submit_eval001_20260515T210423_result.json`
- **Structured JSON:** [`abe845aaaa6144f861a5.json`](../../sessions/ab/abe845aaaa6144f861a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_plan_001_flat_nli_s43 已经在运行中，无需重新提交。**

当前状态：
- **PID 252179** (wrapper) 存活，**PID 252184** (python 进程) 在 cuda:0 上运行，已运行 ~34 分钟，占用 18328 MiB
- **tmux session**: `eval_plan_001_flat_nli_s43` (created 04:30:26)
- **Registry 状态**: RUNNING，提交时间 2026-05-15T20:30:26
- **命令**: `python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43 --no-quantize`

参数符合要求：全量 dev eval、`--no-quantize`、cuda:0。Registry spec 也已填写完整。无需任何操作。

---
