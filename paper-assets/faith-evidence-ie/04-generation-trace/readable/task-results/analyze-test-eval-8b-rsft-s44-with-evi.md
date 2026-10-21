# analyze test eval 8b rsft s44 with evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_8b_rsft_s44_with_evi_20260523T064606_result.json`
- **Structured JSON:** [`8a019e5f117bd0703d96.json`](../../sessions/8a/8a019e5f117bd0703d96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## test_eval_8b_rsft_s44_with_evi 结果

| 指标 | 值 |
|------|-----|
| **ign_f1** | **0.3329** |
| f1 | 0.3329 |
| precision | 0.5133 |
| recall | 0.2463 |
| Evi-F1(TP) | 0.5897 |
| Evi-F1(DREEAM) | 0.2458 |
| EDCR | 0.8090 |

注：`train_annotated.json not found`，所以 ign_f1 = f1。

### 3-seed summary (8B RSFT k1 with-evidence)

| seed | ign_f1 |
|------|--------|
| s42 | 0.3353 |
| s43 | 0.3398 |
| s44 | 0.3329 |
| **mean ± std** | **0.3360 ± 0.0035** |

三个 seed 的 ign_f1 范围 0.3329–0.3398，标准差 0.0035，变异系数约 1.0%，variance 很小，可以支撑 variance compression claim。

---
