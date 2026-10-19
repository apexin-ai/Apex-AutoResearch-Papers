# collect long crm results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_long-crm-results_20260527T224903_result.json`
- **Structured JSON:** [`77127f30a82eb5d605bd.json`](../../sessions/77/77127f30a82eb5d605bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s42/s43 registry 已完整（hypothesis/conclusion/metrics/paths 全齐）。无需额外更新。

## 汇总

| exp_id | Suite | Seed | SR | trigger_rate | status |
|--------|-------|------|----|-------------|--------|
| crm-always-on-long-s42 | Long | 42 | **41.0%** | 100.0% | DONE ✓ |
| crm-always-on-long-s43 | Long | 43 | **45.5%** | 100.0% | DONE ✓ |
| crm-always-on-long-s44 | Long | 44 | — | — | RUNNING (task ~8/10, KITCHEN_SCENE8 5/20) |
| smolvla-tau030-object-s42 | Object | 42 | **79.0%** | 2.3% | DONE ✓ |
| smolvla-tau040-object-s42 | Object | 42 | **73.5%** | 0.9% | DONE ✓ |
| smolvla-tau045-object-s42 | Object | 42 | **71.5%** | 0.8% | DONE ✓ |
| pi05-crm-always-on-long-s42 | Long | 42 | — | — | RUNNING (task 1/10, cqa1 cuda:5) |
| pi05-crm-always-on-object-s42 | Object | 42 | — | — | RUNNING (task 2/10, cqa1) |
| pi05-crm-always-on-spatial-s42 | Spatial | 42 | — | — | RUNNING (task ~8/10, cqa1) |
| pi05-crm-always-on-goal-s42 | Goal | 42 | — | — | RUNNING (task 2/10, cqa1) |

**关键发现：**
- **Table 1 数据**：Long s42/s43 已有结果，s44 预计很快完成（还剩 ~2 个 task）
- CRM always-on Long s42/s43/tau-sweep 三组已在 registry 中完全标记 DONE，无需额外更新
- Pi05 四个实验全在 cqa1-32758 上运行中（registry 状态仍为 PREPARING，实际已在跑）
- C002 检查：s42/s43 日志无 OOM/CUDA error，SR 非零，EXIT_CODE=0，结果可信

---
