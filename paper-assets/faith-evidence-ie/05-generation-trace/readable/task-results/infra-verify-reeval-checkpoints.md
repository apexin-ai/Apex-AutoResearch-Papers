# infra verify reeval checkpoints

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_reeval_checkpoints_20260516T030753_result.json`
- **Structured JSON:** [`ab5f475f76c2632b1d5c.json`](../../sessions/ab/ab5f475f76c2632b1d5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，结果已写入 `memory.md`。

**路径确认：**

| 实验 | Checkpoint 路径 | 状态 |
|------|----------------|------|
| reeval_ced_s44 | `/root/autodl-tmp/rsft_output_s44/checkpoint-510` | ✅ adapter_model.safetensors 存在 |
| reeval_ced_s42 | `/root/autodl-tmp/rsft_output/checkpoint-510` | ✅ adapter_model.safetensors 存在 |
| reeval_flat_nli_s42 | `/root/autodl-tmp/rsft_output_flat_nli/checkpoint-507` | ✅ adapter_model.safetensors 存在 |

**两个发现：**
1. `rsft_output_ced_s44` 不存在——s44 的 CED RSFT checkpoint 在 `rsft_output_s44`（无 `_ced` 前缀）
2. flat-NLI 全系列最终 checkpoint 是 **507**（不是 510），所以 reeval_flat_nli_s42 用 checkpoint-507

提交命令已准备好，`{GPU}` 待 GPU 空闲后替换。

---
