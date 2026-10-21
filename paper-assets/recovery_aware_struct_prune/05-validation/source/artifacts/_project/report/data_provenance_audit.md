# Data Provenance Audit — recovery_aware_struct_prune

Generated: 2026-05-23

**Convention:**
- **Script**: NEW = created ≥ 2026-05-23 (pred_answer/gold_answer format); OLD = before that date
- **Seed**: single seed (42) unless noted; multi-seed results show individual seeds and mean
- ⚠️ = discrepancy or missing registry record

---

## Table 1: Recovery Capacity Spectrum (`tab1_recovery_gradient.tex`)

GRPO dynamics at 20% sparsity, 100 steps. Reward metrics from GRPO training runs.

| Row | Column | Paper Value | Registry exp_id | Server | Script | Seed |
|-----|--------|-------------|-----------------|--------|--------|------|
| CKA-only | Peak Rew. | 0.354 | `grpo_cka_only_20` (peak_reward=0.3544) | westb-23072 | OLD (2026-05-17) | 42 |
| CKA-only | Mean Rew. | 0.285 | `grpo_cka_only_20` (computed from reward curve) | westb-23072 | OLD | 42 |
| CKA-only | Min f₀ | 0.125 | `grpo_cka_only_20` (from training logs) | westb-23072 | OLD | 42 |
| Random | Peak Rew. | 0.190 | `grpo_random_20` (reward_peak=0.19) | westb-23072 | OLD (2026-05-17) | 42 |
| Random | Mean Rew. | 0.164 | `grpo_random_20` (reward_final=0.164) | westb-23072 | OLD | 42 |
| Random | Min f₀ | 0.300 | `grpo_random_20` (from training logs) | westb-23072 | OLD | 42 |
| Standard | Peak Rew. | 0.081 | `grpo_standard_20_fair` (peak_reward=0.081) | westb-23072 | OLD (2026-05-18) | 42 |
| Standard | Mean Rew. | 0.050 | `grpo_standard_20_fair` (final_reward=0.054) | westb-23072 | OLD | 42 |
| Standard | Min f₀ | 0.500 | `grpo_standard_20_fair` (from training logs) | westb-23072 | OLD | 42 |
| RASP (α=1.0) | Peak Rew. | 0.061 | `grpo_rasp_20_fair` (peak_reward=0.061) | westb-23072 | OLD (2026-05-17) | 42 |
| RASP (α=1.0) | Mean Rew. | 0.031 | `grpo_rasp_20_fair` (final_reward=0.01) | westb-23072 | OLD | 42 |
| RASP (α=1.0) | Min f₀ | 0.675 | `grpo_rasp_20_fair` (from training logs) | westb-23072 | OLD | 42 |

**Result file paths** (GRPO training outputs):
- CKA-only: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/`
- Random: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/`
- Standard: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_fair/`
- RASP: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_fair/`

---

## Table 2: Reward-Accuracy Decoupling (`tab2_decoupling.tex`)

GSM8K (N=1,319) accuracy. Multi-seed mean ± std for CKA-only, Standard, Random.

| Row | SFT Acc.(%) | GRPO Acc.(%) | Δ(pp) | Peak Rew. | Registry exp_id (SFT) | Registry exp_id (GRPO) | Seed |
|-----|-------------|--------------|-------|-----------|----------------------|----------------------|------|
| Unpruned | 81.27 | 81.27 | 0.00 | 0.669 | `eval_sft_unpruned_full` (westd-11672, 2026-05-16) | `eval_grpo_unpruned_v2_step100` (westd-11672, 2026-05-16) | 42 |
| CKA-only 20% | 63.91 | 64.39±0.19 | +0.48 | 0.354 | `eval_gsm8k_sft_cka_only_20` (westd-29022, 2026-05-20) | 3-seed mean: see Table below | 3 seeds |
| Standard 20% | 59.29 | 59.84±0.38 | +0.55 | 0.081 | `eval_sft_standard_full_westd` (westd-11672, 2026-05-15) | 3-seed mean: see Table below | 3 seeds |
| RASP (α=1.0) 20% | 61.49 | 60.88 | −0.61 | 0.061 | `eval_gsm8k_sft_rasp_20` (westd-29022, 2026-05-20) | `eval_gsm8k_grpo_rasp_20_fair` (westd-29022, 2026-05-19) | 42 |
| Random 20% | 51.25 | 50.72±0.15 | −0.53 | 0.190 | `eval_gsm8k_sft_random_20` (westd-29022, 2026-05-21) | 3-seed mean: see Table below | 3 seeds |
| ShortGPT 20% | 44.73 | 43.37 | −1.36 | -- | `eval_gsm8k_sft_shortgpt_20` (westd-29022, 2026-05-19) | `eval_gsm8k_grpo_shortgpt_20` (westd-29022, 2026-05-19) | 42 |

