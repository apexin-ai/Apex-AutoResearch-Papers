# Analysis: alpha_sweep_a045_s42_fp32

## 1. Config

| Key | Value |
|-----|-------|
| Model | EleutherAI/pythia-410m |
| Dataset | WikiText-103 (5k subset) |
| α (synthetic_ratio) | 0.45 |
| Seed | 42 |
| Precision | fp32 |
| Generations | 10 (gen_0–gen_10) |
| Steps/gen | 5,000 |
| LR | 5e-5 |
| Batch size | 4 |
| Server | westd-17855 |

## 2. Hypothesis

α=0.45 is an onset-refinement point between α=0.40 (PermG=0/8, blind zone) and α=0.50 (PermG=6/8, detected). If PermG>0, onset ∈ [0.40, 0.45]; if PermG=0, onset ∈ [0.45, 0.50].

## 3. Result Summary

**PermG fwd (FDR) = 0/8. Onset boundary narrowed to [0.45, 0.50].**

The entropy/ECE canaries do not Granger-cause diversity metrics at α=0.45 after FDR correction. However, multiple raw PermG p-values fall in [0.030, 0.070] — marginally sub-threshold — suggesting α=0.45 is near but below the detection onset.

## 4. Training Completion

- **EXIT_CODE**: 0
- **Generations**: gen_0 through gen_10, all present with metrics.json
- **W&B**: No wandb run found

## 5. Per-Generation Metrics

| Gen | token_entropy | ece      | distinct_1 | distinct_2 | distinct_3 | perplexity | effective_rank | mauve   |
|-----|--------------|----------|------------|------------|------------|------------|----------------|---------|
| 0   | 3.2342       | 0.0108   | 0.0980     | 0.5141     | 0.8127     | 26.949     | 46.613         | 0.0311  |
| 1   | 2.4941       | 0.0667   | 0.0976     | 0.5125     | 0.8122     | 22.538     | 58.307         | 0.0314  |
| 2   | 2.5341       | 0.0777   | 0.0839     | 0.4433     | 0.7361     | 25.144     | 62.231         | 0.0326  |
| 3   | 2.5902       | 0.0767   | 0.0784     | 0.4003     | 0.6718     | 26.117     | 63.462         | 0.0322  |
| 4   | 2.5707       | 0.0836   | 0.0731     | 0.3636     | 0.6132     | 27.209     | 63.454         | 0.0317  |
| 5   | 2.5728       | 0.0887   | 0.0698     | 0.3325     | 0.5546     | 28.016     | 62.765         | 0.0306  |
| 6   | 2.5580       | 0.0919   | 0.0677     | 0.3138     | 0.5195     | 28.554     | 61.275         | 0.0283  |
| 7   | 2.5771       | 0.0949   | 0.0657     | 0.2939     | 0.4771     | 29.185     | 62.371         | 0.0260  |
| 8   | 2.6037       | 0.0923   | 0.0644     | 0.2814     | 0.4491     | 29.451     | 59.777         | 0.0261  |
| 9   | 2.6332       | 0.0941   | 0.0639     | 0.2748     | 0.4377     | 30.132     | 58.600         | 0.0257  |
| 10  | 2.6283       | 0.0940   | 0.0633     | 0.2680     | 0.4243     | 30.234     | 57.526         | 0.0234  |

### Trajectory Notes

- **token_entropy**: Sharp drop gen0→gen1 (3.234→2.494, −22.9%), then gradual recovery to ~2.63 by gen10. Net: −18.7%.
- **ece**: Jumps gen0→gen1 (0.011→0.067), continues rising to ~0.094. Net: +770%.
- **distinct_1/2/3**: Monotonic decline; d1 −35.4%, d2 −47.9%, d3 −47.8%.
- **perplexity**: Rises steadily gen1→gen10 (22.5→30.2). Net: +12.2%.
- **mauve**: Gradual decline. Net: −24.9%.

## 6. Drift (gen_0 → gen_10)

| Metric         | gen_0   | gen_10  | Δ%       |
|----------------|---------|---------|----------|
| token_entropy  | 3.2342  | 2.6283  | −18.73%  |
| ece            | 0.0108  | 0.0940  | +770.37% |
| perplexity     | 26.949  | 30.234  | +12.19%  |
| distinct_1     | 0.0980  | 0.0633  | −35.39%  |
| distinct_2     | 0.5141  | 0.2680  | −47.87%  |
| distinct_3     | 0.8127  | 0.4243  | −47.79%  |
| effective_rank | 46.613  | 57.526  | +23.41%  |
| mauve          | 0.0311  | 0.0234  | −24.89%  |

## 7. 5-Method Lead-Lag Summary

