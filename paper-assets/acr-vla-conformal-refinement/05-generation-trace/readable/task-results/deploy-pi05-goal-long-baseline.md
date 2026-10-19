# deploy pi05 goal long baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-goal-long-baseline_20260522T122007_result.json`
- **Structured JSON:** [`7125df2b33ae5c7ebc81.json`](../../sessions/71/7125df2b33ae5c7ebc81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，两个实验已注册并标记为 RUNNING。

| 实验 | GPU | tmux session | 日志 |
|------|-----|-------------|------|
| `eval-pi05-vla-only-goal-seed42-r4` | cuda:4 | `eval-pi05-goal-seed42` | `/tmp/eval-pi05-goal-seed42.log` |
| `eval-pi05-vla-only-long-seed42-r4` | cuda:5 | `eval-pi05-long-seed42` | `/tmp/eval-pi05-long-seed42.log` |

参数确认：n_action_steps=10, TORCHDYNAMO_DISABLE=1, Goal max_steps=300, Long max_steps=520。`vla_only` + `baseline_mode=single` 会自动将 K 设为 1（单次推理，符合预期）。

---
