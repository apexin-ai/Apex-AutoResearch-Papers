# ops gpu monitor and submit queue

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_monitor_and_submit_queue_20260514T215157_result.json`
- **Structured JSON:** [`2676d68fad1491673421.json`](../../sessions/26/2676d68fad1491673421.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

轮询已设置。当前状态：

- **6/6 GPU 全部忙碌**，无 GPU 释放
- Cron job `5633488f` 已创建，每 5 分钟自动轮询
- 待触发的提交队列：
  - GPU 0 释放 → pooled IRT（最高优先级）
  - GPU 3 释放 → 3B d100 v2 aligned eval
  - GPU 4 释放 → 3B d000 para aligned eval

下一次轮询将在 ~5 分钟后自动执行。预计 GPU 0（signals）最先释放。

---
