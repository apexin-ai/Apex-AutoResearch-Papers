# ssh kill duplicates deploy new bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-duplicates-deploy-new-bjb2-28827_20260517T103437_result.json`
- **Structured JSON:** [`eed596b1fff8bf1bdf7d.json`](../../sessions/ee/eed596b1fff8bf1bdf7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
killed: PID 363223, PID 365893 ✓

deployed:
  obs_only ε=0.2 seed46: cuda:2, PID=387642
  perdof ε=0.2 seed46: cuda:4, PID=389051

nvidia-smi 确认:
  GPU 2: python PID 387642, 5645MiB
  GPU 4: python PID 389051, 5645MiB

日志确认 (两个都正常启动):
  [eval] Loading LIBERO object environments...
  [info] using task orders [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  [eval] 10 tasks loaded.
```

---
