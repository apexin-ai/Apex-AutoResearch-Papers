# Paper Framing — causal_style_decomp_judge

> Round 5: **3.5 Borderline Conference** (up from 3.0). 冲刺 4.0 中。
> **D059 Framing 重构**: Dual-contribution + agnostic stance + per-axis confound structure co-primary。
> 补充实验进度：B' placebo ✅ + NLI ablation ✅ + cross-axis gradient ✅ + Llama-70B 🔄 downloading。

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Fallback: EMNLP 2026 Findings
- Deadline: **May 25, 2026 AoE**
- Format: Long paper, 8-page main text + unlimited references

## Title
**The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition**

## Core Claims (D059 重构 — Dual-contribution + Agnostic stance)

### C1 (Method): CSD pipeline — black-box per-axis style bias diagnostic
- NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison
- Reframed as "filtering-based confounder control" (not do-operator)
- 3 target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B [pending]) + 1 negative control (Claude Sonnet 4)
- 3 benchmarks (LLMBar, AlpacaEval, MT-Bench) × 3 axes (formality, verbosity, register)

### C2a (Measurement Insight): Likert Blindspot — agnostic about mechanism
- **Core finding**: Pairwise comparison reliably detects style bias (BT 63-77%) that ALL 7 Likert methods miss (d→0)
- **Agnostic framing**: "We identify two candidate interpretations—measurement attenuation and construct divergence—and show that both point to the same operational conclusion: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines."
- **Per-axis claim stratification**:
  - **Verbosity** = "clean style bias" — BT 77%, GEE Orig OR NS. 7-method sensitivity hierarchy confirms 6/6 Likert NS.
  - **Formality** = "conditional style effect" — BT 63-67%, GEE both Style and Orig significant.
  - **Register** = "style-associated preference" — BT 55%, exploratory, originality-dominated.
- **Detection vs. Amplification** (MF1 — 5-layer defense):
  - Layer 1: **NLI gate ablation** — formality NLI-fail BT reverses to 41.7%, proving gate cleans content not amplifies style
  - Layer 2: Claude negative control + cross-axis gradient + debiased prompt partial reduction
  - Layer 3: **Rewriting artifact acknowledged** — placebo quantifies, GEE controls (Verbosity Orig OR NS)
  - Layer 4: Honest framing — "controlled detection, bounded by five independent controls"
  - Layer 5: Llama-70B (pending) — third independent architecture

### C2b (Analytical Insight — CO-PRIMARY): Per-axis confound structure
- **Novel contribution**: GEE conditional decomposition reveals three qualitatively distinct regimes:
  - **Verbosity** = pure style bias (Style OR 11-13, Orig OR NS) → directly interpretable
  - **Formality** = conditional effect (Style + Orig both sig) → requires decomposition for valid inference
  - **Register** = originality-dominated (Orig OR >> Style OR) → style claim not supported after decomposition
- **Prescriptive value**: Confound structure determines which CSD estimates are directly interpretable vs requiring conditional interpretation
- **Replicates across judges**: Pattern consistent for both GPT-4o and Qwen3-32B
- No prior work does per-axis confound decomposition for LLM judge style bias

### C3 (Empirical): Judge variation — CSD diagnoses which judges are susceptible
- GPT-4o + Qwen3-32B show bias; Claude does not; Llama-70B pending
- NOT "architecture-dependent pattern" — reframed as "CSD can diagnose per-judge susceptibility"
- Negative control (Claude) validates CSD does not fabricate false positives

### C4 (Practical): Measurement mode matters more than scale granularity
- Pairwise comparison with NLI gating + per-axis decomposition for style bias audits
- Confound structure determines interpretability — not all axes are equal
- Prompt-level debiasing insufficient (Qwen3 -5.7pp still sig, GPT-4o -0.4pp)
- Pending: 100-point fine-grained Likert ablation (if NS → scale type < measurement mode)

## Evidence Matrix (Current)

