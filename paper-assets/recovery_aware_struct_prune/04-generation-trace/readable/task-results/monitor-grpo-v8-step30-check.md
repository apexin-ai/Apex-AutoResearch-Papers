# monitor grpo v8 step30 check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo-v8-step30-check_20260515T174235_result.json`
- **Structured JSON:** [`c376cf712fed68b4a0a6.json`](../../sessions/c3/c376cf712fed68b4a0a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都未到 step 30。以下是当前状态：

```
RASP v8 (PID 532861): ~step 28/100, still running
  - grad_norm=0.011, frac_zero_std=0.9, reward=0.026, clipped_ratio=0.963
  - 全部三个 kill 条件自 step 10 起就已满足（grad_norm<0.05, frac_zero_std≥0.85, reward<0.03）
  - COLLAPSED, 指标继续恶化中
  - ETA step 30: ~02:00 Beijing (May 16) ≈ 15 分钟后

Standard v8 (PID 534667): ~step 26/100, HEALTHY
  - grad_norm=1.586, frac_zero_std=0.675, reward=0.061, clipped_ratio=0.638
  - frac_zero_std 趋势: 0.5 → 0.675（上升但仍安全）
  - 无 kill 条件触发

GPU: cuda:0 71.7/97.9GB 100%, cuda:1 71.7/97.9GB 100%
磁盘: 77% used, 58GB free on /root/autodl-tmp/
```

步数估算基于 wandb history_offset 增长率和 completions parquet 时间戳（step 10→20 间隔 ~69 min，~6.9 min/step）。

RASP 尚未到 step 30，暂不执行 kill。需要 ~15 分钟后再查。是否要我到时再来检查？

---
