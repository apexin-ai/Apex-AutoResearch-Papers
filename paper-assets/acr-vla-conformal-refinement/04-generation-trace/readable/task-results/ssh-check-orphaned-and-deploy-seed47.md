# ssh check orphaned and deploy seed47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-orphaned-and-deploy-seed47_20260517T102116_result.json`
- **Structured JSON:** [`c90bee1e63a1c2c6ef83.json`](../../sessions/c9/c90bee1e63a1c2c6ef83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已占用（5645MiB, 21% util），进程正常运行。

## 孤儿实验检查
- perdof-norm01-seed44 (bjb1-18228): **still running** (PID 531963)
- perdof-norm01-seed45 (bjb1-32546): **completed, SR=11%** (11/100)

## 5-seed Fisher test (obs_only ε=0.2 vs argmin, pooled)
```
Fisher p = 0.075456
Odds ratio = 1.3953
```
不显著（p > 0.05），obs_only 和 argmin 的差异无统计学意义。

## 部署结果
eval-perdof-object-norm01-seed47-r2: **deployed on bjb1-32546 cuda:1, PID=414817** (子进程 414824 已上 GPU, 5645MiB)

---
