# analysis reeval sft baseline d076

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_sft_baseline_d076_20260516T072641_result.json`
- **Structured JSON:** [`921b92edca1c8b225393.json`](../../sessions/92/921b92edca1c8b225393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册。结果汇总：

## reeval_sft_baseline_d076 结果

| 指标 | 值 |
|------|-----|
| **F1** | **0.4049** |
| **Ign-F1** | **0.3974** |
| **Evi-F1** | **0.7986** |
| **EDCR** | **0.6982** |
| Evi-F1-Joint | 0.3147 |
| Precision / Recall | 0.4141 / 0.3962 |
| Format OK | 983/985 (99.8%) |
| Truncated | 288/985 |
| Predictions | 16880 |

### 日志状态
- EXIT_CODE=0，无 error/traceback
- 推理完整完成 247/247 batches，耗时 1h57m (7.16 s/doc)

### 注意点
- **288/985 (29.2%) 文档被截断** — max_new_tokens=1024 对长文档不够，可能压低了 recall
- **field_compliance_rate 仅 70.66%** — 近 30% 的输出缺少完整字段（主要是 evidence 格式不完整），与截断高度相关
- **EDCR 0.6982** — 约 70% 的引用为 distractor sentence，evidence 质量有提升空间

### 结论：**Success** — 实验正常完成，数据可用作 D076 统一协议下的 SFT baseline 基准线。

---
