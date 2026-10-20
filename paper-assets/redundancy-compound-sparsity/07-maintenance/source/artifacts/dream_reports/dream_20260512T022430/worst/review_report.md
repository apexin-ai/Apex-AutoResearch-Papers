---
dream_id: dream_20260512T022430
tier: worst
overall_score: weak reject
timestamp: 2026-05-12T03:06:41.850975+00:00
---

# Dream Review Report — worst 档

**Paper:** Limits of Cross-Axis Redundancy Signals: A Multi-Model Analysis of KV Similarity and MLP Sparsity Tolerance  
**Dream ID:** 20260512T022430  
**Tier:** worst  
**Overall Score:** Weak Reject  
**Review Mode:** full (2 Reviewers, roundtable)  
**Convergence:** Reached at Round 2 (no Round 3 required)

---

## Headline Assessment

**Weak Reject.** The paper reports a useful negative result (cross-axis KV→MLP coordination does not generalize across models) but the experimental evidence is too thin to support the breadth of the claims. The secondary contribution (CARC-KV) is underdeveloped. Multiple factual inconsistencies between abstract/body undermine credibility.

---

## Reviewer 1：方法 + 实验

### Strengths

1. **Clean pass/fail protocol.** The r>0.35 threshold and Δ_pert metric provide unambiguous verdicts per model. The confound control (same GQA architecture, instruction vs. reasoning training) is the strongest part of the experimental design.
2. **Granular decomposition.** Per-layer (Table 4) and per-head (Table 5) analysis adds depth beyond aggregate statistics, showing signal concentration in layers 12–18 and heads H0–H4 on Llama.
3. **CARC-KV latency numbers are clean.** Table 8 clearly demonstrates O(1) vs O(n) scaling behavior across sequence lengths.

### Weaknesses

1. **Critically small evaluation set (20 problems).** The paper acknowledges ±0.07 binomial 95% CI on accuracy over 20 problems. This means the central downstream result Δ_acc=+0.01 (Table 6) is completely within noise — it cannot distinguish signal from chance. This undermines the entire downstream validation claim. A minimum of 200–500 problems across multiple domains is needed.
2. **Single domain (math reasoning only).** The negative result could be domain-specific. Math reasoning is known to have distinctive token patterns (numbers, operators, step markers). Without testing on summarization, QA, code generation, or general NLP benchmarks (MMLU, HellaSwag), the paper cannot claim the signal is "model-specific rather than architecture-generic" — it might be "domain-specific."
3. **No scale variation.** All five models are 7–8B. Claims about "architectural properties" require evidence across model scales (1B, 7B, 13B, 70B). Larger models may have different redundancy structures.
4. **Missing statistical rigor on Pearson r.** No confidence intervals or p-values reported for any r value. With 20 problems generating a variable number of tokens, the effective sample size and independence assumptions for Pearson r are unclear.
5. **"Sparsity tolerance" definition is vague.** Section 3.3 says "maximum sparsity before output deviation exceeds threshold" but never specifies the threshold, the metric for output deviation (KL divergence? token-match? perplexity?), or the granularity of the sparsity sweep. This is the core dependent variable — its definition is critical.
6. **CARC-KV only evaluated on one model.** Table 7 reports KV eviction accuracy only for Llama-3.1-8B-Instruct. If the paper's own negative result shows that EMA similarity behaves differently across models, why should we trust that CARC-KV's accuracy tradeoff generalizes?
7. **Wall-clock measurements cover overhead only.** Table 8 measures eviction step latency, not total inference time. If eviction overhead is <1% of total per-step latency (which is plausible at 1ms vs ~50ms for a forward pass), the 12.8× speedup on eviction translates to negligible end-to-end improvement.
8. **Two-tier sparsity is a crude allocation.** Table 6 uses a binary 55%/40% split. A smoother allocation function (e.g., sparsity = f(similarity) with continuous mapping) might perform better. Testing only the crudest possible allocation and declaring the signal useless is not fully convincing.
9. **EMA α=0.1 not justified.** No sensitivity analysis on the decay rate. Different models may have different optimal α values; tuning α per model before declaring the signal absent would strengthen the negative result.

### Minor Issues

- Table 3 sparsity sweep only goes 50–70%; lower sparsity (30–40%) results would show the full curve.
- KS statistic mentioned in Section 3.3 metrics but never reported in results.

---

## Reviewer 2：新颖性 + 相关工作

### Strengths

1. **Negative results have publication value.** The community benefits from knowing that EMA-based cross-axis coordination does not generalize, preventing duplicated effort.
2. **The hypothesis is clearly articulated.** Section 2.3 states the causal chain (high KV similarity → low surprisal → high MLP sparsity tolerance) precisely enough to test and falsify.

### Weaknesses

