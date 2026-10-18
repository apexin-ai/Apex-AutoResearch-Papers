# analysis claim6 panel design 15model

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_claim6-panel-design-15model_20260522T182255_result.json`
- **Structured JSON:** [`d822d0d943f26d3161b4.json`](../../sessions/d8/d822d0d943f26d3161b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰：

**min(η_max) 在所有 12/12 conditions 上都 dominate max(K_eff)**，且对所有 K 值（10, 20, 50）稳健。

| 指标 | 值 |
|---|---|
| min_η_max dominates | **12/12** |
| max_K_eff dominates | 0/12 |
| tie | 0/12 |

关键发现：
- **零失效条件** — min_eta_max 在每个 condition 下都产生更低的 panel ASR
- η_max advantage 范围从 +0.038（arc_challenge×sycophancy）到 +0.511（arc_challenge×prompt_injection）
- prompt_injection 和 position_bias 条件下优势最大
- K 值稳健性完美：K=10/20/50 结果一致
- 相比 6-model 时 5/6 dominance，15-model 扩展到 12/12 完全 dominance

JSON 已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/claim6_panel_design_15model.json`。

---
