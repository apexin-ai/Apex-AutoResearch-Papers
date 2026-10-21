# analysis eval flat nli s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_flat_nli_s44_20260516T022550_result.json`
- **Structured JSON:** [`08e4f38f8e47d9f26de9.json`](../../sessions/08/08e4f38f8e47d9f26de9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_flat_nli_s44 结果

### 核心指标

| 指标 | 数值 | vs s42 (0.4539) |
|------|------|-----------------|
| **rel_f1** | **0.4615** | **+0.0076** |
| rel_p | 0.4779 | — |
| rel_r | 0.4462 | — |
| ign_f1 | 0.4615 | +0.0076 |
| **evi_f1** | **0.8131** | — |
| evi_p | 0.8187 | — |
| evi_r | 0.8077 | — |
| evi_f1_joint | 0.3597 | — |
| EDCR | 0.6458 | — |

### 其他统计

- Format OK: 985/985 (100%)
- Truncated: 206/985
- Predictions: 15,257 (gold: 12,151)
- TP: 5,422
- Inference time: 2h56m (10.74 s/doc)

### 结论

- **Success.** rel_f1 = 0.4615，高于 s42 (+0.76pp)，高于 CED mean (0.4596, +0.19pp)，远高于 SFT baseline。
- flat-NLI RSFT 方法在多个 seed 上表现稳定且优异（s42=0.4539, s44=0.4615）。
- 无异常——进程正常退出，无错误，format compliance 100%。

---
