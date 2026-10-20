# Full Results Summary

Generated: 2026-05-16 | Total experiments with PPL: 47

Baselines: rho=0.4 uniform PPL = 17.694, rho=0.6 uniform PPL = 17.766

## 1. Main Results (uniform, adaptive, ess_only)

| exp_id | method | rho | tau | b | n_min | seed | eval_ppl_holdout | delta_vs_uniform | conclusion | claim | notes |
|--------|--------|-----|-----|---|-------|------|------------------|------------------|------------|-------|-------|
| adaptive_seed123 | adaptive | 0.4 | 0.8 | - | 2 | 123 | 17.6308 | -0.063 | success | 1 | ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。 |
| grid_b0_5_seed123 | grid_b | 0.4 | - | 0.5 | 2 | 123 | 17.6380 | -0.056 | success | 3 |  |
| adaptive_seed456 | adaptive | 0.4 | 0.8 | - | 2 | 456 | 17.6419 | -0.052 | success | 1 | ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。 |
| adaptive_fix_seed123 | adaptive | 0.4 | 0.8 | - | 2 | 123 | 17.6432 | -0.051 | success | 1 | 最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126944 |
| adaptive_seed42 | adaptive | 0.4 | 0.8 | - | 2 | 42 | 17.6440 | -0.050 | success | 1 | ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。 |
| adaptive_fix_seed42 | adaptive | 0.4 | 0.8 | - | 2 | 42 | 17.6527 | -0.041 | success | 1 | 最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801 |
| adaptive_fix_seed456 | adaptive | 0.4 | 0.8 | - | 2 | 456 | 17.6566 | -0.037 | success | 1 | 最终清理后重提交。从 checkpoint-1000 恢复，无 inline eval。PID=127285 |
| uniform_seed123 | uniform | 0.4 | - | - | - | 123 | 17.6861 | -0.008 | success | 1 | Uniform weighting baseline (no provenance information) for comparison with grid- |
| uniform_seed42 | uniform | 0.4 | - | - | - | 42 | 17.6939 | -0.000 | success | 1 | Uniform weighting baseline (no provenance information) for comparison with grid- |
| uniform_seed456 | uniform | 0.4 | - | - | - | 456 | 17.7015 | +0.007 | success | 1 | Uniform weighting baseline (no provenance information) for comparison with grid- |
| ess_only_seed456 | ess_only | 0.4 | - | - | 2 | 456 | 17.7190 | +0.025 | success | 1 | ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual- |
| ess_only_seed123 | ess_only | 0.4 | - | - | 2 | 123 | 17.7200 | +0.026 | success | 1 |  |
| ess_only_seed42 | ess_only | 0.4 | 0.8 | - | 2 | 42 | 17.7300 | +0.036 | success | 1 | ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — pr |
| contamination_60_grid_b0_5_seed42 | grid_b | 0.6 | - | 0.5 | 2 | 42 | 17.7040 | -0.062 | success | 2 | 训练完成 6103/6103 steps。EXIT_CODE=129 (SIGHUP) 发生在训练完成后（与 contamination_60_uniform_ |
| contamination_60_tau07_seed42 | adaptive | 0.6 | 0.7 | - | 2 | 42 | 17.7300 | -0.036 | success | 2 | D045 最高优先级。cuda:0, PID=282223, ρ=0.6 τ=0.7 (formula τ=1-ρ×0.5)。参数确认: tau=0.7, n_ |
| contamination_60_tau06_seed42 | adaptive | 0.6 | 0.6 | - | 2 | 42 | 17.7359 | -0.030 | success | 2 | D045 第二数据点。GPU 队列: cuda:2 (ess_only 完成后)。脚本: scripts/run_contamination_60_tau06. |
| contamination_60_seed42_r2 | adaptive | 0.6 | 0.8 | - | 2 | 42 | 17.7400 | -0.026 | success | 2 | Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 a |
| contamination_60_uniform_seed42 | uniform | 0.6 | - | - | - | 42 | 17.7660 | +0.000 | success | 2 | 训练实际已完成 (6103/6103 steps, 3:35:04)。模型已保存到 output/models/contamination_60_uniform |
| contamination_60_ess_only_seed42 | ess_only | 0.6 | 0.8 | - | 2 | 42 | 17.7700 | +0.004 | success | 2 | ρ=0.6 ESS-only PPL=17.77 ≈ uniform (17.766), max-intervention 在高 contamination 下 |

