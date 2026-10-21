# diagnose pi05 spatial baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-spatial-baseline_20260521T114259_result.json`
- **Structured JSON:** [`426715f504ac7509f480.json`](../../sessions/42/426715f504ac7509f480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断汇总

| exp_id | 状态 | 原因 |
|--------|------|------|
| eval-pi05-vla-only-spatial-seed42 | DONE/failed | 进程被 kill，停在 task 10/10 rollout 10/20 |
| eval-pi05-vla-only-spatial-seed43 | DONE/failed | 同上 |
| eval-pi05-vla-only-spatial-seed44 | DONE/failed | 同上 |

**关键发现：**
- 3 个进程全部已死，无结果 JSON
- 所有 3 个日志停在完全相同的位置（task 10/10, rollout 10/20, 76 行），强烈暗示同时被 kill（可能系统 RAM OOM）
- 已完成的 9/10 个 task × 3 seeds：**全部 0/20 = 0% SR**
- 即使实验未完整跑完，结论已清晰：**PI0.5 VLA-only 在 LIBERO-Spatial 上约 0% 成功率**

如需正式指标，可以重跑单 seed 补全；但考虑到 180/180 rollouts 全部失败，重跑的意义不大。

---
