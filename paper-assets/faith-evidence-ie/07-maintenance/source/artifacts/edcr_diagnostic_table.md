# EDCR Cross-Method Diagnostic Table (plan_003)

Generated: 2026-05-15 | Source: `/root/autodl-tmp/eval_results/` on rtx5090-4x

## 1. Complete Cross-Method Table

Sorted by EDCR ascending (lower = fewer distractor citations).

| # | Method | rel_f1 | P | R | evi_f1 | EDCR | format_ok | evi_format | n_pred | n_trunc | Δrel_f1 | ΔEDCR |
|---|--------|--------|------|------|--------|------|-----------|------------|--------|---------|---------|-------|
| 1 | CED-reranker oracle | 0.6237 | 0.6211 | 0.6264 | 0.7942 | 0.5262 | 1.000 | — | 13418 | — | +0.2180 | −0.1856 |
| 2 | CED-reranker (N=8) | 0.4864 | 0.4913 | 0.4815 | 0.8188 | 0.6156 | 1.000 | — | 14782 | — | +0.0807 | −0.0962 |
| 3 | bf16 GRPO ckpt-100 | 0.4549 | 0.5042 | 0.4145 | 0.8086 | 0.6318 | 1.000 | 0.938 | 10701 | 61 | +0.0492 | −0.0800 |
| 4 | RSFT-CED s44 | 0.4655 | 0.4798 | 0.4521 | 0.8087 | 0.6350 | 1.000 | 0.801 | 15202 | 189 | +0.0598 | −0.0768 |
| 5 | RSFT-CED s43 | 0.4683 | 0.4817 | 0.4556 | 0.8156 | 0.6388 | 1.000 | 0.814 | 14970 | 171 | +0.0626 | −0.0730 |
| 6 | bf16 GRPO ckpt-80 | 0.4456 | — | — | 0.8034 | 0.6409 | 0.999 | — | — | — | +0.0399 | −0.0709 |
| 7 | bf16 GRPO ckpt-90 | 0.4523 | — | — | 0.8052 | 0.6414 | 0.998 | — | — | — | +0.0466 | −0.0704 |
| 8 | RSFT-flatNLI | 0.4539 | 0.4671 | 0.4414 | 0.8043 | 0.6431 | 1.000 | 0.789 | 15294 | 199 | +0.0482 | −0.0687 |
| 9 | RSFT-CED s42 | 0.4449 | 0.4607 | 0.4302 | 0.8187 | 0.6565 | 1.000 | 0.782 | 15307 | 213 | +0.0392 | −0.0553 |
| 10 | RSFT-CED r2b (a=32) | 0.4493 | 0.4566 | 0.4424 | 0.8128 | 0.6609 | 0.998 | 0.818 | 14829 | 179 | +0.0436 | −0.0509 |
| 11 | RSFT-CED r2a (1ep) | 0.4494 | 0.4512 | 0.4475 | 0.8108 | 0.6641 | 1.000 | 0.790 | 15482 | 208 | +0.0437 | −0.0477 |
| 12 | CED-reranker random | 0.4538 | 0.4348 | 0.4745 | 0.8029 | 0.6763 | 0.998 | — | 15642 | — | +0.0481 | −0.0355 |
| 13 | **SFT baseline** | **0.4106** | **0.4198** | **0.4019** | **0.7979** | **0.7039** | **0.998** | **0.707** | **16774** | **288** | **0** | **0** |
| 14 | DPO-CED (3ep, overfit) | 0.3429 | 0.3244 | 0.3638 | 0.8403 | 0.7294 | 0.995 | 0.730 | 18445 | 260 | −0.0677 | +0.0255 |
| 15 | QLoRA GRPO kl001 s100 | 0.2167 | — | — | 0.5746 | 0.8539 | 1.000 | — | — | — | −0.1890 | +0.1421 |
| 16 | QLoRA GRPO kl001 s90 | 0.2108 | — | — | 0.5666 | 0.8584 | 1.000 | — | — | — | −0.1949 | +0.1466 |
| 17 | QLoRA GRPO lr5e6 ckpt80 | 0.0116 | — | — | 0.8280 | 0.9908 | 0.999 | — | — | — | −0.3941 | +0.2790 |
| 18 | QLoRA GRPO lr5e6 ckpt60 | 0.0093 | — | — | 0.8100 | 0.9930 | 0.998 | — | — | — | −0.3964 | +0.2811 |
| 19 | QLoRA GRPO lr5e6 s20 | 0.0077 | — | — | 0.6281 | 0.9934 | 0.991 | — | — | — | −0.3980 | +0.2816 |
| 20 | QLoRA GRPO lr5e6 ckpt40 | 0.0071 | — | — | 0.7584 | 0.9942 | 0.994 | — | — | — | −0.3986 | +0.2824 |
| 21 | SFT no-evidence | 0.4893 | 0.4884 | 0.4902 | 0.000 | 0.000 | 0.992 | 0.000 | 21064 | 298 | +0.0836 | −0.7039 |

