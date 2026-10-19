# analyze pi05 crm always on object s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-crm-always-on-object-s43_20260528T030206_result.json`
- **Structured JSON:** [`3ab68b20387fafb6b468.json`](../../sessions/3a/3ab68b20387fafb6b468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总如下：

## pi05-crm-always-on-object-s43 结果

| 指标 | 值 |
|------|-----|
| **overall SR** | **92.0%** (184/200) |
| trigger_rate | 100% (符合预期, τ=0.001) |
| mean_unc | 0.0789 |
| total_rollouts | 200 |

### Per-task 成功率及与 s42 对比

| Task | s43 | s42 | Δ |
|------|-----|-----|---|
| alphabet_soup | 95 | 100 | -5 |
| cream_cheese | 90 | 100 | -10 |
| salad_dressing | 90 | 95 | -5 |
| bbq_sauce | 85 | 85 | 0 |
| **ketchup** | **75** | **55** | **+20** |
| tomato_sauce | 95 | 90 | +5 |
| butter | 100 | 100 | 0 |
| milk | 100 | 100 | 0 |
| chocolate_pudding | 95 | 95 | 0 |
| **orange_juice** | **95** | **85** | **+10** |
| **Overall** | **92.0** | **90.5** | **+1.5** |

### 分析

- s43 整体 92% 略高于 s42 的 90.5%，两 seed 均值 = **91.25%**
- ketchup 从 55→75 提升显著（+20），orange_juice 从 85→95（+10）
- cream_cheese 从 100→90 下降 10 个点，alphabet_soup 从 100→95
- 无异常：无 OOM、无 CUDA error、无 0% SR task，日志正常完成

---
