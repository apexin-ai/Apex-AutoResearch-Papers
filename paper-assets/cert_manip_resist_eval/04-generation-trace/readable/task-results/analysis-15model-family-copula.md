# analysis 15model family copula

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_15model-family-copula_20260522T175131_result.json`
- **Structured JSON:** [`9a55fc9ca05c2d364215.json`](../../sessions/9a/9a55fc9ca05c2d364215.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/family_copula_15model.json`。

---

**Claim 4: Within vs Cross-Family MI**

| Dataset | N_within | N_cross | Mean Within MI | Mean Cross MI | U stat | p-value | Effect Size |
|---|---|---|---|---|---|---|---|
| mmlu | 14 | 91 | 0.2965 | 0.2431 | 735.0 | 1.79e-01 | -0.1538 |
| arc_challenge | 14 | 91 | 0.3761 | 0.3544 | 668.5 | 3.85e-01 | -0.0495 |

**结论**: Within-family MI 略高但 **不显著** (p=0.18/0.39)。主要原因：家族内方差大（如 llama 70b↔8b MI 仅 0.05，claude haiku 与 opus/sonnet 差距也大）。

**Claim 5: Copula GoF (MI_obs / MI_gaussian)**

| Dataset | Mean Ratio | Median Ratio | % Ratio>1 | Max Ratio | Min Ratio |
|---|---|---|---|---|---|
| mmlu | 0.93 | 0.93 | 35.2% | 1.82 | 0.16 |
| arc_challenge | 7.02 | 0.75 | 24.0% | 212.32 | 0.15 |
| arc (robust, \|ρ\|>0.05) | 0.90 | 0.73 | 18.4% | 3.10 | 0.15 |

**结论**: 与之前 6-model 结果 (MMLU=21×, ARC=10×) 差异巨大。15-model 下 Gaussian copula 拟合良好（median ratio ≈ 0.75-0.93）。ARC 的极端 ratio 全部来自 claude-3-haiku（ρ≈0 但 MI>0 的非线性依赖），过滤后 mean=0.90。

---
