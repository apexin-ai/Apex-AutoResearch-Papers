# Paper Framing — causal_style_decomp_judge

> Round 5: **3.5 Borderline Conference** (up from 3.0). 冲刺 4.0 中。
> **D059 Framing 重构**: Dual-contribution + agnostic stance + per-axis confound structure co-primary。
> 全部补充实验完成：B' placebo ✅ + NLI ablation ✅ + cross-axis gradient ✅ + Llama-70B ✅ + bootstrap attenuation ✅ + 100-point Likert ✅ + NLI sweep ✅ + debiased verbosity ✅ + Gemini-2.5-Flash 4th judge ✅。

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
- 4 target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash ✅) + 1 negative control (Claude Sonnet 4)
- 3 benchmarks (LLMBar, AlpacaEval, MT-Bench) × 3 axes (formality, verbosity, register)

### C2a (Measurement Insight): Likert Blindspot — agnostic about mechanism
- **Core finding**: Pairwise comparison reliably detects style bias (BT 57-77%) across 4 target judges that ALL 7 Likert methods miss (d→0)
- **Agnostic framing**: "We identify two candidate interpretations—measurement attenuation and construct divergence—and show that both point to the same operational conclusion: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines."
- **Per-axis claim stratification**:
  - **Verbosity** = "clean style bias" — BT 77%, GEE Orig OR NS. 7-method sensitivity hierarchy confirms 6/6 Likert NS.
  - **Formality** = "conditional style effect" — BT 63-67%, GEE both Style and Orig significant.
  - **Register** = "style-associated preference" — BT 55-63.5%, judge-dependent regime (Llama Mixed, Qwen3 Orig-Dominated, GPT-4o Mixed).
- **Detection vs. Amplification** (MF1 — 5-layer defense):
  - Layer 1: **NLI gate ablation** — formality NLI-fail BT reverses to 41.7%, proving gate cleans content not amplifies style
  - Layer 2: Claude negative control + cross-axis gradient + debiased prompt partial reduction
  - Layer 3: **Rewriting artifact acknowledged** — placebo quantifies, GEE controls (Verbosity Orig OR NS)
  - Layer 4: Honest framing — "controlled detection, bounded by five independent controls"
  - Layer 5: Cross-architecture replication ✅ — Llama-70B (Form 69.5%, Verb 73.5%) + Gemini-2.5-Flash confirmatory (Verb 70.8%, Form 57.4%) → 4 independent companies

### C2b (Analytical Insight — CO-PRIMARY): Per-axis confound structure
- **Novel contribution**: GEE conditional decomposition reveals three qualitatively distinct regimes:
  - **Verbosity** = style-dominated (Style OR 8-13, Orig OR ≤0.49) → directly interpretable, consistent across all 4 target judges
  - **Formality** = conditional/mixed (Style + Orig both sig) in GPT-4o/Qwen3/Llama; originality-dominated in Gemini (Style OR=1.64 NS, Orig OR=2.51 p=.002) → axis × judge interaction
  - **Register** = judge-dependent (Qwen3 Orig-Dominated OR=5.72; GPT-4o/Llama Mixed OR≈2-3) → most variable axis, reinforces need for per-judge decomposition
- **Prescriptive value**: Confound structure determines which CSD estimates are directly interpretable vs requiring conditional interpretation. Register heterogeneity + Gemini formality divergence further motivate per-judge analysis.
- **Replicates across judges**: Verbosity regime consistent across all 4 target judges; formality regime varies (3 conditional + 1 originality-dominated); register varies → axis × judge interaction
- No prior work does per-axis confound decomposition for LLM judge style bias

### C3 (Empirical): Judge variation — CSD diagnoses which judges are susceptible
- GPT-4o + Qwen3-32B + Llama-70B + Gemini-2.5-Flash all show bias; Claude does not
- NOT "architecture-dependent pattern" — reframed as "CSD can diagnose per-judge susceptibility"
- Negative control (Claude) validates CSD does not fabricate false positives

### C4 (Practical): Measurement mode matters more than scale granularity
- Pairwise comparison with NLI gating + per-axis decomposition for style bias audits
- Confound structure determines interpretability — not all axes are equal
- Prompt-level debiasing insufficient — 5/5 judge×axis combos still significant (model-independent):
  - Verbosity GPT-4o: -13.1pp (76→62.9%) — strongest reduction, 50.4% eliminated
  - Verbosity Llama-70B: -6.6pp (73.5→66.9%) — 28.1% reduced
  - Formality Llama-70B: -5.2pp (69.5→64.3%) — 26.7% reduced
  - Formality Qwen3: -5.7pp (66.5→60.8%) — 34.5% reduced
  - Formality GPT-4o: -0.4pp (63→62.6%) — nearly zero effect, 3.1% reduced
  - → Axis-specific depth + model-independent: debiasing never eliminates bias, all p<0.0001
- **100-point fine-grained Likert** ✅: Both axes NS (formality p=0.725, verbosity p=0.117), 52-66% tie rate even on 101-value scale → Blindspot is absolute-vs-relative paradigm difference, not scale resolution artifact

## Evidence Matrix (Current)

