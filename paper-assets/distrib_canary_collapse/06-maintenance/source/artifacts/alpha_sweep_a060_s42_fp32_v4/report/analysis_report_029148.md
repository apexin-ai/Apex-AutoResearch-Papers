# Analysis Report: alpha_sweep_a060_s42_fp32_v4

## Experiment Configuration

| Field | Value |
|-------|-------|
| exp_id | alpha_sweep_a060_s42_fp32_v4 |
| Model | EleutherAI/pythia-410m |
| Dataset | WikiText-103 (wikitext103_5k) |
| α (synthetic_ratio) | 0.60 |
| Seed | 42 |
| Precision | fp32 |
| Generations | 10 (gen_0 baseline + gen_1–10 trained) |
| Steps/gen | 5000 |
| Batch size | 4, lr=5e-5, optim=adamw_torch |
| Server | westd-17855 |
| EXIT_CODE | 0 (success) |
| W&B run ID | None (wandb disabled) |

**Source**: `results/alpha_sweep/a060_s42_fp32_v4/config.json`

---

## 1. Per-Generation Metrics

**Source**: `results/alpha_sweep/a060_s42_fp32_v4/all_metrics.json`

| Gen | token_entropy | ece | perplexity | distinct_1 | distinct_2 | distinct_3 | mauve | eff_rank |
|-----|--------------|-----|------------|------------|------------|------------|-------|----------|
| 0 | 3.2342 | 0.0108 | 26.949 | 0.0980 | 0.5141 | 0.8127 | 0.0311 | 46.61 |
| 1 | 2.1818 | 0.1273 | 29.129 | 0.0976 | 0.5125 | 0.8122 | 0.0314 | 67.66 |
| 2 | 2.1568 | 0.1557 | 36.304 | 0.0834 | 0.4358 | 0.7230 | 0.0327 | 74.09 |
| 3 | 2.2036 | 0.1562 | 38.572 | 0.0775 | 0.3965 | 0.6675 | 0.0337 | 75.13 |
| 4 | 2.1770 | 0.1675 | 41.920 | 0.0733 | 0.3623 | 0.6087 | 0.0305 | 76.79 |
| 5 | 2.2186 | 0.1666 | 43.967 | 0.0711 | 0.3412 | 0.5676 | 0.0291 | 75.55 |
| 6 | 2.2221 | 0.1712 | 45.621 | 0.0696 | 0.3314 | 0.5490 | 0.0276 | 75.52 |
| 7 | 2.2645 | 0.1765 | 48.236 | 0.0689 | 0.3254 | 0.5391 | 0.0292 | 76.36 |
| 8 | 2.2623 | 0.1770 | 48.994 | 0.0687 | 0.3205 | 0.5282 | 0.0286 | 74.16 |
| 9 | 2.2936 | 0.1803 | 51.399 | 0.0684 | 0.3169 | 0.5210 | 0.0295 | 74.67 |
| 10 | 2.3111 | 0.1794 | 51.832 | 0.0681 | 0.3153 | 0.5180 | 0.0259 | 73.30 |

## 2. Drift Statistics (gen_0 → gen_10)

| Metric | gen_0 | gen_10 | Δ% |
|--------|-------|--------|-----|
| token_entropy | 3.2342 | 2.3111 | **-28.54%** |
| ece | 0.0108 | 0.1794 | **+1560.77%** |
| perplexity | 26.949 | 51.832 | **+92.33%** |
| distinct_1 | 0.0980 | 0.0681 | **-30.51%** |
| distinct_2 | 0.5141 | 0.3153 | **-38.67%** |
| distinct_3 | 0.8127 | 0.5180 | **-36.27%** |
| mauve | 0.0311 | 0.0259 | **-16.73%** |
| effective_rank | 46.613 | 73.299 | **+57.25%** |

---

## 3. 5-Method Lead-Lag Analysis

**Source**: local replication of `run_5method_analysis_d102.py` (n_perm=5000, BH FDR q=0.05, D105 true 3sigma, D111 direction filter peak_lag < 0)

### 3.1 Summary

| Method | Forward (canary→downstream) | Reverse |
|--------|---------------------------|---------|
| **PermG (FDR)** | **0/8** | 0/8 |
| diff_xcorr (FDR) | 6/8 | 6/8 |
| naive_xcorr (D111 filtered) | 2/8 | — |
| threshold_onset_3sigma | 0/8 | — |
| TY Granger | 0/8 | 1/8 |

**K≥3: 0/8 | K≥4: 0/8 | Robust pairs: 0/8**

### 3.2 PermG Forward Detail (per-pair)

| Pair | F-stat | p (raw) | p (FDR) | Sig? |
|------|--------|---------|---------|------|
| token_entropy→distinct_1 | 204.60 | 0.0920 | >0.05 | No |
| token_entropy→distinct_2 | 108.54 | 0.0830 | >0.05 | No |
| token_entropy→distinct_3 | 46.73 | 0.0818 | >0.05 | No |
| token_entropy→mauve | 1.35 | 0.2675 | >0.05 | No |
| ece→distinct_1 | 100.79 | **0.0338** | >0.05 | No |
| ece→distinct_2 | 61.46 | **0.0468** | >0.05 | No |
| ece→distinct_3 | 32.25 | 0.0578 | >0.05 | No |
| ece→mauve | 1.73 | 0.2178 | >0.05 | No |

