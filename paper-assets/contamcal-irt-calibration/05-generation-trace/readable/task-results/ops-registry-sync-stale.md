# ops registry sync stale

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-sync-stale_20260515T191459_result.json`
- **Structured JSON:** [`2f60ef6f401084e075d0.json`](../../sessions/2f/2f60ef6f401084e075d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_004_sim_sweep_v7 状态：运行中**

- 进度：**3/12** 条件已完成，当前正在跑第 4 个 `auc0.9_n50_prior1.0_binary`（7/10 seeds 完成，正在跑 seed 8-9）
- 并行度：2 workers × 2 chains
- results 目录有 13 个文件（12 个 JSON + 1 个 summary），这些是之前 v6 的残留结果，v7 用 `--resume` 模式在补跑缺失的 seeds
- 每个 seed 的 Stan 采样耗时约 25-50 分钟，剩余约 9 个条件 × 若干未完成 seeds，预计还需数小时

---