| Method             | Forward sig / 8 | Notes |
|--------------------|----------------|-------|
| PermG fwd (FDR)    | **0/8**        | Primary metric. All p_fdr > 0.09. Raw p in [0.030, 0.211]. |
| PermG rev (FDR)    | 0/8            | No reverse causality. |
| naive_xcorr        | 7/8            | ece→mauve invalid direction (lag=−5). |
| diff_xcorr (FDR)   | 3/8            | 5/8 sig_fdr, but 2 have invalid direction (lag≤0). |
| threshold_onset    | 8/8            | All canaries onset gen1, downstream gen2 (or gen7 for mauve). |
| TY granger         | 1/8            | ece→mauve only; df_resid=1, unreliable per C003. |
| **K≥3 (consensus)**| **3/8**        | entropy→d3, ece→d2, ece→d3. |
| **K≥4 (consensus)**| **0/8**        | — |

## 8. Per-Pair Detail

| Pair | naive lag | naive sig | diff lag | diff sig_fdr | thresh lead | pgF p_fdr | pgR p_fdr | TY p | TY d_max/df | Votes | Methods |
|------|-----------|-----------|----------|-------------|-------------|-----------|-----------|------|-------------|-------|---------|
| entropy→d1 | 5 | T | −1 | T* | 1 | 0.0936 | 0.9788 | 0.1633 | 1/4 | 2 | naive,thresh |
| entropy→d2 | 5 | T | −1 | T* | 1 | 0.0912 | 0.9788 | 0.1255 | 1/4 | 2 | naive,thresh |
| entropy→d3 | 5 | T | 2 | T | 1 | 0.0912 | 0.9788 | 0.3700 | 1/4 | 3 | naive,diff,thresh |
| entropy→mauve | 3 | T | −1 | F | 6 | 0.2112 | 0.9788 | 0.8656 | 2/1 | 2 | naive,thresh |
| ece→d1 | 2 | T | −1 | T* | 1 | 0.0936 | 0.9788 | 0.3242 | 1/4 | 2 | naive,thresh |
| ece→d2 | 2 | T | 2 | T | 1 | 0.0936 | 0.9788 | 0.4323 | 1/4 | 3 | naive,diff,thresh |
| ece→d3 | 2 | T | 2 | T | 1 | 0.0912 | 0.9788 | 0.2424 | 1/4 | 3 | naive,diff,thresh |
| ece→mauve | −5* | T | 3 | F | 6 | 0.2112 | 0.9788 | 0.0000† | 2/1 | 2 | thresh,ty |

- `*` = D111 direction invalid (lag≤0 for naive/diff); vote excluded from forward consensus.
- `†` = TY ece→mauve: chi2=63.78, p≈0 but df_resid=1 (d_max=2), unreliable per C003.
- `T*` = diff_xcorr FDR-significant but direction invalid (lag<0).

### D111 Direction Audit

**naive_xcorr**: 7/8 forward-valid. ece→mauve (lag=−5) is reverse → excluded.

**diff_xcorr**: Of 5 FDR-significant pairs, 3 have forward direction (lag>0): entropy→d3, ece→d2, ece→d3. Two have lag=−1 (entropy→d1, entropy→d2, ece→d1): excluded from forward count.

## 9. Updated Onset Boundary

| α    | PermG fwd (FDR) | K≥3 | K≥4 | Zone |
|------|-----------------|-----|-----|------|
| 0.30 | 0/8             | 6/8 | 3/8 | Blind (PermG) |
| 0.35 | 0/8             | 6/8 | 2/8 | Blind (PermG) |
| 0.40 | 0/8             | —   | —   | Blind (PermG) |
| **0.45** | **0/8**     | **3/8** | **0/8** | **Blind (PermG)** |
| 0.50 | 6/8             | 6/8 | 1/8 | Detected |
| 0.60 | 0–3/8           | —   | —   | Synchronous collapse |

**Onset ∈ [0.45, 0.50] (Pythia-410M, WikiText-103, seed=42, fp32).**

## 10. Notes

1. **Near-threshold behavior**: 4/8 pairs have PermG raw p < 0.07 (before FDR). This is clearly sub-threshold but noticeably lower than α=0.40 (PermG p values were higher). α=0.45 is the near side of the onset transition.

2. **K≥3 drops from 6/8 (α=0.30–0.50) to 3/8 here**. This is surprising — the non-PermG methods (naive, diff, thresh) provide less consensus at α=0.45 than at lower α values. May reflect the entropy canary's different trajectory at α=0.45 (much sharper gen0→gen1 drop, then recovery) vs lower α.

3. **Entropy trajectory is qualitatively different**: At α=0.10, entropy barely moves (−5.3%). At α=0.45, it drops 22.9% in one generation, then partially recovers. This large initial perturbation followed by recovery may disrupt the smooth lead-lag relationship that lower-α experiments exhibit.

4. **Next step**: If multi-seed confirmation is needed, run α=0.475 to further narrow onset. Otherwise, [0.45, 0.50] is a sufficiently tight bracket for the paper.
