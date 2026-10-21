# analysis k7 wild bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k7-wild-bootstrap_20260523T010244_result.json`
- **Structured JSON:** [`bdd4b5ce43224c8f6ce9.json`](../../sessions/bd/bdd4b5ce43224c8f6ce9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

K=7 Wild Cluster Bootstrap (B=9999) 完成。

## 结果：K_eff **5/12**, η_max **0/12**

## Cross-K Comparison

| K | Bootstrap η_max | Bootstrap K_eff | 
|---|---|---|
| K=3 | 5/12 | 1/12 |
| K=5 | 0/12 | 7/12 |
| K=7 | **0/12** | **5/12** |

**关键发现**：

1. **K_eff 5/12** (全部正方向)：比 K=5 的 7/12 略降，但仍是主导力量。FDR 显著的 5 条全部来自 mmlu(4) + arc_score_manip(1)。
2. **η_max 0/12**：与 K=5 一致（0/12），确认 diversity-vulnerability transition——K≥5 时 η_max 不再是显著预测因子。
3. **Validation passed**：arc×sycophancy K_eff β = -0.176，与 K=3 (-0.192) 方向一致。
4. 几个 arc 条件（verbosity_bias, position_bias）K_eff max-p 接近显著边界（0.044, 0.029）但 FDR 后不过阈值，7-position max-p 更保守。

**Cross-K 叙事**：K=3→K=5→K=7 transition 中，η_max 从显著(5/12)→不显著(0/12)→不显著(0/12)，K_eff 从弱(1/12)→强(7/12)→中等(5/12)。支持 diversity-dominance threshold 在 K≈5 附近的结论。

---
