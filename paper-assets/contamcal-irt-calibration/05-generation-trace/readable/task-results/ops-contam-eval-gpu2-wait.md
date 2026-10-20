# ops contam eval gpu2 wait

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_contam_eval_gpu2_wait_20260514T011258_result.json`
- **Structured JSON:** [`a8437bbc0ac1d25bc629.json`](../../sessions/a8/a8437bbc0ac1d25bc629.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个等待脚本已部署：

| 实验 | GPU | 等待条件 | 守护 PID |
|------|-----|---------|----------|
| exp_001_eval_05B_d100 | cuda:2 | GPU 2 无进程 | 253234 |
| exp_001_eval_05B_d005 | cuda:1 | PID 229375 结束 + >10GB 空闲 | 253447 |

GPU 2 的 d000_s123 eval 还剩 ~11 min，GPU 1 的 d000_s42 eval 还剩 ~12.5 min。两个脚本会在对应 eval 完成后自动启动。4 分钟后回来确认。

---
