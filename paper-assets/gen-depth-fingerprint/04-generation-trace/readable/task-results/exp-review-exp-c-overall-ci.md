# exp review exp c overall ci

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-exp-c-overall-ci_20260515T122440_result.json`
- **Structured JSON:** [`4577b694bc8f7f162346.json`](../../sessions/45/4577b694bc8f7f162346.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

**6-gen Overall LOGO**
- F1 = **0.7879**, 95% CI = **[0.783, 0.793]** (n_boot=1000)

**Per-generator F1**: olmo-2-1b(0.786), pythia-1b(0.828), pythia-2.8b(0.817), qwen3-0.6b(0.800), qwen3-1.7b(0.793), qwen3-8b(0.708)

**Spearman ρ (depth 0–4, 6-gen, all p < 1e-10)**

| Feature | ρ |
|---------|------|
| hapax_ratio | **−0.647** |
| ttr | **−0.630** |
| entropy_mean | **−0.610** |
| entropy_min | **−0.406** |
| entropy_std | −0.200 |
| entropy_max | 0.050 |
| tail_decay | −0.040 |

注意：这些 Spearman ρ 用原始 5 级 depth (0–4) 计算，比 plan-014 用 3-class 的值（hapax −0.558, ttr −0.542）更强，因为保留了更细粒度的序数信息。entropy_min (ρ=−0.406) 有中等负相关，entropy_max (ρ=0.050) 接近零。

脚本：`scripts/review_overall_ci.py`，结果：`results/review_overall_ci_results.json`，registry 已更新为 DONE/success。

---
