# analyze plan019 1 7b rsft s43 r2 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan019_1_7b_rsft_s43_r2_eval_20260519T084109_result.json`
- **Structured JSON:** [`c197f9a6116efec49baf.json`](../../sessions/c1/c197f9a6116efec49baf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果摘要：

## plan019_1_7b_rsft_s43_r2_eval 结果

### 核心指标

| 指标 | s43 (本次) | s42 (canonical) | SFT mean | Δ vs s42 | Δ vs SFT |
|------|-----------|-----------------|----------|----------|----------|
| **ign_f1** | **0.5109** | 0.5122 | 0.4464 | **-0.13pp** | **+6.45pp** |
| ign_precision | 0.5186 | — | — | — | — |
| ign_recall | 0.5035 | — | — | — | — |

### Evidence 指标

| 指标 | 值 |
|------|-----|
| evi_precision | 0.8218 |
| evi_recall | 0.8340 |
| evi_f1 | 0.8278 |
| EDCR | 0.6245 |
| evi_f1_joint | 0.4278 |

### 格式 & 推理

| 指标 | 值 |
|------|-----|
| format_compliance | 99.9% |
| field_compliance | 75.0% |
| n_truncated | 244/985 |
| inference_time | 8498s (~2.4h) |

### 结论

**Success.** ign_f1 = 0.5109 与 s42 canonical (0.5122) 仅差 0.13pp，显著高于 SFT baseline (+6.45pp)。1.7B RSFT 跨 seed 稳健性得到验证。

---
