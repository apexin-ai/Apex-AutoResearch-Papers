# ops double deploy bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_double-deploy-bjb1-32546_20260518T163035_result.json`
- **Structured JSON:** [`c0391388549e9a4191a9.json`](../../sessions/c0/c0391388549e9a4191a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。6 个实验已部署在 bjb1-32546 上双跑，registry 全部 RUNNING。

| GPU | exp_id | 状态 |
|-----|--------|------|
| 0 | eval-perdof-object-norm005-seed46 | RUNNING |
| 1 | eval-obs-only-object-default-seed47 | RUNNING |
| 2 | eval-perdof-object-norm03-seed46 | RUNNING |
| 3 | eval-obs-only-object-norm03-seed46 | RUNNING |
| 4 | eval-scalar-object-seed46 | RUNNING |
| 5 | eval-obs-only-object-norm01-seed47 | RUNNING |

首次启动因 tmux 里 `python` 不在 PATH 而失败，已改用 `/root/miniconda3/bin/python` 全路径重启成功，日志显示模型权重加载正常。

---
