# ssh kill check deploy batch7

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-check-deploy-batch7_20260517T120433_result.json`
- **Structured JSON:** [`d4757f3f6c05b9d5d222.json`](../../sessions/d4/d4757f3f6c05b9d5d222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功，进程运行中，GPU 已占用，日志正常加载到 "10 tasks loaded"。

```
=== A: Kill 401104 (bjb2-28827) ===
结果：DEAD（进程已提前终止，kill 时已不存在）
GPU cuda:2 状态：占用（PID 404983, 5645 MiB）

=== B: Check 617632 (bjb1-18228) ===
判断：进程已终止（PID 不存在）
etime: N/A
日志最后：停在 "10 tasks loaded"，无 rollout 进度——进程挂死后自行退出

=== C: Deploy obs_only norm005 seed43 r2 (bjb1-32546) ===
cuda:0 状态：空闲 → 已占用
部署结果：PID=433499（实际 python 子进程 PID 433500）
GPU 验证：cuda:0 占用 5645 MiB
启动日志：CRM loaded (327,198 params), max_correction_norm=0.05, 10 tasks loaded
```

---
