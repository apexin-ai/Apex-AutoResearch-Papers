# analysis pi05 spatial bjb2 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-spatial-bjb2-batch_20260526T133923_result.json`
- **Structured JSON:** [`ff266888788a704ce08e.json`](../../sessions/ff/ff266888788a704ce08e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验已更新为 DONE。汇总：

## π0.5 Spatial 实验结果汇总

| exp_id | mode | seed | success_rate | trigger_rate | conclusion |
|--------|------|------|-------------|-------------|------------|
| pi05-crm-k2-spatial-s42-bjb2-r2 | CRM K=2 obs_only | 42 | 96.5% (193/200) | — | success |
| pi05-crm-k2-spatial-s43-bjb2-r2 | CRM K=2 obs_only | 43 | 97.0% (194/200) | — | success |
| pi05-crm-k2-spatial-s44-bjb2-r2 | CRM K=2 obs_only | 44 | 97.0% (194/200) | — | success |
| pi05-adaptive-spatial-s42-bjb2-r2 | Adaptive (τ=0.25) | 42 | 96.5% (193/200) | 4.8% | success |
| pi05-adaptive-spatial-s43-bjb2-r2 | Adaptive (τ=0.25) | 43 | 98.0% (196/200) | 4.4% | success |
| pi05-adaptive-spatial-s44-bjb2-r2 | Adaptive (τ=0.25) | 44 | 97.0% (194/200) | 3.9% | success |

**聚合统计：**
- **CRM K=2 Spatial**: mean=96.83%, std=0.29%
- **Adaptive Spatial**: mean=97.17%, std=0.76%, mean trigger_rate=4.37%

两种方法均与 VLA-only baseline (~96%) 持平，CRM 未引入性能退化。Adaptive 模式 trigger rate 极低 (~4.4%)，说明 Spatial 任务上 π0.5 的 uncertainty 普遍较低，conformal gate 几乎不触发 CRM 修正。

---
