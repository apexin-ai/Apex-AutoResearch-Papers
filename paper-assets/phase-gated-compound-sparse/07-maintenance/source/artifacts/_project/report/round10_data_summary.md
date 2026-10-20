# Round 10 Data Summary — All Experimental Evidence

> Compiled: 2026-05-16 | EMNLP 2026 ARR deadline: 2026-05-25

---

## 1. PPL Dose Curve

### 1a. n=500 Unified Analysis (canonical)

**DeepSeek (c2_n500_deepseek, n=496)**

| Sparsity | Imp median II | 95% CI | Wilcoxon p | Rand median II | Rand p (Bonf k=4) |
|----------|--------------|--------|------------|---------------|-------------------|
| s015 | 0.3907 | [0.350, 0.443] | 1.27e-70 | 0.0139 | 0.863 (NS) |
| s020 | 1.2149 | [1.107, 1.337] | 3.98e-75 | 0.0315 | 0.280 (NS) |
| s025 | 3.9857 | [3.527, 4.359] | 1.99e-78 | 0.2574 | 0.0058 ** |
| s030 | 8.4813 | [7.754, 9.692] | 1.09e-79 | 0.5096 | 0.0059 ** |

- Imp/rand ratio: 15.5–38.6×
- Adjacent d_z: s015→s020 = −0.925, s020→s025 = −0.824, s025→s030 = −0.773
- Spearman ρ = 1.0, permutation p = 0.0417
- Dose-response monotonic: ✓

**Qwen (c2_qw_n500_r3, n=475, low+high valid filter)**

| Sparsity | Imp median II | 95% CI | Wilcoxon p | Bonf p | Rand median II | Rand Bonf p |
|----------|--------------|--------|------------|--------|---------------|------------|
| s015 | 0.0659 | [0.049, 0.093] | 8.66e-15 | 3.46e-14 | −0.0111 | 0.687 (NS) |
| s020 | 0.3073 | [0.261, 0.356] | 6.84e-42 | 2.74e-41 | 0.0153 | 0.800 (NS) |
| s025 | 1.0745 | [0.977, 1.179] | 1.06e-68 | 4.25e-68 | 0.3931 | 6.37e-11 *** |
| s030 | 3.1550 | [2.783, 3.558] | 9.21e-74 | 3.69e-73 | 0.9127 | 1.17e-14 *** |

- Imp/rand ratio: 2.7–20.1×
- Adjacent d_z: s015→s020 = −0.629, s020→s025 = −0.865, s025→s030 = −0.767
- Spearman ρ = 1.0, permutation p = 0.0417
- Dose-response monotonic: ✓
- Mid-null rate: 45.2% (filter: low+high valid only)

### 1b. bf16 Paired Statistics (n≈50, per-problem)

**DeepSeek importance (bf16_ds_imp_s015–s030)**

| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Wilcoxon p | n_paired |
|----------|--------------------|--------------|-------------|------------|----------|
| s015 | 0.3236 | 0 | 0.607 | 0 | 49 |
| s020 | 1.1520 | 0 | 0.725 | 0 | 49 |
| s025 | 3.9686 | 0 | 0.953 | 0 | 49 |
| s030 | 9.9436 | 0 | 1.126 | 0 | 49 |

**Qwen importance (bf16_qw_imp_s015–s030)**

| Sparsity | Paired median diff | Permutation p | Cohen's d_z | Bootstrap CI | Wilcoxon p | n_paired |
|----------|--------------------|--------------|-------------|-------------|------------|----------|
| s015 | 0.0476 | 0.0001 | 0.371 | [−0.005, 0.110] | 0.030 | 46 |
| s020 | 0.2075 | 0 | 0.722 | [0.067, 0.402] | 3.4e-5 | 46 |
| s025 | 1.1087 | 0 | 1.233 | [0.609, 1.469] | 0 | 46 |
| s030 | 2.6194 | 0 | 1.439 | [1.722, 3.651] | 0 | 46 |

⚠️ QW s015 n=50 CI crosses zero [−0.005, 0.110]; resolved at n=475 (CI [0.049, 0.093], p=3.5e-14).