### Multi-seed GRPO breakdown (Table 2 & Appendix Tab multiseed)

| Method | Seed 42 | exp_id | Seed 123 | exp_id | Seed 456 | exp_id | Mean |
|--------|---------|--------|----------|--------|----------|--------|------|
| CKA-only 20% | 64.37% | `eval_gsm8k_grpo_cka_only_20_v2` (westb-23072, 05-18) | 64.22% | `eval_gsm8k_grpo_cka_only_20_seed123` (westb-23072, 05-19) | 64.59% | `eval_gsm8k_grpo_cka_only_20_seed456_full` (westd-29022, 05-20) | 64.39% |
| Standard 20% | 59.44% | `eval_gsm8k_grpo_standard_20_fair_v2` (westd-29022, 05-19) | 59.89% | `eval_gsm8k_grpo_standard_20_seed123_full` (westd-29022, 05-20) | 60.20% | `eval_gsm8k_grpo_standard_20_seed456_full` (westd-29022, 05-20) | 59.84% |
| Random 20% | 50.57% | `eval_gsm8k_grpo_random_20_v2` (westd-29022, 05-21) | 50.72% | `eval_gsm8k_grpo_random_20_seed123_v2` (westd-32935, 05-22) ⚠️ NO_METRICS in registry | 50.87% | `eval_gsm8k_grpo_random_20_seed456` (westb-23072, 05-22) | 50.72% |

**Notes:**
- ⚠️ `eval_gsm8k_grpo_random_20_seed123_v2`: status=DONE, conclusion=success, but metrics field empty in registry. Paper value 50.72% sourced from result JSON on disk.
- ⚠️ CKA-only seed456: registry=64.59% (852/1319=64.594%), paper=64.58%. Rounding difference (0.01pp).
- Standard SFT: registry has two entries — `eval_gsm8k_sft_standard_20`=59.21% (seed42 SFT checkpoint) and `eval_sft_standard_full_westd`=59.29% (seeds 123/456 SFT checkpoint). Paper uses 59.29%. Appendix explains: "Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21% vs. 59.29%)."
- All GRPO evals: OLD script era (all before 2026-05-23)

---

## Table 3: α Dose-Response (`table3_alpha.tex`)

GSM8K (N=1,319) at 20% sparsity, varying α. Single seed (42).

| α | SFT Acc.(%) | exp_id (SFT) | GRPO Acc.(%) | exp_id (GRPO) | Δ(pp) |
|---|-------------|--------------|--------------|---------------|-------|
| 0.5 | 60.73 | `eval_gsm8k_sft_alpha0p5_20` (westd-32935, 05-22) | 61.18 | `eval_gsm8k_grpo_alpha0p5_20` (westd-32935, 05-22) | +0.45 |
| 1.0 | 61.49 | `eval_gsm8k_sft_rasp_20` (westd-29022, 05-20) | 60.88 | `eval_gsm8k_grpo_rasp_20_fair` (westd-29022, 05-19) | −0.61 |
| 2.0 | 64.97 | `eval_gsm8k_sft_alpha2p0_20` (westd-32935, 05-22) | 66.11 | `eval_gsm8k_grpo_alpha2p0_20` (westd-32935, 05-22) | +1.14 |
| 3.0 | 64.14 | `eval_gsm8k_sft_alpha3p0_20` (westd-32935, 05-22) | 63.46 | `eval_gsm8k_grpo_alpha3p0_20` (westd-32935, 05-22) | −0.68 |
| 4.0 | 61.94 | `eval_gsm8k_sft_alpha4_20_v5` (westd-32935, 05-22) | 62.77 | `eval_gsm8k_grpo_alpha4_20_v3` (westd-32935, 05-22) | +0.83 |

