# experiment wave3 dir g decoupling 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_wave3-dir-g-decoupling-16639_20260520T100631_result.json`
- **Structured JSON:** [`2dc5e77dd5845a71d501.json`](../../sessions/2d/2dc5e77dd5845a71d501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Direction G 全量运行已启动：

- **服务器**: westd-16639
- **PID**: 307164
- **vLLM**: port 8020 (GPU 0, 已有空闲实例复用)
- **日志**: `/tmp/direction_g_full.log`
- **进度**: 已开始 strategy `conservative`，204 题，共 3 策略 (conservative/standard/aggressive)
- **Baselines**: SC 54.41%, SICA 59.31%

Dry-run 3 题验证通过 (acc=0.667, matched=100%)。预计全量运行约 2-3 小时（204 题 × 3 策略 × 12 traces/题）。

---
