# registry backfill 3dir metrics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_backfill-3dir-metrics_20260523T034954_result.json`
- **Structured JSON:** [`d81ffca76fdb8b609f99.json`](../../sessions/d8/d81ffca76fdb8b609f99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 实验 | SR | 状态 | 备注 |
|------|-----|------|------|
| **eval-3dir-norm005-spatial-s42** | **80%** (160/200) | DONE/success | CRM norm=0.05 |
| **eval-3dir-norm01-spatial-s42** | **79%** (158/200) | DONE/negative | CRM norm=0.1 |
| **eval-3dir-reconvla-spatial-s42** | **79%** (158/200) | DONE/success | ReconVLA K=10 argmin |
| **eval-3dir-adaptive-spatial-s42** | **81%** (162/200) | DONE/success | Adaptive CRM tau=0.075, trigger_rate=91.8% |
| **eval-3dir-norm03-spatial-s42** | **73.9%** (133/180) | DONE/killed | 9/10 tasks complete, T10 partial |

Adaptive 实验 SR=81% 确认，与 Director 引用的数字一致。5 个实验的顶层 metrics（含 per-task breakdown）均已补录到 registry。

---
