# check westd27271 status 20250525

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd27271_status_20250525_20260525T230846_result.json`
- **Structured JSON:** [`f7233356780077622da6.json`](../../sessions/f7/f7233356780077622da6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU0: [运行中] Random k=0.7 Goal — Task 3/10 进行中 (ep 40/50)
  Task 1: 0.0% (0/50)
  Task 2: 0.0% (0/50)
  Task 3: 0.0% (0/40 so far)
  Overall SR (2 tasks done): 0.0% — 全部失败
  速度: ~1.5 eps/min | 剩余 ~360 eps ≈ 4h

GPU1: [运行中] L2norm k=0.9 Goal seed43 — Task 6/10 进行中 (ep 40/50)
  Task 1: 66.0% (33/50)
  Task 2: 92.0% (46/50)
  Task 3: 82.0% (41/50)
  Task 4: 38.0% (19/50)
  Task 5: 94.0% (47/50)
  Task 6: ~67.5% (27/40 so far)
  Avg SR (5 tasks done): 74.4%
  速度: ~2.6 eps/min | 剩余 ~210 eps ≈ 1.3h

空闲 GPU: 无
```

**关键发现：**

- **Random k=0.7 Goal**: 3 个 task 全部 0% SR，已不是样本量问题——random pruning 去掉 30% vision tokens 直接导致模型完全失效。与 L2norm 方法形成鲜明对比。
- **L2norm k=0.9 Goal seed43**: 5 tasks avg 74.4%，与 seed42 的 74.8% 高度一致，验证了结果的稳定性。预计 ~1.3h 后完成。

---
