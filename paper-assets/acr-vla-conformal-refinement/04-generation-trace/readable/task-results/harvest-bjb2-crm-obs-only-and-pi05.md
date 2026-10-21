# harvest bjb2 crm obs only and pi05

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-crm-obs-only-and-pi05_20260525T002621_result.json`
- **Structured JSON:** [`ba12dfc1cc8275367631.json`](../../sessions/ba/ba12dfc1cc8275367631.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 harvest 完成。汇总如下：

## Part A: CRM obs-only (bjb2-28827) — 已验证

三个实验已在 registry 中，服务器 JSON 值完全匹配 Reviewer 确认的数据，无需额外操作：

| exp_id | Benchmark | Seed | SR | Registry Status |
|--------|-----------|------|----|-----------------|
| eval-supp-crm-norm005-spatial-s48 | Spatial | 48 | **78.0%** | DONE ✓ |
| eval-supp-crm-norm005-spatial-s49 | Spatial | 49 | **78.5%** | DONE ✓ |
| eval-supp-crm-norm005-goal-s48 | Goal | 48 | **80.0%** | DONE ✓ |

## Part B: π0.5 VLA-only (bjb1-32546) — 3 个新 harvest

| exp_id | Benchmark | Seed | SR | 操作 |
|--------|-----------|------|----|------|
| eval-pi05-vla-only-object-s43 | Object | 43 | **81.5%** | QUEUED → DONE ✓ |
| eval-pi05-vla-only-object-s44 | Object | 44 | **81.0%** | 新建 → DONE ✓ |
| eval-pi05-vla-only-spatial-s45 | Spatial | 45 | **85.0%** | 新建 → DONE ✓ |

已有（无需更新）：goal-s42 (95.5%), goal-s43 (97.0%), object-s42 (96.5%), spatial-s42 (98.0%), spatial-s43 (96.0%), long-s42 (94.0%)。

另有 6 个 v2 QUEUED 条目是同一实验的重复运行（结果覆盖了相同的 JSON 文件），未处理。

---
