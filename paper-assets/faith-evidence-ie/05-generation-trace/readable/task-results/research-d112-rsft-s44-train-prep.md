# research d112 rsft s44 train prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d112-rsft-s44-train-prep_20260521T061852_result.json`
- **Structured JSON:** [`917334148ea0bceb9231.json`](../../sessions/91/917334148ea0bceb9231.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出写入 `artifacts/d112_rsft_s44_train_prep.md`。

**关键发现**: `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16/` 已存在（2026-05-19 21:02 创建，CED scoring 之后），且 D112 eval 脚本已引用该路径。**训练很可能已经完成过一次。**

如需重训，命令已准备好，推荐 GPU 2（91.7GB 空闲）。4B bf16 + LoRA r=64 预估 ~20-25GB VRAM，~15-20 分钟完成。训练命令使用了新输出目录 `d112_rsft_output_4b_sft_s44` 以避免覆盖已有结果。

---