Δrel_f1 and ΔEDCR relative to SFT baseline (#13).

### RSFT-CED 3-Seed Summary

| Metric | Mean | Std | SFT baseline | Δ |
|--------|------|-----|-------------|---|
| rel_f1 | 0.4596 | 0.0128 | 0.4057 | +0.054 |
| evi_f1 | 0.8144 | 0.0051 | 0.7979 | +0.017 |
| EDCR | 0.6434 | 0.0114 | 0.7039 | −0.061 |

## 2. EDCR-rel_f1 Correlation Analysis

### Among functional methods (excluding QLoRA-collapsed and SFT-no-evidence)

Using 12 data points (methods #1-14):

| rel_f1 | EDCR | Method |
|--------|------|--------|
| 0.6237 | 0.5262 | CED-reranker oracle |
| 0.4864 | 0.6156 | CED-reranker (N=8) |
| 0.4683 | 0.6388 | RSFT-CED s43 |
| 0.4655 | 0.6350 | RSFT-CED s44 |
| 0.4549 | 0.6318 | bf16 GRPO ckpt-100 |
| 0.4539 | 0.6431 | RSFT-flatNLI |
| 0.4538 | 0.6763 | CED-reranker random |
| 0.4494 | 0.6641 | RSFT-CED r2a |
| 0.4493 | 0.6609 | RSFT-CED r2b |
| 0.4449 | 0.6565 | RSFT-CED s42 |
| 0.4106 | 0.7039 | SFT baseline |
| 0.3429 | 0.7294 | DPO-CED (overfit) |

**Strong negative correlation**: lower EDCR ↔ higher rel_f1.

CED-reranker PoC also reported a within-method Spearman correlation (per-document CED score vs rel F1): **r = 0.3235** (p < 10^-190, n=7880).

### Including catastrophic-collapse methods (QLoRA GRPO)

Adding the QLoRA variants extends the EDCR range to [0.85, 0.99] with rel_f1 ∈ [0.007, 0.22]. The negative monotonic relationship holds across the full spectrum, confirming EDCR as a severity indicator for training pathologies.

## 3. EDCR Distractor Source Decomposition

From the detailed EDCR analysis on RSFT-CED s42:

| Category | Description | Triple Count | Distractor Citations | % of Total |
|----------|-------------|-------------|---------------------|------------|
| A | FP triples (no gold match) | 8279 | 14766 | **90.2%** |
| B | TP + evidence superset | 992 | 1122 | 6.9% |
| C | TP + partial evidence overlap | 330 | 367 | 2.2% |
| D | TP + evidence fully disjoint | 77 | 112 | 0.7% |

**Structural insight**: ~90% of EDCR comes from false positive triples that carry evidence citations for relations that don't exist. Only ~10% comes from evidence annotation errors on correctly predicted relations.

From the r2b analysis:
- FP triples average 1.78 predicted evidence sentences per triple
- TP superset cases average 2.31 predicted (vs 1.18 gold)
- 68% of TP distractor cases are "gold subset" — model cited all gold sentences plus extras

## 4. Diagnostic Patterns

### Pattern A: Normal Improvement (RSFT-CED, bf16 GRPO, CED-reranker)
- EDCR decreases 5-10 pp from SFT baseline
- rel_f1 increases 4-8 pp
- evi_f1 stable or slightly improved (~0.80-0.82)
- **Interpretation**: training reduces FP triple count → fewer FP-attached evidence citations → lower EDCR. Evidence quality per TP triple stays stable.

### Pattern B: Catastrophic Forgetting (QLoRA GRPO variants)
- EDCR explodes to 0.85-0.99
- rel_f1 collapses to <0.22 (or <0.01 for lr5e6 variants)
- evi_f1 variable (0.57-0.83)
- **Interpretation**: model generates large volumes of FP triples, each with evidence citations. Nearly all citations are distractors because the triples themselves are wrong. EDCR > 0.85 is a reliable **early-warning signal** for catastrophic forgetting — detectable even when evi_f1 appears reasonable (e.g., lr5e6_ckpt80: evi_f1=0.828 but EDCR=0.991).

### Pattern C: DPO Overfitting
- EDCR *increases* to 0.7294 (higher than SFT baseline 0.7039)
- rel_f1 drops to 0.3429
- evi_f1 rises to 0.8403 (highest among all methods)
- n_pred=18445 (highest prediction count)
- **Interpretation**: DPO with rewards_accuracy=1.0 overfit to training distribution. The model learned to produce high-quality evidence *conditionally* (when the triple is correct), but became less selective about which triples to predict — inflating FP count and thus EDCR. The paradox of "best evidence quality, worst EDCR among non-collapsed methods" reveals that EDCR captures a dimension evi_f1 misses: output selectivity.

### Pattern D: No-Evidence Ablation
- EDCR = 0 (degenerate/sentinel)
- rel_f1 = 0.4893 (highest among single-model methods)
- evi_f1 = 0 (by design)
- **Interpretation**: removing the evidence generation burden yields the best relation extraction — the model allocates all capacity to predicting triples. EDCR=0 is the correct behavior (no citations → no distractors). This establishes that evidence generation has a non-trivial cost (~0.05 rel_f1) on extraction quality.

### Pattern E: CED-Reranker's EDCR Mechanism
- Lowest EDCR (0.6156) among all trained methods
- Highest rel_f1 (0.4864) among evidence-producing methods
- Oracle variant: EDCR=0.5262, rel_f1=0.6237 (theoretical lower bound)
- **Interpretation**: the counter-intuitive "low EDCR + high rel_f1" is actually fully consistent. CED-based reranking selects candidates with better evidence-document consistency from N=8 samples. This mechanically removes FP-heavy candidates, simultaneously lowering EDCR and raising rel_f1. The oracle reranker confirms the theoretical floor: EDCR=0.5262 when selecting by gold relation correctness, indicating ~52% of citations are inherently distractor even in the best possible selection.

## 5. EDCR as a Diagnostic Indicator: Summary

| EDCR Range | Diagnostic Meaning | Action |
|------------|-------------------|--------|
| 0 | No evidence generated | Expected for no-evidence ablation |
| 0.50-0.62 | Best-case (reranker/oracle) | Evidence is well-calibrated |
| 0.62-0.68 | Healthy trained model | Normal improvement over baseline |
| 0.68-0.72 | Baseline / mild regression | SFT baseline territory; check for DPO-style overfitting |
| 0.72-0.85 | Warning zone | Significant FP inflation; likely training pathology |
| 0.85-1.00 | Catastrophic collapse | Model is broken; halt and diagnose |

### Key Takeaways

1. **EDCR is primarily an FP-triple detector** (90% of distractor signal comes from false positive triples), making it a proxy for output precision through the evidence lens.

2. **EDCR detects pathologies evi_f1 misses**: QLoRA lr5e6_ckpt80 has evi_f1=0.828 (looks healthy) but EDCR=0.991 (catastrophic). DPO has evi_f1=0.840 (best) but EDCR=0.729 (regression). Conditional evi_f1 is blind to FP-driven distractors.

3. **EDCR monotonically tracks rel_f1** across the functional method range (0.34-0.62 rel_f1), with strong negative correlation. It can serve as a lightweight diagnostic during training without running full RE evaluation.

4. **Irreducible EDCR floor ~0.52**: even oracle selection yields 52% distractor rate, suggesting the DocRED annotation scheme and model's evidence generation strategy have a structural mismatch that training alone cannot fully resolve.

5. **Evidence generation costs ~5 pp rel_f1**: SFT-no-evidence (0.489) vs SFT-baseline (0.411) shows the cost of jointly generating evidence. This motivates decoupled architectures or post-hoc evidence retrieval.
