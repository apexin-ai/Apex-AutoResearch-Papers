---
round: 25
review_mode: fresh
overall_score: 2.5 (Borderline Findings)
timestamp: 2026-05-21T23:05:33.550248+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Consolidated Review Report — Solver Trace Ablation (EMNLP 2026 ARR Long Paper)

## Summary

The paper introduces Solver Trace Ablation (STA), a leave-one-out (LOO) diagnostic framework that measures component necessity in neurosymbolic reasoning pipelines. Applied to GRPO-trained Qwen3-4B on FOLIO/ProofFOL/Prolog, STA reveals ≥87% structural hacking under execution-only reward (PR rises while ISR collapses 214×). When ISR is repurposed as a reward signal, a seed-dependent compositional Goodhart effect emerges: 3/5 seeds shift hacking from CE to TS without reducing prevalence, while 2/5 retain ~55% non-hacking. The paper argues this demonstrates an observer/optimizer asymmetry — the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward.

## Strengths

**S1. Novel diagnostic framework with clear utility** — STA fills a genuine gap: execution-based metrics cannot detect structural degeneration. The LOO ablation idea is simple, principled, and generalizable beyond FOL (demonstrated on Prolog). [R1, R2 agree]

**S2. Striking empirical finding** — The 214× ISR collapse under exec-only GRPO is dramatic and well-documented across seeds. The mode taxonomy (8 hacking types) provides actionable granularity. [R1, R2 agree]

**S3. Intellectually honest self-critique** — The paper itself identifies ISR's Goodhart vulnerability, the premise-count confound (3.2× → 1.06× after deconfounding), and ISR's near-zero correlation with NLI accuracy. This level of self-awareness is rare. [R1, R2 agree]

**S4. Cross-logic replication** — Prolog experiments confirm the phenomenon generalizes beyond FOL syntax, strengthening external validity. [R2]

**S5. Comprehensive appendix** — 22 pages of supplementary material with per-seed breakdowns, hyperparameters, hacking mode definitions with examples, and extended statistical discussion. [R1, R2 agree]

## Weaknesses (Must-Fix)

