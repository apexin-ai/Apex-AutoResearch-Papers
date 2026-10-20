# Paper Framing — collapse_aware_reward_rebalancing

## Target
EMNLP 2026 ARR (DDL: 2026-05-25)

## Title Candidates
- A: "The Resilience of Output Diversity Under Iterative Reward-Based Curation: A Systematic Empirical Study"

## Core Insight
Reward-based curation in iterative self-consuming training does NOT cause diversity collapse — neither semantic nor format. The apparent "diversity stagnation" under LoRA is a capacity artifact. Format homogenization IS real but is an inherent property of iterative self-training regardless of curation; higher K amplifies severity. Embedding-based metrics (Vendi Score) are blind to format collapse entirely.

## Narrative Arc
Fear → Test → Surprise → Understanding → Guidance

1. **Fear**: Iterative self-consuming training risks diversity collapse (Shumailov et al., Alemohammad et al.). Reward-based curation selects narrower subsets, potentially accelerating this.
2. **Test**: Systematic study across 8 configurations (K=4/8/16, LoRA/Full-FT, LR=5e-6/2e-5, with/without curation) × 3 generations on Qwen3-0.6B.
3. **Surprise**: Semantic diversity (Vendi Score, NN distance) is completely resilient across ALL 8 configs including extreme K=16. Even with 80% training loss reduction, diversity stable.
4. **Understanding**: 
   - LoRA creates a false signal: capacity constraint limits drift in ALL directions, making curation look like it suppresses diversity (3.4pp gap) when it's actually LoRA's ceiling.
   - Full-FT reveals direction reversal: curation HELPS diversity (+0.63pp) under sufficient learning capacity.
   - FORMAT collapse is real but inherent to iterative self-training — same-K comparison (C1 curated vs C5 random, K=4) shows identical degradation (entropy -0.75 bits both). Higher K amplifies severity (K=8: -1.13 bits). Curation is NOT the cause.
   - Embedding metrics (Vendi Score) are completely blind to format collapse.
5. **Guidance**: Practitioners don't need semantic diversity safeguards. Format homogenization is inherent to iterative training (not fixable by removing curation); monitor format-level metrics and be aware higher K worsens it.

## Core Claims

### Claim 1: Semantic Resilience (CONFIRMED — 8 configs)
Reward-based top-K curation does not cause semantic diversity collapse in iterative SFT, across 8 configurations spanning LoRA, Full-FT, K=4/8/16, and varying LR. Even extreme K=16 (6.25% retention) shows only -0.19% Vendi decline.
- Evidence: 8/8 configs P1 FAIL, Vendi Score stable or increasing
- Strength: Strong (8 configs including extreme pressure, consistent direction)

### Claim 2: Format Collapse is Inherent to Iterative Training (CONFIRMED — D013)
Format homogenization (opening pattern entropy drop, near-duplicate increase) is real but NOT caused by curation. Same-K comparison shows identical degradation under curated and random selection. Higher K amplifies severity.
- Evidence: C1 (curated K=4) vs C5 (random K=4): entropy both -0.75 bits, near-dup both +37pp. C2 (curated K=8): entropy -1.13 bits → K is the amplifier, not curation.
- Strength: Strong (controlled same-K comparison isolates variables)

### Claim 3: LoRA Capacity Artifact — Direction Reversal (CONFIRMED)
The apparent diversity suppression under LoRA is a capacity artifact. Under Full-FT with sufficient LR, curation's effect reverses from suppression (-3.4pp) to mild promotion (+0.63pp).
- Evidence: Monotonic trend across 3 training regimes (LoRA → Full-FT low-LR → Full-FT high-LR)
- Strength: Strong (clean gradient across regimes)

### Claim 4: Measurement Contribution (CONFIRMED)
Standard metrics (Vendi Score, self-BLEU) have a blind spot for format homogenization. Propose opening_entropy and near_duplicate_start_rate as complementary metrics.
- Evidence: Vendi flat while opening patterns collapse identically in curated and random
- Strength: Strong (same-K controlled comparison strengthens the "blind spot" narrative)

## Anticipated Reviewer Concerns

### R1: Scale (HIGH RISK)
"0.6B model and 2200 prompts is too small. Would 7B/70B models behave differently?"
- Response: Acknowledge in Limitations. Argue that sub-1B models with <5K data is a common ablation setting in alignment literature. The finding that even aggressive overfitting (80% loss drop) doesn't cause collapse suggests the mechanism, not just the scale, prevents collapse.

### R2: Generation Depth (MEDIUM)
"3 generations is too short for compounding effects."
- Response: Training loss plateau at 0.095 after Gen 2 → model has already maximally overfitted. Additional generations unlikely to produce qualitatively different dynamics. Acknowledge as limitation.

### R3: Novelty (MEDIUM)
"Negative results alone aren't novel enough."
- Response: (1) Controlled causal analysis separating iterative training effect from curation effect, (2) LoRA capacity artifact discovery with direction reversal, (3) new format metrics that detect what Vendi misses. This is causal decomposition, not just "didn't find collapse."

### R4: Actionability (MEDIUM)
"So what? What should practitioners do?"
- Response: (1) Don't over-engineer diversity safeguards for standard iterative SFT. (2) Monitor format-level metrics — format collapse is inherent to iterative training and not fixable by removing curation. (3) Be cautious about LoRA-based evaluations of curation effects. (4) Higher K amplifies format degradation — choose K accordingly.

### R5: CARR Method Not Working
"Your proposed method (CARR) doesn't even work?"
- Response: CARR failure is itself informative: proxy scores are highly correlated (r=0.63-0.77), making adaptive weighting futile. This motivates future work on truly independent reward dimensions. Include as supplementary finding.

## Key Figures/Tables

- **Table 1**: Full metrics across 8 configurations × 3 generations
- **Table 2**: Vendi Score trajectory summary + relative gaps (including C8 K=16)
- **Table 3**: Training loss dynamics (demonstrating real learning)
- **Figure 1**: Pipeline overview diagram
- **Figure 2**: Vendi Score trajectory (all 8 configs including K=16)
- **Figure 3**: Direction reversal bar chart (LoRA -3.4pp → Full-FT +0.63pp)
- **Figure 4**: Format collapse — C1 vs C5 (same K=4, identical degradation) + C2 (K=8, amplified) — KEY VISUAL for D013
- **Table 4**: Format metrics comparison (C1 curated vs C5 random, same K=4)
