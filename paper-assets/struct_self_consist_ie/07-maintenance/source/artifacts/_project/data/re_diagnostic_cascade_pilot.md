## RE Diagnostic Cascade Pilot (2026-05-22, corrected)

### SciERC RE (finetuned, N=8, 397 instances)

Data: exp_012_rerun_1024/samples_with_logprobs.jsonl

| Metric | Value |
|--------|-------|
| Degeneracy | 10.1% (40/397) |
| LP-F1 ρ (pooled) | 0.3501 |
| LP-F1 ρ (within-instance) | 0.1573 |
| Greedy F1 | 0.4042 |
| MV F1 | 0.3452 (Δ = -5.90pp) |
| LP-best F1 | 0.3948 (Δ = -0.94pp) |
| Oracle F1 | 0.5850 (Δ = +18.08pp) |
| Zero-F1% | 40.1% (159/397) |

### Cross-task Diagnostic Comparison

| Task | Dataset | Degen% | LP-F1 ρ | MV Δ(pp) | LP-best Δ(pp) | Zero-F1% |
|------|---------|--------|---------|----------|---------------|----------|
| NER | SciERC | 13.4 | — | -1.24 | -0.32 | — |
| NER | CoNLL | 56.7 | — | +0.20 | -1.62 | — |
| NER | FewNERD | 8.8 | — | -2.74 | — | — |
| RE | SciERC | 10.1 | 0.350 | -5.90 | -0.94 | 40.1 |

### Bug Fix (2026-05-22)

Original values were ALL wrong because the worker script used `re_sc/re_samples.jsonl`
on autodl-5090-c (a much weaker model run) instead of the canonical data on autodl-5090.
Additional bugs: text-based matching instead of span-based, and "all samples zero" instead
of "greedy zero" for zero-F1 definition.