**Notes:**
- ⚠️ α=3.0 GRPO: registry=63.45% (837/1319=63.456%), paper=63.46%. Rounding (paper rounds up).
- All: OLD script era (all 05-22)
- α=4.0 SFT has v5 suffix (multiple reruns due to server issues); GRPO has v3 suffix

---

## Table 4: Sparsity Cliff at 30% (`table4_sparsity_cliff.tex`)

GSM8K at 30% sparsity, N=100 (quick eval) or N=200/500 (registry).

| Method | Acc.(%) | EOS Rate(%) | Registry exp_id | Notes |
|--------|---------|-------------|-----------------|-------|
| Standard | 4 | 5.5 | `eval_postprune_standard_30` (acc=0.04, N=200, 05-17) | Also `prune_eval_standard_30` (acc=2.8%, N=500, 05-20) |
| RASP (α=1.0) | 0 | 3.0 | `eval_postprune_rasp_30` (acc=0, N=200, 05-17) | Exact match |
| CKA-only | 0 | -- | `prune_eval_cka_only_30` (acc=1.6%, N=500 partial, 05-20) | ⚠️ Registry=1.6%, paper=0%. Different N and partial eval |

**Notes:**
- Paper uses N=100 quick eval. Registry has N=200 and N=500 versions.
- ⚠️ Standard: paper=4% matches N=200 registry (8/200=4%). The N=500 version gives 2.8%.
- ⚠️ CKA-only: paper=0% vs registry 1.6% (N=500). Possibly different evaluation run; paper footnote says "Terminated early after collapse confirmed."

---

## Table 5: Inference Efficiency (`table5_inference.tex`, main paper)

Latency averaged over 100 GSM8K problems at 20% sparsity.

| Config | Latency(s) | Speedup(%) | Memory(GB) | Mem.Red.(%) | Registry exp_id |
|--------|-----------|------------|-----------|------------|-----------------|
| Dense | 6.682 | -- | 16.22 | -- | `inference_speedup_plan016_v2` (dense.avg_latency=6.682, peak_memory=16.22GB, 05-16) |
| RASP (α=1.0) 20% | 4.156 | 37.8 | 11.60 | 28.5 | `inference_speedup_plan016_v2` (rasp.avg_latency=4.156, rasp.peak_memory=11.60GB) |
| Standard 20% | 6.167 | 7.7 | 11.61 | 28.4 | `inference_speedup_plan016_v2` (standard.avg_latency=6.167, standard.peak_memory=11.61GB) |

---

## Table (Appendix): Inference TPS/TTFT (`appendix.tex` Tab inference)

| Config | TPS(tok/s) | TTFT(ms) | Per-token(ms) | Params(B) | Registry exp_id |
|--------|-----------|---------|-------------|----------|-----------------|
| Dense 7B | 72.0 | 20.1 | 13.9 | 7.62 | `inference_bench_clean_v2` (original_tps=72.02, 05-19) |
| CKA-only 20% | 58.3 | 16.4 | 16.7 | 6.16 | `inference_bench_clean_v2` (cka_only_tps=58.3) |
| Standard 20% | 58.2 | 16.4 | 16.7 | 6.16 | `inference_bench_clean_v2` (standard_tps=58.2) |

**Notes:**
- Two separate benchmark experiments: `inference_speedup_plan016_v2` (latency/memory, westd-11672, 05-16) and `inference_bench_clean_v2` (TPS/TTFT, westb-23072, 05-19).

---

## Table: MATH-500 (`tab_math500.tex`)

MATH-500 (N=500), greedy decoding, max_new_tokens=2048.

