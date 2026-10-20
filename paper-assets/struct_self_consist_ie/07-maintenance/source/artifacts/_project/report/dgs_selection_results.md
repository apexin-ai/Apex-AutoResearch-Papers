# DGS (Degeneracy-Gated Selection) Results

Generated: 2026-05-18
Source: `output/dgs_selection_results.json`
Script: `code/analysis_degen_gated_selection.py`
Config: N=8 samples/instance, gold-filtered datasets

## DGS Logic

- Degenerate instance (all N sample F1s identical) -> use greedy (first sample)
- Non-degenerate instance -> use LP-best (highest mean log-probability sample)

---

## Summary Table

| Dataset | N | Degen% | Greedy F1 | LP-all F1 | DGS F1 | Oracle F1 | DGS-Greedy (pp) | DGS-LP (pp) |
|---------|---:|-------:|----------:|----------:|-------:|----------:|-----------------:|------------:|
| SciERC  | 551 | 18.7% | 0.6436 | 0.6495 | 0.6507 | 0.7775 | +0.71 | +0.12 |
| CoNLL   | 3453 | 62.0% | 0.9087 | 0.8985 | 0.8985 | 0.9520 | **-1.02** | 0.00 |
| FewNERD | 5000 | 23.1% | 0.7713 | 0.7800 | 0.7805 | 0.8831 | +0.92 | +0.04 |

---

## Bootstrap 95% CIs

### DGS vs Greedy (paired bootstrap, 10k resamples)

| Dataset | Delta (pp) | 95% CI | Significant? |
|---------|----------:|-------:|:------------:|
| SciERC  | +0.71 | [-0.59, +2.07] | No |
| CoNLL   | -1.02 | [-1.41, -0.64] | **Yes (WORSE)** |
| FewNERD | +0.92 | [+0.49, +1.36] | Yes |

### DGS vs LP-all (paired bootstrap)

| Dataset | Delta (pp) | 95% CI | Significant? |
|---------|----------:|-------:|:------------:|
| SciERC  | +0.12 | [0.00, +0.36] | Borderline |
| CoNLL   | 0.00  | [0.00, 0.00]  | No (identical) |
| FewNERD | +0.04 | [0.00, +0.10] | No |

---

## Degenerate vs Non-degenerate Breakdown

### SciERC (103 degen / 448 non-degen)

| Group | Greedy F1 | LP F1 | Oracle F1 | LP-Greedy (pp) |
|-------|----------:|------:|----------:|---------------:|
| Degenerate | 0.6207 | = greedy | 0.6142 | n/a |
| Non-degen  | 0.6489 | 0.6576 | 0.8150 | +0.87 [-0.74, +2.54] |

### CoNLL (2141 degen / 1312 non-degen)

| Group | Greedy F1 | LP F1 | Oracle F1 | LP-Greedy (pp) |
|-------|----------:|------:|----------:|---------------:|
| Degenerate | 0.9431 | = greedy | 0.9431 | n/a |
| Non-degen  | 0.8524 | 0.8255 | 0.9666 | **-2.69 [-3.70, -1.69]** |

### FewNERD (1156 degen / 3844 non-degen)

| Group | Greedy F1 | LP F1 | Oracle F1 | LP-Greedy (pp) |
|-------|----------:|------:|----------:|---------------:|
| Degenerate | 0.7790 | = greedy | 0.7772 | n/a |
| Non-degen  | 0.7690 | 0.7809 | 0.9149 | +1.19 [+0.61, +1.76] |

---

## Verdict

**DGS is NOT a viable method contribution.**

1. **CoNLL: DGS significantly worse than greedy** (-1.02pp, CI entirely below 0). Root cause: LP selection is significantly worse than greedy on non-degenerate CoNLL instances (-2.69pp). High degeneracy rate (62%) means most instances fall through to greedy, but the non-degenerate LP penalty dominates.

2. **SciERC: not significant.** +0.71pp but CI crosses zero [-0.59, +2.07].

3. **FewNERD: significant vs greedy** (+0.92pp) but DGS adds essentially nothing over plain LP-all (+0.04pp, not significant). The gating mechanism provides no value.

4. **DGS vs LP-all is never significantly positive.** The degeneracy gate adds no meaningful improvement over simply using LP selection on all instances.

**Implication for paper framing**: The paper remains pure diagnostic. DGS cannot be positioned as a method contribution.
