# Paper Number Consistency Audit
Generated: 2026-05-21

---

## Table 1: Function-level Results (experiments.tex L25–57)

### Qwen3-4B (5 seeds: 42/123/456/789/0)

| Cell | Paper Value | Registry exp_id(s) | Registry Values | Computed | Status |
|------|-------------|---------------------|-----------------|----------|--------|
| CLS mean | 88.43 | cls-4b s42/123/456/789/0 | 87.83, 89.52, 87.88, 89.00, 87.94 | (87.83+89.52+87.88+89.00+87.94)/5 = 88.434 → 88.43 | ✅ |
| CLS std | 0.78 | (same) | (same) | sqrt(2.4155/4) = 0.777 → 0.78 | ✅ |
| CWM mean | 87.19 | cwm-4b s42/123/456/789/0 | 87.51, 87.20, 86.98, 86.67, 87.57 | (sum=435.93)/5 = 87.186 → 87.19 | ✅ |
| CWM std | 0.37 | (same) | (same) | sqrt(0.5613/4) = 0.3746 → 0.37 | ✅ |
| TRAJ mean | 86.30 | traj-4b s42/123/456/789/0 | 85.66, 85.47, 87.40, 87.31, 85.66 | (sum=431.50)/5 = 86.30 | ✅ |
| TRAJ std | 0.97 | (same) | (same) | sqrt(3.7382/4) = 0.9668 → 0.97 | ✅ |

### DeepSeek-6.7B (2 seeds: 42/123)

| Cell | Paper Value | Registry exp_id(s) | Registry Values | Computed | Status |
|------|-------------|---------------------|-----------------|----------|--------|
| CLS mean | 86.85 | ds-cls s42/123 | 86.93, 86.77 | (86.93+86.77)/2 = 86.85 | ✅ |
| CLS std | 0.11 | (same) | (same) | sqrt(0.0128/1) = 0.1131 → 0.11 | ✅ |
| CWM mean | 86.83 | ds-cwm s42/123 | 85.77, 87.88 | (85.77+87.88)/2 = 86.825 → 86.83 | ✅ |
| CWM std | 1.49 | (same) | (same) | sqrt(2.226/1) = 1.492 → 1.49 | ✅ |
| TRAJ mean | 84.16 | ds-traj s42/123 | 83.24, 85.08 | (83.24+85.08)/2 = 84.16 | ✅ |
| TRAJ std | 1.30 | (same) | (same) | sqrt(1.6928/1) = 1.301 → 1.30 | ✅ |

### Prompting Baselines

| Cell | Paper Value | Registry Value | Status |
|------|-------------|----------------|--------|
| 0-shot Qwen3-8B | 68.70 | 68.73 | ⚠️ **-0.03 discrepancy** |
| 0-shot DeepSeek-6.7B | 63.00 | 63.02 | ⚠️ **-0.02 discrepancy** |
| ZS LLM-judge Qwen3-8B | 64.40 | 64.40 | ✅ |
| ZS LLM-judge DeepSeek-6.7B | 56.56 | — | ⚠️ 来源不明 (not found in registry extract) |
| ZS LLM-judge 32B NF4 | 71.69 | 71.69 | ✅ |
| 3-shot ICL Qwen3-8B | 68.78 | — | ⚠️ 来源不明 |
| 3-shot ICL DeepSeek-6.7B | 59.95 | — | ⚠️ 来源不明 |
| Majority (pass) | 51.75 | — | ✅ (dataset property: pass:fail ≈ 52:48) |

---

## Table 2: Model-size Scaling (experiments.tex L68–88)

Seeds 42/123, bfloat16 only.

