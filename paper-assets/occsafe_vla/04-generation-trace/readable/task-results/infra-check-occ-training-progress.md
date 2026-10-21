# infra check occ training progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_occ_training_progress_20260521T015829_result.json`
- **Structured JSON:** [`d82c3d72d2b222d6640d.json`](../../sessions/d8/d82c3d72d2b222d6640d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：occ_s1 之前 crash 了，已被重启但进度大幅落后。

```
occ_s0: step ~35235/50005 (70.5%), 1.08 it/s, 剩余 ~3h48m
         loss@35200: occ=0.0083, action=0.0542
         checkpoints: 5000, 7500, 30000, 32500, 35000

occ_s1: ⚠️ 之前 crash (PID 28900, exitcode 1, 07:57:05)
         已重启为 PID 58875, 运行 43 分钟
         实际 step ~10279/50005 (20.6%), 1.09 it/s, 剩余 ~10h07m
         tqdm 显示 2779/50005 (从 0 计数, 实际 global step = 7500+2779=10279)
         log → /root/occsafe_vla/occ_s1_restart.log
         checkpoints: 5000, 7500, 10000

occ_s2: step ~35221/50005 (70.4%), 1.08 it/s, 剩余 ~3h48m
         loss@35200: occ=0.0099, action=0.0635
         checkpoints: 5000, 7500, 30000, 32500, 35000

Monitor PID 61526: alive (运行 9m48s)

GPU utilization:
  cuda:0  99%, 62203/97887 MiB
  cuda:1  99%, 62203/97887 MiB
  cuda:2  99%, 62209/97887 MiB
  cuda:3 100%,     0/97887 MiB (空闲,仅显示计算占用)
```

**occ_s1 问题总结**：原进程 PID 28900 在 07:57 crash（torchrun ChildFailedError, exitcode 1, 无详细 traceback）。已被重启（可能由 monitor 脚本触发），从 7500 checkpoint resume，当前在 step ~10279，比 s0/s2 落后约 25000 步（~6.4 小时）。s0 和 s2 预计还需 ~3h48m 完成，s1 需要 ~10h。

---
