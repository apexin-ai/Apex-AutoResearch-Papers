# research 2pl full pipeline coverage

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_2pl-full-pipeline-coverage_20260515T104045_result.json`
- **Structured JSON:** [`cd3b46f363b53cddfdc6.json`](../../sessions/cd/cd3b46f363b53cddfdc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无需重跑——`results_pooled_05B_15B_gsm8k_s1only_2pl` 已包含完整 pipeline（含 coverage、evaluation、baselines）。Director 所说的"只有 joint_fit"是 `_v2` 目录。

**核心结果**：

| 指标 | 4PL+γ | 2PL+γ |
|------|-------|-------|
| **coverage_95** | **0.500** | **1.000** |
| **coverage_80** | **0.375** | **1.000** |
| coverage_50 | 0.125 | 0.500 |
| MAE | 0.036 | 0.013 (↓2.8×) |
| max_rhat | 1.015 ❌ | 1.002 ✅ |
| min_ESS | 330 ❌ | 1808 ✅ |
| gamma_mean | 0.187 | 0.167 |

2PL 完全解决了 4PL 的 coverage collapse。不过存在 confound：2PL 用了 4000 samples/chain (16k total draws) vs 4PL 的 1000 samples/chain (4k total draws)。报告已写入 `artifacts/2pl_vs_4pl_ablation.md` 并注册。如需 matched-draws (1000 samples) 的 2PL run 来排除 draws 差异的影响，可以安排。

---
