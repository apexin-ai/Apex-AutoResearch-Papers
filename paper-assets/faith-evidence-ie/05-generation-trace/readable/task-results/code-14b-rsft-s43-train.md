# code 14b rsft s43 train

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b-rsft-s43-train_20260523T134440_result.json`
- **Structured JSON:** [`d246b8605f039a3366a9.json`](../../sessions/d2/d246b8605f039a3366a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交并注册完成。

**摘要：**
- **exp_id**: `plan017_14b_rsft_s43_train`
- **GPU**: cuda:1 @ rtx5090-4x (96GB, 空闲)
- **PID**: 257025
- **模式**: 单 GPU bf16（96GB 足够 14B + LoRA，无需 ZeRO-3）
- **SFT adapter**: `/root/autodl-tmp/sft_output_14b_s43`（运行时合并，无需预合并）
- **数据**: 3,017 条 CED-scored RSFT 数据
- **关键参数差异 vs s42**: seed 43, gradient_accumulation_steps=16（补偿单卡，保持有效 batch=16）
- **Cron 监控**: 已注册，120s 轮询

---
