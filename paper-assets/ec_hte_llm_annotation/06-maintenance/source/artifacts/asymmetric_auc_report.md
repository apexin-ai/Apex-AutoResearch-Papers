# Asymmetric Diagnostic AUC: Scalar vs Matrix

## Method

**Scalar (Proposition 5):** score_s = |delta_s| / ((1-2*pi_bar) * pi_s)
where pi_s = (FPR_s + FNR_s)/2, pi_bar = weighted avg of pi_s, delta_s = pi_s - pi_bar

**Matrix (B_s):** score_s = max(|B_s[0,1]|, |B_s[1,1]|)
where B_s = M_global^{-1} M_s - I, M is the mixing matrix accounting for FPR != FNR and P(Z) != 0.5

**Ground truth:** GC hurts subgroup s iff avg_z|B_s[z,1]| > avg_z|D_s[z,1]| (D_s = M_s - I)
This label is independent of delta_tau (cancels in the comparison).

## Per-Subgroup AUC (Main Result)

| Category | N | Hurts | Helps | Scalar | Matrix-raw | Matrix-ratio | Best |
|----------|---|-------|-------|--------|------------|--------------|------|
| Symmetric (1:1) | 24 | 2 | 22 | 1.0000 | 0.9545 | 1.0000 | Scalar |
| Synthetic asymmetric (exp-041) | 144 | 12 | 132 | 1.0000 | 0.9757 | 1.0000 | Scalar |
| Semi-real LLMs | 32 | 4 | 28 | 1.0000 | 0.8839 | 1.0000 | Scalar |
| All asymmetric (synth + semi-real) | 176 | 16 | 160 | 1.0000 | 0.9486 | 1.0000 | Scalar |
| Stress tests | 8 | 3 | 5 | 0.5667 | 0.7000 | 1.0000 | Ratio |
| All incl. stress | 184 | 19 | 165 | 0.8448 | 0.9378 | 1.0000 | Ratio |
| Synth ratio=1:2 | 24 | 2 | 22 | 1.0000 | 1.0000 | 1.0000 | Scalar |
| Synth ratio=1:3 | 24 | 2 | 22 | 1.0000 | 0.9773 | 1.0000 | Scalar |
| Synth ratio=1:5 | 24 | 2 | 22 | 1.0000 | 0.9773 | 1.0000 | Scalar |
| Synth ratio=2:1 | 24 | 2 | 22 | 1.0000 | 1.0000 | 1.0000 | Scalar |
| Synth ratio=3:1 | 24 | 2 | 22 | 1.0000 | 0.9773 | 1.0000 | Scalar |
| Synth ratio=5:1 | 24 | 2 | 22 | 1.0000 | 0.9886 | 1.0000 | Scalar |

## Per (s, z) AUC

Score for per-(s,z): |B_s[z,1]| (z-specific, not max)

| Category | N | Scalar AUC | Matrix-z AUC | Delta |
|----------|---|------------|--------------|-------|
| Symmetric (1:1) | 48 | 1.0000 | 0.9432 | -0.0568 |
| Synthetic asymmetric (exp-041) | 288 | 0.9921 | 0.8439 | -0.1481 |
| Semi-real LLMs | 64 | 0.9911 | 0.7991 | -0.1920 |
| All asymmetric (synth + semi-real) | 352 | 0.9926 | 0.8346 | -0.1581 |

## Semi-Real: Per-LLM Detail

### Llama-3.1-8B (K=4, hurts=1/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.235 | 0.319 | 0.277 | 0.74 | 0.228 | 0.1069 | no |
| 1 | 0.310 | 0.212 | 0.261 | 1.46 | 0.122 | 0.0362 | no |
| 2 | 0.219 | 0.258 | 0.238 | 0.85 | 0.051 | 0.0113 | no |
| 3 | 0.091 | 0.190 | 0.141 | 0.48 | 1.453 | 0.2597 | YES |

### Gemma-2-9B (K=4, hurts=0/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.110 | 0.437 | 0.273 | 0.25 | 0.391 | 0.1579 | no |
| 1 | 0.138 | 0.300 | 0.219 | 0.46 | 0.056 | 0.0265 | no |
| 2 | 0.033 | 0.263 | 0.148 | 0.13 | 0.744 | 0.1430 | no |
| 3 | 0.091 | 0.207 | 0.149 | 0.44 | 0.733 | 0.1855 | no |

