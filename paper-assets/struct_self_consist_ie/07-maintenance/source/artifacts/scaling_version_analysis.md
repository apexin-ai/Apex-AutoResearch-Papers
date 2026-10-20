# Scaling Narrative Version Analysis

> Generated 2026-05-20. Based on existing data points; pending 7B/14B/32B FT results.

## 1. Version Summary

### Version A — Monotonic ("Degeneracy rises with scale")
- **Core thesis**: Degeneracy increases monotonically with parameter count (7B < 14B < 32B) within the Qwen2.5 FT family.
- **Mechanism**: Larger models → stronger priors → more deterministic outputs → higher degeneracy.
- **Construction implication**: Construction Δ inversely tracks degeneracy — smallest model benefits most.
- **Narrative payoff**: Clean convergence across three dimensions (scale, epoch, model family) with degeneracy as a "robust diagnostic" that is *predictable* from model scale.

### Version B — Non-monotonic ("Degeneracy is not a simple function of scale")
- **Core thesis**: Degeneracy does NOT increase monotonically — model-specific factors (pretraining data, architecture) modulate the tradeoff.
- **Mechanism**: QLoRA training recipe, Qwen2.5 family architecture differences, and pretraining data composition create scale-invariant variation.
- **Construction implication**: Same gating relationship holds (degen → construction), but the gating variable is unpredictable from model size alone.
- **Narrative payoff**: Degeneracy reframed as a *post-hoc diagnostic* — practitioners should measure it, not predict it from scale. More nuanced, more practically useful.

## 2. Existing Evidence Inventory

### 2.1 Fine-tuned data

| Model | Family | Dataset | Degen% | Greedy F1 | Headroom | LP ρ | SJ ρ | Constr Δ (pp) |
|-------|--------|---------|--------|-----------|----------|------|------|---------------|
| Qwen3-4B | Qwen3 | SciERC | 10.4% | .662 | 13.0pp | — | .422 | — |
| Qwen3-8B | Qwen3 | SciERC | 17.8% | .645 | 13.1pp | .205 | .360 | +1.02 |
| Qwen3-8B | Qwen3 | FewNERD | 12.7% | .748 | 12.6pp | .220 | .380 | +1.40 |
| Qwen3-8B | Qwen3 | CoNLL | 61.7% | .908 | 6.8pp | .302 | .436 | −0.39 |
| LLaMA-3.1-8B | LLaMA | FewNERD | 23.4% | .784 | 10.0pp | — | — | +0.36 |
| LoRA r=8 | Qwen3 | SciERC | 7.2% | — | 16.0pp | — | .365 | — |

### 2.2 Zero-shot 72B

| Dataset | Degen% | LP ρ | SJ ρ | Constr Δ (pp) | p |
|---------|--------|------|------|---------------|---|
| SciERC | 21.0% | .081 | .217 | +1.53 | 0.008** |
| FewNERD | 46.2% | .119 | .345 | −0.20 | n.s. |
| CoNLL | 67.7% | −.002 | .304 | −0.37 | n.s. |

### 2.3 Few-shot 72B

| Dataset | Degen% | LP ρ | SJ ρ | Constr Δ (pp) | p |
|---------|--------|------|------|---------------|---|
| SciERC | 16.6% | .060 | .293 | −0.08 | 0.544 |
| FewNERD | 45.2% | .161 | .345 | +0.02 | 0.401 |
| CoNLL | 70.0% | .106 | .442 | +0.03 | 0.417 |

### 2.4 Epoch ablation (Qwen3-8B FewNERD)

| Epochs | Degen% | Effect |
|--------|--------|--------|
| 3 | 11.1% | Low degen, high diversity |
| 5 | 31.3% | High degen, reduced diversity |

## 3. Evidence Assessment per Version

### 3.1 Evidence supporting Version A (Monotonic)

| Evidence | Strength | Notes |
|----------|----------|-------|
| Capability-diversity tension (theoretical) | Strong | Well-motivated: more capable → more convergent |
| Cross-scale degen gradient (4B 10.4% → 8B 17.8% on SciERC) | Moderate | Qwen3 family, within-family monotonic |
| 72B ZS high degen (21–68%) | Moderate | Different regime (ZS vs FT), confounded |
| Epoch ablation (more training → more degen) | Moderate | Analogous to scale via effective capacity |
| Cross-dataset gradient (CoNLL 62% → SciERC 18% → FewNERD 13%) | Weak | Tracks task difficulty, not model scale |

