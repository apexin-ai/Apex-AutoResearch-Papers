# experiment cross transfer llama8b to qwen7b rerun

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_cross-transfer-llama8b-to-qwen7b-rerun_20260520T030034_result.json`
- **Structured JSON:** [`8899a801087949c765f0.json`](../../sessions/88/8899a801087949c765f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Part A** — `kstar_indexing: "1-indexed"` 已写入 `wiki_qwen7b__to__wiki_llama8b.json`，验证通过。

**Part B** — 训练任务已提交：
- **exp_id**: `exp_cross_transfer_llama8b_to_qwen7b_v2`
- **PID**: 275361
- **tmux session**: `exp_cross_transfer_llama8b_to_qwen7b_v2`
- **日志**: `~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b_v2.log`
- **GPU**: cuda:0，`--gpu 0`
- **命令**: `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python scripts/run_deberta_cross_transfer.py --train_model wiki_llama8b --test_model wiki_qwen7b --gpu 0`

---
