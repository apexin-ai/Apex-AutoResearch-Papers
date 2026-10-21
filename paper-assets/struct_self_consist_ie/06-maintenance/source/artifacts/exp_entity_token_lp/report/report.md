# Entity-Token LP vs Full-Sequence LP for Sample Selection

## Setup

- Model: Qwen3-8B fine-tuned (SciERC / CoNLL2003)
- n_samples = 8, temperature = 0.7
- Per-token logprobs extracted from vLLM 0.18.1 via `output.logprobs`
- Entity tokens identified by matching `"text": "<mention>"` patterns in reconstructed token text, mapping char offsets to token indices
- Entity-token LP = mean logprob of tokens corresponding to entity mention text in JSON output
- Full-sequence LP = mean logprob of all output tokens (cumulative_logprob / n_tokens)

## Results

| Metric | SciERC (n=529) | CoNLL (n=2756) |
|--------|---------------|----------------|
| Greedy F1 | 0.6430 | 0.9065 |
| Full-LP Selection F1 | 0.6465 (+0.35pp) | 0.8989 (-0.76pp) |
| Entity-LP Selection F1 | 0.6262 (-1.68pp) | 0.8659 (-4.06pp) |
| Majority Vote F1 | 0.6265 | 0.8879 |
| Oracle F1 | 0.7845 | 0.9480 |

## Within-Instance Variance

| Metric | SciERC | CoNLL |
|--------|--------|-------|
| Full-LP median variance | 1.61e-4 | 4.58e-4 |
| Entity-LP median variance | 6.44e-4 | 2.02e-10 |
| Entity-LP / Full-LP ratio | 4.0x | ~0x |
| Full-LP tied fraction (<0.01 range) | 1.9% | 18.4% |
| Entity-LP tied fraction (<0.01 range) | 35.0% | 79.4% |

## Entity Token Statistics

| Metric | SciERC | CoNLL |
|--------|--------|-------|
| Median entity tokens per sample | 10 | 5 |
| Median total tokens per sample | 188 | 66 |
| Mean entity token fraction | 5.3% | 7.7% |

## Key Findings

1. **Entity-LP selection is strictly worse than full-LP selection on both datasets.** On SciERC, entity-LP loses 2.03pp vs full-LP; on CoNLL, it loses 3.30pp. Neither LP-based method consistently beats greedy.

2. **Entity-LP variance is dataset-dependent.** On SciERC, entity-LP has 4x higher median within-instance variance than full-LP, confirming the hypothesis that focusing on entity tokens amplifies signal differences. However, on CoNLL, entity-LP has essentially zero variance (median ~0), because the model is extremely confident on entity tokens (logprobs near 0.0).

3. **CoNLL entity tokens are saturated.** With 79.4% of instances having entity-LP range < 0.01, the entity-token signal is useless for discrimination on CoNLL. The model has learned the NER patterns so well that entity tokens are generated with near-certainty.

4. **SciERC entity-LP has more variance but noisier signal.** Despite 4x higher variance, entity-LP selection is worse because the variance comes from a small number of tokens (median 10 out of 188 = 5.3%) and is more influenced by random fluctuations in individual entity-mention logprobs.

5. **When entity-LP and full-LP disagree on sample selection:**
   - SciERC: 443 disagreements, full-LP wins 105 vs entity-LP wins 80 (full-LP is better in 56.8% of contested cases)
   - CoNLL: 1920 disagreements, full-LP wins 242 vs entity-LP wins 94, 1584 ties in F1 outcome

6. **Z-score normalization is irrelevant for within-instance selection.** Z-score is a monotonic transform of raw logprobs within each instance, so argmax(z_lps) == argmax(raw_lps). It only matters for cross-instance comparisons.

## Conclusion

**Entity-token LP does not improve sample selection F1.** The hypothesis that focusing on entity-relevant tokens would provide a better quality signal is not supported. On high-confidence tasks (CoNLL), entity tokens are saturated and carry no discriminative information. On harder tasks (SciERC), the higher variance in entity-LP reflects noise rather than signal, because the entity-token subset is too small (5.3% of tokens) to be a reliable quality indicator.

Full-sequence LP remains the better (though still weak) proxy for sample quality. The oracle gap (greedy vs oracle: +14pp SciERC, +4pp CoNLL) suggests that better selection methods could yield significant gains, but LP-based approaches are limited because LP correlates weakly with output correctness.
