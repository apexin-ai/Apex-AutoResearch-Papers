# analyze 14b sft test and cascade

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_14b-sft-test-and-cascade_20260522T001628_result.json`
- **Structured JSON:** [`58c3737129cf2d540b29.json`](../../sessions/58/58c3737129cf2d540b29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B SFT Test 结果

| 指标 | 值 |
|------|-----|
| **Ign-F1** | **0.3886** |
| F1 | 0.3886 |
| Precision | 0.4220 |
| Recall | 0.3602 |
| Evi-F1 (DREEAM joint) | 0.2437 |
| Evi-F1 (TP-only) | 0.5912 |
| EDCR | 0.8367 |
| Format OK | 499/500 |
| Truncated | 253/500 |
| Predictions | 22,352 |

注：test set 无 train_annotated.json，Ign-F1 = F1。

## Cascade: 1.7B no-evi test eval

| 项目 | 值 |
|------|-----|
| 状态 | 已提交，RUNNING |
| PID | 147596 |
| GPU | cuda:1 |
| Cron | 每 12 分钟轮询 (job 7c70083f) |

---
