# ops double deploy bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_double-deploy-bjb2-28827_20260518T163024_result.json`
- **Structured JSON:** [`fcdcecaf621c2fb7678f.json`](../../sessions/fc/fcdcecaf621c2fb7678f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个实验全部部署完成，registry 已更新为 RUNNING。

**汇总：**

| GPU | exp_id | PID | 显存 |
|-----|--------|-----|------|
| 0 | eval-random-selection-object-seed45 | 604514 | 5922MB |
| 1 | eval-perdof-object-norm003-seed46 | 604782 | 3162MB |
| 2 | eval-obs-only-object-norm02-k5-seed45 | 604856 | 2234MB |
| 3 | eval-obs-only-object-default-seed48 | 604925 | 2234MB |
| 4 | eval-perdof-object-default-seed47 | 605833 | 1735MB |
| 5 | eval-perdof-object-norm03-seed47 | 606098 | 1539MB |

每张卡双跑总显存 3.6-11.6GB / 24.6GB，均安全。注意首次启动时 `python` 不在 tmux 的 PATH 里，已改用全路径 `/root/miniconda3/bin/python` 解决。

---
