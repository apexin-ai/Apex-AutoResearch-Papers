# code plan 004 5model analysis

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_004_5model_analysis_20260520T191544_result.json`
- **Structured JSON:** [`3f3e3d002639a44e85f1.json`](../../sessions/3f/3f3e3d002639a44e85f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 3 全部完成。以下是 5 模型统一分析的 C1-C4 结果摘要。

---

## 5 模型统一分析结果 (N=2,997)

### C1: Binary Effect (歧义 vs 非歧义)

| Model | Amb Rate | Unamb Rate | Δpp | McNemar p | Matched OR |
|-------|---------|------------|-----|-----------|------------|
| claude-sonnet-4-6 | 30.3% | 4.7% | +25.7% | <0.0001 | 81:4 |
| gpt-5.4 | 41.0% | 2.7% | +38.3% | <0.0001 | 118:3 |
| gpt-4.1 | 40.7% | 6.0% | +34.7% | <0.0001 | 106:2 |
| qwen3-235b | 43.1% | 10.7% | +32.4% | <0.0001 | 109:14 |
| deepseek-v3 | 49.7% | 10.7% | +39.0% | <0.0001 | 130:13 |
| **Pooled** | **41.0%** | **6.9%** | **+34.0%** | **<0.0001** | **OR=15.1 [10.8, 21.2]** |

所有 5 个模型的 McNemar p 均 <0.0001，效果一致且强烈。Bootstrap 95% CI for pooled Δ: [31.2%, 36.9%]。

### C2: Type Hierarchy (歧义条件下 6 类违规率差异)

Pooled 6-way χ²=28.02, p<0.0001, Cramér's V=0.137

| Type | Violation Rate (Amb) |
|------|---------------------|
| incompleteness | **53.6%** |
| lexical | 42.8% |
| authorization_scope | 41.6% |
| scopal | 39.4% |
| conditional_precedence | 36.8% |
| coreferential | **31.6%** |

**incompleteness 显著高于其他类型**（vs coreferential: Δ=22pp, CI不含0）。各模型内部 χ² 结果：
- claude-sonnet-4-6: p=0.003, V=0.244
- gpt-5.4: p=0.0003, V=0.280
- qwen3-235b: p=0.007, V=0.230
- gpt-4.1: p=0.078 (marginal)
- deepseek-v3: p=0.277 (n.s.) — deepseek 各类型违规率较均匀(38%-60%)

### C3: Layer Effect (Specification vs Linguistic)

| Layer | Types | Rate | N |
|-------|-------|------|---|
| Specification | auth_scope, cond_prec, incompleteness | **44.0%** | 750 |
| Linguistic | coreferential, lexical, scopal | **37.9%** | 749 |

Δ=6.1pp, χ²=5.73, p=0.017, OR=1.29 [1.05, 1.58], Bootstrap CI=[1.1%, 11.0%]

Specification-layer 歧义导致更高违规率，效果显著但 effect size 较小 (V=0.062)。

### C4: Model × Type Interaction

Overall model effect: χ²=31.0, p<0.0001, V=0.102
Ambiguous-only model effect: χ²=24.0, p<0.0001

**模型间违规率排序（整体）**：
1. claude-sonnet-4-6: 17.5% (最低)
2. gpt-5.4: 21.8%
3. gpt-4.1: 23.3%
4. qwen3-235b: 27.0%
5. deepseek-v3: 30.2% (最高)

**模型间 pairwise 差异**（Bootstrap CI）：
- claude vs deepseek: Δ=12.7pp, CI=[8.2%, 17.7%] — 显著
- claude vs qwen: Δ=9.5pp, CI=[4.6%, 14.0%] — 显著
- deepseek vs gpt-5.4: Δ=8.3pp, CI=[3.5%, 13.3%] — 显著
- deepseek vs gpt-4.1: Δ=6.8pp, CI=[1.8%, 11.8%] — 显著
- gpt-4.1 vs gpt-5.4: Δ=1.5pp, CI含0 — 不显著
- deepseek vs qwen: Δ=3.2pp, CI含0 — 不显著

**Type ranking 差异**：模型对类型敏感度的排序不一致。incompleteness 在 4/5 模型中排第1-2，但 authorization_scope 在 gpt-5.4/deepseek-v3 中排第1，在 claude/qwen 中排最后。这表明存在 model × type 交互效应。

---

所有分析输出已写入 `full_study/analysis/`，包含 full_statistics.json, aggregated_rates.csv, mcnemar_matched.json, bootstrap_ci.json, layer_effect_test.json 等 10 个文件。

---
