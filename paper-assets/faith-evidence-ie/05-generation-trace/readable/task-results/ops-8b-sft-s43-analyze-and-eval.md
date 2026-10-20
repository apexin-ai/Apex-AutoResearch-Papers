# ops 8b sft s43 analyze and eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_8b_sft_s43_analyze_and_eval_20260519T135834_result.json`
- **Structured JSON:** [`8caec6088f8cf78f0217.json`](../../sessions/8c/8caec6088f8cf78f0217.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**训练 plan019_8b_sft_s43** — 成功 ✓
- Checkpoint: `/root/autodl-tmp/sft_output_qwen3_8b_s43`（adapter 698MB，含 checkpoint-190/570）
- train_loss=0.5684, eval_loss=0.719, token_accuracy=0.8378
- 训练耗时 ~1h51m（570 steps, 3 epochs）
- Registry 已更新为 DONE/success

**Eval plan019_8b_sft_s43_eval** — ALLOCATED，等待提交
- Eval 脚本: `/root/autodl-tmp/freige/scripts/seed_expansion/eval_8b_sft_s43.sh`（D076 协议，bf16, no-quantize, bs=4）
- 分配 GPU: cuda:1, server: rtx5090-4x
- 提交命令: `CUDA_VISIBLE_DEVICES=1 bash scripts/seed_expansion/eval_8b_sft_s43.sh`

---