### Primary (LLMBar)
| | GPT-4o BT / Likert | Qwen3-32B BT / Likert | Claude BT / Likert | Llama-70B (pending) |
|---|-----|------|------|------|
| **Formality** | 63.0% p<.001 / p=.332 | 66.5% p<.0001 / p=.908 | 56.2% p=.091 / p=.721 | TBD |
| **Verbosity** | 76.0% p=.0001 / p=.403 | 77.3% p<.0001 / p=.179 | 54.1% p=.284 / p=.743 | TBD |
| **Register** | 57.0% p=.04 / p=.785 | 55.3% p=.076 / p=.505 | — | TBD |

### Cross-Benchmark (Formality)
| Benchmark | GPT-4o BT | Qwen3-32B BT | Blindspot? |
|-----------|-----------|-------------|------------|
| LLMBar | 63.0% | 66.5% | Yes |
| AlpacaEval | 72.7% | 65.7% | Yes |
| MT-Bench | 69.2% | 71.2% | No (d≈0.15) |

### GEE Decomposition (LLMBar)
| Axis | GPT-4o Style OR | GPT-4o Orig OR | Qwen3 Style OR | Qwen3 Orig OR |
|------|:---:|:---:|:---:|:---:|
| Verbosity | **11.34** p<.0001 | 0.45 NS | **13.10** p<.0001 | 0.49 NS |
| Formality | 2.58 p=.002 | 2.32 p=.006 | 4.20 p=.0002 | 4.70 p<.0001 |
| Register | 1.88 p=.029 | 2.21 p=.006 | 1.91 p=.046 | 5.72 p<.0001 |

## Key Robustness Results
- **Bootstrap Attenuation Curve** (NEW — smoking gun): Formality×Qwen3 d_median flat at -0.017 across n=50→355, CI always contains 0. Not power gap (d would be constant non-zero), IS measurement attenuation (d≈0 regardless of n). Verbosity d≈0.15-0.19, stable, CI contains 0. Attenuation ratio >10× vs BT.
- **BT GoF**: formality χ² p=0.198, verbosity p=0.905 (model fits well)
- **Stratified BT**: Stable across originality subgroups
- **Originality-minimal subset**: |Likert Δ|=0 pairs → style Δ < 2pp, CI contains 0
- **Claude TOST**: Δ=15pp equivalence passes both axes
- **NLI full validation**: 200-pair GPT-4o (formality 92.1%, verbosity 82.6%)
- **Rewriter independence**: GPT-4o formality BT 64.4% vs Qwen3 66.5% (Δ=−2.1pp)
- **Sensitivity hierarchy**: 7 Likert methods × 2 axes (formality + verbosity) all NS, only BT detects
- **Length robustness**: Verbosity Style OR survives all length controls (<2% change)
- **NLI ablation** (NEW): Formality NLI-fail BT 41.7% (reversal → prefer casual); Verbosity NLI-fail 75% (stable)
- **Cross-axis gradient** (NEW): NLI rejection rate vs BT positive correlation across 3 axes
- **Rewriting artifact control** (NEW): Placebo orig-vs-DR quantifies artifact; GEE Orig OR captures it. Verbosity Orig OR NS = style effect uncontaminated.

## Completed Supplementary Experiments

### B': Double-Rewrite Placebo BT ✅ (hypothesis falsified — artifact exists)
- Result (BT re-analysis, choix.ilsr_pairwise + ALL pairs + bootstrap 10000):
  - GPT-4o: Formality P(orig)=0.418 p=.037, Verbosity P(orig)=0.167 p<.0001
  - Qwen3-32B: Formality P(orig)=0.377 p=.0006, Verbosity P(orig)=0.082 p<.0001
  - → Judges prefer DR (polished text) over original in all conditions
- Interpretation: Rewriting artifact is real (judges prefer LLM-polished text). This does NOT invalidate style bias conclusions.
- Paper role: Validates GEE decomposition as necessary for correct inference. Honest acknowledgment of artifact.
- GEE controls for it: Verbosity Orig OR=0.49 NS → style effect uncontaminated by artifact.

### B: NLI Gate Ablation ✅ (strong new evidence)
- Formality: NLI-fail BT reverses to 41.7% (prefer casual) → NLI gate cleans content noise, not amplifies style
- Verbosity: NLI-fail BT stable at 75% → style effect too strong to be affected by content noise
- Paper role: Strongest anti-amplification evidence. If pairwise amplified bias, removing the gate should amplify further — instead it reverses.