| Row | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) | Script |
|-----|--------|--------------|---------|---------------|-------|--------|
| **Dense** | 53.0 | `eval_math500_dense_2048` (05-18) | -- | -- | -- | OLD |
| **20% method comparison** | | | | | | |
| CKA-only | 26.8 | `eval_math500_sft_cka_only_20_westd` (westd-32935, 05-22) | 27.4 | `eval_math500_grpo_cka_only_20_2048_v2` (westd-32935, 05-23) | +0.6 | SFT:OLD, GRPO:**NEW** |
| Standard | 25.8‡ | `eval_math500_sft_standard_20_2048_v2` (westd-32935, 05-19) | 26.4‡ | `eval_math500_grpo_standard_20_fair_2048_v2` (westd-32935, 05-22) | +0.6 | OLD (‡earlier extraction) |
| RASP (α=1.0) | 21.2 | `eval_math500_sft_rasp_alpha1p0_20_v2` (05-22) | 22.6 | `eval_math500_grpo_rasp_alpha1p0_20` (05-22) | +1.4 | OLD |
| Random | 14.4 | `eval_math500_sft_random_20_v3` (westd-32935, 05-22) | --- | -- | --- | OLD |
| **20% α dose-response** | | | | | | |
| α=0.5 | 25.4 | `eval_math500_sft_rasp_alpha0p5_20` (05-22) | 24.8 | `eval_math500_grpo_rasp_alpha0p5_20` (westb-23072, 05-23) | −0.6 | SFT:OLD, GRPO:**NEW** |
| α=2.0 | 24.0 | `eval_math500_sft_rasp_alpha2p0_20` (westd-32935, 05-22) | 26.2 | `eval_math500_grpo_rasp_alpha2p0_20` (westd-32935, 05-22) | +2.2 | OLD |
| α=3.0 | 23.2 | `eval_math500_sft_rasp_alpha3p0_20` (05-22) | 22.8 | `eval_math500_grpo_rasp_alpha3p0_20` (westd-32935, 05-23) | −0.4 | SFT:OLD, GRPO:**NEW** |
| α=4.0 | 26.6 | `eval_math500_sft_rasp_alpha4p0_20` (05-22) | 26.2 | `eval_math500_grpo_rasp_alpha4p0_20` (05-23) | −0.4 | SFT:OLD, GRPO:**NEW** |
| **25% sparsity** | | | | | | |
| CKA-only | 19.2 | `eval_math500_sft_cka_only_25_v2` (westd-29022, 05-21) | 18.4 | `eval_math500_grpo_cka_only_25_v2` (westd-29022, 05-21) | −0.8 | OLD |
| Standard | 14.0 | `eval_math500_sft_standard_25` (westb-23072, 05-21) | 12.8 | ⚠️ 无 registry 记录 | −1.2 | -- |

**Notes:**
- ⚠️ MATH-500 Standard 25% GRPO=12.8%: 无对应 registry 条目 (`eval_math500_grpo_standard_25` 不存在)
- `eval_math500_grpo_cka_only_20` (OLD, 05-18) gave 26.6% — superseded by `eval_math500_grpo_cka_only_20_2048_v2` (NEW, 05-23) = 27.4% after answer extraction update
- Dense 53.0% uses 2048 token limit (`eval_math500_dense_2048`). Unlimited version: 73.6% (`eval_math500_unpruned`)

---

## Table: MBPP (`tab_mbpp.tex`)

MBPP code generation (N=374), greedy decoding.

| Row | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) | Script |
|-----|--------|--------------|---------|---------------|-------|--------|
| Dense | -- | -- | 53.48 | `eval_mbpp_dense_unpruned` (pass@1=0.5348, 200/374, 05-19) | -- | OLD |
| CKA-only 20% | 12.83 | `eval_mbpp_sft_cka_only_20` (48/374, 05-19) | 14.17 | `eval_mbpp_grpo_cka_only_20` (53/374, 05-19) | +1.34 | OLD |
| Standard 20% | 12.03 | `eval_mbpp_sft_standard_20_v4` (45/374, 05-19) | 13.10 | `eval_mbpp_grpo_standard_20_v4` (49/374, 05-19) | +1.07 | OLD |
| RASP (α=1.0) 20% | 11.76 | `eval_mbpp_sft_rasp_20` (44/374, 05-19) | 13.10 | `eval_mbpp_grpo_rasp_20` (49/374, 05-19) | +1.34 | OLD |
| ShortGPT 20% | 10.43 | `eval_mbpp_sft_shortgpt_20_v2` (39/374, 05-19) | 14.44 | `eval_mbpp_grpo_shortgpt_20_v2` (54/374, 05-19) | +4.01 | OLD |

