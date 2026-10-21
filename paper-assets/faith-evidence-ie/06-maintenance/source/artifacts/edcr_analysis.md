# EDCR Cross-Method Diagnostic Analysis

## 1. The EDCR Paradox

Across all evidence-producing methods, **rel_f1 and EDCR are strongly negatively correlated**: methods with higher relation extraction performance consistently show lower EDCR.

| rel_f1 range | EDCR range | Representative methods |
|-------------|-----------|----------------------|
| 0.48–0.49 | 0.61–0.62 | CED reranker |
| 0.44–0.47 | 0.63–0.66 | RSFT-CED variants, flat-NLI, bf16 GRPO |
| 0.40–0.41 | 0.71 | SFT baseline |
| 0.22 | 0.85 | QLoRA GRPO (catastrophic) |

**Spearman ρ = −0.905** (n=8 methods, including QLoRA GRPO catastrophic case).

This is not a paradox but a predictable consequence of how EDCR is defined. EDCR measures the proportion of predictions where cited evidence genuinely supports the predicted relation. When a model becomes more aggressive in prediction (higher recall → higher F1), the marginal predictions tend to carry weaker evidence support, diluting the average EDCR.

## 2. Mechanistic Explanation

EDCR ≈ (predictions with correctly coupled evidence) / (total predictions).

The key driver is **prediction count**:

| Method | n_pred | rel_f1 | EDCR |
|--------|--------|--------|------|
| QLoRA GRPO | 7,460 | 0.2167 | 0.8539 |
| SFT baseline | 12,234 | 0.4057 | 0.7118 |
| bf16 GRPO | 10,701 | 0.4549 | 0.6318 |
| CED reranker | 14,782 | 0.4864 | 0.6156 |
| RSFT-CED r1 | 15,307 | 0.4449 | 0.6565 |

Three regimes emerge:

1. **Under-prediction** (QLoRA GRPO, 7460 preds vs 12151 gold): Model predicts conservatively. The few predictions it makes have high evidence coupling, but it misses most relations entirely. High EDCR is an artifact of low coverage, not quality.

2. **Calibrated prediction** (SFT baseline, ~12234 preds ≈ 12151 gold): Prediction count roughly matches gold count. EDCR reflects genuine evidence quality at the model's natural operating point.

3. **Over-prediction** (RSFT/CED reranker, 14782–15307 preds): Recall-oriented training pushes models to generate ~25% more predictions than gold. The additional predictions often cite plausible but non-supporting evidence sentences → EDCR drops. However, the F1 gain from increased recall outweighs the precision loss.

## 3. EDCR's Diagnostic Value

### What EDCR reveals that rel_f1/evi_f1 cannot

**evi_f1 is a recall-oriented metric over evidence sentences.** It answers: "did the model cite the right evidence sentences?" But it does not assess whether those evidence sentences are correctly *paired* with their respective relations. A model could cite all correct evidence sentences but assign them to wrong relations, achieving high evi_f1 but low EDCR.

**EDCR captures evidence-relation alignment quality.** It answers: "for each predicted relation, does the cited evidence actually support *that specific* relation?"

Concrete diagnostic examples:

- **CED reranker** (rel_f1=0.4864, evi_f1=0.8188, EDCR=0.6156): Best at finding relations, good at recalling evidence, but worst at coupling them correctly. The reranking selects candidates that maximize individual component scores, not joint evidence-relation coherence.

- **SFT baseline** (rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118): Modest relation/evidence performance, but highest evidence-relation coupling among working methods. The base model's predictions are conservative but well-grounded.

- **QLoRA GRPO** (rel_f1=0.2167, evi_f1=0.5746, EDCR=0.8539): Catastrophic collapse in extraction ability, but extremely high EDCR. This reveals the failure mode: the model learned to suppress generation rather than improve it. The few relations it produces are well-evidenced, but it abandoned the extraction task.

### bf16 GRPO checkpoint trajectory

The GRPO checkpoint sweep reveals a training dynamic:

| ckpt | rel_f1 | EDCR | Δrel_f1 | ΔEDCR |
|------|--------|------|---------|-------|
| 80 | 0.4456 | 0.6409 | — | — |
| 90 | 0.4523 | 0.6414 | +0.0067 | +0.0005 |
| 100 | 0.4549 | 0.6318 | +0.0026 | −0.0096 |

From ckpt-80 to ckpt-90: both rel_f1 and EDCR improve (Pareto improvement). From ckpt-90 to ckpt-100: rel_f1 still improves but EDCR drops — the model is trading evidence coupling quality for extraction recall. This suggests ckpt-90 may be a better operating point when evidence quality matters.

## 4. RSFT Seed Variance

| Metric | Mean ± Std | CV |
|--------|-----------|-----|
| rel_f1 | 0.4596 ± 0.0127 | 2.8% |
| evi_f1 | 0.8143 ± 0.0052 | 0.6% |
| EDCR | 0.6434 ± 0.0111 | 1.7% |

EDCR variance across seeds is moderate (CV=1.7%), between rel_f1 (higher variance) and evi_f1 (very stable). This suggests EDCR captures a relatively stable property of the training method rather than being dominated by random seed effects.

## 5. Paper Claims

Based on this analysis, the paper can make the following claims:

1. **EDCR as complementary metric**: EDCR fills a blind spot between rel_f1 (relation correctness) and evi_f1 (evidence recall) by measuring evidence-relation *coupling* quality. Neither rel_f1 nor evi_f1 captures whether the right evidence is paired with the right relation.

2. **Recall-oriented training degrades EDCR**: All methods that improve rel_f1 over SFT baseline (RSFT, GRPO, CED reranker) show lower EDCR. This is a quantifiable trade-off: +0.08 rel_f1 (CED reranker vs SFT) costs −0.096 EDCR. This trade-off should be reported transparently.

3. **EDCR detects catastrophic failure modes**: QLoRA GRPO's high EDCR (0.8539) combined with catastrophic rel_f1 (0.2167) exposes a generation-suppression failure that evi_f1 alone partially reveals but EDCR makes unmistakable.

4. **EDCR enables training-phase diagnostics**: The GRPO checkpoint trajectory shows EDCR can detect the point where continued training trades evidence quality for extraction recall, potentially guiding early stopping or checkpoint selection.

5. **Limitation to acknowledge**: EDCR is inversely correlated with rel_f1 (ρ = −0.905) by construction — more predictions mechanically lower average coupling quality. It should not be used as a standalone optimization target but as a diagnostic complement that reveals the quality-quantity trade-off in faithfully-grounded IE.
