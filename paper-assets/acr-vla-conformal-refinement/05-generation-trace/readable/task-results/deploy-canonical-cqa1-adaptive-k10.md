# deploy canonical cqa1 adaptive k10

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_canonical-cqa1-adaptive-k10_20260524T230544_result.json`
- **Structured JSON:** [`d929bcd885e7ae892c83.json`](../../sessions/d9/d929bcd885e7ae892c83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署 5 个任务，等待 120s 后验证启动状态。

**部署摘要（待验证）：**
```
前置检查：
  CRM checkpoint: 存在 (1.3MB, May 24 02:37)
  SmolVLA 模型: 存在 (smolvla_libero/)
  VLA-only baselines: s42=存在, s43=存在, s44=存在, s48=存在, s49=存在
    (logs/eval_spatial_vla_only_seed{42,43,44,48,49}.json)
  GPU: 6× RTX 4090D 24GB, GPU 0-4 空闲

部署结果：
  eval-canonical-adaptive-k10-spatial-s42: GPU 0, PID=209904 [已提交]
  eval-canonical-adaptive-k10-spatial-s43: GPU 1, PID=210181 [已提交]
  eval-canonical-adaptive-k10-spatial-s44: GPU 2, PID=210458 [已提交]
  eval-canonical-adaptive-k10-spatial-s48: GPU 3, PID=210816 [已提交]
  eval-canonical-adaptive-k10-spatial-s49: GPU 4, PID=211568 [已提交]

需要额外补跑的 VLA-only：无
```

---