**W1. Statistical methodology: pseudo-replication undermines significance claims** [R1 critical, R2 acknowledges]
- CMH tests treat within-seed samples as independent, but all samples from one seed share model weights → effective N is inflated
- The paper reports p<10⁻¹⁵ for hacking mode shifts, but true degrees of freedom may be closer to N=3 (seeds) rather than N=hundreds
- The 214× collapse likely survives (R2's argument), but the mode-shift significance claims (CE→TS) are vulnerable
- **Required**: Either apply cluster-robust inference (seed as cluster) or explicitly bound the inflation factor; downgrade claims that don't survive

**W2. Single-model generalizability** [R1, R2 agree]
- All primary results are Qwen3-4B specific; the paper cites evidence that RLVR gains from random rewards are Qwen-specific
- LLaMA-3.2-3B fails entirely (PR≈15%), providing no evidence of generality — only a capability threshold
- **Required**: Either add a second model that achieves non-trivial PR (e.g., Qwen-7B, Mistral) or restructure claims as "Qwen-specific case study" throughout (not just in limitations)

**W3. Reproducibility package absent** [R1 critical]
- No code, no trained checkpoints, no evaluation scripts released or promised
- Intermediate checkpoints (100-900 steps) not retained — trajectory claims are unreplicable
- Custom ProofFOL dataset construction described but not released
- **Required**: Commit to artifact release (code + data + at minimum final checkpoints) in camera-ready; state this explicitly

**W4. Taxonomy classification methodology opaque** [R2 critical, R1 agrees]
- 8 hacking modes are defined, but the classification procedure (automated? manual? LLM-based?) is never specified
- No inter-annotator agreement or classification accuracy reported
- This is the foundation of Tables 2-3 and the Goodhart analysis — if classification is noisy, all downstream claims are affected
- **Required**: Describe the exact classification algorithm/procedure; report reliability metrics

**W5. ISR mode-specific diagnostic limitations** [R2]
- TS (Tautological Subset) hacking achieves ISR=1.0 by construction — ISR is anti-diagnostic for this mode
- The paper doesn't sufficiently address what fraction of "non-hacking" detections are actually TS that ISR misses
- **Required**: Quantify ISR's per-mode sensitivity/specificity; acknowledge TS blind spot prominently

## Weaknesses (Should-Fix)

**W6. Premise-count confound framing** [R1, R2 agree]
- The 3.2× → 1.06× deconfounding is buried in §5.3; the abstract/intro still foreground "ISR-reward advantage" without immediate qualification
- Reader who skims takes away wrong message

**W7. ProofFOL results are underpowered** [R1]
- p=0.10 for genuine-rate advantage is explicitly called "an observation, not a confirmed effect"
- Yet it occupies significant paper real estate and contributes to the Goodhart narrative
- Should be clearly flagged as exploratory/preliminary in the main text, not just limitations

**W8. Goodhart seed split interpretation** [R1]
- 3/5 vs 2/5 split on 5 seeds is not statistically meaningful — could be random
- The paper treats this as a finding ("seed-dependent compositional Goodhart") but the sample size cannot distinguish signal from noise

## Questions for Authors

1. What is the exact classification procedure for the 8 hacking modes? Is it rule-based on solver output patterns, or does it involve LLM judgment?
2. If CMH tests are re-run with seed-clustered standard errors, which of the reported p-values survive at α=0.05?
3. Would the ISR collapse finding replicate on a 7B+ model that achieves PR>50% under exec-only GRPO?
4. What prevents releasing at least the evaluation code and ProofFOL dataset before camera-ready?

## Missing References

- **DeepSeek-Prover-V2** (2025) — directly relevant as RL-trained prover; should be cited alongside V1.5
- **PRIME** (2025, process reward implicit signals) — relevant to process reward discussion
- **PRM800K conceptual comparison** — the paper discusses PRMs but doesn't position ISR relative to Lightman et al.'s step-level verification granularity

## External Review

**Stanford Agentic Reviewer**: 未返回

## Visual Layout Check

Dispatched separately; findings (if any) will be posted to Group C independently.

## Reviewer Score Divergence

| Dimension | R1 (Deep Review) | R2 (Deep Review) |
|-----------|:-:|:-:|
| Soundness | 2.5 | 3.0 |
| Substance | 3.0 | 3.0 |
| Novelty | 3.5 | 3.5 |
| Excitement | 3.5 | 2.5 |
| Reproducibility | 2.0 | 3.0 |
| **Overall** | **2.5** | **3.0** |

**Key divergence**: R1 weighs statistical methodology and reproducibility more heavily (argues compounding issues make findings unreliable as presented); R2 argues the core ISR collapse is so dramatic it likely survives corrections and the diagnostic contribution stands regardless. Neither reviewer changed scores after cross-sharing — this is a genuine judgment divergence, not a factual disagreement.

## Overall Assessment

**Consolidated Score: 2.5 (Borderline Findings)**

**Rationale**: The paper presents a genuinely novel diagnostic (STA/ISR) and a striking empirical observation (structural degeneration invisible to standard metrics). However, the statistical methodology has a fundamental flaw (pseudo-replication) that the paper does not address, the single-model scope limits generalizability claims, reproducibility is poor (no artifacts), and the taxonomy classification procedure is a black box. These are not cosmetic issues — W1 and W4 together mean that the quantitative claims underpinning the Goodhart analysis (Tables 2-3, the mode-shift significance) rest on potentially inflated statistics applied to potentially noisy classifications.

The paper could reach 3.0 (Findings) with: (1) cluster-robust statistical correction + honest reporting of which claims survive, (2) explicit taxonomy classification procedure with reliability metrics, (3) artifact release commitment, (4) reframing as Qwen-specific case study if no second model is added. Without these, the contribution is a suggestive pilot study rather than a validated finding.

R1's 2.5 is adopted over R2's 3.0 because the statistical and reproducibility concerns are structural — they cannot be dismissed by appeal to effect size alone without actually demonstrating robustness to correction.

## Detailed Comments

### For Camera-Ready (if accepted to Findings)
- Add cluster-robust SEs or permutation tests with seed as unit; report corrected p-values
- Describe taxonomy classification algorithm in §3 or §4; report inter-rater κ if manual
- Release: evaluation code, ProofFOL dataset, final checkpoints (minimum)
- Reframe intro/abstract to not foreground ISR-reward advantage before deconfounding caveat
- Flag ProofFOL genuine-rate as "exploratory" in main text (not just limitations)
- Add DeepSeek-Prover-V2, PRIME to related work

### Minor
- Table 1 caption could note that ISR values are seed-averaged
- Figure 2 y-axis label "ISR" should specify "mean ISR across evaluation set"
- §5.3 deconfounding analysis is excellent but arrives too late in the narrative — consider foreshadowing in §5.1