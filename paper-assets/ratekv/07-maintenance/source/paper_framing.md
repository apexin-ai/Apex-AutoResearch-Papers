# Paper Framing — ratekv

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)
- Track: Efficient Methods for NLP

## bf16 Consistency Resolution (2026-05-14)

**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。

**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。

| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |
|------|---------------------|----------------------|-----------|
| Baseline | **9.8106** | 8.819 | 9.81 |
| Uniform 4-bit | **15.4454** | — | 15.45 |
| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |
| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |

## Core Insight

Per-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16} has an unreported universal failure mode: 2-bit quantization distortions compound non-additively through the residual stream, causing ALL tested unconstrained solvers (greedy, MCKP) to systematically over-allocate 2-bit heads and underperform uniform 4-bit across 9/9 architectures (1.07×–3.31× baseline). A cardinality constraint (≤k heads at 2-bit) universally prevents this over-allocation, and furthermore reduces the feasible set to where solver choice becomes irrelevant (greedy = MCKP, Δ=0.0000). Under moderate compression (4×), only 1/9 architectures benefits from non-uniform allocation over uniform 4-bit — providing the first empirical evidence that the implicit assumption "non-uniform is always better than uniform" is wrong in KV cache quantization. The core contribution is the compounding effect discovery + universal constraint fix, not the allocation algorithm.

## Core Claims (3 条)

1. **2-bit compounding is a universal failure mode for unconstrained per-head allocation**: On hardware-aligned non-consecutive bit-widths {2,4,8,16}, per-head independent profiling distortions compound non-additively when multiple heads are simultaneously assigned 2-bit quantization. This causes ALL tested unconstrained solvers to over-allocate 2-bit heads and underperform uniform 4-bit across 9/9 diverse architectures (Qwen 3.31×, Gemma-2 1.47×, Yi 1.08×, Llama 1.07×, Mistral 1.08×, CodeLlama, Pythia, Qwen-14B, Phi-3-medium). Quantitative evidence of non-additivity: per-head profiling predicts joint PPL ≈11 but actual joint 2-bit PPL is 32–37 (3× prediction error). This is the first systematic characterization of compounding effects in per-head KV cache quantization. Long-context amplifies the failure: at 8K tokens, uniform 4-bit degrades 11.15× baseline while constrained MCKP degrades only 1.23× — a 9× gap in degradation rate.

2. **A cardinality constraint is the universal fix — and makes solver choice irrelevant**: A simple cardinality constraint (max_2bit ≤ k) is sufficient to prevent compounding across ALL tested architectures. Three universally beneficial properties: (a) prevents catastrophic over-allocation on sensitive architectures (Qwen: 32.45 → 10.91), (b) prevents moderate over-allocation on flat architectures (Gemma-2: 8.85 → 6.17, reducing 2-bit heads from 106 to 8), (c) reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce IDENTICAL bit allocations and PPL (Δ=0.0000). The constraint is parameterizable via small-scale compounding test (k≤8 universally safe: <2.5% degradation across all architectures). Practical implication: practitioners need only add one integer parameter to existing pipelines.

3. **Non-uniform allocation benefit is rare — most models should use uniform 4-bit**: Under moderate compression (4×), only 1/9 tested architectures (Qwen2.5-7B, "spread" sensitivity pattern) benefits from non-uniform allocation (+27.3% PPL, +1.9pp downstream avg). The remaining 8/9 show no benefit or minor degradation (<1pp avg downstream). A 2-metric empirical diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly classifies all 9 tested models (9/9 accuracy), providing practitioners a simple check: if the diagnostic says "no" — skip profiling and use uniform 4-bit with zero quality loss. This is the first systematic study of *when* non-uniform KV cache quantization is beneficial, correcting the implicit assumption that it always helps.

## Story Spine

