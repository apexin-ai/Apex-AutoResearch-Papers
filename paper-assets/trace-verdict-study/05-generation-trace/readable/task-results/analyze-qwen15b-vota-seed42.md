# analyze qwen15b vota seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen15b_vota_seed42_20260516T110847_result.json`
- **Structured JSON:** [`468d641e2b4c460c1218.json`](../../sessions/46/468d641e2b4c460c1218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## qwen15b_vota_seed42 评估结果

**训练状态：正常完成** (EXIT_CODE=0, 3 epochs, loss=0.0607, 耗时 2922s)

### 评估指标 (n=1190)

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | 99.58% | [99.2%, 99.9%] |
| Majority baseline | 71.5% (always "pass") | — |
| **Lift** | +28.1pp | [+25.7pp, +30.6pp] |

### Per-class

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| **pass** | 0.9965 | 0.9976 | 0.9971 |
| **fail** | 0.9941 | 0.9912 | 0.9926 |

VOTA condition 下 Qwen2.5-Coder-1.5B 表现极强，accuracy 接近饱和，fail class F1 也达到 0.993。

---
