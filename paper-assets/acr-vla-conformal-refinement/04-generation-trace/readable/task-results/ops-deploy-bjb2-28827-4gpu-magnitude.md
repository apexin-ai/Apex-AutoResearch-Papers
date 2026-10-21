# ops deploy bjb2 28827 4gpu magnitude

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb2-28827-4gpu-magnitude_20260517T235048_result.json`
- **Structured JSON:** [`eb6510b485ecc747d907.json`](../../sessions/eb/eb6510b485ecc747d907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署结果：

| # | exp_id | GPU | 状态 |
|---|--------|-----|------|
| 1 | eval-obs-only-object-norm02-seed42 | cuda:0 | **跳过** — GPU 被占用 (PID 492545, 5609 MiB) |
| 2 | eval-obs-only-object-norm01-seed42 | cuda:1 | **运行中** ✓ |
| 3 | eval-perdof-object-norm01-seed42 | cuda:3 | **运行中** ✓ |
| 4 | eval-perdof-object-norm03-seed43 | cuda:5 | **跳过** — GPU 被占用 (PID 488665, 5645 MiB) |

已成功部署 2/4 实验（tmux sessions: `eval-obs-only-norm01-s42`, `eval-perdof-norm01-s42`），已注册至 registry。

GPU 0 和 GPU 5 各有一个 python 进程占用约 5.6 GB 显存，需要等现有任务结束后才能部署剩余两个实验。

---
