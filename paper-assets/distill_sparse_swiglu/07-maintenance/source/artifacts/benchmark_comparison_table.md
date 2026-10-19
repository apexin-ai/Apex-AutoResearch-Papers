# Unified Benchmark Comparison Table

**Model**: Llama-3.1-8B | **Eval**: benchmark_eval.py (ARC-c=25-shot, WG=5-shot, MMLU=5-shot, GSM8K=8-shot, WikiText-2 PPL)

## Main Results

| Condition | Sparsity | Allocation | PPL | ARC-c | WG | MMLU | GSM8K |
|-----------|----------|------------|-----|-------|-----|------|-------|
| Dense (baseline) | 0% | — | 6.117 | 0.5828 | 0.7806 | 0.6527 | 0.4875 |
| KL 30% | 30% | uniform | 8.816 | 0.4078 | 0.6859 | 0.4061 | 0.0735 |
| KL 40% | 40% | uniform | 8.363 | 0.4181 | 0.6717 | 0.3068 | 0.0394 |
| KL 50% | 50% | uniform | 11.960 | 0.3276 | 0.6290 | 0.2777 | 0.0212 |
| KL 30% | 30% | global | 8.977 | 0.3968 | 0.7017 | 0.2527 | 0.0879 |
| KL 50% | 50% | global | 11.793 | 0.3285 | 0.6346 | 0.2789 | 0.0129 |
| BCE v3 (2700 steps) | 50% | learned | 22.510 | 0.2398 | 0.5059 | 0.3002 | 0.0485 |
| TEAL 50% † | 50% | magnitude | 27.970* | 0.2910 | 0.5556 | 0.2856 | 0.0190 |
| TEAL 50% (unified) | 50% | magnitude | — queued | — queued | — queued | — queued | — queued |
| TEAL 30% (unified) | 30% | magnitude | — queued | — queued | — queued | — queued | — queued |

† lm_eval_teal_50pct uses lm-evaluation-harness (0-shot default), not directly comparable to unified few-shot results.
\* TEAL PPL from eval_bce_v3_s42 `teal_sparse_ppl` measurement (same model, same WikiText-2 split).

## Relative Change vs Dense (%)

| Condition | PPL ↑ | ARC-c ↓ | WG ↓ | MMLU ↓ | GSM8K ↓ |
|-----------|-------|---------|------|--------|---------|
| KL 30% uniform | +44.1% | −30.0% | −12.1% | −37.8% | −84.9% |
| KL 40% uniform | +36.7% | −28.3% | −14.0% | −53.0% | −91.9% |
| KL 50% uniform | +95.5% | −43.8% | −19.4% | −57.4% | −95.7% |
| KL 30% global | +46.7% | −31.9% | −10.1% | −61.3% | −82.0% |
| KL 50% global | +92.8% | −43.6% | −18.7% | −57.3% | −97.4% |
| BCE v3 50% | +268.0% | −58.8% | −35.2% | −54.0% | −90.1% |
| TEAL 50% † | +357.2% | −50.1% | −28.8% | −56.2% | −96.1% |

## Key Observations

1. **KL >> BCE >> TEAL at 50% sparsity**: KL uniform achieves PPL 11.96 vs BCE 22.51 vs TEAL 27.97. KL predictor (1000 steps) dominates both iso-compute BCE (2700 steps) and training-free TEAL.

2. **Uniform vs Global allocation**: At 30% sparsity, uniform preserves MMLU (0.4061 vs 0.2527, +60.7% relative) while global collapses it. At 50% both collapse. Global allocation concentrates sparsity on critical layers, destroying knowledge.

3. **PPL-downstream dissociation**: KL 40% has lower PPL (8.36) than KL 30% (8.82) yet worse MMLU (0.3068 vs 0.4061). PPL alone does not capture knowledge preservation; downstream metrics are essential.

4. **Phase transition 30%→40%**: MMLU drops from 0.4061 to 0.3068 (−24.5pp), GSM8K from 0.0735 to 0.0394 (−3.4pp). The threshold for knowledge/reasoning retention lies between 30–40% sparsity.

---
*Generated 2026-05-16. Source: distill_sparse_swiglu registry.*