Note: ece→distinct_1 (p=0.0338) and ece→distinct_2 (p=0.0468) are raw-significant at α=0.05 but do not survive BH FDR correction across 8 tests. The high F-statistics (>30) with marginal p-values indicate the permutation null distribution also generates high F-values at this sample size (T=10 after differencing), reducing discriminative power.

### 3.3 Threshold Onset (D105 3σ)

| Pair | Canary onset | Downstream onset | Lead time | Sig? |
|------|-------------|-----------------|-----------|------|
| token_entropy→distinct_* | gen 1 | None | — | No |
| token_entropy→mauve | gen 1 | None | — | No |
| ece→distinct_* | gen 2 | None | — | No |
| ece→mauve | gen 2 | None | — | No |

Canary metrics (token_entropy, ece) show early onset (gen 1–2), but **no downstream metric (distinct_1/2/3, mauve) ever exceeds its 3σ threshold**. The downstream degradation is gradual and spread across all generations, never crossing the 3σ spike threshold.

### 3.4 Consensus (forward, D111 direction filter)

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 1/5 | diff |
| token_entropy→distinct_2 | 1/5 | diff |
| token_entropy→distinct_3 | 1/5 | diff |
| token_entropy→mauve | 1/5 | naive |
| ece→distinct_1 | 1/5 | diff |
| ece→distinct_2 | 1/5 | diff |
| ece→distinct_3 | 1/5 | diff |
| ece→mauve | 1/5 | naive |

---

## 4. Cross-α Reference Comparison

All WikiText-103, Pythia-410M, fp32:

| α | Seed | PermG_fwd | K≥3 | threshold_3σ | TY | diff_xcorr | entropy_drift% | ppl_drift% |
|---|------|-----------|-----|-------------|-----|------------|----------------|------------|
| 0.45 | s43 | 0/8 | 2/8 | 8/8 | 7/8 | 1/8 | -19.6 | +12.4 |
| 0.50 | s42 | 6/8 | 3/8 | 0/8 | 4/8 | 2/8 | ~-16 | ~+17 |
| 0.50 | s43 | 6/8 | 6/8 | 8/8 | 5/8 | 6/8 | -15.8 | +17.2 |
| **0.60** | **s42** | **0/8** | **0/8** | **0/8** | **0/8** | **6/8** | **-28.5** | **+92.3** |
| 0.75 | s42 | 6/8 | — | 8/8 | 8/8 | 6/8 | -29.4 | +188.3 |
| 0.75 | s43 | 5/8 | 7/8 | 8/8 | 6/8 | 6/8 | -27.4 | +182.3 |

### Key Observations

1. **Non-monotonic PermG dip at α=0.60**: PermG drops from 6/8 at α=0.50 to **0/8** at α=0.60, then recovers to 5–6/8 at α=0.75. This is the most striking finding.

2. **Degradation is strong but PermG-invisible**: α=0.60 shows entropy drift (-28.5%) and ppl drift (+92.3%) **comparable to α=0.75** (-29.4%, +188.3%), yet PermG detects nothing. The collapse signal exists in raw metrics but not in the temporal lead-lag structure.

3. **Only diff_xcorr maintains detection**: 6/8 pairs show significant differenced cross-correlation, consistent with α=0.50 and α=0.75. But without PermG or other method confirmation, consensus K≥3 = 0/8.

4. **threshold_onset also fails**: Unlike α=0.45/0.50/0.75 where threshold_onset = 8/8, at α=0.60 it's 0/8 — downstream metrics degrade gradually without a 3σ spike.

5. **Possible explanation**: At α=0.60, the degradation trajectory is smooth and monotonic across all generations (see perplexity 26.9→51.8 with no acceleration), making the temporal *lead* of canary over downstream undetectable. At α=0.75, the stronger signal may create a detectable acceleration pattern.

---

## 5. Conclusion

**Status**: success (training completed normally, valid metrics for all 10 generations)

**Finding**: α=0.60 s42 fp32 exhibits a **non-monotonic dip in PermG signal** — PermG_fwd = 0/8 despite substantial model degradation. This confirms the α=0.60 position as a "sync collapse" regime where canary and downstream degrade simultaneously without detectable temporal lead-lag.

**Implication for dose-response curve**: The transition from onset (α=0.50, PermG=6/8) to detection (α=0.75, PermG=5–6/8) is **non-monotonic**, with a PermG blind spot at α=0.60. This requires additional seeds (s43, s44) at α=0.60 to confirm the dip is not a seed-specific artifact.

**Data provenance**:
- Raw metrics: `westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_fp32_v4/all_metrics.json`
- Analysis JSON: `artifacts/alpha_sweep_a060_s42_fp32_v4/5method_leadlag.json`
- Config: `results/alpha_sweep/a060_s42_fp32_v4/config.json`
- Log: `westd-17855:~/runs/distrib_canary_collapse/alpha_sweep_a060_s42_fp32_v4.log`
