# Pretrained FewNERD Per-Type MV Analysis (θ=0.5 strict)

**Model**: Qwen2.5-7B-Instruct (pretrained, no finetuning)
**Dataset**: FewNERD test set (37,648 instances, 32,565 with gold entities)
**N**: 8 samples per instance
**θ**: 0.5 strict (count > N/2, i.e. ≥5/8 votes required)
**Seeds**: 42, 123, 456

## 3-seed average

| Entity Type | n_inst | greedy_f1 | MV F1 | MV Δ (pp) |
|-------------|--------|-----------|-------|-----------|
| person | 8,016 | 0.6374±0.0003 | 0.6792±0.0046 | +4.17±0.43 |
| organization | 6,647 | 0.5247±0.0007 | 0.5562±0.0059 | +3.15±0.54 |
| location | 8,023 | 0.5650±0.0008 | 0.5898±0.0007 | +2.47±0.01 |
| event | 1,306 | 0.4277±0.0008 | 0.4510±0.0021 | +2.34±0.28 |
| building | 1,587 | 0.4379±0.0017 | 0.4577±0.0021 | +1.98±0.04 |
| product | 2,276 | 0.4932±0.0017 | 0.5110±0.0008 | +1.78±0.24 |
| art | 1,277 | 0.4224±0.0009 | 0.4297±0.0073 | +0.73±0.70 |
| other | 3,433 | 0.3761±0.0014 | 0.3717±0.0029 | −0.45±0.32 |

## Correlation

| Metric | Value |
|--------|-------|
| Pearson r(greedy_f1, MV_delta) | r=0.8620, p=0.0059 |
| Spearman ρ(greedy_f1, MV_delta) | ρ=0.8810, p=0.0039 |

Per-seed Pearson r: seed42=0.8385 (p=0.009), seed123=0.9007 (p=0.002), seed456=0.7690 (p=0.026)

## Pretrained vs Finetuned Comparison (θ=0.5 strict)

| Entity Type | Pretrained MV Δ | Finetuned MV Δ | Direction |
|-------------|----------------|----------------|-----------|
| person | +4.17 | −0.67 | **FLIP** |
| organization | +3.15 | −2.65 | **FLIP** |
| location | +2.47 | −1.52 | **FLIP** |
| event | +2.34 | −3.17 | **FLIP** |
| building | +1.98 | −3.90 | **FLIP** |
| product | +1.78 | −3.38 | **FLIP** |
| art | +0.73 | −1.51 | **FLIP** |
| other | −0.45 | −3.02 | SAME |

Finetuned reference: θ=0.5 strict, exp_021 seed=42.

**7/8 entity types flip direction**: pretrained shows positive MV delta (SC helps), finetuned shows negative (SC hurts). Only "other" stays negative in both settings, likely due to its heterogeneous nature (catch-all category with lowest greedy F1).

**Positive correlation in pretrained**: higher greedy_f1 types benefit more from MV (r=0.86, p<0.01), suggesting SC amplifies existing model capability when the model hasn't been finetuned.

## Data paths

- seed=42: `autodl-5090:output/e2_pretrained_fewnerd/samples.jsonl`
- seed=123: `autodl-5090-c:output/e2_pretrained_fewnerd_s123/samples.jsonl`
- seed=456: `autodl-5090:output/e2_pretrained_fewnerd_s456/samples.jsonl`
- JSON output: `autodl-5090:output/pretrained_fewnerd_per_type_mv_analysis.json`