## 2. Ablations (nmin, tau_sweep, batchsize)

| exp_id | method | rho | tau | b | n_min | seed | eval_ppl_holdout | delta_vs_uniform | conclusion | claim | notes |
|--------|--------|-----|-----|---|-------|------|------------------|------------------|------------|-------|-------|
| bs8_nmin2_seed42_r2 | batchsize | 0.4 | 0.8 | - | 2 | 42 | 17.7300 | +0.036 | negative | 3 | 训练完成 6103/6103 steps, train_loss=5.4065. EXIT_CODE=129 (SIGHUP) 发生在训练完成后 W&B fin |
| nmin4_seed42 | nmin_ablation | 0.4 | 0.8 | - | 4 | 42 | 17.6947 | +0.001 | success | 3 | Mid-training check @step 2036/6103: b=0.0, ess=4.0 (=n_min), weighted_loss==unwe |
| nmin1_seed42 | nmin_ablation | 0.4 | 0.8 | - | 1 | 42 | 17.7890 | +0.095 | success | 3 | 训练完成(EXIT_CODE=0, 4h50m)。PPL=17.789，比 adaptive_fix(n_min=2, 17.650) 差 +0.139，比 u |
| tau_07_seed42 | tau_sweep | 0.4 | 0.7 | - | 2 | 42 | 17.6793 | -0.015 | success | 3 | τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ redu |
| tau_06_seed42 | tau_sweep | 0.4 | 0.6 | - | 2 | 42 | 17.6805 | -0.013 | success | 3 | PPL=17.681 劣于 τ=0.8 baseline (17.650)，conclusion=negative。概念修正：τ 越低 → α_eff 下界越松 |
| tau_05_seed42 | tau_sweep | 0.4 | 0.5 | - | 2 | 42 | 17.6880 | -0.006 | success | 3 | τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower boun |
| tau_09_seed42 | tau_sweep | 0.4 | 0.9 | - | 2 | 42 | 17.7120 | +0.018 | negative | 3 | τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality |
| tau_095_seed42 | tau_sweep | 0.4 | 0.95 | - | 2 | 42 | 17.7230 | +0.029 | negative | 3 | τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — |

## 3. Alternative Baselines (golden_ratio, detect_remove, threshold, random_reweight)

| exp_id | method | rho | tau | b | n_min | seed | eval_ppl_holdout | delta_vs_uniform | conclusion | claim | notes |
|--------|--------|-----|-----|---|-------|------|------------------|------------------|------------|-------|-------|
| detect_remove_baseline_seed42 | detect_remove | 0.4 | - | - | - | 42 | 17.2900 | -0.404 | success | 1 | 完成时 conclusion 指引: b=0 throughout; adaptive degenerates to uniform post-filterin |
| golden_ratio_seed42 | golden_ratio | 0.4 | 0.8 | - | 2 | 42 | 17.6540 | -0.040 | success | 1 | Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real  |

## 4. Grid Sweep (all grid_b points)

