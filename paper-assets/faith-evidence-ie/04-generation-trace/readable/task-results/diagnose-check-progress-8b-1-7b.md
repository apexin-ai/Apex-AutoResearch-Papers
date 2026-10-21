# diagnose check progress 8b 1 7b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check-progress-8b-1_7b_20260523T034816_result.json`
- **Structured JSON:** [`d5cdd7a3a149a7e95f10.json`](../../sessions/d5/d5cdd7a3a149a7e95f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 stale PIDs are dead (no output = no matching processes).

---

## 状态报告

### 活跃任务

| # | 任务 | GPU | PID | 进度 | ETA |
|---|------|-----|-----|------|-----|
| 1 | **8B RSFT s43 no-evi test eval** | GPU 0 (26.8/97.9 GB) | 220069 | **24/32 batches = 75%** | ~18 min (8 batches × ~135s) |
| 2 | **1.7B RSFT s43 with-evi test eval** | GPU 3 (6.1/97.9 GB) | 214028 | **217/500 docs = 43%** | ~3.5h (283 docs × ~45s) |
| 3 | **14B s43 RSFT generation** | GPU 1 (32.5/97.9 GB) | 194682 | **13,192 lines** generated (ongoing) | — |
| 4 | **DPO rebuilt 1ep eval** (bonus) | GPU 2 (11.8/97.9 GB) | 221956 | **22/247 batches = 9%** | ~3h |

8B no-evi test eval 应在 ~20 分钟内完成。1.7B with-evi 还需约 3.5 小时。

### 6 个 Stale 实验（PID 全部 DEAD，结果均已完成）

| # | 实验 | 结果文件 | RE F1 | Ign F1 | Evi F1 Joint | 备注 |
|---|------|---------|-------|--------|-------------|------|
| 1 | **test_eval_14b_rsft_s42** | test_summary.json + predictions.json + codalab | 38.49 | 38.49 | 26.88 | with-evi, test set, 500 docs |
| 2 | **eval_llama_rsft_s42_no_evi_2048** | metrics.json + predictions.json | 57.03 | 55.59 | 0.06 | no-evi (field_compliance=0%), dev set |
| 3 | **d140_4b_sft_s42_with_evi_2048** | metrics.json + predictions.json | 40.33 | 39.46 | 31.29 | with-evi, dev set |
| 4 | **d140_8b_sft_s42_no_evi_2048_fix** | metrics.json + predictions.json | 52.27 | 50.19 | 1.30 | no-evi, dev set |
| 5 | **d140_1_7b_sft_s42_no_evi_2048_fix** | metrics.json + predictions.json | 44.36 | 42.33 | 0 | no-evi, dev set |
| 6 | **d140_4b_sft_s42_no_evi_2048_fix** | metrics.json + predictions.json | 40.95 | 40.16 | 0 | no-evi, dev set |

6 个 stale 实验全部已完成且有完整结果，可以安全地将 registry 标记为 COMPLETED。

---
