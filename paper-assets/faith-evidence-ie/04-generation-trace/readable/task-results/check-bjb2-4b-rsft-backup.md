# check bjb2 4b rsft backup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2_4b_rsft_backup_20260521T185014_result.json`
- **Structured JSON:** [`e3871d963a9237893fbd.json`](../../sessions/e3/e3871d963a9237893fbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**bjb2-12179 可连接。**

**4B RSFT s42 adapter（`rsft_output`、`rsft_output_r2b`）：未找到。** 该服务器上没有这两个目录，也没有任何包含 `s42` 的目录。

**bjb2-12179 上现有的 4B 相关目录：**
- `/root/autodl-tmp/rsft_output_4b_sft_s44` — 完整的 LoRA adapter（有 `adapter_config.json` + `adapter_model.safetensors`，以及 checkpoint-400/450/500/550/567）
- `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16`
- `/root/autodl-tmp/rsft_generations_4b_sft_s44`
- `/root/autodl-tmp/rsft_scored_4b_sft_s44`

这些都是 **s44** 的，不是 s42。s42 的 4B RSFT checkpoint 在 bjb2-12179 上没有备份。

---
