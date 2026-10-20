# eval mvp2 eval sft baseline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp2_eval_sft_baseline_20260514T215035_result.json`
- **Structured JSON:** [`642c50e28d86ce5d3519.json`](../../sessions/64/642c50e28d86ce5d3519.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **脚本**: `/root/autodl-tmp/scripts/eval_sft_baseline.sh` — 基于 `eval_lr5e6_ckpt20.sh`，checkpoint 指向 SFT adapter (`/root/autodl-tmp/sft_output`)，output 到 `/root/autodl-tmp/sft_baseline_eval_results`，其余参数完全一致（docred dev, batch_size=16, max_new_tokens=1024, seed=42, quantize）
- **提交**: tmux session `mvp2_eval_sft_baseline`，GPU 3，已开始推理（985 docs / 62 batches）
- **Registry**: `mvp2_eval_sft_baseline` 状态 RUNNING

---
