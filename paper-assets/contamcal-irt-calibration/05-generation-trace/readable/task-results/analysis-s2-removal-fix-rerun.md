# analysis s2 removal fix rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s2-removal-fix-rerun_20260523T111111_result.json`
- **Structured JSON:** [`2c6059a0448d89a800ab.json`](../../sessions/2c/2c6059a0448d89a800ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Pipeline | MAE | τ | γ_mean [95% CI] | PPP |
|----------|-----|---|-----------------|-----|
| Raw Accuracy | — | -0.058 | — | — |
| Full RRF (S1+S2+S4) | 0.0076 | -0.056 | -0.698 [-1.762, 0.361] | 0.392 |
| No-S2 RRF (S1+S4) | 0.0070 | -0.075 | -0.358 [-1.316, 0.595] | 0.382 |

**关键发现**：移除 S2 (Min-K++) 对校准影响微乎其微（ΔMAE = -0.0005）。两个 pipeline 的 γ 95% CI 都包含 0，均未检测到显著 contamination effect。PPP 值均健康。注意这些 τ 值与任务描述中的参考值（Full RRF τ=0.731）差异很大——参考值可能来自不同的 benchmark 或模型子集。

结果已写入本地 `artifacts/s2_removal_ablation/s2_removal_results.md`。

---
