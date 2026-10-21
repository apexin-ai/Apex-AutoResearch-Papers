# Paper Framing — causal_style_decomp_judge

> Round 5: **3.5 Borderline Conference** (up from 3.0). 冲刺 4.0 中。
> 4 补充实验并行执行：Llama-70B third judge + double-rewrite placebo + NLI ablation + cross-axis gradient。

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Fallback: EMNLP 2026 Findings
- Deadline: **May 25, 2026 AoE**
- Format: Long paper, 8-page main text + unlimited references

## Title
**The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition**

## Core Claims (Round 5 stratified)

### C1 (Method — application contribution): CSD pipeline detects per-axis style bias in black-box LLM judges
- NLI-gated content control + per-axis style decomposition + position-controlled pairwise comparison
- **NOT** "approximates the do-operator" — reframed as "filtering-based confounder control" (Round 5 MF2)
- 3 target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B [pending]) + 1 negative control (Claude Sonnet 4)
- 3 benchmarks (LLMBar, AlpacaEval, MT-Bench) × 3 axes (formality, verbosity, register)

### C2 (Measurement Insight — 主贡献): Likert Blindspot — measurement attenuation spectrum
- **Per-axis claim stratification** (Round 5):
  - **Verbosity** = "clean style bias" — BT 77%, GEE Orig OR NS, confound-free. 7-method sensitivity hierarchy confirms 6/6 Likert NS.
  - **Formality** = "conditional style effect" — BT 63-67%, GEE both Style and Orig significant. Moderated by content quality changes.
  - **Register** = "style-associated preference" — BT 55%, exploratory, originality-dominated.
- Attenuation spectrum: BT 63-67% → complete attenuation (d→0); BT 77% → still complete; BT >80% → Likert starts detecting
- **Detection vs. Amplification** (Round 5 MF1 — Comparative Trap defense):
  - Layer 1: NLI gate blocks content-mediated amplification
  - Layer 2: Claude negative control (same format, no bias), debiased prompt partial reduction, cross-axis gradient inconsistent with uniform format amplification
  - Layer 3: Honest acknowledgment — "controlled detection with bounded amplification risk"
  - **Pending**: Double-rewrite placebo BT (if ≈50%, eliminates format amplification hypothesis)

### C3 (Empirical): Style bias detectability varies by axis and judge
- GEE confound gradient: Verbosity (pure) > Formality (mixed) > Register (originality-dominated)
- Judge-dependent: GPT-4o + Qwen3-32B show bias; Claude does not
- **Pending**: Llama-3.3-70B as third target judge

### C4 (Practical): Practitioner guidance
- Use content-controlled pairwise comparison (with NLI gating) for style bias audits
- Per-axis decomposition reveals axis-specific confound structure
- Prompt-level debiasing insufficient (Qwen3 -5.7pp still sig, GPT-4o -0.4pp)

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
- **BT GoF**: formality χ² p=0.198, verbosity p=0.905 (model fits well)
- **Stratified BT**: Stable across originality subgroups
- **Originality-minimal subset**: |Likert Δ|=0 pairs → style Δ < 2pp, CI contains 0
- **Claude TOST**: Δ=15pp equivalence passes both axes
- **NLI full validation**: 200-pair GPT-4o (formality 92.1%, verbosity 82.6%)
- **Rewriter independence**: GPT-4o formality BT 64.4% vs Qwen3 66.5% (Δ=−2.1pp)
- **Sensitivity hierarchy**: 7 Likert methods × 2 axes (formality + verbosity) all NS, only BT detects
- **Length robustness**: Verbosity Style OR survives all length controls (<2% change)

## Pending Experiments (冲刺 4.0)

### A: Llama-3.3-70B Third Target Judge
- Purpose: 2→3 target judges = generalizability quality jump
- Coverage: verbosity + formality on LLMBar
- Impact: Directly addresses SF3 + strengthens MF1 defense

### B': Double-Rewrite Placebo BT
- Purpose: MF1 最强防御 — original vs double-rewrite (same style, rewriting noise only)
- Expected: BT ≈ 50% → pairwise format doesn't create bias from rewriting artifact
- Both GPT-4o and Qwen3-32B judges

### B: NLI Gate Ablation
- Purpose: Quantify NLI gate effect on BT signal
- Method: BT on NLI-pass vs NLI-fail vs all pairs

### C: Cross-Axis Gradient Formalization
- Purpose: Qualitative anti-amplification argument
- Method: NLI rejection rate vs BT across 3 axes

## Novelty Positioning (honest)
"The first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges."
- Domain transfer of Thurstone 1927 / Stevens 1946 — acknowledged
- Incremental contribution from method execution quality (per-axis + NLI + 7-method hierarchy)
- Jeong et al. 2025 (Comparative Trap) discusses amplification; we discuss controlled detection

## Story Spine

### Problem
LLM-as-judge is core infrastructure for NLP evaluation and alignment. Style bias is the dominant bias (SOS-Bench R=0.999), but standard Likert scoring systematically misses it.

### Gap (integrative, not cherry-picked)
Prior work addresses parts of the problem: RATE (Likert-based ATE), CASSE (multi-dimensional but correlational), LC-AlpacaEval (single dimension). CSD integrates NLI-gated content control + per-axis decomposition + pairwise comparison — no prior work combines all three.

### Our Contribution
Controlled Style Decomposition (CSD): a black-box framework for per-axis style bias detection. Core finding: Likert Blindspot — measurement attenuation across a severity spectrum.

### Detection vs. Amplification (Round 5 addition)
Jeong et al. (2025) show pairwise amplifies bias. Our evidence chain: NLI gate + Claude negative control + cross-axis gradient + double-rewrite placebo → "controlled detection with bounded amplification risk."

## Bibliography
50 verified references including Jeong 2025, Stureborg 2024, Park 2024.

## Venue Fit
Round 5: 3.5 Borderline Conference. Path to 4.0: MF1 (Comparative Trap) + 3rd judge + placebo control.
Novelty ceiling (domain transfer) is structural. Statistical methodology depth is primary strength.
