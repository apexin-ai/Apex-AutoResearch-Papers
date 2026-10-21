# analyze pi05 adaptive spatial tau035 bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-adaptive-spatial-tau035-bjb2_20260526T174012_result.json`
- **Structured JSON:** [`2cb4eaa46944c775759d.json`](../../sessions/2c/2cb4eaa46944c775759d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报：

**pi05-adaptive-spatial-s42-tau035-bjb2 结果**

| 指标 | 值 |
|------|-----|
| **SR** | **96.5%** (193/200) |
| **trigger_rate** | 2.55% (567/22218 steps) |
| **mean_correction_norm** | 0.200 |
| **mean_uncertainty** | 0.1055 |

**Per-task SR**: 8/10 tasks 100%，cookie_box 95%，ramekin 75%（唯一低分 task）。

**与 tau=0.25 对比**: tau=0.25 三种子均值 97.2±0.8%，tau=0.35 单种子 96.5%——略低但在 1σ 范围内。trigger_rate 从 ~5-6%（tau=0.25）降到 2.55%，符合预期（更高阈值 → 更少触发）。

**GPU**: cuda:1 已释放（1 MiB / 24564 MiB）。

**日志检查**: 无 OOM、无 CUDA error、无 SR=0% task，EXIT_CODE=0，结果可信。

---
