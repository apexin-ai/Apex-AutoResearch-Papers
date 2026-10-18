# audit deploy westd 38929 20260524

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_westd-38929-20260524_20260524T053420_result.json`
- **Structured JSON:** [`e595573c846daa2b1795.json`](../../sessions/e5/e595573c846daa2b1795.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都不需要重跑。

```
GPU Status:
- GPU 0: free (1 MiB / 97887 MiB, 0%)
- GPU 1: free (1 MiB / 97887 MiB, 0%)
- GPU 2: occupied (4672 MiB / 97887 MiB, 35%) — eval_xvla_l2norm_k05_long_seed42_v3 仍在运行
- GPU 3: free (1 MiB / 97887 MiB, 0%)

实验 A (k07 spatial v2): 实际完成 SR=72.8% (364/500)
  - cron 误判为 failed，已更新 registry → conclusion=success + metrics
  - Per-task: T0=98% T1=42% T2=96% T3=94% T4=82% T5=0% T6=98% T7=34% T8=94% T9=90%

实验 B (k05 long v3): 仍在运行中，未被 kill
  - 已完成 Task 0-7，当前 Task 8 ep 41/50，剩余 Task 9
  - 已完成任务 SR: T0=26% T1=0% T2=48% T3=84% T4=36% T5=88% T6=48% T7=78%
  - 预计 ~20-30min 完成（registry DONE+killed 状态无法回退 RUNNING）

已部署: 无（两个实验均无需重跑）
剩余空闲 GPU: cuda:0, cuda:1, cuda:3
```

---
