# ops harvest bjb1 18228 round3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-bjb1-18228-round3_20260519T030425_result.json`
- **Structured JSON:** [`8ffb703aa7a904886b1c.json`](../../sessions/8f/8ffb703aa7a904886b1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**这些实验尚未完成。** 以下是实际状态:

### 仍在运行 (7 个, 各完成 ~4/10 tasks, 约 40-50% 进度)

| tmux session | registry exp_id | 进度 |
|---|---|---|
| eval-obs-only-object-norm003-seed43 | eval-obs-only-object-norm003-seed43-r2 | 4/10 tasks |
| eval-obs-only-norm003-seed45-t16 | eval-obs-only-object-norm003-seed45-r2 | 4/10 tasks |
| eval-obs-only-norm003-seed46 | eval-obs-only-object-norm003-seed46 | 4/10 tasks |
| eval-obs-only-norm003-seed47 | eval-obs-only-object-norm003-seed47 | 4/10 tasks |
| eval-obs-only-norm003-seed49-t16 | eval-obs-only-object-norm003-seed49 | 4/10 tasks |
| eval-obs-only-norm005-seed46 | eval-obs-only-object-norm005-seed46 | 4/10 tasks |
| eval-perdof-norm03-seed48 | eval-perdof-object-norm03-seed48 | 4/10 tasks |

所有 tmux session 今天 04:42-05:26 创建，当前日志写入 `/root/logs/`，实时更新中。旧 `/root/acr-vla-conformal-refinement/logs/` 中的同名 log 是之前被 kill 的 partial runs（1-2 tasks）。

### 不在此服务器 (2 个)

| registry exp_id | 状态 |
|---|---|
| eval-obs-only-object-norm005-seed47 | 服务器上无任何 log/tmux |
| eval-perdof-object-norm003-seed48 | 服务器上无任何 log/tmux |

### 结论

无法收割，所有实验要么仍在运行（~50% 进度，预计再需 5-7 小时完成），要么不在此服务器上。是否需要等待完成后再收割，或者先查找 norm005-seed47 和 perdof-norm003-seed48 在其他服务器上的状态？

---