**Random controls (bf16, both models):** All 8 conditions FAIL — no structured phase gradient. DS rand median II range 0.09–4.04; QW rand median II range 0.14–8.07. All permutation p > 0.01 or CI overlapping.

### 1c. Boundary Sparsity (s010, s035)

| Condition | II_low median | II_mid median | II_high median | Verdict |
|-----------|--------------|--------------|----------------|---------|
| DS imp s010 | 0.0151 | 0.0061 | 0.0027 | FAIL (near-zero II) |
| DS imp s035 | 28.76 | 4.95 | 0.11 | PASS (extends monotonic) |
| QW imp s010 | −0.0444 | −0.0359 | 0.0001 | FAIL (near-zero II) |
| QW imp s035 | 8.24 | 0.96 | 0.02 | PASS (extends monotonic) |

---

## 2. QW Accuracy Dose Curve (MATH-500, n=100)

Source: acc_qw_dense_n100, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100

| Sparsity | Accuracy | Correct/100 | Δ vs dense | Note |
|----------|----------|-------------|-----------|------|
| dense | 0.40 | 40 | — | |
| s015 | 0.36 | 36 | −0.04 | |
| s020 | 0.36 | 36 | −0.04 | b2_fix: +1 vs original (35→36) |
| s025 | 0.33 | 33 | −0.07 | b2_fix: unchanged (33→33) |
| s030 | 0.19 | 19 | −0.21 | steep cliff from s025 |

- s015 ≈ s020 plateau (−4pp); cliff at s025→s030 (−14pp)
- b2_fix used max_new_tokens=8192 for batch2; batch1 used 2048 (mismatch noted)
- ⚠️ s015/s030/dense batch1 未走 v2 rescore; s020 v2 rescore confirmed no change

---

## 3. DS Accuracy (8k v2, n=50, 定性观察)

Source: acc_ds_dense_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2 + pending

| Sparsity | Accuracy | Truncation Rate | Avg Tokens | Status |
|----------|----------|-----------------|-----------|--------|
| dense | 0.74 | 0.16 | 3126 | DONE |
| s015 | — | — | — | **RUNNING** |
| s020 | 0.30 | 0.58 | — | DONE |
| s025 | 0.08 | 0.76 | 6344 | DONE |
| s030 | — | — | — | **RUNNING** |

**Caveat (D086):** Truncation rate 58–76% even at 8k tokens. DS under sparsity generates extremely long outputs; accuracy = lower bound under token budget constraint. 降为定性观察，不纳入统计检验。

4k baseline for reference: ds_dense_acc=0.52 (truncation 56%), ds_s015_acc=0.36, ds_s030_acc=0.10.

---

## 4. GSM8K Cross-Benchmark (C10)

### 4a. Importance Masking Phase Gradient

Source: gsm8k_profiling_ds, gsm8k_profiling_qw

| Model | s015 | s020 | s025 | s030 | Monotonic |
|-------|------|------|------|------|-----------|
| DS median gradient | 0.241 | 0.740 | 1.992 | 4.682 | ✓ |
| DS CI | [0.077, 0.478] | [0.314, 1.119] | [0.933, 2.820] | [2.121, 10.557] | |
| DS Wilcoxon p | 0.0003 | 0.0001 | 0.0001 | 0.0001 | |
| QW median gradient | 0.039 | 0.158 | 1.100 | 2.092 | ✓ |

### 4b. Strategy Specificity (imp/rand ratio)

| Sparsity | Ratio (GSM8K) | Ratio (MATH-500 DS) | Ratio (MATH-500 QW) |
|----------|--------------|--------------------|--------------------|
| s015 | 2.3× | 28.1× | 5.9× |
| s020 | 2.5× | 38.6× | 20.1× |
| s025 | 3.8× | 15.5× | 2.7× |
| s030 | 2.8× | 16.6× | 3.5× |

Strategy specificity ratio 从 MATH-500 的 15–36× 衰减至 GSM8K 的 2.3–3.8×（task-dependent）。

### 4c. QW Random GSM8K (补全数据)

Source: gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2

