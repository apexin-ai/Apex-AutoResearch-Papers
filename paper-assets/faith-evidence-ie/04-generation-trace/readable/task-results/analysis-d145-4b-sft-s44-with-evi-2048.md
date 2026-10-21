# analysis d145 4b sft s44 with evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d145_4b_sft_s44_with_evi_2048_20260521T182643_result.json`
- **Structured JSON:** [`d67720a70ea9b1373288.json`](../../sessions/d6/d67720a70ea9b1373288.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d145_4b_sft_s44_with_evi_2048 实验结果

**模型**: Qwen3-4B + SFT adapter (sft_output_seed44), with evidence, max_new_tokens=2048

### RE Metrics
| Metric | Value |
|--------|-------|
| **Ign-F1** | **0.4665** |
| F1 | 0.4778 |
| Precision | 0.4684 |
| Recall | 0.4874 |
| Ign-Precision | 0.4460 |
| Ign-Recall | 0.4889 |
| TP / Pred / Gold | 5923 / 12644 / 12151 |

### Evidence Metrics
| Metric | Value |
|--------|-------|
| **Evi-F1 (DREEAM/Joint)** | **0.3751** |
| Evi-F1 (TP-only) | 0.7769 |
| Evi Precision (TP) | 0.8139 |
| Evi Recall (TP) | 0.7431 |
| Evi Joint Precision | 0.3692 |
| Evi Joint Recall | 0.3811 |
| **EDCR** | **0.7076** |
| Distractor / Total Citations | 24685 / 34884 |

### Format & Inference
| Metric | Value |
|--------|-------|
| Format OK | 983/985 (99.8%) |
| Truncated | 198/985 (20.1%) |
| n_predictions | 22679 |
| Inference Time | 8239.7s (8.37 s/doc) |

无 fair comparison 文件。

---
