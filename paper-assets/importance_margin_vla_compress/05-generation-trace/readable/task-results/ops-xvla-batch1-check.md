# ops xvla batch1 check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-batch1-check_20260520T100730_result.json`
- **Structured JSON:** [`c40395352b768231a045.json`](../../sessions/c4/c40395352b768231a045.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Batch 1 结果:
  k=1.0:  SR=99.2% (496/500) ✓ 完成 | tokens: 50→50
  k=0.95: SR=99.0% (495/500) ✓ 完成 | tokens: 50→47
  k=0.9:  SR=97.6% (488/500) ✓ 完成 | tokens: 50→45
  k=0.7:  进行中 — Task 8/10, ep 11/50 | tokens: 50→35

k=0.7 已完成 task 进度:
  Task 0: 94.0% (47/50)
  Task 1:  2.0%  (1/50)  ← 崩塌
  Task 2: 100.0% (50/50)
  Task 3: 80.0% (40/50)
  Task 4: 28.0% (14/50) ← 严重退化
  Task 5: 92.0% (46/50)
  Task 6: 12.0% (6/50)  ← 崩塌
  Task 7: 66.0% (33/50)
  Task 8: 0/11 全部 FAIL（进行中）
  当前累计: 237/411 ≈ 57.7%

Batch 2 状态: 未启动
  原因: sweep 脚本用 `wait` 阻塞，k=0.7 未完成，Batch 2 不会启动

GPU 状态:
  GPU 0: 1 MiB / 97887 MiB, 0% — 空闲 (k=1.0 已完成)
  GPU 1: 1 MiB / 97887 MiB, 0% — 空闲 (k=0.95 已完成)
  GPU 2: 1 MiB / 97887 MiB, 0% — 空闲 (k=0.9 已完成)
  GPU 3: 4872 MiB / 97887 MiB, 1% — k=0.7 运行中
```

关键发现：k=0.7（保留 70% tokens）出现严重的 task-level 不均匀退化。Task 1/4/6/8 几乎完全失败，而 Task 0/2/5 仍接近正常。这说明某些 task 对被剪掉的 vision tokens 高度敏感。k=0.7 最终 SR 预估在 **45-55%** 左右（Task 8 目前全 FAIL，Task 9 未知）。

k=0.7 预计还需 ~25 分钟完成（剩余 Task 8 的 39 eps + 整个 Task 9），之后 Batch 2 自动启动。

---
