# analyze eval falcon3 d050 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_falcon3_d050_s42_20260522T122939_result.json`
- **Structured JSON:** [`1b3e92d85fe1c4db67ba.json`](../../sessions/1b/1b3e92d85fe1c4db67ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估正常完成（EXIT_CODE=0，.done sentinel 已写入）。

## 结果

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| **MMLU 5-shot** | **62.09%** | 8718/14042 |
| **ARC-Challenge 25-shot** | **83.28%** | 976/1172 |

## 对比

| Dosage | MMLU | ARC |
|--------|------|-----|
| d000 | 58.77% | 81.57% |
| d005 | 59.02% | 83.11% |
| d025 | 61.23% | 84.81% |
| **d050** | **62.09%** | **83.28%** |

MMLU 持续上升（+3.32pp vs d000），符合 benefit pattern。ARC 相对 d025 回落 1.53pp，可能 d050 剂量下 ARC 出现饱和/轻微过拟合。无错误或异常。

---
