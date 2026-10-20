# harvest llama rsft s42 withevi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_llama-rsft-s42-withevi-2048_20260521T070416_result.json`
- **Structured JSON:** [`677db8d585333d83c414.json`](../../sessions/67/677db8d585333d83c414.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项任务完成：

**Part 1: RSFT s42 with-evi@2048 收割**
| 指标 | @1024 | @2048 | Delta |
|------|-------|-------|-------|
| ign_f1 | 0.5714 | **0.5774** | +0.60pp |
| f1 | - | 0.5892 | - |
| evi_f1(TP) | - | 0.8222 | - |
| edcr | - | 0.6143 | - |
| truncated | - | 90/985 | - |

Delta +0.60pp < 1pp → **RSFT @1024 evidence tax 可信，不受 truncation 显著影响。** Registry → DONE(success)。

**Part 2: d140_4b_sft_s42_no_evi_2048 已提交**
- PID: 85668, cuda:0
- `--no_evidence` 参数已传 (C005)
- `CUDA_VISIBLE_DEVICES=0` 已设 (C002/C003)
- Registry → RUNNING

---