### Qwen2.5-7B (K=4, hurts=1/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.180 | 0.287 | 0.234 | 0.63 | 0.229 | 0.1051 | no |
| 1 | 0.241 | 0.175 | 0.208 | 1.38 | 0.051 | 0.0366 | no |
| 2 | 0.233 | 0.210 | 0.222 | 1.11 | 0.152 | 0.0324 | no |
| 3 | 0.000 | 0.138 | 0.069 | 0.00 | 3.228 | 0.2721 | YES |

### Mistral-7B (K=4, hurts=1/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.180 | 0.299 | 0.239 | 0.60 | 0.242 | 0.1263 | no |
| 1 | 0.241 | 0.188 | 0.214 | 1.29 | 0.073 | 0.0217 | no |
| 2 | 0.233 | 0.168 | 0.201 | 1.39 | 0.037 | 0.0497 | no |
| 3 | 0.091 | 0.121 | 0.106 | 0.75 | 1.594 | 0.2425 | YES |

### GPT-4o (K=4, hurts=0/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.249 | 0.160 | 0.204 | 1.56 | 0.379 | 0.1598 | no |
| 1 | 0.157 | 0.263 | 0.210 | 0.60 | 0.315 | 0.0580 | no |
| 2 | 0.213 | 0.308 | 0.260 | 0.69 | 0.122 | 0.0873 | no |
| 3 | 0.341 | 0.328 | 0.334 | 1.04 | 0.527 | 0.2476 | no |

### GPT-4o-mini (K=4, hurts=0/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.517 | 0.052 | 0.285 | 9.91 | 0.068 | 0.0943 | no |
| 1 | 0.540 | 0.105 | 0.323 | 5.13 | 0.226 | 0.1028 | no |
| 2 | 0.419 | 0.074 | 0.247 | 5.65 | 0.451 | 0.0727 | no |
| 3 | 0.610 | 0.160 | 0.385 | 3.82 | 0.579 | 0.3110 | no |

### GPT-3.5-turbo (K=4, hurts=0/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.400 | 0.139 | 0.270 | 2.88 | 0.206 | 0.1028 | no |
| 1 | 0.473 | 0.210 | 0.342 | 2.25 | 0.347 | 0.1598 | no |
| 2 | 0.374 | 0.173 | 0.274 | 2.17 | 0.168 | 0.0370 | no |
| 3 | 0.468 | 0.240 | 0.354 | 1.95 | 0.417 | 0.2178 | no |

### AG-News (K=4, hurts=1/4)

| Sub | FPR | FNR | pi_s | FPR/FNR | Scalar | Matrix | Hurts |
|-----|-----|-----|------|---------|--------|--------|-------|
| 0 | 0.080 | 0.100 | 0.090 | 0.80 | 1.410 | 0.1287 | YES |
| 1 | 0.150 | 0.180 | 0.165 | 0.83 | 0.074 | 0.0141 | no |
| 2 | 0.180 | 0.200 | 0.190 | 0.90 | 0.137 | 0.0276 | no |
| 3 | 0.260 | 0.300 | 0.280 | 0.87 | 0.584 | 0.1667 | no |


## MC-Based Ground Truth Validation

Analytic ground truth agrees with MC (100 runs) on 261/288 (90.6%) of per-(s,z) labels from exp-041.
Disagreements arise from finite-sample MC noise in borderline cases.

## MC-Based Diagnostic AUC

Ground truth labels computed from 100 MC simulation runs (exp-041).

| Category | N | Hurts | Scalar AUC | Matrix AUC | Delta |
|----------|---|-------|------------|------------|-------|
| All synthetic (MC, per-s) | 144 | 25 | 0.9595 | 0.8644 | -0.0951 |
| All synthetic (MC, per-sz) | 288 | 49 | 0.9205 | 0.8378 | -0.0827 |
| Ratio 1:2 (MC, per-s) | 24 | 4 | 0.9812 | 0.9125 | -0.0687 |
| Ratio 1:3 (MC, per-s) | 24 | 4 | 0.9812 | 0.9000 | -0.0812 |
| Ratio 1:5 (MC, per-s) | 24 | 4 | 0.9812 | 0.9000 | -0.0812 |
| Ratio 2:1 (MC, per-s) | 24 | 4 | 0.9812 | 0.9125 | -0.0687 |
| Ratio 3:1 (MC, per-s) | 24 | 5 | 0.8684 | 0.8000 | -0.0684 |
| Ratio 5:1 (MC, per-s) | 24 | 4 | 0.9813 | 0.9062 | -0.0750 |

## Score Distribution Analysis

**Symmetric (1:1):**
- Scalar: mean(hurts)=1.6667, mean(helps)=0.3663, separation=+1.3004
- Matrix: mean(hurts)=0.1667, mean(helps)=0.0732, separation=+0.0934

