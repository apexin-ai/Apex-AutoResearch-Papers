# ops urgent 3h status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_3h_status_check_20260517T115401_result.json`
- **Structured JSON:** [`3bf52d0af887f8fb224a.json`](../../sessions/3b/3bf52d0af887f8fb224a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 实验 | 状态 | 结果 |
|-----|------|------|------|
| cuda:0 | rsft_s43_dev_eval_preds | **完成** | predictions.json + metrics.json 存在 |
| cuda:1 | plan_006_qwen3_1_7b_rsft_eval_r2 | **完成** | predictions.json + metrics.json 存在 |
| cuda:2 | plan_006_llama_rsft_r3_eval | **完成** | predictions.json + metrics.json 存在 |
| cuda:3 | plan_006_qwen3_8b_rsft_train_r2 | **完成** | epoch 3.0, train_loss=0.3008, EXIT_CODE=0 |

磁盘: 58GB 可用 (77% used)

## Metrics 详情

| 指标 | s43 (Qwen3-4B) | 1.7B (Qwen3-1.7B) | LLaMA-3.1-8B |
|------|-----------------|---------------------|---------------|
| **Ign-F1** | 0.4512 | 0.5050 | **0.5563** |
| **F1** | 0.4601 | 0.5219 | **0.5674** |
| **Evi-F1** | 0.8063 | **0.8309** | 0.8255 |
| **Evi-F1-Joint** | 0.3605 | 0.4223 | **0.4571** |
| **EDCR** | 0.6542 | 0.6297 | 0.5856 |
| Format Rate | 100% | 99.9% | 99.7% |
| Field Compliance | 80.9% | 73.2% | 80.7% |
| Truncated | 184 | 258 | 187 |
| Inference Time | 10982s | 9464s | 8650s |

**LLaMA-3.1-8B 在 Ign-F1 和 Joint-Evi-F1 上领先，Qwen3-1.7B 的 Evi-F1 最高。** s43 (Qwen3-4B CED variant) Ign-F1=0.4512 明显低于其他两个模型。

## 8B 训练完成

- train_loss: 0.3008, mean_token_accuracy: 0.9172
- train_runtime: 8983s (~2.5h), epoch 3.0/3.0
- 模型 checkpoint 可用于后续 eval

## Lead 1 CED Filter 已提交

- PID: 441954
- GPU: cuda:0
- Log: `~/runs/faith-evidence-ie/lead1_ced_evidence_filter.log`
- 输入: s43 dev eval predictions, tau=[0.3, 0.5, 0.7]
- 输出目录: `/root/autodl-tmp/lead1_ced_filter_results`

---
