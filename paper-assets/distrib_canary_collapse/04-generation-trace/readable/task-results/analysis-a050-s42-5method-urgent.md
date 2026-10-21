# analysis a050 s42 5method urgent

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a050_s42_5method_urgent_20260516T203706_result.json`
- **Structured JSON:** [`079490f8b4c55c28729b.json`](../../sessions/07/079490f8b4c55c28729b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data. Here's the complete output:

---

```
=== a050_s42 5-method Results ===

FORWARD (canary → downstream)
Pair                       NaiveR  NLag  DiffR  DLag  DiffFDR_p  Onset  PermF     PermFDR_p  TY_F    TY_p    dmax
token_entropy→distinct_1   -0.973     4  0.883    -1    0.0023*   None   127.478   0.0974     48.846  0.0905    2
token_entropy→distinct_2   -0.979     4  0.887    -3    0.0078*   None    35.753   0.0974      2.398  0.3650    2
token_entropy→distinct_3   -0.978     4  0.888    -3    0.0078*   None    12.429   0.0974      1.141  0.4790    2
token_entropy→perplexity   -0.905     1  0.920    -1    0.0014*   None    12.138   0.0974     32.830  0.1100    2
ece→distinct_1              0.955    -1  0.954    -1    0.0005*   None    79.241   0.0852      6.102  0.2449    2
ece→distinct_2              0.938    -5  0.955    -3    0.0016*   None    28.060   0.0852     56.784  0.0840    2
ece→distinct_3              0.937    -5  0.939    -3    0.0023*   None    12.689   0.0852      0.051  0.8591    2
ece→perplexity              0.900    -1  0.916    -1    0.0014*   None    15.211   0.0852     79.689  0.0710    2

REVERSE (downstream → canary)
Pair                       NaiveR  NLag  DiffR  DLag  DiffFDR_p  Onset  PermF    PermFDR_p  TY_F   TY_p    dmax
distinct_1→token_entropy   -0.973    -4  0.883     1    0.0023*   None    1.999   0.4706     0.004  0.9603    2
distinct_2→token_entropy   -0.979    -4  0.887     3    0.0078*   None    1.235   0.4706     5.014  0.2674    2
distinct_3→token_entropy   -0.978    -4  0.888     3    0.0078*   None    0.264   0.6351     3.536  0.3111    2
perplexity→token_entropy   -0.905    -1  0.920     1    0.0014*   None    4.162   0.4119     0.160  0.7579    2
distinct_1→ece              0.955     1  0.954     1    0.0005*   None    1.574   0.4706     0.268  0.6960    2
distinct_2→ece              0.938     5  0.955     3    0.0016*   None    1.078   0.4706     2.143  0.3815    2
distinct_3→ece              0.937     5  0.939     3    0.0023*   None    0.372   0.6351     1.209  0.4698    2
perplexity→ece              0.900     1  0.916     1    0.0014*   None    3.875   0.4119     0.271  0.6946    2

CONSENSUS (forward):
  token_entropy→distinct_1  2/5  [naive, diff]
  token_entropy→distinct_2  2/5  [naive, diff]
  token_entropy→distinct_3  2/5  [naive, diff]
  token_entropy→perplexity  2/5  [naive, diff]
  ece→distinct_1            1/5  [diff]
  ece→distinct_2            1/5  [diff]
  ece→distinct_3            1/5  [diff]
  ece→perplexity            1/5  [diff]

  Robust pairs (>=3/5): 0/8
  Perm Granger FDR sig (fwd): 0/8
  Diff XCorr FDR sig (fwd): 8/8
  Threshold sig: 0/8
  TY sig: 0/8
```

```
=== Pipeline Parameter Comparison ===

| Parameter              | method_ablation.py (MVP)              | analyze_alpha_sweep.py (old sweep)        | run_5method_analysis.py (new)         |
|------------------------|---------------------------------------|-------------------------------------------|---------------------------------------|
| n_perm (perm_granger)  | 1000                                  | 5000                                      | 5000                                  |
| max_lag (xcorr)        | 3                                     | 3                                         | 5                                     |
| max_lag (perm_granger) | 1                                     | 1                                         | 1                                     |
| FDR method             | BH (statsmodels multipletests)        | BH (statsmodels multipletests)            | BH (custom implementation)            |
| FDR family scope       | per-method, ALL pairs×seeds (~64)     | per-alpha, per-method (8×N_seeds)         | per-direction, per-method (8 pairs)   |
| Naive xcorr p-value    | parametric pearsonr                   | **permutation-based** (5000 perms)        | parametric pearsonr                   |
| Diff xcorr p-value     | parametric pearsonr                   | **permutation-based** (5000 perms)        | parametric pearsonr                   |
| Canaries               | 4 (ent, bleu, ece, rank)              | 2 (ent, ece)                              | 2 (ent, ece)                          |
| Downstreams            | 4                                     | 4                                         | 4                                     |
| Data scope             | MVP rep_{42-45} (multi-seed)          | all alpha_sweep runs (multi-seed)         | single run (single-seed)              |
| Preprocessing          | orient (sign flip)                    | orient (sign flip)                        | orient (sign flip)                    |
| Differencing           | in perm_granger only                  | in perm_granger + diff method             | in perm_granger + diff method         |
| TY d_max               | ADF-determined                        | ADF-determined                            | ADF-determined                        |
```

**Critical differences that affect results:**

1. **max_lag 3→5 (xcorr)**: New pipeline searches wider lags. At T=11, lag=4-5 uses only 6-7 points — very noisy, inflates naive r by cherry-picking.

2. **Naive/Diff p-value method**: `analyze_alpha_sweep` uses permutation p (5000 shuffles), which is much more conservative than parametric pearsonr at T=11. The new pipeline's parametric pearsonr p-values are anti-conservative because pearsonr assumes i.i.d. normality which non-stationary series violate.

3. **FDR family size**: New pipeline corrects only 8 tests together (tightest family = most power). `method_ablation` pooled up to 64 (most conservative).

4. **Perm Granger n_perm**: `method_ablation` used only 1000 permutations (coarser p resolution: min p=1/1001��0.001), while both sweep scripts use 5000 (min p≈0.0002).

---