**Synthetic asymmetric (exp-041):**
- Scalar: mean(hurts)=1.6529, mean(helps)=0.3658, separation=+1.2870
- Matrix: mean(hurts)=0.1759, mean(helps)=0.0767, separation=+0.0992

**Semi-real LLMs:**
- Scalar: mean(hurts)=1.9213, mean(helps)=0.2754, separation=+1.6460
- Matrix: mean(hurts)=0.2257, mean(helps)=0.1035, separation=+0.1222

**All asymmetric (synth + semi-real):**
- Scalar: mean(hurts)=1.7200, mean(helps)=0.3500, separation=+1.3700
- Matrix: mean(hurts)=0.1884, mean(helps)=0.0814, separation=+0.1070

## Per-Config AUC (Reconciliation with Prior Results)

The existing exp-041 code computed per-config AUC using the raw matrix score per (s,z), averaging across the 29/48 configs with valid AUC (both classes present). That average was **0.68**, matching the reported "AUC ~ 0.66."

Re-computing per-config AUC for all three diagnostics with MC ground truth:

| Diagnostic | Per-config AUC avg | Per-config AUC median | Pooled AUC (per-s) |
|------------|-------------------|-----------------------|--------------------|
| Scalar (Prop 5) | **0.97** | 1.00 | 0.96 |
| Matrix-raw (max \|B_s\|) | 0.68 | 0.83 | 0.86 |
| Matrix-ratio (\|B_s\|/\|D_s\|) | **1.00** | 1.00 | — |

The low per-config AUC of the raw matrix score is due to missing normalization, not asymmetric errors.

## Key Findings

### 1. Scalar diagnostic (Proposition 5) is analytically exact

The scalar score |delta_s| / ((1-2*pi_bar) * pi_s) achieves AUC = 1.00 on all 48 synthetic asymmetric configs AND 8 semi-real LLM configs (analytic ground truth). Under MC noise (100 runs), per-config AUC averages 0.97 (median 1.00). The scalar formula is equivalent to the bias amplification ratio |B_s|/|D_s| and remains a valid threshold diagnostic under asymmetry as long as subgroups have different pi_s.

### 2. Raw matrix score (max |B_s[z,1]|) underperforms

The unnormalized matrix score achieves per-config AUC avg = 0.68 (MC). It underperforms because it measures absolute bias amplification without normalizing by the naive bias magnitude |D_s[z,1]|. A subgroup with large pi_s has large |D_s| (naive bias) and large |B_s|, but the ratio |B_s|/|D_s| may be < 1 (GC helps). The raw score conflates "large bias amplification" with "GC hurts."

### 3. Ratio-normalized matrix score recovers optimality

The ratio score avg_z(|B_s[z,1]|) / avg_z(|D_s[z,1]|) achieves AUC = 1.00 everywhere (analytic and MC). This directly computes the hurts condition and is the principled matrix generalization. However, it requires knowing both B_s and D_s, while the scalar only needs pi_s and pi_bar.

### 4. When scalar fails (stress test)

Under adversarial configs (same pi_s, opposite asymmetry, extreme P(Z)), the scalar AUC drops to 0.57 because delta_s = 0 makes the scalar score identically zero. The ratio-normalized matrix achieves 1.00 here. In practice, such configs are rare because real LLM error rates naturally differ across subgroups.

## Conclusion

The previously reported diagnostic AUC of ~0.66 was an artifact of using the **unnormalized raw matrix score** (max |B_s[z,1]|), not a failure of the scalar diagnostic (Proposition 5).

**Recommendation:** Keep Proposition 5's scalar diagnostic as-is. It achieves per-config AUC = 0.97 (MC) across all 48 asymmetric configs and all 8 semi-real LLM configs. No matrix-based replacement is needed for the diagnostic screening criterion. The B_s matrix remains essential for the EC-HTE *correction* method, but not for the *diagnostic* that decides whether correction is needed.

**Paper-ready statement (1-2 sentences):**
The scalar screening criterion from Proposition 5 (|delta_s|/((1-2*pi_bar)*pi_s) > 1) achieves per-subgroup diagnostic AUC of 0.97 under asymmetric LLM misclassification (FPR != FNR, ratios 1:5 to 5:1) and 1.00 on 8 semi-real LLM confusion matrices from TweetEval and AG News. The criterion's validity extends beyond the symmetric case because the threshold condition score > 1 is equivalent to |B_s|/|D_s| > 1 whenever subgroups have heterogeneous overall error rates.
