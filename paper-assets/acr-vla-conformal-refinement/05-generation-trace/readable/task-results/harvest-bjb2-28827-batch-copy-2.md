# harvest bjb2 28827 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-batch_20260518T141519_result.json`
- **Structured JSON:** [`b1a8863eaccff5221090.json`](../../sessions/b1/b1a8863eaccff5221090.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个进程均存活，无需收割。当前状态：

```
eval-obs-only-object-norm02-k5-seed44:      [RUNNING] task 2/10, rollout 4/10  (1h13m, cuda:2)
eval-random-selection-object-seed43:         [RUNNING] task 9/10, rollout 9/10  (15h, cuda:0) ← 即将完成
eval-random-selection-object-seed44:         [RUNNING] task 8/10, rollout 4/10  (11h50m, cuda:4)
eval-obs-only-object-norm01-seed45-r2:       [RUNNING] task 1/10, rollout 5/10  (51m, cuda:1)
eval-obs-only-object-default-seed45-r2:      [RUNNING] task 1/10, rollout 5/10  (51m, cuda:3)
```

**GPU 释放情况**: 无。cuda:0 预计很快释放（seed43 已跑到 task 9/10 尾声），cuda:4 也较接近完成。其余三个还在早期阶段。

---