### Primary (LLMBar)
| | GPT-4o BT / Likert | Qwen3-32B BT / Likert | Llama-70B BT / Likert | Gemini-2.5-Flash BT / Likert | Claude BT / Likert |
|---|-----|------|------|------|------|
| **Formality** | 63.0% p<.001 / p=.332 | 66.5% p<.0001 / p=.908 | 69.5% p=.0001 / p=.846 | 57.4% p=.031 / d=−0.082 NS | 56.2% p=.091 / p=.721 |
| **Verbosity** | 76.0% p=.0001 / p=.403 | 77.3% p<.0001 / p=.179 | 73.5% p=.0001 / p=.752 | 70.8% p<.0001 / d=0.051 NS | 54.1% p=.284 / p=.743 |
| **Register** | 57.0% p=.04 / p=.785 | 55.3% p=.076 / p=.505 | 63.5% p=.0014 / p=.690 | — | — |

### Cross-Benchmark (Formality)
| Benchmark | GPT-4o BT | Qwen3-32B BT | Blindspot? |
|-----------|-----------|-------------|------------|
| LLMBar | 63.0% | 66.5% | Yes |
| AlpacaEval | 72.7% | 65.7% | Yes |
| MT-Bench | 69.2% | 71.2% | No (d≈0.15) |

### Cross-Benchmark (Verbosity)
| Benchmark | Qwen3-32B BT | Likert d | Blindspot? |
|-----------|-------------|----------|------------|
| LLMBar | 77.3% | 0.08 | Yes |
| AlpacaEval | 84.1% | 0.41 | No (effect too strong) |
→ Effect-size gradient: Blindspot appears at moderate effects, disappears when bias is overwhelming

### GEE Decomposition (LLMBar)
| Axis | GPT-4o Style OR | GPT-4o Orig OR | Qwen3 Style OR | Qwen3 Orig OR | Llama Style OR | Llama Orig OR | Gemini Style OR | Gemini Orig OR |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Verbosity | **11.34** p<.0001 | 0.45 NS | **13.10** p<.0001 | 0.49 NS | **8.21** p<.0001 | 0.38 p=.020 | **8.98** p<.0001 | 0.46 NS |
| Formality | 2.58 p=.002 | 2.32 p=.006 | 4.20 p=.0002 | 4.70 p<.0001 | 4.81 p<.0001 | 3.12 p=.0007 | 1.64 NS | 2.51 p=.002 |
| Register | 1.88 p=.029 | 2.21 p=.006 | 1.91 p=.046 | 5.72 p<.0001 | **3.33** p=.0003 | **3.07** p=.0008 | — | — |

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
- **100-point Likert** (NEW): Formality p=0.725, Verbosity p=0.117, both NS. 52-66% tie rate on 101-value scale. Proves Blindspot is absolute-vs-relative paradigm shift, not scale granularity artifact.
- **NLI threshold sweep** (NEW): 44/44 (judge × axis × threshold) points significant. BT stable ≤3pp across τ=0.50→0.98. Rules out threshold selection bias.
- **Power analysis** (NEW): Likert requires 3.9x–206x current n to detect BT-equivalent effects (336–27,159 pairs). Formality worst: d≈0.02 → n>18k. Converges with bootstrap attenuation: structural limitation, not power gap.
- **GEE S×O interaction** (NEW): 0/8 cells significant (all p>0.13), 6/8 regime classifications stable. Additive model (Eq. 1) justified.

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

### D: Gemini-2.5-Flash Confirmatory 4th Judge ✅ (D062)
- Verbosity: BT 70.8% [63.7, 77.2] p<0.0001; Likert d=0.051 NS; GEE Style OR=8.98 p<0.0001, Orig OR=0.46 p=0.061 NS → pure style, consistent with other 3 judges
- Formality: BT 57.4% [50.0, 64.2] p=0.031; Likert d=−0.082 NS; GEE Style OR=1.64 NS, Orig OR=2.51 p=0.002 → originality-dominated (differs from other 3 judges)
- Confirmatory replication outside Holm-Bonferroni family (Method A). Not in primary 6-test family.
- Paper role: 4th independent architecture (Google) confirms Blindspot universality. Formality divergence enriches per-axis confound taxonomy.

## Pending Experiments

(None — all experiments complete)

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
5. Gemini-2.5-Flash ✅ confirmatory → 4 independent architectures (OpenAI + Alibaba + Meta + Google), Verb 70.8%, Form 57.4%

## Bibliography
52+ verified references including Jeong 2025, Stureborg 2024, Park 2024, Chen 2024, Saito 2023.

## Venue Fit
Round 5: 3.5. Dream: 3.0 (floor — dream papers weaker). Target: 4.0.
**Path to 4.0 (D059)**:
1. Framing 重构: dual contribution + agnostic stance → 消除 "predictable" objection
2. Per-axis confound structure as co-primary → 真正 novel 贡献可见度提升
3. 5-layer MF1 defense → Comparative Trap 充分回应
4. Bootstrap attenuation curve + 100-point Likert → 新实验证据
5. Gemini-2.5-Flash ✅ → 4 target judges from 4 independent companies, 8/8 Blindspot cells confirmed (verbosity all 4 judges + formality all 4 judges)
Novelty ceiling (Blindspot as domain transfer) mitigated by dual-contribution positioning. Statistical methodology depth + honest artifact handling + per-axis novelty + 4-architecture generalizability are primary strengths.
