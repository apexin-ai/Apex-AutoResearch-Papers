## Complete Diagnostic Cascade Table (2026-05-22, corrected)

All finetuned, N=8, seed=42.

| Task | Dataset | Degen% | LP-F1 ρ (pooled) | LP-F1 ρ (within) | MV Δ(pp) | LP-best Δ(pp) | Zero-F1% |
|------|---------|--------|-------------------|-------------------|----------|---------------|----------|
| NER | FewNERD | 8.8 | 0.674 | 0.541 | −2.74 | — | 5.4 |
| NER | SciERC | 13.4 | 0.312 | 0.188 | −1.24 | −0.32 | 4.7 |
| NER | CoNLL | 56.7 | 0.411 | 0.284 | +0.20 | −1.62 | 2.7 |
| RE | SciERC | 10.1 | 0.350 | 0.157 | −5.90 | −0.94 | 40.1 |

### Key Findings (updated)
1. MV Δ is worst for RE (−5.90pp), confirming MV failure at low agreement
2. LP-F1 ρ is moderate for RE (0.350 pooled) — not as weak as originally reported
3. RE has the highest zero-F1 rate (40.1%) but NOT 71.8% as originally reported
4. Oracle headroom is large for RE (+18.08pp) — much more room than originally reported (+7.89pp)
5. LP-best slightly hurts RE (−0.94pp), not near-zero as originally reported (+0.08pp)

### Data Sources
- SciERC NER: output/scierc_mf4v2_seed42/samples.jsonl (551 instances)
- CoNLL NER: output/conll_mf4v2_seed42/samples.jsonl (3453 instances, on 5090-c)
- FewNERD NER: output/fewnerd_mf4v2_seed42_v3/samples.jsonl (37648 instances, on 5090-c)
- SciERC RE: output/exp_012_rerun_1024/samples_with_logprobs.jsonl (397 RE instances)
- Script: code/re_diagnostic_cascade.py (corrected version)