---

## Table: Cross-Scale Validation (`tab5_cross_scale.tex`)

7B values cross-referenced from Tables 1–2. 1.5B: DeepSeek-R1-Distill-Qwen-1.5B, single seed.

| Method | Scale | Rew. | GSM8K(%) | Registry exp_id (GRPO eval) | Registry exp_id (training) |
|--------|-------|------|----------|---------------------------|--------------------------|
| CKA-only | 7B | 0.354 | 64.39 | (see Table 2 multi-seed) | `grpo_cka_only_20` |
| Standard | 7B | 0.081 | 59.84 | (see Table 2 multi-seed) | `grpo_standard_20_fair` |
| RASP | 7B | 0.061 | 60.88 | (see Table 2) | `grpo_rasp_20_fair` |
| Random | 7B | 0.190 | -- | -- | `grpo_random_20` |
| CKA-only | 1.5B | 0.238 | 35.48 | `eval_gsm8k_grpo_cka_only_20_1p5b` (0.3548, 468/1319, 05-18) | `grpo_cka_only_20_1p5b` (reward_mean=0.2375) |
| Standard | 1.5B | 0.084 | 22.29 | `eval_gsm8k_grpo_standard_20_1p5b` (0.2229, 294/1319, 05-18) | `grpo_standard_20_1p5b` (reward_mean=0.0844) |
| RASP | 1.5B | 0.099 | 26.16 | `eval_gsm8k_grpo_rasp_20_1p5b` (0.2616, 345/1319, 05-18) | `grpo_rasp_20_1p5b` (final_reward=0.099) |

**Notes:** All 1.5B experiments: OLD script, single seed (42), server westb-23072 (05-18).

---

## Table: CKA Stability (`tab_cka_stability.tex`)

| Metric | Paper Value | Registry exp_id | Registry Value |
|--------|-------------|-----------------|----------------|
| Spearman ρ (min) | 0.964 | `cka_scoring_stability_ablation` (05-19) | min_combined_rho=0.964 ✓ |
| Spearman ρ (mean) | 0.979 | `cka_scoring_stability_ablation` (05-19) | mean_combined_rho=0.979 ✓ |

Also: `cka_calibration_stability_ablation` (split_half_rho=0.9932, 05-19)

---

## Table (Appendix): Cross-Sparsity Validation

| Sparsity | Method | SFT(%) | exp_id (SFT) | GRPO(%) | exp_id (GRPO) | Δ(pp) |
|----------|--------|--------|--------------|---------|---------------|-------|
| 15% | CKA-only | 72.18 | `eval_gsm8k_sft_cka_only_15` (952/1319, 05-20) | 72.76±0.57 | 3-seed mean (see below) | +0.58 |
| 15% | Standard | 66.49 | `eval_gsm8k_sft_standard_15` (877/1319, 05-20) | 65.56±0.50 | 3-seed mean (see below) | −0.93 |
| 20% | CKA-only | 63.91 | (see Table 2) | 64.39 | (see Table 2) | +0.48 |
| 20% | Standard | 59.29 | (see Table 2) | 59.84 | (see Table 2) | +0.55 |
| 25% | CKA-only | 60.12 | `eval_gsm8k_sft_cka_only_25` (westd-29022, 05-21) | 59.59 | `eval_gsm8k_grpo_cka_only_25_v3` (westd-29022, 05-21) | −0.53 |
| 25% | Standard | 50.87 | `eval_gsm8k_sft_standard_25` (westd-29022, 05-21) | 51.86 | `eval_gsm8k_grpo_standard_25` (westb-23072, 05-21) | +0.99 |
| 30% | All | Collapse | (see Table 4) | -- | -- | -- |

### 15% multi-seed breakdown

