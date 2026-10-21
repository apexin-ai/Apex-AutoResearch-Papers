# test_eval_llama_rsft_s42_no_evi_v2 Analysis

## Key Metrics

| Metric | Value |
|--------|-------|
| Ign-F1 / F1 | 0.3380 |
| Precision | 0.4639 |
| Recall | 0.2659 |
| Evi-F1 (TP) | 0.0075 |
| Evi-F1 (DREEAM/joint) | 0.0067 |
| EDCR | 0.9374 |
| Format OK | 499/500 (99.8%) |
| Truncated | 263/500 |
| Predictions (scored) | 9,943 |
| TP | 4,613 |
| Gold count | 17,350 |
| batch_size | 16 |
| seed | 42 |
| no_evidence | true |

## Evidence Tax (s42, batch_size=16)

| Condition | Ign-F1 | Source |
|-----------|--------|--------|
| with-evi (v3) | 0.3554 | test_eval_llama_rsft_s42_with_evi_v3 |
| no-evi (v2) | 0.3380 | this experiment |
| **Tax** | **-1.74pp** | |

Evidence helps: removing evidence costs 1.74pp on s42.

## Comparison with Original s42 no-evi (batch_size=1)

| | batch_size=1 (orig) | batch_size=16 (v2) | Delta |
|---|---|---|---|
| Ign-F1 | 0.3334 | 0.3380 | **+0.46pp** |
| Evidence tax | -2.20pp | -1.74pp | +0.46pp |

batch_size=16 improved Ign-F1 by +0.46pp, reducing the apparent evidence tax from -2.20pp to -1.74pp. The original -2.20pp was inflated by the batch_size=1 confound.

## Comparison with s43 no-evi

| Seed | no-evi Ign-F1 | with-evi Ign-F1 | Tax |
|------|---------------|-----------------|-----|
| s42 (v2, bs=16) | 0.3380 | 0.3554 | -1.74pp |
| s43 (bs=16) | 0.3371 | 0.3488 | -1.17pp |

s42 and s43 no-evi are now closely matched (0.3380 vs 0.3371, diff=0.09pp), confirming the original divergence was a batch_size artifact.

## Impact on LLaMA Multi-seed Evidence Tax

### Before (with batch_size=1 confound)
- s42: -2.20pp, s43: -1.17pp
- Mean: **-1.69pp**, spread: 1.03pp

### After (both batch_size=16)
- s42: -1.74pp, s43: -1.17pp
- Mean: **-1.46pp**, spread: 0.57pp

Corrections:
1. Mean evidence tax shrinks from -1.69pp to -1.46pp (evidence still helps, but less than previously estimated)
2. Cross-seed variance halves (spread 1.03pp → 0.57pp), improving estimate reliability
3. Both seeds consistently show evidence helps (negative tax), with s42 showing a larger benefit than s43
