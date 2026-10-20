# ops local progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_local-progress-check_20260514T110907_result.json`
- **Structured JSON:** [`50e8b6495f0e54ee91af.json`](../../sessions/50/50e8b6495f0e54ee91af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-004 sim sweep v2

- **状态**: 运行中 (PID 411032, uptime 3h57m)
- **当前**: condition [3/12] `auc0.8_n100_prior1.0_binary`, seed 1/10 — chains 3/4 正在采样 (chains 1/2 已完成 ~10:57 UTC)
- **已完成**: 5 个 condition 结果文件已写入，condition 3 刚开始
- **结果目录**: 5 个 condition JSON + sweep_summary.json
- **ETA**: 日志显示 condition 3 开始时预估剩余 15.3h（约 May 15 ~01:30 UTC）
- **异常**: 无，采样正常 (γ 收敛良好, θ_corr > 0.94)

## exp-005 noise prop v3

- **状态**: 运行中 (PID 426335/426336, uptime 2h43m)
- **当前**: fit 9/25 — `σ_e=0.3, seed=45` ME(analytic) 模型, chains 3/4 正在采样 (chains 1/2 完成 ~11:02 UTC)
- **已完成**: 8/25 fits (32%)
- **速率**: 每个 fit (simple + ME) 约 35 min，剩余 17 个 fit ≈ 10h
- **ETA**: ~21:00 UTC May 14
- **注意**: `results/exp005/exp005_run.log` 记录了旧版 v2 的崩溃 (Stan `normal_lpdf` scale=0 → chains 3/4 retcode=1)。当前 v3 运行正常 (Rhat ~1.006-1.009)，无采样异常。

---
