# ops redocred rsft eval r3 cuda1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_redocred_rsft_eval_r3_cuda1_20260516T173632_result.json`
- **Structured JSON:** [`2dd8aae6c36f0c8d7cf8.json`](../../sessions/2d/2dd8aae6c36f0c8d7cf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**总结：**

1. **plan_014** 已完成并更新 registry：Ign-F1 = **0.4721**（no-evidence 4B SFT）
2. **plan_007_redocred_rsft_eval_r3** 已提交到 cuda:1，PID=368363，正常推理中
   - 配置已修正：model_path=`/root/autodl-tmp/models/Qwen3-4B`（base），sft_adapter=`/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510`（RSFT ckpt）
   - 500 docs / 124 batches，预计约 1 小时完成（28s/it × 124 ≈ 58 min）
   - Log: `/root/runs/faith-evidence-ie/plan_007_redocred_rsft_eval_r3.log`

---
