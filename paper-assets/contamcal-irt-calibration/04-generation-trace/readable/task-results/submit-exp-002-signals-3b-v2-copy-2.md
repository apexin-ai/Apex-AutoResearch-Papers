# submit exp 002 signals 3B v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_002_signals_3B_v2_20260515T160809_result.json`
- **Structured JSON:** [`29b368cc5727f2893621.json`](../../sessions/29/29b368cc5727f2893621.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_002_signals_3B_v2 已成功提交到 GPU 4。**

- **PID**: 590509（compute_signals.py 子进程在 GPU 4，CUDA_VISIBLE_DEVICES=4 ✓）
- **tmux session**: `exp002_3B_v2`
- **任务**: 12 个（4 dosages × 3 benchmarks）
- **日志**: `/root/contamcal-irt-calibration/exp002/exp002_3B_v2.log`
- **Registry**: RUNNING

**修复了一个 bug**：`run_batch.py` line 202 原来无条件用 `--gpu` 参数覆盖 `CUDA_VISIBLE_DEVICES`，导致子进程跑到 GPU 0。已改为：当父进程已设置 `CUDA_VISIBLE_DEVICES` 时不覆盖。这就是 v1 失败（GPU 映射 bug）的根因之一。

---