1. **Title and framing overgeneralize.** "Limits of Cross-Axis Redundancy Signals" implies the paper tests the *concept* of cross-axis coordination. In reality, it tests one specific signal (EMA cosine similarity on key vectors) with one specific α. Other cross-axis signals (attention entropy, gradient norms, layer-wise mutual information) are never considered. The paper should be titled "Limits of EMA-Based KV Similarity as a Cross-Axis Signal" or similar.
2. **Abstract claims "MLA proxy" architecture but no MLA model is tested.** The abstract states "five 7–8B parameter models spanning two attention architectures (GQA, MLA proxy)" but Table 1 lists all five models as GQA variants. No model uses Multi-head Latent Attention. This is a factual error that should not appear in a submitted paper.
3. **Internal contradiction on layer counts.** The conclusion states "the signal concentrates in 7 of 32 layers" but Section 4.4 states "9 of 32 layers have r>0.4." Table 4 shows layers 12–18 (7 layers) with "Strong" signal. The inconsistency — 7 vs. 9 — is confusing and suggests careless editing.
4. **CARC-KV novelty is limited.** The method is: maintain an EMA of key vectors, compute cosine similarity, evict tokens above a threshold. This is a standard application of exponential smoothing to a similarity-based filter. The O(1) property is inherent to the EMA formulation, not a design insight. StreamingLLM (also O(1)) uses a different but equally simple mechanism.
5. **Related work gaps.**
   - No discussion of PyramidKV (Cai et al., 2024), which also adaptively allocates KV budget per layer — directly relevant to the per-layer signal decomposition analysis.
   - No mention of ScissorHands (Liu et al., 2024) or GEAR (Kang et al., 2024) for KV cache compression.
   - Kim et al. (2024) and Wang et al. (2024) references are incomplete — no arXiv IDs, just "arXiv preprint, 2024." These may not be verifiable.
6. **Contribution (2) is not a contribution.** "A hypothesis-testing protocol for evaluating cross-axis efficiency signals" is described as: test on ≥3 models, do per-layer decomposition, require downstream improvement. This is standard scientific methodology, not a novel contribution. Listing it inflates the contribution count.
7. **Missing "why EMA" discussion.** The paper never justifies why EMA cosine similarity is the right signal to test. Are there theoretical reasons to expect this to work? If not, finding that an arbitrary signal doesn't generalize is less informative than it appears.

### Story Consistency

- The abstract promises "two attention architectures (GQA, MLA proxy)" — the paper delivers only GQA variants. This is a broken promise that reviewers will catch immediately.
- The paper frames itself as a "multi-model analysis" but tests same-scale, same-domain, same-eval-size. The "multi" aspect is limited to 5 models at one scale.
- Mistral's sliding window attention (SWA) is described as the explanation for its low r, but SWA with window 4096 should still allow the EMA anchor to be representative for tokens within the window. The explanation is hand-wavy.

---

## 交叉分享要点

### R1 → R2 补充

R2 flagged the MLA proxy inconsistency — R1 confirms this is not just a labeling issue but an experimental gap. The paper's claim to test "two attention architectures" is unsupported. Additionally, the 20-problem evaluation that R1 flagged as statistically underpowered compounds R2's concern about overgeneralized framing: the evidence is both too narrow in domain and too small in sample size to support the breadth of claims.

### R2 → R1 补充

R2's identification of incomplete references (Kim et al., Wang et al.) raises a concern for R1's experimental evaluation: if key baselines are incompletely cited, they may also be incompletely compared against. Specifically, PyramidKV's per-layer adaptive allocation is relevant to Table 4's per-layer analysis — if CARC-KV were combined with layer-adaptive budgets, the results might differ.

---

## 收敛判断

Both reviewers converge on **Weak Reject**. Agreement on core issues:
1. Evaluation scale is critically insufficient (20 problems, 1 domain, 1 model scale)
2. MLA proxy claim is a factual error
3. CARC-KV contribution is underdeveloped (single-model evaluation, limited novelty)
4. Framing overgeneralizes from what the experiments actually show

No significant disagreements remain after cross-share. Round 3 not needed.

---

## 综合结论

### 核心问题

| # | Issue | Source | Severity |
|---|-------|--------|----------|
| 1 | Evaluation on only 20 math problems — statistically underpowered, single-domain | R1 | Critical |
| 2 | Abstract claims "MLA proxy" architecture but no MLA model tested — factual error | R2 | Critical |
| 3 | Sparsity tolerance definition incomplete (threshold, metric unspecified) | R1 | Major |
| 4 | CARC-KV only evaluated on Llama — contradicts paper's own multi-model lesson | R1 | Major |
| 5 | Framing overgeneralizes — tests one signal (EMA cosine), claims about "cross-axis signals" broadly | R2 | Major |
| 6 | Internal contradiction: 7 vs. 9 layers in conclusion vs. Section 4.4 | R2 | Minor |
| 7 | Incomplete references (Kim et al., Wang et al. lack arXiv IDs) | R2 | Minor |
| 8 | EMA α=0.1 not tuned per model; no sensitivity analysis | R1 | Minor |

### 跨维度协同结论

The method limitations (R1) and the novelty/framing concerns (R2) compound: the paper tests one specific, unjustified signal on a critically small evaluation set, then frames the negative result as a broad statement about "cross-axis redundancy signals." The CARC-KV contribution, which could partially rescue the paper, is evaluated on only one model — directly contradicting the paper's own methodological lesson that single-model results don't generalize.

### 与 worst 档叙事方向的吻合度

**High alignment.** This paper exhibits the hallmarks of a worst-tier outcome: the central hypothesis fails, the downstream benefit is negligible (Δ_acc=+0.01), and the salvaged contribution (CARC-KV) is insufficiently developed to stand alone. The experimental scope is too narrow to make the negative result itself a strong contribution. The factual errors (MLA proxy, layer count inconsistency) suggest rushed preparation.

### Actionable Recommendations (if revising)

1. Expand evaluation to ≥200 problems across ≥3 domains (math, QA, summarization/code).
2. Remove the "MLA proxy" claim or add an actual MLA-architecture model (e.g., DeepSeek-V2).
3. Define sparsity tolerance precisely with explicit threshold and deviation metric.
4. Evaluate CARC-KV on all 5 models and add end-to-end latency measurements.
5. Narrow the title/framing to match what was actually tested.
6. Add sensitivity analysis on α.
7. Complete all references with verifiable identifiers.