| Method | Seed 42 | exp_id | Seed 123 | exp_id | Seed 456 | exp_id | Mean |
|--------|---------|--------|----------|--------|----------|--------|------|
| CKA-only 15% | 73.09% | `eval_gsm8k_grpo_cka_only_15_v2` (05-20) | 73.09% | `eval_gsm8k_grpo_cka_only_15_seed123` (05-20) | 72.10% | `eval_gsm8k_grpo_cka_only_15_seed456` (05-20) | 72.76% |
| Standard 15% | 66.11% | `eval_gsm8k_grpo_standard_15_v2` (05-20) | 65.13% | `eval_gsm8k_grpo_standard_15_seed123_v3` (05-20) | 65.43% | `eval_gsm8k_grpo_standard_15_seed456_v3` (05-20) | 65.56% |

---

## Table (Appendix): Cross-Architecture Qwen2.5-Math-7B

GSM8K (N=200) at 20% sparsity.

| Method | Post-Prune(%) | Registry | Post-SFT(%) | Registry | EOS Rate(%) |
|--------|--------------|----------|-------------|----------|-------------|
| CKA-only | 1.0 | ⚠️ 无 registry 记录 | 51.50±3.53 | ⚠️ 无 registry 记录 (N=200 SFT eval not registered) | 27.0 |
| Standard | 18.5 | ⚠️ 无 registry 记录 | 21.00±2.88 | `eval_gsm8k_sft_qwen_standard_20` (0.21, 42/200, 05-20) | 36.5 |

**Notes:**
- ⚠️ CKA-only Post-Prune=1.0% and Post-SFT=51.50%: no registry entries found. Results likely from server-side JSON files.
- ⚠️ Standard Post-Prune=18.5%: no registry entry. Only the Post-SFT value is registered.
- Qwen GRPO eval: `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` = 48.60% (N=500, 83.8% truncated, footnote only)
- Qwen MATH-500: `eval_math500_sft_qwen_math_cka_only_20` = 21.6% (registered but not in paper)

---

## Table (Appendix): Gradient Flow Analysis

| Comparison | Gradient Ratio | Sig. Layers | Registry exp_id |
|------------|---------------|-------------|-----------------|
| CKA-only vs Standard | 2.89× | 55/56 | `gradient_flow_v3` (cka_vs_standard_ratio=2.89, 05-19) |
| CKA-only vs RASP | 2.26× | 56/56 | `gradient_flow_v3` (computed: cka_mean/rasp_mean=0.3229/0.1431=2.26×) |
| RASP vs Standard | 1.28× | 45/56 | `gradient_flow_v3` (rasp_vs_standard_ratio=1.28, 05-19) |

---

## Inline Values (experiments.tex)

| Location | Paper Value | Registry exp_id | Match? |
|----------|-------------|-----------------|--------|
| §4.1 "original unpruned model achieves 90.83%" | 90.83% | `eval_gsm8k_dense_unpruned` (0.9083, 1198/1319, 05-20) | ✓ |
| §4.1 "200 of 784 across 28 layers, ~1.45B parameters" | structural | N/A (architecture constant) | -- |
| §4.1 "4.55pp gap... p=0.0009, Cohen's d=11.1, 95% CI [3.62, 5.47]" | computed | From Table 2 multi-seed data | ✓ (derived) |
| §4.2 "CKA-only reaches 0.354 peak reward with recovery event at step 90" | 0.354 | `grpo_cka_only_20` (peak=0.3544) | ✓ |
| §4.2 "Random oscillates between 0.142 and 0.190" | 0.142–0.190 | `grpo_random_20` training logs | ✓ |
| §4.2 "Standard peaks at 0.081 (step 40)" | 0.081 | `grpo_standard_20_fair` (peak=0.081) | ✓ |
| §4.2 "RASP peaks at 0.061 (step 50) then declines to 0.010" | 0.061→0.010 | `grpo_rasp_20_fair` (peak=0.061, final=0.01) | ✓ |
| §4.2 "5.8× peak reward gap" | 5.8× | 0.354/0.061=5.80× | ✓ (derived) |
| §4.3 "mean |Δ|=0.54pp" | 0.54 | mean(0.48, 0.55, 0.53, 0.61)=0.5425≈0.54 | ✓ (derived) |
| §4.3 "15%: SFT gap 5.69pp (72.18% vs 66.49%)" | 5.69pp | 72.18−66.49=5.69 | ✓ (derived) |
| §4.3 "GRPO gap 7.20pp (72.76% vs 65.56%)" | 7.20pp | 72.76−65.56=7.20 | ✓ (derived) |
| §4.3 "extending training to 300 steps: CKA 64.37%→64.37%, Standard 59.44%→59.29%" | | See extended training section | |
| §4.4 "CKA-only achieves active learning (peak reward 4.4× Standard)" | 4.4× | 0.354/0.081=4.37≈4.4× | ✓ (derived) |
| §4.4 "unstructured pruning: SFT 87.87%, GRPO 87.64%, Δ=−0.23pp" | 87.87%, 87.64% | `eval_unstructured_20` (0.8787, 05-17), `eval_gsm8k_grpo_unstructured_20` (0.8764, 05-19) | ✓ |
| §4.5 "CKA-only diverges most (μ=0.62), Standard (μ=0.90), Random (μ=0.92), RASP (μ=0.88)" | CKA values | From CKA heatmap analysis (not a separate registry entry) | -- |
| §4.5 "2.89× mean gradient magnitude vs Standard across 55/56 layer groups" | 2.89× | `gradient_flow_v3` | ✓ |
| §4.5 "Extended GRPO: CKA 5.5× gap (0.308 vs 0.056 at step 300)" | 0.308, 0.056 | `grpo_cka_only_20_extended_300`, `grpo_standard_20_extended_300_v2` | ✓ |
| §4.5 "1.5B: CKA 35.48% ≫ RASP 26.16% > Standard 22.29%" | | (see Cross-Scale table) | ✓ |
| §4.5 "Qwen2.5-Math-7B: CKA 1.0%→51.50%, Standard 18.5%→21.00%" | | (see Cross-Arch table) | Partial (⚠️ some values not in registry) |

