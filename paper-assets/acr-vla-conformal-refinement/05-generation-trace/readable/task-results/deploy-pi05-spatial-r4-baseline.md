# deploy pi05 spatial r4 baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-spatial-r4-baseline_20260522T115041_result.json`
- **Structured JSON:** [`977a55cb2dba1c99d8d1.json`](../../sessions/97/977a55cb2dba1c99d8d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

**汇总：**

| Exp ID | GPU | 显存占用 | 状态 |
|--------|-----|---------|------|
| `eval-pi05-vla-only-spatial-seed42-r4` | cuda:1 | 14123 MiB | RUNNING ✅ |
| `eval-pi05-vla-only-spatial-seed43-r4` | cuda:2 | 14663 MiB | RUNNING ✅ |
| `eval-pi05-vla-only-spatial-seed44-r4` | cuda:3 | 14663 MiB | RUNNING ✅ |

参数确认：`n_action_steps=10`，`max_steps=280`，`benchmark=spatial`，`mode=vla_only`（single, K=1）。tmux session 名称：`eval-spatial-seed{42,43,44}`，日志：`/tmp/eval-spatial-seed{42,43,44}.log`。

注意：代码中 `vla_only` + `baseline_mode=single`（默认）会将 K 覆盖为 1。如果需要 K=10 mean baseline，需要加 `--baseline_mode mean`。

---
