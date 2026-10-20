# verify 8b s44 rsft scripts intact

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_8b_s44_rsft_scripts_intact_20260518T203711_result.json`
- **Structured JSON:** [`17d27d46737ab9945cf7.json`](../../sessions/17/17d27d46737ab9945cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**脚本状态：正确，无需恢复。**

`train_8b_s44.sh`：
- `--sft_adapter` → `/root/autodl-tmp/sft_output_qwen3_8b_bf16`（s42 adapter ✓）
- `--rsft_data_path` → `/root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl`（s42 scored data ✓）
- `--seed 44` ✓
- `--output_dir` → `/root/autodl-tmp/rsft_output_qwen3_8b_k1_s44` ✓

`eval_8b_s44.sh`：
- `--sft_adapter` → `/root/autodl-tmp/sft_output_qwen3_8b_bf16`（s42 adapter ✓）
- D076 protocol（bs=4, no-quantize, seed=42）✓

不需要的文件 `rsft_generate_8b_s44.sh` / `rsft_score_8b_s44.sh` 不存在 ✓

---
