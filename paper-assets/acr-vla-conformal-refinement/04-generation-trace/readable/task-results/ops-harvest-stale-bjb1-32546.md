# ops harvest stale bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-stale-bjb1-32546_20260519T112208_result.json`
- **Structured JSON:** [`498b8fc859bde36d9032.json`](../../sessions/49/498b8fc859bde36d9032.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

7/8 实验全部更新为 DONE。汇总：

| exp_id | success_rate | conclusion |
|--------|-------------|------------|
| eval-obs-only-object-norm01-seed47 | 17% | success |
| eval-scalar-object-seed46 | 9% | success |
| eval-obs-only-object-norm03-seed46 | 17% | success |
| eval-perdof-object-norm03-seed46 | 4% | success |
| eval-obs-only-object-default-seed47 | 16% | success |
| eval-perdof-object-norm005-seed46 | 11% | success |
| eval-perdof-object-norm01-seed48 | 12% | success |
| eval-perdof-object-norm003-seed48 | **仍在运行** | — |

**eval-perdof-object-norm003-seed48** 仍有活跃 tmux session 和 GPU 进程（pid 719459），正在跑 orange_juice 任务 rollout 9/10，尚未生成 JSON。保持 RUNNING 状态不动。

---