- **Problem**: Per-head mixed-precision KV cache quantization promises better quality-compression tradeoffs than uniform bit-width. But on hardware-aligned non-consecutive bit-widths {2,4,8,16}, we discover that existing allocation algorithms (greedy, MCKP) systematically FAIL — producing worse results than naive uniform 4-bit across ALL tested architectures. The failure mode is unreported: 2-bit quantization distortions compound non-additively, and solvers consistently over-allocate 2-bit heads. Meanwhile, the field implicitly assumes non-uniform allocation always helps, but no systematic study has tested this across architectures.

- **Existing approaches & gaps**: RateQuant provides R-D optimal per-head allocation via continuous closed-form and discrete greedy (optimal on consecutive integers {2,...,6}). KIVI and ARKV apply uniform or heuristic mixed-precision. However, on hardware-aligned {2,4,8,16}: (a) RateQuant's greedy produces PPL 32.45 vs optimal ~10.91 — polymatroid optimality breaks, (b) unconstrained MCKP fares even worse (PPL 36.92) due to compounding, (c) NO prior work addresses *when* non-uniform allocation is actually beneficial vs when uniform suffices.

- **Our framing**: We present three contributions: (1) the first characterization of 2-bit compounding effects in per-head KV cache quantization — showing that profiling non-additivity causes ALL unconstrained solvers to fail on {2,4,8,16} across 9/9 architectures; (2) a simple universal fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding, makes solver choice irrelevant (greedy=MCKP, Δ=0.0000), and is safely parameterizable (k≤8 universally safe); (3) the first systematic study of *when* non-uniform allocation helps — answer: rarely (1/9 architectures at moderate compression), with a 2-metric diagnostic (9/9 correct) that tells practitioners whether to invest in profiling or just use uniform 4-bit.

- **Headline result template**: "We show that per-head KV cache quantization on hardware-aligned bit-widths has a universal failure mode: 2-bit distortions compound non-additively, causing ALL unconstrained solvers to underperform uniform 4-bit across 9 architectures. A cardinality constraint (≤k heads at 2-bit) universally fixes this, making solver choice irrelevant (greedy=MCKP, Δ=0.0000). Surprisingly, under moderate compression, only 1/9 architectures benefits from non-uniform allocation at all — most models should simply use uniform 4-bit. A 2-metric diagnostic (9/9 accuracy) provides practitioners a simple check to determine when profiling is worthwhile. At long context (8K tokens), the constraint reduces degradation from 11.15× to 1.23× baseline, demonstrating critical deployment value."

## "When Does Non-Uniform Allocation Help?" — Analysis Chapter

Five case studies representing the full spectrum of heterogeneity:

| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |
|------|-------|-----|--------------|------------------------------|---------------|
| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; "spread" pattern (L0 cluster, 4 heads, 26× dominance) |
| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; "spike" pattern (L4H3 single outlier, 64% of total delta) |
| **Marginal** | Llama-3.1-8B | 4:1 | 0.57 (hires) | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |
| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |
| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |

**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.

**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).

**Joint diagnostic** (n=9, 9/9 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike), CodeLlama (0.80, t₁/t₅=0.81 — spike), and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.

## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)

| Method | PPL | Bit Distribution | Budget |
|--------|-----|-------------------|--------|
| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |
| MCKP unconstrained | 36.92 | — | 0.25 |
| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |

Key takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.

## Cross-Architecture Evidence Summary

| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |
|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|
| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |
| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |
| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |
| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |
| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |

**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:
- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding
- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta
- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)
- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads

**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):

Three-tier labeling (NOT binary catastrophe/benign):
- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding
- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions
- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)

Reviewer-suggested paragraph for paper (1 段, 3-4 句):
"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape."

This **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.

⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.

**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 9/9 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.

**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.

### Mistral k Ablation (256 KV heads, budget=0.25)

PPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).

| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |
|---|-----|-------|-------|-------|--------|-----|
| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |
| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |
| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |
| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |
| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |
| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |

Contrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.

