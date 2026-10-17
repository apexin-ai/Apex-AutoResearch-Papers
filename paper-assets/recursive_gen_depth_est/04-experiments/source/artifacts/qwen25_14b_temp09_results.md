# qwen25_14b_temp09 — Final Results

**Model**: Qwen2.5-14B | **Precision**: FP16 | **Reference**: self (Qwen2.5-14B)
**Temperature**: 0.9 | **Samples**: 5000 per depth (d0–d3), 20000 total | **Features**: 19 (self-ref)
**Server**: gpu-6000pro-2 | **Runtime**: 24.9h | **Seed**: 42

## Classification Results

### RF 4-class (d0–d3), 5-fold CV
- **Accuracy**: 50.5% (95% CI: [49.76%, 51.24%])
- **Chance baseline**: 25% → **2.02× chance**

### LR 4-class, 5-fold CV
- **Accuracy**: 48.65% (95% CI: [48.01%, 49.38%])

### RF 3-class (d1/d2/d3 only), 5-fold CV
- **Accuracy**: 52.44% (95% CI: [51.61%, 53.23%])
- **Chance baseline**: 33.3% → **1.57× chance**

## Pairwise AUC (RF)

| Pair | AUC |
|------|-----|
| d0v1 | 0.6318 |
| d0v2 | 0.9178 |
| d0v3 | 0.9584 |
| d1v2 | 0.7259 |
| d1v3 | 0.8447 |
| d2v3 | 0.6184 |

**Adjacent-depth AUC**: d0v1=0.63, d1v2=0.73, d2v3=0.62. Note: under nucleus (scale_002), d2v3=0.728 was the strongest adjacent boundary; under temp09, d2v3=0.618 is the weakest — temperature scaling accelerates d2→d3 convergence (§3 theory).

### Pairwise AUC (LR)

| Pair | AUC |
|------|-----|
| d0v1 | 0.5637 |
| d0v2 | 0.9158 |
| d0v3 | 0.9430 |
| d1v2 | 0.7318 |
| d1v3 | 0.8314 |
| d2v3 | 0.6150 |

## Top-10 Feature Importance (RF)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | p90_ppl | 0.0768 |
| 2 | skew_ppl | 0.0755 |
| 3 | kurt_ppl | 0.0730 |
| 4 | p90_surprisal | 0.0721 |
| 5 | var_surprisal | 0.0707 |
| 6 | mean_surprisal | 0.0587 |
| 7 | hapax_ratio | 0.0558 |
| 8 | type_token_ratio | 0.0546 |
| 9 | median_surprisal | 0.0543 |
| 10 | median_ppl | 0.0533 |

## Data Completeness

| File | Lines |
|------|-------|
| depth_0.jsonl | 5000 |
| depth_1.jsonl | 5000 |
| depth_2.jsonl | 5000 |
| depth_3.jsonl | 5000 |
| features_self_ref.jsonl | 20000 |

## Checkpoints

- `lora_depth_0`, `lora_depth_1`, `lora_depth_2` at `/root/autodl-tmp/recursive_gen_depth_est/checkpoints/qwen25_14b_temp09/`

## Metrics Not Available

Per-depth recall, confusion matrix, MAE, QWK, EDD_{0.70} — not computed by this pipeline run.

## Assessment

**Conclusion: success**. RF 4-class 50.5% is 2× chance (25%), confirming depth signal persists at 14B scale under temperature sampling (τ=0.9). Adjacent-depth AUC shows a non-monotonic pattern (d0v1=0.63 < d1v2=0.73 > d2v3=0.62), with d1v2 being the most separable pair. This contrasts with 14B nucleus where d2v3=0.728 was the strongest adjacent boundary (monotonically increasing). The reversal is strategy-specific: temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths — d2→d3 feature space collapse happens faster under temperature than under nucleus truncation (consistent with §3 theoretical analysis). Feature importance dominated by tail perplexity (p90_ppl) and distribution shape (skew, kurtosis) — consistent with other atlas cells.

Compared to other temp09 cells in the atlas, 50.5% is lower than smaller models (pythia ~73%, olmo ~81%, gpt2xl ~83%), confirming 14B generates more coherent recursive text that compresses inter-depth statistical distances. This aligns with the scaling hypothesis.
