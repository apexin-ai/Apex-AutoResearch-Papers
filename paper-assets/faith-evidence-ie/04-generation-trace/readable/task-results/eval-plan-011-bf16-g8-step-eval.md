# eval plan 011 bf16 g8 step eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_011_bf16_g8_step_eval_20260515T194521_result.json`
- **Structured JSON:** [`8a630204e9abbc4a3e0d.json`](../../sessions/8a/8a630204e9abbc4a3e0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功提交并运行。Step 30 的模型正在加载，模块解析正常。

总结：
- **Checkpoint 目录**: `/root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-{30,50,70}`（LoRA adapter）
- **GPU**: cuda:0（cuda:1 被 plan_009 占用，已切换）
- **修复**: work_dir 改为 `/root/autodl-tmp`（freige 包的父目录），并补上 `--sft_adapter` 参数
- **输出**: `/root/autodl-tmp/eval_results/plan_011_bf16_g8_step{30,50,70}/`
- **预计耗时**: 每个 step ~2h（62 batch × ~130s/batch），3 个 step 共约 6h

---