---

## Extended Training 300 Steps (experiments.tex §4.5, appendix)

| Claim | Registry exp_id | Registry Value | Notes |
|-------|-----------------|----------------|-------|
| CKA reward at step 300 = 0.308 | `grpo_cka_only_20_extended_300` (05-18) | reward_step300=0.3075 | ⚠️ Registry=0.3075, paper=0.308 (rounding) |
| Standard reward at step 300 = 0.056 | `grpo_standard_20_extended_300_v2` (05-18) | reward_mean_step300=0.0562 | ⚠️ Registry=0.0562, paper=0.056 (rounding) |
| CKA GSM8K stays at 64.37% | No 300-step eval registered | -- | ⚠️ Paper reuses step-100 eval (`eval_gsm8k_grpo_cka_only_20_v2`=64.37%) |
| Standard 59.44%→59.29% | No 300-step eval registered | -- | ⚠️ No separate 300-step GSM8K eval. 59.44%=step-100 GRPO seed42, 59.29%=SFT baseline |

---

## Inline Values (abstract.tex)

| Paper Value | Source |
|-------------|--------|
| "|Δ(GRPO−SFT)| ≤ 0.61pp across all four fine-grained criteria" | max(0.48, 0.55, 0.53, 0.61)=0.61 ✓ |
| "max 1.34pp including dose-response and MBPP" | MBPP CKA Δ=+1.34pp or MBPP RASP Δ=+1.34pp ✓ |
| "peak reward 4.4× vs importance-only" | 0.354/0.081=4.37≈4.4× ✓ |
| "α=2.0 (66.11%)" | Table 3 ✓ |

## Inline Values (introduction.tex)

| Paper Value | Source |
|-------------|--------|
| "mean |Δ|=0.54pp at 20%" | mean(0.48, 0.55, 0.53, 0.61)=0.5425≈0.54 ✓ |
| "max 0.61pp; 1.34pp including dose-response and MBPP" | Table 2 max=0.61; MBPP max=1.34 ✓ |
| "ShortGPT |Δ|>1pp (−1.36pp on GSM8K)" | Table 2 ✓ |
| "α=2.0 (66.11%)" | Table 3 ✓ |
| "CKA-only peak reward 4.4× Standard" | 0.354/0.081=4.37≈4.4× ✓ |

---

## Figures

### Figure 1: Dose-Response Curve (`fig1_dose_response.pdf`)
- Data source: Table 3 (α ablation) — same experiments
- Both SFT and GRPO curves plotted from the 5 α values

