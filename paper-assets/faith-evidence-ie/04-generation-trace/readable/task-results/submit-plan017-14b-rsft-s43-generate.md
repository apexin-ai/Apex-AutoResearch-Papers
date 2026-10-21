# submit plan017 14b rsft s43 generate

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_plan017_14b_rsft_s43_generate_20260522T185529_result.json`
- **Structured JSON:** [`cd10a8c067eaada55f08.json`](../../sessions/cd/cd10a8c067eaada55f08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**s43 generation 已经在运行，无需重复提交。**

Registry 中 `plan017_14b_rsft_s43_generate` 状态为 RUNNING：
- **PID**: 194682
- **GPU**: cuda:1（32GB 占用）
- **命令**: `CUDA_VISIBLE_DEVICES=1 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b_s43 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_generations_14b_s43 --num_generations 8 --max_new_tokens 1024 --seed 43`
- **进度**: 114/3027 docs（~4%），已运行约 38 分钟
- **预估完成**: 以当前 ~20s/doc 速度，剩余 ~16 小时
- **质量**: format_ok=100%, truncation=7.8%, diversity=7.2/8（与 s42 的 7.28 一致）

---
