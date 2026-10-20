# code exp 005 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_005_v2_20260514T152032_result.json`
- **Structured JSON:** [`f58e890bdcf76080ae57.json`](../../sessions/f5/f58e890bdcf76080ae57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 artifact 已更新。

## exp-005 v2 结果汇总

### 温度敏感性对比表（Full-set, Spearman ρ）

| Signal | T=0.7 NER | T=1.0 NER | Δρ NER | Class | T=0.7 RE | T=1.0 RE | Δρ RE | Class |
|---|---|---|---|---|---|---|---|---|
| **soft_jaccard** | 0.391 | 0.378 | +0.014 | MODERATE | 0.060 | 0.069 | -0.010 | ROBUST |
| **fleiss_kappa** | 0.334 | 0.274 | **+0.060** | SENSITIVE | 0.105 | 0.202 | **-0.097** | SENSITIVE |
| **exact_match** | 0.295 | 0.263 | +0.033 | MODERATE | -0.089 | -0.098 | +0.008 | ROBUST |
| **voting_conf** | 0.457 | 0.445 | +0.012 | MODERATE | 0.515 | 0.501 | +0.014 | MODERATE |
| **mean_logprob** | N/A | 0.134 | N/A | N/A | N/A | 0.361 | N/A | N/A |

### 关键发现

1. **FK 温度敏感**：NER Δ=+0.06, RE Δ=-0.097 — 确认之前 exp_005 结论
2. **SJ 近似鲁棒**：RE Δ=-0.010 (ROBUST)，NER Δ=+0.014 (MODERATE, 略超 0.01 阈值)
3. **voting_conf 两端 MODERATE**：Δρ ≈ 0.012-0.014，接近鲁棒边界
4. **EM 混合**：NER MODERATE (Δ=+0.033), RE ROBUST (Δ=+0.008)
5. **所有 bootstrap 95% CI 跨越零**——温度差异无统计学显著性
6. **Conditional filtering >> temperature tuning**：NER 条件过滤改善最大 0.12 vs 温度最大 0.06；RE 条件过滤改善最大 0.54 vs 温度最大 0.10
7. **logprob** 仅有 T=1.0 数据（NER ρ=0.134, RE ρ=0.361），无法做温度对比

---