| Condition | II_high median | II_mid median | II_low median | Verdict |
|-----------|---------------|--------------|--------------|---------|
| QW rand s025 | 0.718 | 1.127 | 1.459 | PASS |
| QW rand s030 | 2.310 | 2.700 | 5.200 | PASS |

Random masking 在 GSM8K s025+s030 也产生 positive compound interaction（与 MATH-500 random FAIL 不同）。

---

## 5. Additional Evidence

### 5a. sf5 Asymmetric Sparsity (sf5_asymmetric_spot)

| Config | Head% | KV% | II_low | II_mid | II_high | D (low−high) |
|--------|-------|-----|--------|--------|---------|-------------|
| A | 0.20 | 0.30 | 19.51 | 6.05 | 0.38 | 19.13 |
| B | 0.30 | 0.20 | 18.77 | 3.97 | 0.52 | 18.25 |

- Phase gradient direction 完全稳健（D > 0 both configs）
- KV sparsity 较高时 mid-phase II 更大（6.05 vs 3.97）
- Head sparsity 较高时 high-phase II 略升（0.52 vs 0.38）
- Pre-registered criterion: PASS

### 5b. Appendix B G× Correction

- 旧值: 58–241×
- 修正值: **21–64×**（per-problem additive II + aggregate PPL 修正）
- 计算脚本: `/root/autodl-tmp/pacs/compute_gx_final.py`
- 来源: memory.md（未注册为独立实验）

### 5c. Cross-Model Mann-Whitney U (n=475 reanalysis)

- Qwen 从 n=274 (complete-case) 修正为 n=475 (low+high valid only)
- 分析脚本: `analyze_n500_v2.py` → `n500_unified_final.{csv,json}`, `n500_full_statistics.md`
- Bonferroni 修订 (D066): k=4 family-wise（原 k=48）
- DS rand s025/s030: Bonf p ≈ 0.006（恢复为显著）
- BH-FDR (48 tests): rand s025/s030 fdr_p = 0.0019
- 所有 imp 条件 *** 在 n=475 下保持显著

### 5d. c4_entropy — Discrimination Collapse Mechanism

**DeepSeek (c4_entropy, 30 problems)**

| Metric | s015 | s020 | s025 | s030 |
|--------|------|------|------|------|
| Imp entropy Δ | −0.040 | −0.047 | −0.045 | −0.044 |
| Rand entropy Δ | +0.128 | +0.136 | +0.217 | +0.233 |
| Imp Gini Δ | −0.030 | −0.040 | −0.065 | −0.081 |
| Imp CV Δ | −0.564 | −0.774 | −1.287 | −1.665 |

**Qwen (qwen_c4_entropy, 30 problems)**

| Metric | s015 | s020 | s025 | s030 |
|--------|------|------|------|------|
| Imp entropy Δ | −0.073 | −0.076 | **+0.045** | −0.007 |
| Rand entropy Δ | +0.084 | +0.090 | +0.217 | +0.197 |
| Imp Gini Δ | −0.010 | −0.012 | −0.010 | −0.020 |
| Imp CV Δ | −0.045 | −0.208 | −1.491 | −1.142 |

**结论:** Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy redistribution DS 一致但 QW s025 方向反转（+0.045）— model-dependent，不作为主线机制。

### 5e. c3_llama — Cross-Architecture Validation

- Model: DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)
- 8/8 conditions complete (imp + rand × 4 sparsity)
- Within-importance phase gradient: d_z ≈ 1.0 across all sparsity levels ✓
- imp_vs_rand d_z: 0.19→0.26→0.29→0.34（仅 s030 Bonferroni p=0.029 显著）
- Random also shows significant phase gradient (d_z 0.35→0.44, CI excludes zero)
- Qualitative direction consistent; strategy×phase interaction weaker + architecture-dependent

### 5f. c5b_pilot — Phase-Gated Controller

| Metric | s025 |
|--------|------|
| Uniform median II | 1.0435 |
| Oracle median II | 0.856 |
| Oracle recovery | 18% (CI [−39, 45.8], p=0.002) |
| Heuristic median II | 0.713 |
| Heuristic recovery | 31.7% (CI [−22.8, 66], p=0.024) |
| Gate criterion | oracle > 30% |
| Gate result | **FAIL** |

