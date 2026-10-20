# ops c4 arc ppp

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4_arc_ppp_20260517T145201_result.json`
- **Structured JSON:** [`9d370a84f325c6b0b871.json`](../../sessions/9d/9d370a84f325c6b0b871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**ARC within-family (Qwen-only, J=13, 排除 0.5B) PPP = 0.027**

来源：`/root/autodl-tmp/exp006/pooled_irt_all_scales/arc_challenge/irt_results.json`（2026-05-16 18:59 生成）

关键信息：
- n_models = 13（6 × 1.5B + 7 × 3B）
- model_type = 2pl_gamma
- PPP = 0.027 — **低于 0.05 阈值，表示模型失配**
- MCMC 诊断全部通过（Rhat=1.007, ESS=1670, 无 divergence）
- gamma CI 包含零（ci_excludes_zero = false），contamination signal 不显著

注意：之前 Round 1 报告的 PPP=0.003 来自 `results_pooled_irt_qwen_n24`（N=16，包含更多 3B s123 模型）。当前 J=13 run 的 PPP=0.027 有所改善但仍 < 0.05，处于 misfit 区间。

---
