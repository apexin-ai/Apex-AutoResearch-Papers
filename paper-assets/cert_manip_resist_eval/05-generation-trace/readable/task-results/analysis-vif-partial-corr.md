# analysis vif partial corr

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vif-partial-corr_20260522T233637_result.json`
- **Structured JSON:** [`32957294faf868ccd3b8.json`](../../sessions/32/32957294faf868ccd3b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json`。

**VIF 结果：**
- Mean = 2.98, Min = 1.23 (mmlu×sycophancy), Max = 7.03 (arc_challenge×score_manipulation)
- 高于预期的 ~1.96，arc_challenge 上几个条件 VIF 较高（score_manipulation 7.03, position_bias 6.53），说明这些条件下 log(K_eff) 和 log(η_max) 共线性较强

**Partial Correlation 结果：**
- η_max → ASR | K_eff: mean r = 0.305, 11/12 conditions 显著 (p < 0.05)
- K_eff → ASR | η_max: mean r = 0.116, 8/12 conditions 显著 (p < 0.05)
- η_max 控制 K_eff 后仍有较强独立解释力；K_eff 控制 η_max 后效应较弱但多数条件仍显著

---