| exp_id | method | rho | tau | b | n_min | seed | eval_ppl_holdout | delta_vs_uniform | conclusion | claim | notes |
|--------|--------|-----|-----|---|-------|------|------------------|------------------|------------|-------|-------|
| grid_b0_3_seed42 | grid_b | 0.4 | - | 0.3 | 2 | 42 | 17.6400 | -0.054 | success | 3 | Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-be |
| grid_b0_5_seed123 | grid_b | 0.4 | - | 0.5 | 2 | 123 | 17.6380 | -0.056 | success | 3 |  |
| grid_b0_5_seed456 | grid_b | 0.4 | - | 0.5 | 2 | 456 | 17.6500 | -0.044 | success | 3 | 重提交成功（retry_count=1）。原 OOM 因 cuda:1 残留 eval 进程。已清理 exit marker，日志重定向正常。step 56/6 |
| grid_b0_5_seed42 | grid_b | 0.4 | - | 0.5 | 2 | 42 | 17.6510 | -0.043 | success | 3 | From batch run grid_b_seed42_batch, b=0.5 |
| grid_b1_0_seed123 | grid_b | 0.4 | - | 1.0 | 2 | 123 | 17.6740 | -0.020 | success | 3 |  |
| grid_b1_0_seed456 | grid_b | 0.4 | - | 1.0 | 2 | 456 | 17.6800 | -0.014 | success | 3 | Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b basel |
| grid_b1_0_seed42 | grid_b | 0.4 | - | 1 | 2 | 42 | 17.6920 | -0.002 | success | 3 | From batch run grid_b_seed42_batch, b=1 |
| grid_b1_5_seed123 | grid_b | 0.4 | - | 1.5 | 2 | 123 | 17.7010 | +0.007 | success | 3 |  |
| grid_b1_5_seed456 | grid_b | 0.4 | - | 1.5 | 2 | 456 | 17.7100 | +0.016 | success | 3 | Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b basel |
| grid_b1_5_seed42 | grid_b | 0.4 | - | 1.5 | 2 | 42 | 17.7180 | +0.024 | success | 3 | From batch run grid_b_seed42_batch, b=1.5 |
| grid_b2_0_seed123 | grid_b | 0.4 | - | 2.0 | 2 | 123 | 17.7250 | +0.031 | success | 3 |  |
| grid_b2_0_seed42 | grid_b | 0.4 | - | 2 | 2 | 42 | 17.7410 | +0.047 | success | 3 | From batch run grid_b_seed42_batch, b=2 |
| grid_b2_0_seed456 | grid_b | 0.4 | - | 2.0 | 2 | 456 | 17.9890 | +0.295 | success | 3 | checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2 |
| grid_b3_0_seed123 | grid_b | 0.4 | - | 3.0 | 2 | 123 | 17.7600 | +0.066 | success | 3 | 训练完成，eval 未执行（should_evaluate=false，缺少 --eval_data_path 和 --eval_steps）。Checkpoi |
| grid_b3_0_seed42 | grid_b | 0.4 | - | 3 | 2 | 42 | 17.7740 | +0.080 | success | 3 | From batch run grid_b_seed42_batch, b=3 |
| grid_b3_0_seed456 | grid_b | 0.4 | - | 3.0 | 2 | 456 | 17.9210 | +0.227 | success | 3 | checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2 |
| grid_b5_0_seed123 | grid_b | 0.4 | - | 5.0 | 2 | 123 | 17.8039 | +0.110 | success | 3 | PID 94717 已确认存活（SSH 验证 2026-05-14T11:39）。旧 PID 92798 已 kill，cron 重新注册。 |
| grid_b5_0_seed42 | grid_b | 0.4 | - | 5 | 2 | 42 | 17.8180 | +0.124 | success | 3 | From batch run grid_b_seed42_batch, b=5 |
| grid_b5_0_seed456 | grid_b | 0.4 | - | 5.0 | 2 | 456 | 17.9930 | +0.299 | success | 3 | checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2 |
| contamination_60_grid_b0_5_seed42 | grid_b | 0.6 | - | 0.5 | 2 | 42 | 17.7040 | -0.062 | success | 2 | 训练完成 6103/6103 steps。EXIT_CODE=129 (SIGHUP) 发生在训练完成后（与 contamination_60_uniform_ |