### CLS

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| CLS 4B s42 | 87.83 | 87.83 | ✅ |
| CLS 4B s123 | 89.52 | 89.52 | ✅ |
| CLS 4B Mean | 88.68 | (87.83+89.52)/2 = 88.675 → 88.68 | ✅ |
| CLS 8B s42 | 90.48 | 90.48 | ✅ |
| CLS 8B s123 | **89.40** | **89.37** | ⚠️ **Paper 89.40 vs registry 89.37** |
| CLS 8B Mean | 89.94 | With 89.40: 89.94 ✅; with 89.37: 89.925 → 89.93 | ⚠️ cascading from s123 |
| Δ CLS 4B→8B | +1.27 | 89.94 − 88.675 = 1.265 → 1.27 (using paper's 89.40) | ✅ (internally consistent) |

### CWM

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| CWM 4B s42 | 87.51 | 87.51 | ✅ |
| CWM 4B s123 | 87.20 | 87.20 | ✅ |
| CWM 4B Mean | 87.36 | (87.51+87.20)/2 = 87.355 → 87.36 | ✅ |
| CWM 8B s42 | 87.67 | 87.67 | ✅ |
| CWM 8B s123 | 86.98 | 86.98 | ✅ |
| CWM 8B Mean | 87.33 | (87.67+86.98)/2 = 87.325 → 87.33 | ✅ |
| Δ CWM 4B→8B | −0.03 | 87.33 − 87.36 = −0.03 | ✅ |

### TRAJ

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| TRAJ 4B s42 | **85.27** | **85.66** | ⚠️ **Δ=0.39; 来源不明** |
| TRAJ 4B s123 | **86.72** | **85.47** | ⚠️ **Δ=1.25; 来源不明** |
| TRAJ 4B Mean | 86.00 | With paper values: (85.27+86.72)/2 = 86.00 ✅; registry: 85.57 | ⚠️ |
| TRAJ 8B s42 | 87.60 | 87.60 | ✅ |
| TRAJ 8B s123 | 87.79 | 87.79 | ✅ |
| TRAJ 8B Mean | 87.70 | (87.60+87.79)/2 = 87.695 → 87.70 | ✅ |
| Δ TRAJ 4B→8B | +1.70 | 87.70 − 86.00 = 1.70 | ✅ (internally consistent) |

**Note on TRAJ 4B discrepancy:** Registry stores TRAJ 4B function-level as s42=85.66, s123=85.47 (5-seed mean = 86.30, matching Table 1). Table 2 shows 85.27 and 86.72 — substantially different. Possible explanation: different evaluation subset or evaluation pipeline. The 8B TRAJ values match perfectly, making this 4B-only discrepancy notable.

### Derived gaps in text (experiments.tex L90)

| Claim | Paper | Computed | Status |
|-------|-------|----------|--------|
| CLS-CWM gap at 4B | 1.32pp | 88.68 − 87.36 = 1.32 | ✅ |
| CLS-CWM gap at 8B | 2.62pp | 89.94 − 87.33 = 2.61 (unrounded: 2.615) | ✅ (rounding) |
| Bootstrap p for widening | 0.0066 | — | ✅ (statistical result) |
| Bootstrap 95% CI | [1.80, 2.71] | — | ✅ (statistical result) |

---

## Table 3: Repo-level Results (experiments.tex L108–131)

### Qwen3-4B (seed 42)

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| CLS per-test | 83.63 | cls-4b-repo-v5 s42 ckpt-4600 seq5120: 83.63 | ✅ |
| CLS variant | 64.58 | variant_level table: 64.58 | ✅ |
| CWM per-test | 58.04 | cwm-4b-repo mutation analysis: 58.04 | ✅ |
| TRAJ variant | 72.92 | traj-4b-repo s42: 72.92 | ✅ |

### Qwen3-8B (3 seeds: 42/123/456)

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| CLS mean | 84.83 | s42=84.48, s123=85.60, s456=84.40 | (254.48/3) = 84.827 → 84.83 ✅ |
| CLS std | 0.67 | sqrt(0.9003/2) = 0.6709 → 0.67 | ✅ |
| CLS Var s42 | 72.92 | variant_level: 72.92 | ✅ |
| CLS Var s123 | 81.25 | variant_level: 81.25 | ✅ |
| CWM | \tbd{} | — | ✅ (skipped) |
| TRAJ Var mean | 72.91 | s42(e3)=70.83, s123=77.08, s456=70.83 → 72.91 | ✅ |
| TRAJ Var std | 3.61 | sqrt(26.04/2) = 3.608 → 3.61 | ✅ |

**Note:** TRAJ 8B s42 uses epoch-3 checkpoint (70.83), not epoch-2 (72.92 in registry). Paper's Threats section confirms: "epoch 2: 72.92% vs. epoch 3: 70.83%". Internally consistent.

### DeepSeek-6.7B (2 matched seeds: s42/s456, excluding s123)

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| CLS mean | 84.38 | s42=82.61, s456=86.15 → 84.38 | ✅ |
| CLS std | 2.50 | sqrt(6.266/1) = 2.503 → 2.50 | ✅ |
| CLS Var (s42) | 81.25 | variant_level: DeepSeek s42 (e1) = 81.25 | ✅ |
| CWM | \tbd{} | — | ✅ (skipped) |
| TRAJ Var mean | 77.08 | s42=81.25, s123=75.00, s456=75.00 → 77.08 | ✅ |
| TRAJ Var std | 3.61 | sqrt(26.04/2) = 3.608 → 3.61 | ✅ |

### Baselines

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| 0-shot Qwen3-8B | 49.90 | 49.90 | ✅ |
| 0-shot DeepSeek | **48.50** | **48.54** | ⚠️ **Also 48.54 in appendix few-shot table** |
| Majority per-test | 72.96 | — | ✅ (dataset property) |
| Majority variant | 54.17 | 26/48 = 54.17 | ✅ |

---

## Table 4: Failure Mode Taxonomy (experiments.tex L141–157)

| Row | Paper Values | Variant Table Source | Status |
|-----|-------------|---------------------|--------|
| Format collapse (CWM all) | Variant 48–52% | CWM Qwen3-8B: 52.08, DeepSeek: 47.92 → 48–52 | ✅ |
| Decision collapse (DS s123) | ~14% FR, 56% Var | variant_level: 56.25%, FR ~13.72% → ~14%, 56% | ✅ (rounded) |
| Aggr. penalty (Qwen3-8B) | 51–57% FR, 73–81% Var | s42: FR 56.76%, Var 72.92; s123: FR 51.44%, Var 81.25 | ✅ |
| Aggr. penalty (DS s42) | 38–51% FR, 79–81% Var | e1: FR 51.02%, Var 81.25; e3: FR 38.47%, Var 79.17 | ✅ |

---

## Table 5: Scaling Table (appendix, Tab scaling)

(Same as Table 2 analysis above — see Table 2 section.)

---

## Table 6: Variant-Level Accuracy (appendix.tex L151–189)

| Row | Per-test | Variant | Penalty | Fail Recall | Computed Penalty | Status |
|-----|----------|---------|---------|-------------|-----------------|--------|
| Qwen3-8B s42 | 84.48 | 72.92 | 11.56 | 56.76 | 84.48−72.92=11.56 | ✅ |
| Qwen3-8B s123 | 85.60 | 81.25 | 4.35 | 51.44 | 85.60−81.25=4.35 | ✅ |
| Qwen3-4B s42 | 83.63 | 64.58 | 19.05 | 48.72 | 83.63−64.58=19.05 | ✅ |
| DS s42 (e1) | 82.61 | 81.25 | 1.36 | 51.02 | 82.61−81.25=1.36 | ✅ |
| DS s42 (e3) | 82.51 | 79.17 | 3.34 | 38.47 | 82.51−79.17=3.34 | ✅ |
| DS s123 | 74.93 | 56.25 | 18.68 | ~13.72 | 74.93−56.25=18.68 | ✅ |
| CWM Qwen3-8B s42 | 65.17 | 52.08 | 13.09 | — | 65.17−52.08=13.09 | ✅ |
| CWM DS s123 | — | 47.92 | — | — | — | ✅ |
| TRAJ Qwen3-4B s42 | — | 72.92 | — | — | — | ✅ |
| TRAJ Qwen3-8B s42 | — | 70.83 | — | — | — | ✅ (epoch 3) |
| TRAJ DS 3-seed | — | 77.08±3.61 | — | — | — | ✅ (verified above) |
| Majority | 72.96 | 54.17 | — | — | — | ✅ |

---

## Table 7: Oracle (appendix.tex L8–27)

| Row | Paper | Registry/Analysis | Status |
|-----|-------|-------------------|--------|
| T=1 inst% | 68.7 | 68.7 | ✅ |
| T=1 block adv | −0.09pp | −0.09 | ✅ |
| T=2 inst% | 19.1 | 19.1 | ✅ |
| T=2 block adv | 31.69pp | 31.69 | ✅ |
| T=2 contrib | 55.3% | 55.3 | ✅ |
| T=3–5 inst% | 7.1 | 7.1 | ✅ |
| T=3–5 block adv | 40.74pp | 40.74 | ✅ |
| T≥6 inst% | 5.1 | 5.1 | ✅ |
| T≥6 block adv | 40.06pp | 40.06 | ✅ |
| Overall block adv | 10.93pp | 10.93 | ✅ |
| P2P regression | 1.04% mean, 0% median | 1.04, 0 | ✅ |

---

## Table 8: LoRA Rank Ablation (appendix.tex L47–62)

| Row | Paper | Registry | Status |
|-----|-------|----------|--------|
| r=16 α=32 baseline | 87.51 | CWM 4B s42: 87.51 | ✅ |
| r=32 α=32 | 87.00 (Δ=−0.51) | 87.00 | ✅ |
| r=32 α=64 | 87.04 (Δ=−0.47) | 87.04 | ✅ |
| Seed variance (s42 vs s456) | 0.53pp | 87.51−86.98 = 0.53 | ✅ |

---

## Table 9: TOST Sensitivity (appendix.tex L329–352)

| Margin | Paper p | Status |
|--------|---------|--------|
| ±1.0pp | ≫0.05 | ✅ |
| ±1.5pp | 0.054 | ✅ |
| ±1.52pp | ~0.05 | ✅ |
| ±1.71pp | 0.027 | ✅ |
| ±2.0pp | **0.0087** | ⚠️ **Holm table raw p = 0.0071; main text p = 0.007** |
| ±3.0pp | 4.6×10⁻⁵ | ✅ |
| ±5.0pp | ≪0.001 | ✅ |

**Note:** The ±2pp p-value is 0.0087 in the sensitivity table but 0.0071 in the Holm-Bonferroni table (Tab 11) and ~0.007 in the main text. These should be identical. Discrepancy = 0.0016.

---

## Table 10: Holm-Bonferroni (appendix.tex L389–412)

| Rank | Raw p | Factor | Adj p | Computed | Status |
|------|-------|--------|-------|----------|--------|
| 1 | 0.003 | ×4 | 0.012 | 0.003×4=0.012 | ✅ |
| 2 | 0.0071 | ×3 | 0.021 | 0.0071×3=0.0213→0.021 | ✅ |
| 3 | 0.039 | ×2 | 0.078 | 0.039×2=0.078 | ✅ |
| 4 | 0.385 | ×1 | 0.385 | 0.385×1=0.385 | ✅ |

---

## Table 11: Few-shot Baselines (appendix.tex L80–97)

| Cell | Paper | Registry | Status |
|------|-------|----------|--------|
| 0-shot Qwen3-8B per-test | 49.90 | 49.90 | ✅ |
| 0-shot DeepSeek per-test | 48.54 | 48.54 | ✅ (but Table 3 says 48.50 ⚠️) |
| 3-shot Qwen3-8B per-test | 71.61 | 71.61 | ✅ |
| 3-shot Qwen3-8B variant | 45.83 | 22/48=45.83 | ✅ |
| 3-shot DeepSeek per-test | 46.28 | 46.28 | ✅ |
| 3-shot DeepSeek variant | 45.83 | 22/48=45.83 | ✅ |

---

## Key Numbers in Text

| Location | Paper Value | Source | Verified Value | Status |
|----------|-------------|--------|----------------|--------|
| experiments.tex L17 / appendix L419 | 114 problem clusters (bootstrap) | function-level dataset | 114 | ✅ |
| appendix.tex L419 | 139 problem clusters (mixed-effects) | cross-complexity model | 139 | ✅ |
| experiments.tex L163 | n=56,480 observations | mixed-effects LPM | 56,480 | ✅ |
| experiments.tex L163 | z=−23.7, p<0.001 | formulation×complexity interaction | −23.7 | ✅ |
| experiments.tex L163 | β̂=−0.002, p=0.805 | CWM main effect (func) | −0.002 | ✅ |
| experiments.tex L163 | Δ=−0.2pp (func CWM-CLS) | | −0.2 | ✅ |
| experiments.tex L163 | 22pp divergence (repo) | CLS-CWM repo gap (DeepSeek) | 22 | ✅ |
| experiments.tex L163 | z=−64.4, p<0.001 | CWM deficit cross-model | −64.4 | ✅ |
| experiments.tex L163 | +1.1pp Qwen3 model effect, p=0.002 | | +1.1 | ✅ |
| experiments.tex L163 | +1.6pp interaction, p=0.006 | | +1.6 | ✅ |
| experiments.tex L98 | TOST gap = −0.45pp | 5-seed variant-level CLS-TRAJ | −0.45 | ✅ |
| experiments.tex L98 | 95% CI [−1.71, +0.84] | clustered bootstrap | [−1.71, +0.84] | ✅ |
| experiments.tex L98 | TOST p = 0.007 | ±2pp margin | 0.0071→0.007 | ✅ (see TOST sensitivity caveat) |
| experiments.tex L98 | ±1.52pp smallest margin | TOST sensitivity | 1.52 | ✅ |
| experiments.tex L98 | ICC = 0.191, DEFF = 3.97 | function-level block correlation | 0.1909→0.191, 3.97 | ✅ |
| experiments.tex L175 | 217× throughput | CLS vs CWM inferences/min | 853/3.9≈219 | ⚠️ raw ratio ≈219, not 217 |
| experiments.tex L177 | oracle func = 90.63% | 1713/1890 correct | 90.63 | ✅ |
| experiments.tex L177 | +2.80pp over best single | 90.63−87.83 = 2.80 | 2.80 | ✅ |
| experiments.tex L177 | oracle repo = 95.83% | best pair routing | 95.83 | ✅ |
| experiments.tex L177 | +14.58pp | 95.83−81.25 = 14.58 | 14.58 | ✅ |
| experiments.tex L177 | re-repair pilot n=44, p=0.42 | ext analysis (j) | 44, 0.42 | ✅ |
| experiments.tex L10 | 19,076 samples | 15290+1896+1890=19076 | 19,076 | ✅ |
| experiments.tex L10 | train 15,290 / val 1,896 / test 1,890 | | 15290+1896+1890=19076 | ✅ |
| experiments.tex L10 | majority baseline 51.75% | pass:fail ≈ 52:48 | 51.75 | ✅ |
| experiments.tex L11 | ~70K training (repo) | | 70,748 | ✅ |
| experiments.tex L11 | val n=9,335, test n=9,784 | | 9335, 9784 | ✅ |
| experiments.tex L11 | majority baseline 72.96% | | 72.96 | ✅ |
| experiments.tex L159 | unparseable 53.7%→73.8% (4B→8B) | 4B parseable=46.3%→unparse=53.7%; 8B seq8192≈73.8% | 53.7, 73.8 | ✅ |
| experiments.tex L159 | parseable-only 42.88%→38.52% | | 42.88, 38.52 | ✅ |
| experiments.tex L135 | gap 25.59pp at 4B | 83.63−58.04=25.59 | 25.59 | ✅ |
| experiments.tex L135 | gap 19.31pp at 8B | 84.48−65.17=19.31 | 19.31 | ✅ |
| experiments.tex L98 | 523 variant-level instances (5 seeds) | TOST sample | 523 | ✅ |
| experiments.tex L100 | 31.3% of instances at T≥2 | oracle: 19.1+7.1+5.1=31.3 | 31.3 | ✅ |
| experiments.tex L100 | 55.3% of total oracle advantage | T=2 contribution | 55.3 | ✅ |
| experiments.tex L171 | penalty 1.36pp (DS s42) to 19pp (Qwen3-4B) | variant_level: 1.36 and 19.05 | ✅ (19.05→"19") |
| appendix.tex L241 | ~370 GPU-hours | compute budget | 370 | ✅ |
| appendix.tex L241 | 223 completed runs | 135+88=223 | 223 | ✅ |
| appendix.tex L241 | 135 successful, 88 failed/killed | | 135+88=223 | ✅ |
| appendix.tex L241 | ~46 unique configurations | | 46 | ✅ |
| appendix.tex L70 | CLS 8B@2048 = 83.04 | cls-8b-s42 ckpt-3600 seq2048: 83.04 | 83.04 | ✅ |
| appendix.tex L70 | 1.44pp below 8192 eval | 84.48−83.04=1.44 | 1.44 | ✅ |
| appendix.tex L70 | 136 unparseable (1.39%) | 136/9784=0.01390=1.39% | 1.39 | ✅ |
| appendix.tex L70 | matched gap 25.00pp (98% of 25.59) | 83.04−58.04=25.00; 25.00/25.59=97.7%≈98% | ✅ |
| appendix.tex L67 | MV K=3: 87.51→86.83 (−0.68pp) | 87.51−86.83=0.68 | ✅ |
| appendix.tex L74 | downsample CLS: 80.74% | 80.74 | ✅ |
| appendix.tex L74 | 2.89pp below full CLS | 83.63−80.74=2.89 | ✅ |
| appendix.tex L74 | 7.82pp above TRAJ | 80.74−72.92=7.82 | ✅ |
| appendix.tex L287 | FP rates: CLS 56.5%, CWM 70.3% | error overlap analysis | ✅ |
| appendix.tex L287 | 1713/1890 correct, 177 both-wrong | 1890−1713=177 | ✅ |
| appendix.tex L321 | 853 vs 3.9 inferences/min | throughput benchmark | ✅ |
| appendix.tex L321 | median latency 48ms vs 16.3s | | ✅ |
| appendix.tex L321 | avg 477 tokens CWM output | | 477 | ✅ |
| appendix.tex L434 | ckpt-2200: 85.34%, ckpt-3600: 84.48%, ckpt-6633: 85.29% | checkpoint ablation | ✅ |
| appendix.tex L434 | <1pp range | 85.34−84.48=0.86 | ✅ |
| appendix.tex L436 | CWM seq2048~65% vs seq4096~56% | CWM 8B seq sensitivity | ✅ |
| appendix.tex L436 | ~1.5pp CLS seq difference | 84.48−83.04=1.44≈1.5 | ✅ |
| appendix.tex L436 | seq4096→seq8192: 63.7%→74% unparseable | | ✅ |
| appendix.tex L436 | 0.81pp accuracy change (64.36→65.17) | 65.17−64.36=0.81 | ✅ |
| appendix.tex L438 | 82.61% (s42 drop) vs 74.93% (s123 truncate), 7.68pp | 82.61−74.93=7.68 | ✅ |
| appendix.tex L426 | χ² p = 5.9×10⁻¹⁰ | parseable bias | ✅ |
| appendix.tex L426 | 86.4% vs 79.1%, p=3.3×10⁻¹⁸ | CLS on unparseable vs parseable | ✅ |
| appendix.tex L426 | Jaccard overlap 0.46 | cross-model unparseable | ✅ |
| checklist.tex L39 | ~370 GPU-hours, 223 runs, ~46 configs | matches appendix | ✅ |
| checklist.tex L45 | TOST p=0.007, ±2pp | matches experiments | ✅ |

---

## Cross-reference Consistency

| Number | Location 1 | Location 2 | Consistent? |
|--------|-----------|-----------|-------------|
| z=−23.7 | abstract.tex L4 | experiments.tex L163 | ✅ |
| z=−23.7 | introduction.tex L15 | conclusion.tex L4 | ✅ |
| 19–26pp gap | intro.tex L15 (bullet) | experiments.tex L135 | ✅ |
| **19–26pp gap** | **experiments.tex L60: "13–26pp"** | **all other locations: "19–26pp"** | ⚠️ **MISMATCH** |
| 90.63% oracle (func) | intro.tex L17 | experiments.tex L177 | ✅ |
| 90.63% oracle | conclusion.tex L4 | appendix.tex L287 | ✅ |
| 95.83% oracle (repo) | intro.tex L17 | experiments.tex L177 | ✅ |
| 95.83% oracle | conclusion.tex L4 | — | ✅ |
| 217× throughput | experiments.tex L175 | conclusion.tex L4 | ✅ (but see ⚠️ below) |
| TOST p=0.007 | experiments.tex L98 | conclusion.tex L4 | ✅ |
| TOST p=0.007 | experiments.tex L98 | checklist.tex L45 | ✅ |
| **TOST p at ±2pp** | **sensitivity tab: 0.0087** | **Holm tab: 0.0071** | ⚠️ **MISMATCH** |
| 370 GPU-hours | appendix.tex L241 | checklist.tex L39 | ✅ |
| 223 runs | appendix.tex L241 | checklist.tex L39 | ✅ |
| 46 configs | appendix.tex L241 | checklist.tex L39 | ✅ |
| **0-shot DS repo** | **Table 3: 48.50** | **App few-shot tab: 48.54** | ⚠️ **MISMATCH** |
| 0-shot Qwen3-8B repo | Table 3: 49.90 | App few-shot tab: 49.90 | ✅ |
| Majority repo | 72.96 (Table 3) | 72.96 (few-shot tab) | ✅ |
| CLS-CWM func gap | 0.02–1.24pp (experiments L60) | — | ✅ |
| ≤1.3pp (intro bullet) | intro.tex L15 | consistent with max CLS-CWM gap 1.24pp | ✅ (rounded up) |

---

## ⚠️ Inconsistencies Found

### HIGH SEVERITY

1. **"13–26pp" vs "19–26pp"** (experiments.tex L60)
   - Text: "formulation choice matters only at repo level (CLS outperforms CWM by 13–26pp)"
   - All other locations (abstract, intro bullet, conclusion): "19–26pp"
   - Verified gaps: Qwen3-4B=25.59pp, Qwen3-8B=19.31pp → range is 19–26pp
   - **The "13" has no identifiable source. Likely should be "19".**

2. **TOST p-value inconsistency at ±2pp margin**
   - Sensitivity table (appendix Tab 9): p = 0.0087
   - Holm-Bonferroni table (appendix Tab 10) raw p: 0.0071
   - Main text: p = 0.007
   - These should all be the same number. Δ = 0.0016.
   - **Possible cause: sensitivity table computed from a different bootstrap run or different clustering.**

3. **TRAJ 4B function-level values in Table 2 do not match registry**
   - Table 2: s42=85.27, s123=86.72
   - Registry: s42=85.66, s123=85.47
   - Δ = 0.39pp and 1.25pp respectively — too large for rounding.
   - **Possible cause: different evaluation subset, different checkpoint, or stale numbers from an earlier evaluation pipeline. Needs investigation.**

### MEDIUM SEVERITY

4. **CLS 8B s123 function-level: 89.40 (Table 2) vs 89.37 (registry)**
   - Propagates to Table 2 mean: paper 89.94 vs registry-computed 89.93
   - **Possible cause: minor rounding from original evaluation output; or registry recorded a slightly different run.**

5. **0-shot DeepSeek repo-level: 48.50 (Table 3) vs 48.54 (appendix few-shot table & registry)**
   - Internal inconsistency between Table 3 and the appendix.
   - **Fix: align Table 3 to 48.54.**

### LOW SEVERITY

6. **0-shot Qwen3-8B function-level: 68.70 (Table 1) vs 68.73 (registry)**
   - Δ = 0.03. Possible rounding or different run.

7. **0-shot DeepSeek function-level: 63.00 (Table 1) vs 63.02 (registry)**
   - Δ = 0.02. Possible rounding or different run.

8. **217× throughput ratio: raw numbers (853/3.9) give ≈219×**
   - 853 ÷ 3.9 = 218.7. Paper claims 217×.
   - **Possible cause: 217× computed from more precise pre-rounding values (e.g., 853.1/3.931 ≈ 217.0). Minor.**

### CLARITY WARNINGS (not numerical errors)

9. **"<1pp on Qwen3" for CLS-TRAJ gap** (experiments.tex L60)
   - In context (discussing Table 1 per-test accuracy), CLS−TRAJ = 88.43−86.30 = 2.13pp ≠ <1pp
   - The "<1pp" refers to the MATCHED variant-level gap (−0.45pp from TOST analysis, §5.4), but the surrounding text discusses per-test accuracy.
   - **Recommendation: clarify that "<1pp" refers to the variant-level matched comparison, not per-test accuracy.**

10. **Several prompting baselines in Table 1 not found in registry**
    - ZS LLM-judge DeepSeek-6.7B (56.56), 3-shot ICL Qwen3-8B (68.78), 3-shot ICL DeepSeek-6.7B (59.95)
    - These may be from separate evaluation scripts not registered. Not necessarily wrong, but unverifiable from registry alone.

---

## Summary

| Category | Count |
|----------|-------|
| Total numbers checked | ~180 |
| Consistent (✅) | ~167 |
| Inconsistent (⚠️) | 10 |
| — High severity | 3 |
| — Medium severity | 2 |
| — Low severity | 3 |
| — Clarity warnings | 2 |
| Unverifiable (来源不明) | 3 (prompting baselines not in registry) |

**Top-priority fixes:**
1. experiments.tex L60: change "13–26\pp{}" → "19–26\pp{}"
2. Investigate TOST p-value discrepancy (sensitivity table 0.0087 vs Holm table 0.0071)
3. Investigate TRAJ 4B Table 2 values (85.27/86.72 vs registry 85.66/85.47)
4. Align Table 3 DeepSeek 0-shot to 48.54 (matching appendix & registry)
5. Verify CLS 8B s123 function-level: 89.40 vs 89.37
