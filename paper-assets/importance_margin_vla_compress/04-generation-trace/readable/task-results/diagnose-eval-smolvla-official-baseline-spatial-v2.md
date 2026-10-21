# diagnose eval smolvla official baseline spatial v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_smolvla_official_baseline_spatial_v2_20260519T135546_result.json`
- **Structured JSON:** [`018bba84f2a7a40e1a12.json`](../../sessions/01/018bba84f2a7a40e1a12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：实验正常完成。**

**eval_smolvla_official_baseline_spatial_v2** — 10 tasks × 50 episodes 全部跑完，进程正常退出。

| 指标 | 值 |
|------|-----|
| Overall SR | **43.8%** (219/500) |
| 95% Wilson CI | [39.5%, 48.2%] |

Per-task SR:

| Task | SR | 描述 |
|------|-----|------|
| 0 | 54% | between plate and ramekin |
| 1 | 48% | next to ramekin |
| 2 | **8%** | from table center |
| 3 | **76%** | on cookie box |
| 4 | 38% | in top drawer |
| 5 | 20% | on ramekin |
| 6 | 34% | next to cookie box |
| 7 | **78%** | on stove |
| 8 | 48% | next to plate |
| 9 | 34% | on wooden cabinet |

Registry 已更新为 DONE/success，metrics 已写入。cqa1 cuda:1 现已释放。

---
