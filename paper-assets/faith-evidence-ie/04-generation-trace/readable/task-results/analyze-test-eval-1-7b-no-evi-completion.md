# analyze test eval 1 7b no evi completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_1_7b_no_evi_completion_20260522T035601_result.json`
- **Structured JSON:** [`97830f9f21c5f6d75f55.json`](../../sessions/97/97830f9f21c5f6d75f55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果汇总：

**test_eval_1_7b_sft_s42_no_evi — 成功**

| 指标 | 值 |
|------|-----|
| **Ign-F1** | **0.2093** |
| Precision | 0.3899 |
| Recall | 0.1430 |
| Format OK | 498/500 (99.6%) |
| Truncated | 467/500 |
| Predictions | 34,571 |
| Inference time | 3h 36m |

**Test set 1.7B evidence tax：**

| 模型 | Test Ign-F1 |
|------|------------|
| with evidence (test_eval_1_7b_sft_s42) | 0.2579 |
| no evidence (本次) | 0.2093 |
| **Δ (evidence tax)** | **-4.86pp** |

与 dev matched@2048 的 fair_tax -5.63pp 方向一致：evidence helps at 1.7B，test set 上差距略小（-4.86 vs -5.63）。

---
