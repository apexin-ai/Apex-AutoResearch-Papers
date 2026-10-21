# ops gpu status and ced s45 diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-ced-s45-diagnosis_20260516T012459_result.json`
- **Structured JSON:** [`d6e236bcd1bb8ced8e6c.json`](../../sessions/d6/d6e236bcd1bb8ced8e6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

| GPU | PID | 显存占用 | 实验 ID | 状态 |
|-----|-----|---------|---------|------|
| 0 | 270467 | 11091 / 32607 MiB (34%) | eval_flat_nli_s44 | 运行中，164/247 batches (66%)，预计剩余 ~1h |
| 1 | 277315 | 28679 / 32607 MiB (88%) | rsft_ced_s43_train_r3 | 运行中，340/510 steps (67%)，预计剩余 ~17min |
| **2** | **-** | **0 / 32607 MiB (0%)** | **空闲** | **可用** |
| 3 | 272169 | 11095 / 32607 MiB (34%) | eval_flat_nli_seed45 | 运行中，129/247 batches (52%)，预计剩余 ~1.5h |

## rsft_ced_s45_train_r4 诊断

**训练成功完成。**
- 510/510 steps, 3 epochs, runtime 2924s (~49min)
- Final train_loss: **0.6097**
- Final mean_token_accuracy: **0.8517**
- 模型保存: `/root/autodl-tmp/rsft_output_ced_s45`（含 checkpoint-510 + adapter_model.safetensors 528MB）
- Registry 已更新: status=ANALYZING, conclusion=success

**GPU 2 空闲，显存 0 MiB，可立即提交 eval_plan_014_no_evidence。**

---
