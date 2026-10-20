# analysis reeval ced s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_ced_s44_20260516T075802_result.json`
- **Structured JSON:** [`624c72fb555a713ae257.json`](../../sessions/62/624c72fb555a713ae257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## reeval_ced_s44 结果 Summary

**状态**: 成功完成 (EXIT_CODE=0)

### 核心指标

| 指标 | 值 |
|------|-----|
| **F1** | 0.4621 |
| **Ign-F1** | 0.4511 |
| **Precision** | 0.4762 |
| **Recall** | 0.4488 |
| **Evi-F1** | 0.8050 |
| **Evi-Precision** | 0.8097 |
| **Evi-Recall** | 0.8004 |
| **EDCR** | 0.6350 |
| **Evi-F1 (joint)** | 0.3677 |

### 辅助信息

- **W&B run ID**: 无（日志中未找到 wandb 相关记录）
- **Format compliance**: 985/985 (100%)
- **Truncated**: 190/985
- **Predictions**: 15,264
- **推理时间**: 3h38m (13,078s, 13.28s/doc)
- **Checkpoint**: `/root/autodl-tmp/rsft_output_s44/checkpoint-510`

### Artifact

已注册: `art_20260516_36e4c6` → `projects/faith-evidence-ie/artifacts/reeval_ced_s44/report/metrics_summary.json`

### 结论

**Success.** 实验正常完成，所有指标已提取。F1=0.4621 / Evi-F1=0.8050 / EDCR=0.6350，数据可用于 paired t-test。待 reeval_ced_s42 完成后即可进行跨 seed 统计检验。

---
