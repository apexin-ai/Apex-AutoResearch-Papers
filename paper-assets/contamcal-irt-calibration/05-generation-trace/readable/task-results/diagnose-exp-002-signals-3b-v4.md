# diagnose exp 002 signals 3B v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_3B_v4_20260515T195359_result.json`
- **Structured JSON:** [`d44e2189f2033e1cb3f0.json`](../../sessions/d4/d44e2189f2033e1cb3f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断报告如下：

---

## 诊断结果

### v4 死因
**EXIT_CODE=143 (SIGTERM)**，非 OOM/段错误。根因是 `run_batch.py` 的 bug：`--signal` 参数未正确传递给 `compute_signals.py` 子进程。11/12 combo 立即失败（rc=2, `error: --signal required`），d000_s42/mmlu 被 kill (rc=-15)。Batch report: **0/12 passed**。死亡时间 May 15 23:23 UTC。

### 3B Signals 完成度 (12 combos: 4 dosages × 3 benchmarks)

| Combo | Status | Notes |
|-------|--------|-------|
| d000/gsm8k | **COMPLETE** | signals_merged 存在 |
| d000/arc | **COMPLETE** | signals_merged 存在 |
| d005/arc | **COMPLETE** | signals_merged 存在 |
| d025/gsm8k | **COMPLETE** | signals_merged 存在 |
| d025/arc | **COMPLETE** | signals_merged 存在 |
| d000/mmlu | IN PROGRESS | PID 617202, cuda:3, ~60min, has emb+minkpp |
| d005/mmlu | IN PROGRESS | PID 622856, cuda:2, ~15min, has emb+minkpp |
| d025/mmlu | IN PROGRESS | v5 on cuda:4 |
| d100/mmlu | IN PROGRESS | PID 622558, cuda:4, ~15min, has emb+minkpp |
| d005/gsm8k | **STALLED** | has emb+minkpp, NO selfcritique/merged, no active process |
| d100/gsm8k | PENDING | v5 will cover |
| d100/arc | PENDING | v5 will cover |

**5/12 complete, 4/12 in progress, 1/12 stalled, 2/12 pending**

### v5 状态
**PID 623826 存活**，cuda:4。计划 4 tasks：d025_s42/mmlu (当前), d100_s42/{mmlu,gsm8k,arc}。跳过了已完成的 d025/{gsm8k,arc}。

### cuda:3 状态
**不空闲。** PID 617202（新 batch runner PID 617201 的子进程）正在 cuda:3 活跃计算 d000_s42/mmlu signals，占用 7526MiB。

### 需要注意的问题
1. **cuda:4 冲突**：PID 622558（独立 d100/mmlu）与 v5 子进程（PID 623837）共享 cuda:4，且 v5 后续也要做 d100/mmlu — 重复计算
2. **d005/gsm8k 掉队**：有 embedding+minkpp 但无人计算 selfcritique，需要单独补跑

---