### Figure 2: Reward Trajectories (`fig2_reward_trajectories.pdf`)
- Data source: GRPO training logs from:
  - `grpo_cka_only_20` (CKA-only, peak=0.354)
  - `grpo_random_20` (Random, peak=0.190)
  - `grpo_standard_20_fair` (Standard, peak=0.081)
  - `grpo_rasp_20_fair` (RASP, peak=0.061)
  - Unpruned: `grpo_unpruned_v2` or similar
- Result paths: `/root/autodl-tmp/recovery_aware_struct_prune/{exp_name}/` training logs (tensorboard/wandb)

### Figure 3: Collapse Dynamics (`fig3_collapse_dynamics.pdf`)
- (a) f₀ dynamics: from same GRPO training logs as Figure 2
- (b) Gradient norm: from same GRPO training logs
- Specific values cited: "Standard transient minimum 0.017 at step 90, recovers to 2.41 at step 100"
- "RASP gradient norms remain predominantly near zero"

### Figure 4: CKA Heatmap (`fig4_cka_heatmap.pdf`)
- Data source: CKA analysis during pruning
- μ values: CKA-only=0.62, Standard=0.90, Random=0.92, RASP=0.88
- ⚠️ No dedicated registry entry for CKA heatmap data; computed during pruning step

### Figure 5: Extended Training (`fig5_extended_training.pdf`)
- Data source: `grpo_cka_only_20_extended_300` and `grpo_standard_20_extended_300_v2`
- (a) Reward: CKA oscillates 0.22–0.44; Standard 0.054→0.056
- (b) f₀: Standard > 0.5 throughout; CKA < 0.30

### Figure (Appendix): KL Divergence (`fig_appendix_kl.pdf`)
- Data source: GRPO training logs (KL between policy and reference model)
- RASP < 0.001, Random ~0.004–0.005

---

## Summary of Issues

### ⚠️ Values with No Registry Record (4)

| Paper Location | Value | Notes |
|----------------|-------|-------|
| MATH-500 tab, Standard 25% GRPO | 12.8% | No `eval_math500_grpo_standard_25` in registry |
| Cross-Arch tab, CKA Post-Prune | 1.0% | No post-prune eval registered for Qwen CKA |
| Cross-Arch tab, CKA Post-SFT | 51.50%±3.53 | N=200 SFT eval not registered |
| Cross-Arch tab, Standard Post-Prune | 18.5% | No post-prune eval registered for Qwen Standard |

### ⚠️ Minor Numerical Discrepancies (4)

| Paper Value | Registry Value | Diff | Cause |
|-------------|---------------|------|-------|
| CKA seed456 = 64.58% | 64.59% (852/1319) | 0.01pp | Rounding |
| α=3.0 GRPO = 63.46% | 63.45% (837/1319) | 0.01pp | Rounding direction |
| Extended CKA reward = 0.308 | 0.3075 | 0.0005 | Rounding |
| Extended Standard reward = 0.056 | 0.0562 | 0.0002 | Rounding |

### ⚠️ Registry Records with Empty Metrics (3)

| exp_id | Status | Notes |
|--------|--------|-------|
| `eval_gsm8k_grpo_random_20_seed123_v2` | DONE/success | Paper uses 50.72% from result JSON on disk |
| `eval_gsm8k_sft_depth_first_20` | DONE/success | Disk-full error prevented metric recording |
| `eval_gsm8k_grpo_depth_first_20` | DONE/success | Disk-full error prevented metric recording |

### ⚠️ 30% Cliff Inconsistency

| Method | Paper | Registry | N |
|--------|-------|----------|---|
| CKA-only | 0% | 1.6% | Paper: N=100, registry: N=500 partial |
| Standard | 4% | 4% (N=200) / 2.8% (N=500) | Paper: N=100 |

---

## Server Summary

| Server | Role | GPU |
|--------|------|-----|
| westb-23072 | Primary early experiments, some later seeds | 2× RTX PRO 6000 |
| westd-11672 | Early evals (unpruned, Standard SFT) | 2× RTX PRO 6000 |
| westd-29022 | Mid-phase (20%/25% evals, 1.5B) — replaced by westd-32935 | -- |
| westd-32935 | Late-phase (α dose-response, MATH-500 reruns) | 4× GPU |