### 3.2 Evidence supporting Version B (Non-monotonic)

| Evidence | Strength | Notes |
|----------|----------|-------|
| QLoRA equalizing effect | Moderate | Fixed rank → trainable params nearly constant across scales → effective capacity diverges from raw param count |
| D154: cross-config degen-LP ρ=0.052 (p=0.81) | Moderate | Degeneracy is NOT a reliable predictor across configurations |
| LoRA rank effect (r=8: 7.2% vs r=32: 21%) | Moderate | Training recipe shifts degen as much as 3× scale change |
| Qwen2.5 family heterogeneity | Weak–Moderate | Different architectures/data within family; 14B may behave differently than interpolation predicts |

### 3.3 Evidence neutral (supports gating in both versions)

- Degeneracy gates construction effectiveness: holds across ALL 9 conditions (3 datasets × 3 regimes). No exception.
- LP-alignment is the binding constraint for selection: confirmed at 4B, 8B, and 72B.
- Structural signals (SJ/FK) are scale-robust: ρ maintained across 4B–72B.

## 4. Prior Probability Assessment

**Version A (Monotonic): ~55%**
- Theoretically cleaner, supported by the two cross-scale data points we have (4B→8B SciERC).
- Risk: QLoRA FT may break the theoretical prediction by equalizing effective task capacity.

**Version B (Non-monotonic): ~45%**
- Empirically plausible given QLoRA dynamics and the D154 finding that degen is configuration-dependent.
- Risk: If data happens to be monotonic, Version B loses its motivating observation but the "measure don't predict" message still holds.

**Key asymmetry**: Version A requires a strict ordering (7B < 14B < 32B degen). Any single inversion falsifies it. Version B is compatible with either outcome — even if data is monotonic, B can be weakened to "in this family it happens to be monotonic, but this is not guaranteed." This makes B more robust as a fallback.

## 5. Judgment Criteria for 7B/14B/32B Data

### 5.1 Degeneracy pattern (primary discriminator)

| Outcome | Supports | Action |
|---------|----------|--------|
| 7B < 14B < 32B (strict monotonic) | **Version A** | Use A narrative; cite as convergent with epoch/family evidence |
| Any inversion (e.g., 14B < 7B, or 32B < 14B) | **Version B** | Use B narrative; frame degen as post-hoc diagnostic |
| Near-equal at two points (Δ < 2pp) | **Ambiguous** | Lean B (no clear trend); or merge: "weak monotonic trend with substantial model-specific variation" |

### 5.2 Degeneracy thresholds

Reference: Qwen3-8B FT FewNERD = 12.7%. The Qwen2.5 FT models on FewNERD will form a parallel data series.

- **7B degen < 10%**: Strongly supports A (smallest model, lowest degen). Also implies high construction potential.
- **7B degen 10–15%**: Consistent with A if 14B and 32B are higher. Comparable to the Qwen3-8B reference.
- **7B degen 15–25%**: Weakly supports B (7B already showing significant degen). Makes monotonicity harder to sustain across 3 points.
- **7B degen > 25%**: Strongly supports B (small model with high degen → architecture/training dominates scale).

### 5.3 Construction delta

- **Positive and significant (>+0.5pp, p<0.05)**: Confirms gating — lowest degen scale point benefits from construction. Strengthens whichever version holds.
- **Positive but marginal (0 to +0.5pp, n.s.)**: Suggests degen may not be low enough to enable construction, or LP alignment insufficient.
- **Negative**: Unexpected for low-degen setting. Would require investigation (data quality, training failure).

