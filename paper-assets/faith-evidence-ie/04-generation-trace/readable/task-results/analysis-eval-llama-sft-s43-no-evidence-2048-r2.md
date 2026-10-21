# analysis eval llama sft s43 no evidence 2048 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_llama_sft_s43_no_evidence_2048_r2_20260521T024145_result.json`
- **Structured JSON:** [`71d066a5df529f74f66d.json`](../../sessions/71/71d066a5df529f74f66d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_llama_sft_s43_no_evidence_2048_r2 结果

### 核心 RE 指标
| Metric | Value |
|--------|-------|
| **ign_f1** | **0.3389** |
| ign_precision | 0.4167 |
| ign_recall | 0.2856 |
| f1 | 0.3575 |
| precision | 0.4493 |
| recall | 0.2968 |
| tp / pred / gold | 3607 / 8027 / 12151 |

### Evidence 指标（符合预期，no_evidence 模式）
| Metric | Value |
|--------|-------|
| evi_f1 | 0.0 |
| evi_f1_joint | 0.0 |
| edcr | 0.0 |

### 格式与截断
| Metric | Value |
|--------|-------|
| n_format_ok | 834/985 |
| format_ok_rate | 84.67% |
| n_parseable | 824 |
| n_truncated | 359/985 (36.4%) |
| n_predictions | 23070 |

### 推理时间
| Metric | Value |
|--------|-------|
| inference_time_seconds | 14987.0s (~4h10m) |
| per_doc | 15.22 s/doc |

### 配置确认
- `no_evidence: true` ✓
- model: `sft_output_llama_3_1_8b_s43`
- max_new_tokens: 2048
- split: dev

---

### 数据质量判断

**结果较差。** 与对比基线相比：

- **ign_f1=0.3389** 显著低于 s42 no-evi (0.5210) 和 s44 no-evi (0.4373)，是三个 seed 中最差的
- **format_ok_rate=84.67%** 低于 s44 (99.19%)，但略好于 s42 (88.73%)
- **truncated=359** 高于 s42 (201) 和 s44 (246)，截断率最高（36.4%），这部分解释了低 recall (0.2856)
- precision (0.4493) 也比 s42 (对应值更高) 低，说明不只是截断问题，模型输出质量也弱
- evi_f1=0.0 符合 no_evidence 模式预期

s43 checkpoint 质量在三个 seed 中排名最末，truncation 严重且 RE 精度/召回均低。没有 fair_tax_pp 子集分析文件。

---
