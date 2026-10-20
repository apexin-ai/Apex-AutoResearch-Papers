# check cpu irt status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cpu-irt-status_20260515T001803_result.json`
- **Structured JSON:** [`28fd7da3bdb484d835c0.json`](../../sessions/28/28fd7da3bdb484d835c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个任务全部 **running**：

| 任务 | 状态 | 进度 |
|------|------|------|
| **exp006-oracle-gsm8k-extended** | running | 4 chains, ~50-53% sampling (warmup 2000 + samples 4000 = 6000 total), ~3.6 it/s, 预计还需 ~14 min |
| **exp006-pooled-s1only-gsm8k** | running | 刚开始 warmup, 4 chains 约 5-10% warmup (200/2000), ~4-5 it/s |
| **exp006-pooled-s1only-arc** | running | chains 1&2 在 65-70% sampling, chains 3&4 在 55-60% sampling (总共 2000 samples), ~7.5 it/s, 预计还需 ~2-3 min |

**预计完成顺序**: arc (最快, ~2-3 min) → oracle-extended (~14 min) → s1only-gsm8k (最慢, 刚开始 warmup)

另外注意：服务器上还有 2 个其他 exp006 进程在跑：
- `results_pooled_05B_15B_gsm8k_v3_rrf`
- `results_pooled_05B_15B_2pl_ablation`

---
