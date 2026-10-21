# collect bjb2 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_bjb2-results_20260527T223002_result.json`
- **Structured JSON:** [`ef6fe6fdc4d768013fe8.json`](../../sessions/ef/ef6fe6fdc4d768013fe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验收割完毕，registry 已更新。

## 最终结果

| 实验 | Benchmark | SR | Trigger Rate | 备注 |
|------|-----------|-----|-------------|------|
| **crm-always-on-long-s42** | Long | **41.0%** | 100% | τ=0.001, always-on |
| **crm-always-on-long-s43** | Long | **45.5%** | 100% | τ=0.001, always-on |
| **smolvla-tau030-object-s42** | Object | **79.0%** | 2.31% | τ=0.30 |
| **smolvla-tau040-object-s42** | Object | **73.5%** | 0.91% | τ=0.40 |
| **smolvla-tau045-object-s42** | Object | **71.5%** | 0.75% | τ=0.45 |

CRM always-on Long 两个 seed 均值 = **43.25%**。Object tau-sweep 清晰显示 τ 越高 → trigger 越少 → SR 越低的单调趋势。全部无 OOM/CUDA error。

---
