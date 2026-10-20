# submit plan019 1 7b sft s43 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_plan019_1_7b_sft_s43_eval_20260518T201933_result.json`
- **Structured JSON:** [`93e3c94616e7fb59e56b.json`](../../sessions/93/93e3c94616e7fb59e56b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 1. plan019_1_7b_sft_s43_r2 训练结果
- **状态**: 完成 (EXIT_CODE=0)
- **train_loss**: 0.6881
- **eval_loss**: 0.8029
- **eval_mean_token_accuracy**: 0.8237
- **eval_entropy**: 0.6810
- **epoch**: 3.0
- **runtime**: 2697s (~45min)
- **checkpoint**: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43/` (checkpoint-380, checkpoint-570, adapter 278MB)

### 2. wave1_sft_4b_s43_eval_r2
- **仍在运行** (PID 568649/568654, cuda:2, 10404MiB)
- 输出目录为空，尚未产出 eval_result.json

### 3. plan019_1_7b_sft_s43_eval
- **未提交** — cuda:2 被 wave1_sft_4b_s43_eval_r2 占用 (10404MiB)，违反 C001 约束
- 需等 wave1_sft_4b_s43_eval_r2 完成后再提交

---
