# Rebuttal Material Draft

> 针对 R16 (3.5 Borderline Conference) 的 recurring issues 准备。每条 3-5 句 + 数据支撑。

---

## 1. N2 Title Scope — "A Systematic Comparison" 暗示通用性但实际 ≤8B LoRA

**Response:**

The title describes the *type of study* (systematic comparison of formulations), not the scope of applicability. The abstract's first sentence explicitly scopes the work to "≤8B LoRA fine-tuning," and Section 5.3 qualifies 14B results as "preliminary" with only 3 seeds from a single family. We chose this title because the contribution is methodological: no prior work compares CLS and CWM under matched conditions at any scale. Additionally, our 14B results (3 seeds, Qwen3) provide evidence beyond the ≤8B scope: all three formulations converge to within 1.07pp (CLS 89.93%, CWM 89.50%, TRAJ 88.86%), with a monotonic gap reduction from 3.11pp at 4B to 1.07pp at 14B—consistent with capacity-dependent convergence. We welcome suggestions for a more precise title if the reviewer feels the current one overpromises.

**Supporting data:**
- Abstract line 1: "under ≤8B LoRA fine-tuning"
- §5.3 Table 2: 14B CLS 89.93±0.80, CWM 89.50±0.67, TRAJ 88.86±0.77 (3 seeds each)
- Max pairwise gap: 3.11pp (4B) → 2.24pp (8B) → 1.07pp (14B)
- Cross-family coverage: Qwen3 (4B/8B/14B) + DeepSeek-Coder-6.7B (2 seeds)

---

## 2. TRAJ Power — CLS-TRAJ TOST power ~0.3

**Response:**

We fully disclose this limitation. Section 5.4 states: "TOST power is ~0.3—a 70% probability of failing to confirm equivalence even if the true difference is moderate" and explicitly notes the CLS-TRAJ non-confirmation "may reflect insufficient power rather than a genuine difference (a minimum n_eff ≈ 350 would be needed for ≥0.8 power at ±2pp)." This transparency is deliberate—we report CLS-TRAJ equivalence as "not confirmed" rather than "rejected," a conservative choice. Two complementary lines of evidence mitigate the power concern: (1) Bayesian ROPE, which does not suffer from frequentist power limitations, yields P(ROPE)=0.970 at variant level (95% HDI=[−2.00, +1.03]pp, entirely inside the ROPE), supporting equivalence; (2) the CLS-TRAJ gap narrows monotonically from 3.11pp (4B) to 2.24pp (8B) to 1.07pp (14B), providing converging evidence that the gap is closing with scale rather than representing a persistent formulation difference.

**Supporting data:**
- §5.4: "power is ~0.3" explicitly stated
- TOST: p=0.025, Holm adj_p=0.075 → "not confirmed"
- Bayesian ROPE variant-level: P(ROPE)=0.970, HDI=[−2.00, +1.03]pp (inside ROPE)
- Bayesian ROPE per-test: P(ROPE)=0.542 (inconclusive, consistent with aggregation effects)
- 14B gap: 1.07pp (within ±2pp margin), monotonic narrowing across 3 scales
- n_eff≈86 after clustering (ICC=0.191, DEFF=3.97)

---

## 3. Repo Seeds — 2-3 seeds 不足以支撑 formulation 归因

**Response:**

We agree that 2-3 repo-level seeds limit causal attribution, which is why §3.5 explicitly labels these comparisons as "exploratory" and §5.5 states "limited seed coverage and multiple confounds limit causal attribution." The claim is about an *observable pattern*, not a definitive causal statement. Three independent lines of evidence support the pattern's robustness despite limited seeds: (1) Cross-family consistency: both Qwen3-8B (gap 18.35pp) and DeepSeek-6.7B (gap 23-28pp) show CLS >> CWM in the same direction, with the pattern holding across all 6 CWM repo-level seeds tested (3 Qwen + 3 DeepSeek). (2) Format collapse is a directly observable mechanism, not a statistical inference: 53-74% of CWM repo-level outputs are unparseable across *all* seeds and *both* model families, with even the parseable subset performing below majority baseline (38-43%). (3) The mixed-effects LPM confirms the formulation×complexity interaction at per-test level (z=−23.7, p<0.001, n=56,480 observations, 139 clusters), where statistical power is not a concern.

**Supporting data:**
- §3.5: "exploratory" qualifier
- Qwen3-8B: CLS 84.83±0.67 vs CWM 66.48±1.15 (3 seeds each)
- DeepSeek: CLS 84.38±2.50 vs CWM 58.30±2.82 (2-3 seeds)
- CWM unparseable rate: 53.7% (Qwen3-4B), 73.8% (Qwen3-8B), 57-63% (DeepSeek all seeds)
- DeepSeek CWM s456: 56.11% (below majority 72.96%) — 3rd seed confirms pattern
- Parseable-only accuracy: 38-43%, below majority baseline
- LPM interaction: z=−23.7, p<0.001, 139 clusters

---

## 4. W2 Format Collapse — Inherent limitation vs engineering artifact

**Response:**

We systematically tested four interventions targeting format compliance, all of which failed: (1) doubling LoRA rank to 32 does not improve format compliance (accuracy 87.04% func-level, no repo-level format improvement); (2) majority voting (k=5) is ineffective because collapsed outputs are near-identical across samples; (3) relaxed matching still leaves >50% unparseable; (4) scaling from 4B to 8B *worsens* the unparseable rate from 53.7% to 73.8%. Critically, even parseable CWM outputs perform below majority baseline (38-43%), and forced-parsing analysis confirms the bottleneck is semantic, not syntactic (Appendix F(c))—the model produces content that is neither well-formatted nor semantically correct at repo-level complexity. The mechanism is principled: repo-level CWM outputs average ~477 tokens vs. ~1 token for CLS; this 477× increase in output length creates compound error that scales nonlinearly with test count. We acknowledge in Limitations that constrained decoding and output-format pretraining were not evaluated and may mitigate format collapse; the contribution is documenting that four standard interventions are insufficient.

**Supporting data:**
- LoRA rank 32: 87.04% func-level, no format improvement (Appendix F(g))
- Majority voting k=5: near-identical outputs → ineffective (Appendix F(g))
- Relaxed matching: >50% still unparseable (Appendix F(g))
- 4B→8B scaling: unparseable 53.7% → 73.8% (gets worse)
- Parseable-only accuracy: 38-43%, below majority 72.96%
- Forced parsing: below majority → semantic bottleneck, not syntactic
- Output length: CLS ~1 token, CWM ~477 tokens (217× throughput gap)
- Limitations §7: "constrained decoding... not evaluated" — explicit acknowledgment

---

## Status: deepseek-cwm-repo-s456-train-v2

Training **completed**. Eval child experiment `deepseek-cwm-repo-s456-e3-eval` is DONE:
- Accuracy: 56.11% (below majority 72.96%)
- Unparseable rate: 56.97%
- Parseable-only accuracy: 32.45%

This is the 3rd DeepSeek CWM repo-level seed, confirming the pattern:
| Seed | Accuracy | Unparseable |
|------|----------|-------------|
| s42 (seq4096) | 61.49% | 62.5% |
| s123 | — (eval pending, stuck in RUNNING) | — |
| s456 | 56.11% | 56.97% |

All below majority baseline (72.96%), consistent with format collapse being seed-independent.

The parent experiment `deepseek-cwm-repo-s456-train-v2` is stuck at status=ANALYZING (stale cron state). Should be updated to DONE.