Direction correct (Wilcoxon significant) but effect size insufficient. → §8 Future Work.

---

## 6. Claim–Evidence Mapping

| Claim | Status | Primary Evidence (exp_id) |
|-------|--------|--------------------------|
| C1: Strategy- and task-modulated severity | confirmed | c2_n500_deepseek, c2_qw_n500_r3 (imp/rand ratio 15–39× DS, 2.7–20× QW); gsm8k_profiling_ds/qw (ratio 衰减至 2.3–3.8×) |
| C2: Phase-modulated (low > high) | confirmed | bf16_ds_imp_s015–s030 (0.32→9.94); bf16_qw_imp_s015–s030 (0.048→2.619); n500 confirms all p < 1e-14 |
| C3: Phase-strategy crossover | confirmed | bf16_importance_s025 (imp low=7.196 > rand low=1.363; imp high=0.032 < rand high=0.818) |
| C4: Discrimination collapse | partially | c4_entropy (DS: Gini/CV ✓, entropy ✓); qwen_c4_entropy (Gini/CV ✓, entropy ✗ at s025) |
| C5: Cross-model generalization | confirmed | c2_n500_deepseek + c2_qw_n500_r3: ρ=1.0 both, QW magnitude ~1/4 DS |
| C5b: Phase-aware mitigation | gate_failed | c5b_pilot: oracle 18% < 30% gate → future work |
| C6: Sub-exponential growth | confirmed | Δ growth factors: 3.8×→4.8×→2.0× (递减) |
| C7: n=500 dose-response | confirmed | c2_n500_deepseek (n=496) + c2_qw_n500_r3 (n=475): monotonic, ρ=1.0 |
| C8: Cross-architecture (LLaMA) | partially | c3_llama: within-imp d_z≈1.0 ✓; imp_vs_rand weak (d_z 0.19–0.34); rand also shows gradient |
| C10: Cross-benchmark (GSM8K) | confirmed | gsm8k_profiling_ds/qw: monotonic ✓; gsm8k_qw_rand_s025/s030_v2: random 也显著 |
| S3→C: Model-dependent onset | confirmed | QW s015 n=50 CI crosses zero; n=475 resolves (p=3.5e-14). DS significant from s015+ |
| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 both models (n=500), perm p=0.0417 |

---

## 7. Known Caveats

1. **DS accuracy truncation-dominated**: 58–76% truncation even at 8k tokens. All DS accuracy = lower bound (D086).
2. **QW batch mismatch**: b2_fix experiments used max_new_tokens=8192 vs batch1's 2048. Impact minimal (s020: +1, s025: 0).
3. **QW s015 n=50 marginal**: bf16 CI [−0.005, 0.110] crosses zero. Resolved at n=475.
4. **Entropy mechanism model-dependent**: Qwen s025 entropy reversed (+0.045). Paper uses discrimination collapse (Gini/CV) as primary mechanism.
5. **LLaMA strategy×phase interaction weak**: d_z 0.19–0.34; random also shows phase gradient. Use "suggests"/"partial support" language.
6. **GSM8K strategy specificity 衰减**: 2.3–3.8× vs MATH-500 15–36×. Phase gradient robust, magnitude ratio task-dependent.
7. **c5b pilot gate failed**: Oracle 18% < 30%. CI crosses zero for both oracle and heuristic.
8. **Bonferroni revision (D066)**: k=4 family-wise (revised from k=48). DS rand s025/s030 restored to significant.
9. **G× correction**: Paper must update from 58–241× to 21–64×.

---

## 8. Missing / Pending Data

| Item | Status | Impact |
|------|--------|--------|
| acc_ds_s015_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |
| acc_ds_s030_8k_v2 | RUNNING | DS accuracy dose curve incomplete (3/5 points) |
| QW batch1 v2 rescore (s015/s030/dense) | Not started | Low priority: s020 v2 showed zero change |
| G× values not in registry | Post-hoc computation | Reference compute_gx_final.py; values in memory.md |
| GSM8K QW importance full metrics | In gsm8k_profiling_qw | Only summary values (0.039/0.158/1.1/2.092) without CI |