# eval llama31 clean eval batch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama31-clean-eval-batch_20260516T143620_result.json`
- **Structured JSON:** [`a70cfdc0503d6d890369.json`](../../sessions/a7/a70cfdc0503d6d890369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 已在 autodl-5090 上并行运行：
- **Eval 1** (llama31-taxei-s42-clean): cuda:0, 16.8GB 占用，正常运行
- **Eval 2** (llama31-random-s0-clean): cuda:1, 14.8GB 占用，模型加载中

Eval 2 首次启动时因 tmux 中 `CUDA_VISIBLE_DEVICES` 没生效导致与 eval 1 抢 cuda:0 OOM，已用 `export CUDA_VISIBLE_DEVICES=1` 修复重启。4.5 分钟后轮询进度。

---