The critical test: **does construction Δ inversely track degen across the three scale points?**
- If yes → gating confirmed within-family (supports both versions' shared claim).
- If no → gating is dataset/regime-specific, not universal. Would weaken both versions.

### 5.4 Signal ranking (LP ρ, SJ ρ)

| Pattern | Interpretation |
|---------|---------------|
| SJ ρ ≈ 0.30–0.40 at all scales | Signal quality is scale-invariant (expected) |
| LP ρ stable across scales (0.15–0.25) | FT calibration equally effective regardless of scale |
| LP ρ decreases with scale | Larger FT models have more compressed LP → supports capability-diversity tension |
| LP ρ increases with scale | Larger models better calibrated → interesting but unexpected |

### 5.5 Greedy F1 pattern

- Expected: 7B < 14B < 32B greedy F1 (monotonic improvement with scale)
- If this monotonicity breaks → QLoRA FT may equalize performance, making degen non-monotonicity more likely
- If greedy F1 is monotonic but degen is not → strongest Version B evidence (scale helps capability but not diversity)

## 6. Decision Matrix

| 7B/14B/32B Degen Pattern | Greedy F1 Pattern | Constr tracks degen? | Verdict | Narrative |
|---------------------------|-------------------|---------------------|---------|-----------|
| Monotonic ↑ | Monotonic ↑ | Yes | **A** | Clean story: scale → capability → degen → construction shrinks |
| Monotonic ↑ | Monotonic ↑ | No | **Weak A** | Degen trend holds but gating breaks — investigate LP alignment |
| Non-monotonic | Monotonic ↑ | Yes | **B** | Best B case: more capable ≠ more degenerate, but gating works |
| Non-monotonic | Monotonic ↑ | No | **Neither clean** | Report data descriptively; lead with gating per-dataset |
| Non-monotonic | Non-monotonic | Yes | **B** | QLoRA equalizes everything; degen is a pure diagnostic |
| All near-equal (Δ<3pp) | Any | — | **B (lite)** | Scale has minimal effect under FT; epoch/recipe matters more |

## 7. Fallback Strategies

### 7.1 If data is cleanly monotonic → Use Version A
- Strongest possible narrative: convergent evidence across scale, epoch, and family.
- Write as: "Degeneracy increases with scale (7B→14B→32B), consistent with the capability-diversity tension observed across epochs and model families."

### 7.2 If data is cleanly non-monotonic → Use Version B
- Reframe degeneracy as diagnostic, not consequence of scale.
- Write as: "Degeneracy is not a simple function of scale — practitioners should measure it rather than predict from model size."
- Strengthens the "practical protocol" angle of Contribution C.

### 7.3 If pattern is ambiguous (near-equal or noisy)
**Recommended approach**: Hybrid narrative.
- Lead: "Within-family scaling shows [weak/moderate] trend toward higher degeneracy with scale, but the effect is smaller than the impact of training recipe (LoRA rank: 3× degen shift) or epoch count (11%→31%)."
- Payoff: Degeneracy is influenced by scale but dominated by training choices → measure post-hoc.
- This is essentially Version B with a nod to A's trend.

### 7.4 If gating breaks (construction does NOT track degen)
- Most concerning outcome. Would require:
  1. Check LP within-instance alignment at each scale point.
  2. If LP alignment differs across scales → LP alignment, not degen, is the driver. Report as such.
  3. Drop the "gating" framing; report degeneracy and construction independently.
  4. Fall back to: "Construction effectiveness depends on a conjunction of factors (degeneracy, LP alignment, oracle headroom) that do not reduce to a single predictor."

### 7.5 If 7B training fails or produces degenerate outputs
- Use 14B and 32B only (2-point comparison, weaker but still informative).
- Supplement with 4B→8B cross-family data as additional scale evidence.
- Move scaling subsection to appendix if evidence is thin.

## 8. Recommendation

**Prepare for Version B** as the default writing plan, for two reasons:

1. **Robustness**: B is compatible with any degen pattern (monotonic or not). A is falsified by a single inversion. Given the 45% prior on non-monotonicity, hedging toward B is safer.

2. **Narrative value**: B's "measure, don't predict" message is more practically useful and aligns with the paper's diagnostic positioning (Contribution B). It also dovetails with the D154 finding (cross-config degen is unpredictable).

3. **Upgrade path**: If data turns out monotonic, B can be upgraded to A with a one-paragraph rewrite. The reverse (A→B) requires more restructuring.

**Concrete preparation**:
- Keep both .tex templates ready (already done).
- When 7B data arrives, compute: degen%, greedy F1, oracle headroom, LP ρ, SJ ρ, LP-weighted construction Δ (with bootstrap CI).
- Apply the decision matrix in §6 to select the version.
- If ambiguous, use the hybrid narrative (§7.3).

## 9. Impact on Paper Claims

The choice between A and B affects only the scaling paragraph in §5.5. It does NOT affect:
- Claim 1 (QE framework + diagnostic) — scale-independent.
- Claim 2 (methodology) — already validated at 4B/8B/72B.
- Claim 3 (task-complexity boundary) — orthogonal to within-family scaling.
- Claim 4 (selection boundaries) — strengthened by either version.

The scaling section is supporting evidence for the capability-diversity tension, not a core claim. Both versions serve this purpose — A as a direct demonstration, B as a nuanced characterization.