### C: Cross-Axis Gradient ✅ (qualitative support)
- NLI rejection rate: Register 6% → Formality 12% → Verbosity 14%
- BT: Register 55.3% → Formality 66.5% → Verbosity 77.3%
- Positive correlation: higher manipulation invasiveness → higher BT → inconsistent with uniform amplification
- Paper role: Qualitative argument in §5.2, 3 points only.

## Pending Experiments

### A: Llama-3.3-70B Third Target Judge 🔄 (downloading, ~4h remaining)
- Purpose: 2→3 target judges = generalizability quality jump
- Coverage: verbosity + formality on LLMBar
- Impact: Directly addresses SF3 + strengthens MF1 defense
- Three independent architectures: GPT-4o (proprietary US) + Qwen3-32B (open CN) + Llama (open US)

## Novelty Positioning (D059 重构)
**Dual contribution**:
1. CSD framework: first to combine NLI-gated content control + per-axis decomposition + position-controlled pairwise comparison for LLM judge style bias
2. Per-axis confound structure: first demonstration that different style axes have qualitatively different confound regimes (pure / conditional / originality-dominated) — prescriptive for practitioners

**Honest acknowledgment**:
- Likert < pairwise sensitivity is predicted by Thurstone 1927 / Stevens 1946 — we provide empirical quantification in the LLM judge setting, NOT a new theoretical insight
- Per-axis confound structure IS novel — no prior work does per-axis decomposition
- Jeong et al. 2025 (Comparative Trap) discusses amplification; we provide bounded detection with 5 independent controls

## Story Spine (D059 重构)

### Problem
LLM-as-judge is core infrastructure for NLP evaluation and alignment. Style bias is the dominant bias (SOS-Bench R=0.999), but: (1) standard Likert scoring systematically misses it, and (2) no prior work characterizes the per-axis confound structure that determines when bias estimates are reliable.

### Gap
Prior work addresses parts: RATE (Likert-based ATE), CASSE (multi-dimensional but correlational), LC-AlpacaEval (single dimension), Comparative Trap (amplification in pairwise). Missing: (a) content-controlled per-axis decomposition, (b) systematic comparison of measurement modes on identical data, (c) characterization of confound structure across style axes.

### Our Contribution (Dual)
1. **Likert Blindspot** (C2a): We identify two candidate interpretations—measurement attenuation and construct divergence—and show that both point to the same operational conclusion: Likert-only audits miss style preferences that affect pairwise-based alignment. Agnostic about mechanism; the practical finding is robust.
2. **Per-axis confound structure** (C2b): GEE decomposition reveals three regimes — verbosity (pure, directly interpretable), formality (conditional, requires decomposition), register (originality-dominated, style claim unsupported). This structure determines which bias estimates are actionable.

### Detection vs. Amplification
Five independent controls bound the risk of format-level amplification:
1. NLI ablation reverses formality BT → gate cleans content, not amplifies
2. Claude negative control → same format, no bias
3. Cross-axis gradient → inconsistent with uniform amplification
4. Placebo quantifies rewriting artifact → GEE controls for it
5. Llama-70B (pending) → third independent architecture

## Bibliography
52+ verified references including Jeong 2025, Stureborg 2024, Park 2024, Chen 2024, Saito 2023.

## Venue Fit
Round 5: 3.5. Dream: 3.0 (floor — dream papers weaker). Target: 4.0.
**Path to 4.0 (D059)**:
1. Framing 重构: dual contribution + agnostic stance → 消除 "predictable" objection
2. Per-axis confound structure as co-primary → 真正 novel 贡献可见度提升
3. 5-layer MF1 defense → Comparative Trap 充分回应
4. Bootstrap attenuation curve + 100-point Likert → 新实验证据
5. Llama-70B → 3 target judges
Novelty ceiling (Blindspot as domain transfer) mitigated by dual-contribution positioning. Statistical methodology depth + honest artifact handling + per-axis novelty are primary strengths.