### Llama k Ablation (256 KV heads, budget=0.25)

All k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).

### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)

**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅

| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |
|------|---------------|------------|---|---------------|
| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |
| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |
| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |
| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |
| **Avg recovery** | — | — | **72.8%** | — |

**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)

| Task | Uniform 4-bit | MCKP (k=8) | Δ |
|------|---------------|------------|---|
| arc_easy | 0.7946 | 0.7854 | -0.92pp |
| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |
| hellaswag | 0.5857 | 0.5797 | -0.60pp |
| piqa | 0.7927 | 0.7894 | -0.33pp |
| winogrande | 0.7174 | 0.7301 | +1.27pp |
| **Average** | **0.6822** | **0.6745** | **-0.77pp** |

**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)

| Task | Uniform 4-bit | MCKP (k=8) | Δ |
|------|---------------|------------|---|
| arc_easy | 0.8173 | 0.8039 | -1.34pp |
| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |
| hellaswag | 0.6026 | 0.6012 | -0.14pp |
| piqa | 0.7867 | 0.7802 | -0.65pp |
| winogrande | 0.7253 | 0.7238 | -0.15pp |
| **Average** | **0.6915** | **0.6816** | **-0.99pp** |

**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)

| Task | Uniform 4-bit | MCKP (k=4) | Δ |
|------|---------------|------------|---|
| arc_easy | — | — | — |
| arc_challenge | — | — | — |
| hellaswag | — | — | — |
| piqa | — | — | — |
| winogrande | — | — | — |
| **Average** | **0.6894** | **0.6846** | **-0.48pp** |

**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)

| Task | Uniform 4-bit | MCKP | Δ |
|------|---------------|------|---|
| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |

**Downstream summary (Reviewer-verified framing)**:
- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**
- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)
- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)
- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise
- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)
- **Paper must**: (a) report full per-task tables, not just averages, (b) use "shows minor degradation" NOT "preserves accuracy" — the latter has spin, (c) note arc_challenge as worst-case explicitly
- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance
- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论："ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate."
- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞："Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge)."

## Allocation Baseline Evidence (plan_015, mckp_reeval)

All numbers from unified bf16 eval pipeline, budget=0.25.

| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |
|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|
| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |
| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |
| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |

**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.

**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.

## Differentiation from RateQuant

| Aspect | RateQuant | Ours |
|--------|-----------|------|
| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |
| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |
| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |
| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |
| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |
| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |
| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |

## Venue Fit Risks

- **"The constraint is just a heuristic, not a real contribution"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.
- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.
- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive "higher GQA = more benefit" hypothesis and shows our diagnostic is needed.
- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 9/9 correct). The "spike vs spread" analysis explains WHY same-GQA models differ.
- **Statistical power**: n=9 models is directional evidence, not statistical claim. Do NOT claim "significant correlation" — use "consistent pattern across 9 architectures" or "9/9 correctly classified by the 0.50 threshold."
- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.

## Anticipated Reviewer Concerns

1. **"The cardinality constraint is trivial — just cap the extreme allocations"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.
2. **"This is just RateQuant with a constraint added"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.
3. **"The method only works on Qwen — isn't this a Qwen paper?"** → We systematically test 9 architectures spanning GQA 1:1 (MHA) to 8:1 and honestly report negative results (Gemma-2, Mistral, etc.). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.
4. **"How does this work at different compression ratios?"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.
5. **"n=3/4/5 models is not enough for the heterogeneity claim"** → Acknowledged as limitation. We present directional evidence across 9 architectures spanning GQA 1:1 (MHA) to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.
6. **"RateQuant does K/V asymmetric allocation, do you?"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.
7. **"Where are the downstream task results?"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use "shows minor degradation" not "preserves accuracy".
8. **"The profiler distortion=0.0 on Mistral suggests the profiling method is broken"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.
9. **"If solver doesn't matter, why present MCKP at all?"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.
