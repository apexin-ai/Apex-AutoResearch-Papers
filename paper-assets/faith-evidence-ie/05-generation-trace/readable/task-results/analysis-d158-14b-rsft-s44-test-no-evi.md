# analysis d158 14b rsft s44 test no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d158_14b_rsft_s44_test_no_evi_20260525T124554_result.json`
- **Structured JSON:** [`e3267b51680b8beec4b7.json`](../../sessions/e3/e3267b51680b8beec4b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常退出，EXIT_CODE=0，无 error/traceback。

## d158_14b_rsft_s44_test_no_evi 结果

| Metric | Value |
|--------|-------|
| **ign_f1** | **0.3666** |
| precision | 0.4161 |
| recall | 0.3276 |
| evi_f1 / evi_f1_joint / edcr | 0.0 (no-evidence, 符合预期) |
| format_ok_rate | 99.6% (498/500) |
| n_truncated | 271/500 |
| n_documents | 500 |
| n_predictions | 29840 |

## Evidence Tax (seed=44)

| | ign_f1 |
|--|--------|
| with_evi | 0.3716 |
| no_evi | 0.3666 |
| **tax (with - no)** | **+0.50pp** |

## 三个 seed test tax 汇总

| Seed | with_evi | no_evi | Tax |
|------|----------|--------|-----|
| s42 | — | — | +0.77pp |
| s43 | — | — | +0.08pp |
| s44 | 0.3716 | 0.3666 | +0.50pp |
| **Mean** | | | **+0.45pp** |

三个 seed 的 evidence tax 均为正值（evidence helps），范围 +0.08 ~ +0.77pp，均值 +0.45pp。

---
