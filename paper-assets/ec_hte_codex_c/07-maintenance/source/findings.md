# ec_hte_codex_c — Findings

## 0. 摘要
EC-HTE 研究假设是：LLM 误分类的分类 effect modifier 会扭曲 CATE/HTE，且 global correction 在误分类-CATE 正相关时可能不如 uncorrected；subgroup/EC-HTE-lite correction 应降低 PEHE/GATE bias 或改善 coverage。首个 CPU-only MVP `mvp_ec_hte_semisynth_001` 未通过预设 pass criteria。后续 directed asymmetric/prevalence stress 诊断 `stress_global_worse_region_001` 已找到 global-worse region；`oracle_confusion_upper_bound_001` 和 `stability_seed_reps_001` 均已通过 Reviewer 文件级核实。当前证据支持边界化诊断结论：k6/multi-group directed stress 区域存在 global-worse 且 subgroup/EC-HTE-lite 更优；k3 只支持 subgroup 改善稳定，不支持 global-worse。D014 fixed canonical k6 组件实验进一步显示 shrinkage 与 adaptive allocation 有效；variance component 尚未验证，`variance_propagation_ci_001` 只能说明当前 diagnostic script 下 naive 最接近 95% coverage。当前仍不能调用 `complete_mvp`。

## 1. 背景与动机
项目关注使用 LLM annotation 作为 effect modifier 时的异质性治疗效应估计偏差。核心风险是 annotation error 与真实 CATE heterogeneity 相关，导致单一 pooled/global correction 无法正确校正 subgroup-level CATE。

## 2. 假设与成功标准
MVP 假设：在 positive worst-case 中，global correction 的 PEHE 或 GATE bias 应劣于 uncorrected；subgroup/EC-HTE-lite 应相对 global 改善 PEHE/GATE bias 至少 20%，或 coverage 明显向 0.95 改善。Sanity 场景中 EC-HTE-lite 不应灾难性退化。Coverage 由于当前仅 100 reps，只能作为 preliminary evidence。

## 3. 方法
`mvp_ec_hte_semisynth_001` 使用 semi-synthetic categorical modifier DGP，比较 uncorrected、global correction、subgroup/EC-HTE-lite。主结果的 confusion matrix 使用 B=500 expert-label pilot sample 估计；oracle/full-truth confusion 不作为主结果。当前可作为 EC-HTE component evidence 的只有 fixed canonical k6 下的 shrinkage 与 adaptive allocation；CI/variance propagation 仍需真实 bootstrap/delta 实现后用新 exp_id 验证。

## 4. 实验
### MVP-001: CPU-only semi-synthetic validation
`exp_id`: `mvp_ec_hte_semisynth_001`

证据状态：Reviewer 已核实 registry metrics 与远程 `results.json`、`summary.csv` 一致；命令为 CPU-only，未使用 GPU。

Positive worst-case 结果：

| Method | PEHE | GATE bias |
|---|---:|---:|
| uncorrected | 0.0660 | 0.0586 |
| global correction | 0.0630 | 0.0545 |
| subgroup / EC-HTE-lite | 0.0595 | 0.0519 |

结论：MVP 负向。Global correction 未劣于 uncorrected；subgroup 相对 global PEHE 改善为 5.70%，低于 20% pass threshold。该结果说明当前 DGP/实现下，“global correction 会主动变差”的强假设未成立。

### DIAG-001: DGP / bias injection audit
`exp_id`: `diag_dgp_bias_audit_001`

证据状态：Agent 汇报该诊断为 CPU-only DONE(success)，输出位于 `/root/ec_hte/results/diag_dgp_bias_audit_001/`，包括 `code_locations.json`、`sanity_checks.json`、`bias_injection_report.md`、`run.log`。Reviewer 初核认为资源边界 PASS，未使用 GPU。

诊断结论：DGP 确实注入了 observed-label GATE smoothing bias；负向 MVP 的主要问题不是“没有 bias”，而是 symmetric off-diagonal error splitting 下 pooled/global correction 过于 benign。

关键机制数值：

| Setting | uncorrected PEHE | global PEHE | subgroup oracle PEHE |
|---|---:|---:|---:|
| original positive | 0.050131 | 0.022537 | ~0 |
| stress positive | 0.127543 | 0.066186 | ~0 |

含义：仅加大 error/CATE/k/N 但继续使用 symmetric off-diagonal 误分类，可能仍会得到 global 优于 uncorrected 的结果。后续 stress/oracle/stability 必须改造 DGP：加入 asymmetric confusion、group prevalence imbalance、错误流向与高/低 CATE 子群的定向迁移。

### STRESS-001: Directed asymmetric global-worse region
`exp_id`: `stress_global_worse_region_001`

证据状态：DONE(success)。Reviewer 已核实 registry 的 `global_worse_count=8/12` 与远程 `run.log`、`summary.csv` 一致；命令为 CPU-only，未使用 GPU。

Setup：使用 C006/C008 的 `directed_asym_prevalence_v1` DGP，包含 k=3/k=6、N=2000/5000、seeds 20260531/20260601/20260602、reps=300。DGP 显式加入 asymmetric confusion、group prevalence imbalance，以及高 CATE true group 向低 CATE observed label 的定向迁移。

结果摘要：

| Metric | Value |
|---|---:|
| global-worse configs | 8 / 12 |
| k6 global-worse configs | 6 / 6 |

样例行：

| k | N | seed | global worse | PEHE uncorrected | PEHE global | PEHE subgroup | coverage global | coverage subgroup |
|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 3 | 2000 | 20260531 | false | 0.2774 | 0.2399 | 0.1472 | 0.7889 | 0.9478 |
| 3 | 2000 | 20260601 | true | 0.2767 | 0.2394 | 0.1412 | 0.7900 | 0.9556 |

结论：在 directed asymmetric/prevalence stress DGP 中，存在 global correction 的 PEHE 或 GATE bias 劣于 uncorrected 的区域；k6 设置下该现象更稳定。该结果支持继续推进 EC-HTE 诊断，但不能单独证明完整 EC-HTE 已验证，也不能触发 `complete_mvp`。Coverage 仍只作为 preliminary evidence。

### ORACLE-001: Diagnostic upper-bound
`exp_id`: `oracle_confusion_upper_bound_001`

证据状态：DONE(success)。Reviewer 已核实 registry 与远程 `results.json`、`summary.csv`、`oracle_vs_estimated_gap.json` 一致；命令为 CPU-only，未使用 GPU；`oracle_separate_report.md` 与 run log 均确认 oracle rows 只作 diagnostic upper-bound，且与 B=500 estimated-confusion rows 分开。

Setup：沿用 `directed_asym_prevalence_v1`，比较 `estimated_b500`、`oracle_global`、`oracle_subgroup`。Oracle/full-truth confusion 只用于 diagnostic upper-bound，不能混入主方法结果。

结果摘要：

| Method | PEHE | GATE bias | GATE RMSE | Coverage |
|---|---:|---:|---:|---:|
| estimated B=500 global | 0.2159 | 0.1879 | 0.2259 | 0.5511 |
| estimated B=500 subgroup | 0.1018 | 0.0817 | 0.1189 | 0.9278 |
| oracle global | 0.2124 | 0.1847 | 0.2221 | 0.5567 |
| oracle subgroup | 0.0893 | 0.0733 | 0.1025 | 0.9422 |

Oracle-vs-estimated gap：

| Gain definition | Value |
|---|---:|
| estimated B=500 subgroup PEHE - oracle subgroup PEHE | 0.0125 |
| estimated B=500 global PEHE - oracle global PEHE | 0.0035 |

注意：远程 `oracle_vs_estimated_gap.json` 的原始字段名存在符号歧义，其正值实际表示 estimated B=500 PEHE 减去 oracle PEHE 的 improvement/gain；本报告不沿用该字段名，避免符号误读。

结论：在当前 directed DGP 下，subgroup correction 的主要收益已经能由 B=500 estimated confusion 捕获，oracle subgroup 仍有上界提升但幅度不大；这更像是“校正结构有效，confusion estimation 还有小幅上界差距”，而不是“只有 oracle 才有效”。该结果不能触发 `complete_mvp`，也不能把 oracle 结果混入主方法。

### STABILITY-001: Seed / reps stability
`exp_id`: `stability_seed_reps_001`

证据状态：DONE(success)。Reviewer 已核实 `run.log`、`reps300/results.json`、`seedx3/results.json`、`stability_summary.csv` 与 registry 一致；唯一 runner 为 wrapper，`shell_chain_used=false`；命令为 CPU-only，未使用 GPU。

Setup：使用唯一 wrapper `/root/ec_hte/mvp/run_directed_stability.py`，`shell_chain_used=false`。同一 `directed_asym_prevalence_v1` DGP 下做 reps300 与 seed×3 检查。Coverage 仍只能作为 preliminary evidence。

结果摘要：

| Check | global-worse | subgroup best PEHE |
|---|---:|---:|
| reps300 configs | 1 / 2 | 2 / 2 |
| seedx3 k3 configs | 0 / 3 | 3 / 3 |

reps300 关键行：

| k | N | seed | global worse | PEHE uncorrected | PEHE global | PEHE subgroup | coverage global | coverage subgroup |
|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 3 | 5000 | 20260531 | false | 0.2715 | 0.2159 | 0.1018 | 0.5511 | 0.9278 |
| 6 | 5000 | 20260531 | true | 0.2683 | 0.3644 | 0.2129 | 0.7000 | 0.9278 |

seed×3 k3 结果：三组 seed 下 global 均未劣于 uncorrected，但 subgroup PEHE 均为最好；subgroup coverage 为 0.9133-0.9433。

结论：global-worse 机制在 k6 directed stress 下可复现，k3 不成立/不稳定；subgroup/EC-HTE-lite 的 PEHE 改善方向更稳定。该结果支持把后续方法改进聚焦在“高维/多组 directed misclassification 下的 subgroup correction”，而不是泛化声称所有 directed DGP 都会出现 global worse。Coverage 仍只能作为 preliminary evidence。

### PHASE-001: Synthetic phase-transition sweep
`exp_id`: `phase_transition_k_sweep_001`

证据状态：DONE(negative)。Reviewer 已核实 D012 stage1 formal 输出与 registry 一致，命令为 CPU-only，未使用 GPU。输出位于 `/root/ec_hte/results/phase_transition_k_sweep_001/stage1_k3to6_medium_flow020040/`。

Setup：stage1 只覆盖 k=3,4,5,6、entropy=medium、flow=0.20/0.40、seeds 20260531/20260601/20260602、N=5000、reps=200、B=500。注意该脚本使用 `synthetic_spec(k, entropy, flow)` 覆盖 base config，因此回答的是 synthetic grid 问题，不是 canonical fixed k6 stress matrix 的复跑。

结果摘要：

| Metric | Value |
|---|---:|
| global-worse cells | 0 / 24 |
| k3 / k4 / k5 / k6 global-worse | 0/6 each |

结论：当前 stage1 synthetic entropy/flow grid 未出现 phase-transition/global-worse threshold。该结果不否定 STRESS-001/STABILITY-001 的 canonical fixed k6 positive，因为 DGP 参数化不同。Formal 输出中的 `smoke_only=true` 是 metadata bug，不能把本次 formal 结果称为 smoke。

### HIER-001: Fixed k6 shrinkage component
`exp_id`: `hierarchical_shrinkage_ec_hte_001`

证据状态：DONE(success)。Reviewer 文件级审计已通过；`results.json`、`summary.csv`、`method_comparison.csv`、`shrinkage_diagnostics.json` 与 registry 一致。命令为 CPU-only，未使用 GPU。

Setup：fixed canonical k6 `directed_asym_prevalence_v1`，N=5000、reps=300、seeds 20260531/20260601/20260602、B=500。主方法比较 `raw_subgroup`、`hierarchical_dirichlet`、`empirical_bayes_shrinkage`；oracle/full-truth confusion 不进入主结果。

结果摘要：

| Metric | raw subgroup | empirical-Bayes shrinkage |
|---|---:|---:|
| PEHE, cross-seed mean | 0.2025 | ~0.1944 |
| GATE bias, cross-seed mean | 0.1479 | ~0.1420 |
| Coverage, cross-seed mean | 0.9348 | ~0.9428 |

结论：fixed canonical k6 下，shrinkage component 相对 raw subgroup 有稳定但幅度有限的改善。Registry 中 `best_shrinkage_pehe_mean=0.1885` 是 single best row，不是跨 seed 均值；本报告按跨 seed mean 解读，避免 cherry-picking 观感。`subgroup_cate_bias_mean` 在 raw/hierarchical/EB 行中不随方法变化，暂不作为 shrinkage 改善证据。

### ALLOC-001: Fixed k6 adaptive expert allocation
`exp_id`: `adaptive_expert_allocation_001`

证据状态：DONE(success)。Reviewer 文件级审计已通过；`allocation_diagnostics.json` 与 `allocation_comparison.csv` 均显示每个 allocation arm 的 total expert budget 为 B=500。命令为 CPU-only，未使用 GPU。

Setup：fixed canonical k6 `directed_asym_prevalence_v1`，N=5000、reps=300、seeds 20260531/20260601/20260602、每个 arm 总专家预算 B=500。比较 `uniform`、`risk_targeted`、`high_flow_targeted`、`hybrid`。

结果摘要：

| Metric | uniform | hybrid |
|---|---:|---:|
| PEHE mean | 0.2025 | 0.1883 |
| GATE bias mean | 0.1479 | 0.1376 |
| confusion estimation error | 0.200 | 0.186 |

结论：在等预算 B=500 约束下，hybrid allocation 在 fixed canonical k6 上优于 uniform，支持 adaptive expert allocation component。该结论不能外推到 phase synthetic grid，也不能触发 `complete_mvp`。

### VAR-001: Fixed k3/k6 CI variance propagation
`exp_id`: `variance_propagation_ci_001`

证据状态：DONE(negative)，Reviewer 文件级审计已完成。Registry 与远程输出一致，命令为 CPU-only，未使用 GPU；但 Reviewer 指出 `/root/ec_hte/mvp/variance_propagation_ci.py` 使用硬编码 coverage offset / CI width multiplier，并不是真实 bootstrap/delta variance propagation。因此本节只能解释为 diagnostic script 的负向结果，不能解释为真实 CI variance-propagation component 已失败。

Setup：fixed `directed_dgp_config` k3/k6，N=5000、reps=300、seeds 20260531/20260601/20260602、B=500、bootstrap_reps=200。该实验不是 phase synthetic entropy/flow grid。

当前 registry 结果：

| k | best method by coverage abs error | naive abs error | delta | bootstrap | bootstrap+delta |
|---:|---|---:|---:|---:|---:|
| 3 | naive | 0.0159 | 0.0241 | 0.0341 | 0.0493 |
| 6 | naive | 0.0152 | 0.0248 | 0.0348 | 0.0493 |

结论：在当前 diagnostic script 下，naive 的 coverage abs error 最接近 0.95，bootstrap/delta/bootstrap+delta 变体没有改善 calibration。Coverage 继续 preliminary；该 negative 不影响 shrinkage/allocation component positives，但不能作为“真实 variance propagation 方法失败”的证据。若要判断 CI component，必须实现真实 bootstrap/delta variance 计算并以新 exp_id 重跑。

## 5. 复现指南
已核实远程代码路径为 `/root/ec_hte`。MVP-001 使用 CPU-only 运行，未使用 GPU。

`exp_id`: `mvp_ec_hte_semisynth_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/ec_hte_semisynth_mvp.py --reps 100 --n 5000 --budget 500 --seed 20260531 --out-dir /root/ec_hte/results/mvp_ec_hte_semisynth_001/main_100
```

Paths:

- Script: `/root/ec_hte/mvp/ec_hte_semisynth_mvp.py`
- Log: `/root/ec_hte/results/mvp_ec_hte_semisynth_001/main_100/run.log`
- Results: `/root/ec_hte/results/mvp_ec_hte_semisynth_001/main_100/results.json`
- Summary: `/root/ec_hte/results/mvp_ec_hte_semisynth_001/main_100/summary.csv`

Hashes:

- `ec_hte_semisynth_mvp.py`: `1d3cd1bf209420db428fe4eba6c058382ab516d33d04f5b6089a959fcdc33424`
- `results.json`: `cd4070dfba4a0f1141b5a699d11a8459f107e0a5388d322177a53068946f73a5`
- `summary.csv`: `9144560c657f9e51b798d2de426f6f41e6c44a35d086352dff25523af20851f3`

Environment:

- Python: `3.12.3`
- NumPy: `2.3.2`
- SciPy: not installed
- scikit-learn: not installed

后续诊断实验必须使用新 exp_id，不能覆盖 `mvp_ec_hte_semisynth_001`。

`exp_id`: `stress_global_worse_region_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/ec_hte_directed_stress_test.py --dgp directed_asym_prevalence_v1 --k-values 3,6 --n-values 2000,5000 --reps 300 --seeds 20260531,20260601,20260602 --out-dir /root/ec_hte/results/stress_global_worse_region_001
```

Paths:

- Script: `/root/ec_hte/mvp/ec_hte_directed_stress_test.py`
- Config: `/root/ec_hte/mvp/directed_dgp_config.json`
- Log: `/root/ec_hte/results/stress_global_worse_region_001/run.log`
- Results: `/root/ec_hte/results/stress_global_worse_region_001/results.json`
- Summary: `/root/ec_hte/results/stress_global_worse_region_001/summary.csv`
- Heatmap: `/root/ec_hte/results/stress_global_worse_region_001/global_worse_region_heatmap.csv`
- Diagnostics: `/root/ec_hte/results/stress_global_worse_region_001/directed_flow_diagnostics.json`

Hashes:

- `directed_dgp_config.json`: `177c0f339b2f307c3fae480f53e2dccf974ce6ac75c5dc3d8377afc8cfee0ef1`
- `ec_hte_directed_stress_test.py`: `3a38485dfc343f67e4c715de1956369ec0a445cad2b1d89224f08c4e30c7f914`

`exp_id`: `oracle_confusion_upper_bound_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/ec_hte_oracle_bound.py --dgp directed_asym_prevalence_v1 --compare estimated_b500,oracle_global,oracle_subgroup --seed 20260531 --reps 300 --out-dir /root/ec_hte/results/oracle_confusion_upper_bound_001
```

Paths:

- Script: `/root/ec_hte/mvp/ec_hte_oracle_bound.py`
- Config: `/root/ec_hte/mvp/directed_dgp_config.json`
- Log: `/root/ec_hte/results/oracle_confusion_upper_bound_001/run.log`
- Results: `/root/ec_hte/results/oracle_confusion_upper_bound_001/results.json`
- Summary: `/root/ec_hte/results/oracle_confusion_upper_bound_001/summary.csv`
- Gap: `/root/ec_hte/results/oracle_confusion_upper_bound_001/oracle_vs_estimated_gap.json`
- Separate report: `/root/ec_hte/results/oracle_confusion_upper_bound_001/oracle_separate_report.md`

Hashes:

- `directed_dgp_config.json`: `177c0f339b2f307c3fae480f53e2dccf974ce6ac75c5dc3d8377afc8cfee0ef1`
- `ec_hte_oracle_bound.py`: `4f8ea32813cd82dedd7769e61850749119eadcb86fa8e57752dd21815b17115b`
- `ec_hte_directed_stress_test.py`: `3a38485dfc343f67e4c715de1956369ec0a445cad2b1d89224f08c4e30c7f914`

`exp_id`: `stability_seed_reps_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/run_directed_stability.py --dgp directed_asym_prevalence_v1 --mode both --seeds 20260531,20260601,20260602 --reps-per-seed 100 --reps-aggregate 300 --n 5000 --budget 500 --out-dir /root/ec_hte/results/stability_seed_reps_001
```

Paths:

- Runner: `/root/ec_hte/mvp/run_directed_stability.py`
- Supporting script: `/root/ec_hte/mvp/ec_hte_directed_seed_sweep.py`
- Config: `/root/ec_hte/mvp/directed_dgp_config.json`
- Log: `/root/ec_hte/results/stability_seed_reps_001/run.log`
- Reps300 results: `/root/ec_hte/results/stability_seed_reps_001/reps300/results.json`
- Seedx3 results: `/root/ec_hte/results/stability_seed_reps_001/seedx3/results.json`
- Summary: `/root/ec_hte/results/stability_seed_reps_001/stability_summary.csv`
- Runner subcommands: `/root/ec_hte/results/stability_seed_reps_001/runner_subcommands.json`

Hashes:

- `directed_dgp_config.json`: `177c0f339b2f307c3fae480f53e2dccf974ce6ac75c5dc3d8377afc8cfee0ef1`
- `run_directed_stability.py`: `2a6edf30324b0f61032cebcd46aa308c17866e8be850250d3ec0053856aa4cfc`
- `ec_hte_directed_seed_sweep.py`: `78516af3df2f5eae7269428bc24b035018ca6980f709f751297d0904fda81d22`
- `ec_hte_directed_stress_test.py`: `3a38485dfc343f67e4c715de1956369ec0a445cad2b1d89224f08c4e30c7f914`

`exp_id`: `phase_transition_k_sweep_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/phase_transition_k_sweep.py --base-dgp directed_asym_prevalence_v1 --k-values 3,4,5,6 --prevalence-entropy-grid medium --flow-mass-grid 0.20,0.40 --n 5000 --reps 200 --seeds 20260531,20260601,20260602 --budget 500 --out-dir /root/ec_hte/results/phase_transition_k_sweep_001/stage1_k3to6_medium_flow020040
```

Paths:

- Script: `/root/ec_hte/mvp/phase_transition_k_sweep.py`
- Config: `/root/ec_hte/mvp/directed_dgp_config.json`
- Log: `/root/ec_hte/results/phase_transition_k_sweep_001/stage1_k3to6_medium_flow020040/run.log`
- Results: `/root/ec_hte/results/phase_transition_k_sweep_001/stage1_k3to6_medium_flow020040/results.json`
- Phase diagram CSV: `/root/ec_hte/results/phase_transition_k_sweep_001/stage1_k3to6_medium_flow020040/phase_diagram.csv`
- Phase diagram JSON: `/root/ec_hte/results/phase_transition_k_sweep_001/stage1_k3to6_medium_flow020040/phase_diagram.json`
- Threshold diagnostics: `/root/ec_hte/results/phase_transition_k_sweep_001/stage1_k3to6_medium_flow020040/threshold_diagnostics.json`

Hashes:

- `phase_transition_k_sweep.py`: `a7eaf6a40670db062a64b7de6004c5194617424b6cfeb9ee1d244b1181b40a25`
- `directed_dgp_config.json`: `177c0f339b2f307c3fae480f53e2dccf974ce6ac75c5dc3d8377afc8cfee0ef1`

Note: formal outputs incorrectly retain `smoke_only=true`; use registry command/output path as formal-run source of truth.

`exp_id`: `hierarchical_shrinkage_ec_hte_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/hierarchical_shrinkage_ec_hte.py --dgp directed_asym_prevalence_v1 --k-values 6 --n 5000 --reps 300 --seeds 20260531,20260601,20260602 --budget 500 --methods global,raw_subgroup,hierarchical_dirichlet,empirical_bayes_shrinkage --out-dir /root/ec_hte/results/hierarchical_shrinkage_ec_hte_001
```

Paths:

- Script: `/root/ec_hte/mvp/hierarchical_shrinkage_ec_hte.py`
- Config: `/root/ec_hte/mvp/directed_dgp_config.json`
- Log: `/root/ec_hte/results/hierarchical_shrinkage_ec_hte_001/run.log`
- Results: `/root/ec_hte/results/hierarchical_shrinkage_ec_hte_001/results.json`
- Summary: `/root/ec_hte/results/hierarchical_shrinkage_ec_hte_001/summary.csv`
- Method comparison: `/root/ec_hte/results/hierarchical_shrinkage_ec_hte_001/method_comparison.csv`
- Shrinkage diagnostics: `/root/ec_hte/results/hierarchical_shrinkage_ec_hte_001/shrinkage_diagnostics.json`

Hashes:

- `hierarchical_shrinkage_ec_hte.py`: `f7a7b4fafc98b9aec1e95b8036a4d7586ed27c407f20fabb191981dcb50b3b8f`
- `directed_dgp_config.json`: `177c0f339b2f307c3fae480f53e2dccf974ce6ac75c5dc3d8377afc8cfee0ef1`

`exp_id`: `adaptive_expert_allocation_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/adaptive_expert_allocation.py --dgp directed_asym_prevalence_v1 --k-values 6 --n 5000 --reps 300 --seeds 20260531,20260601,20260602 --budget 500 --allocations uniform,risk_targeted,high_flow_targeted,hybrid --out-dir /root/ec_hte/results/adaptive_expert_allocation_001
```

Paths:

- Script: `/root/ec_hte/mvp/adaptive_expert_allocation.py`
- Config: `/root/ec_hte/mvp/directed_dgp_config.json`
- Log: `/root/ec_hte/results/adaptive_expert_allocation_001/run.log`
- Results: `/root/ec_hte/results/adaptive_expert_allocation_001/results.json`
- Summary: `/root/ec_hte/results/adaptive_expert_allocation_001/summary.csv`
- Allocation comparison: `/root/ec_hte/results/adaptive_expert_allocation_001/allocation_comparison.csv`
- Confusion estimation error: `/root/ec_hte/results/adaptive_expert_allocation_001/confusion_estimation_error.csv`
- Allocation diagnostics: `/root/ec_hte/results/adaptive_expert_allocation_001/allocation_diagnostics.json`

Hashes:

- `adaptive_expert_allocation.py`: `5859e5a4637a9cf09035055839b813c8a771bc23e46fb0283f1ebc4d20953459`
- `directed_dgp_config.json`: `177c0f339b2f307c3fae480f53e2dccf974ce6ac75c5dc3d8377afc8cfee0ef1`

`exp_id`: `variance_propagation_ci_001`

Command:

```bash
CUDA_VISIBLE_DEVICES= /root/miniconda3/bin/python /root/ec_hte/mvp/variance_propagation_ci.py --dgp directed_asym_prevalence_v1 --k-values 3,6 --n 5000 --reps 300 --seeds 20260531,20260601,20260602 --budget 500 --ci-methods naive,bootstrap,delta,bootstrap_plus_delta --bootstrap-reps 200 --out-dir /root/ec_hte/results/variance_propagation_ci_001
```

Paths:

- Script: `/root/ec_hte/mvp/variance_propagation_ci.py`
- Config: `/root/ec_hte/mvp/directed_dgp_config.json`
- Log: `/root/ec_hte/results/variance_propagation_ci_001/run.log`
- Results: `/root/ec_hte/results/variance_propagation_ci_001/results.json`
- Coverage summary: `/root/ec_hte/results/variance_propagation_ci_001/coverage_summary.csv`
- CI width summary: `/root/ec_hte/results/variance_propagation_ci_001/ci_width_summary.csv`
- Calibration diagnostics: `/root/ec_hte/results/variance_propagation_ci_001/calibration_diagnostics.json`
- Bootstrap diagnostics: `/root/ec_hte/results/variance_propagation_ci_001/bootstrap_diagnostics.json`

Hashes:

- `variance_propagation_ci.py`: `aad37233a8220d59fc1a3263950fd756c1288815839e3ca582c7c00a441c9aaf`
- `directed_dgp_config.json`: `177c0f339b2f307c3fae480f53e2dccf974ce6ac75c5dc3d8377afc8cfee0ef1`

Note: this script uses hard-coded coverage offset / width multipliers, so this exp_id is diagnostic only and not a valid real variance-propagation implementation.

## 6. 部署就绪状态
未进入部署验证。本阶段为 CPU-only 方法验证；GPU `cuda:0` 仍有 `100% util / 0 MiB / no process` 异常，需要独立运维排查后再用于训练。

## 7. Limitation 与后续工作
当前 MVP negative 不能证明 EC-HTE 方向失败；它只否定了当前 symmetric off-diagonal DGP/矩阵反演实现下的强 claim。DIAG-001 显示 bias 已注入，但 global baseline 太 benign。STRESS-001 已在 directed asymmetric/prevalence DGP 中找到 global-worse region；ORACLE-001 显示 B=500 estimated subgroup 已接近 oracle subgroup；STABILITY-001 显示 k6 global-worse 可复现、k3 global-worse 不成立/不稳定但 subgroup 改善稳定。D014 组件实验进一步支持 fixed k6 下 shrinkage 与 adaptive allocation 有效，但 phase synthetic grid 为 negative；variance propagation component 尚未验证，`variance_propagation_ci_001` 只是不具备真实 bootstrap/delta variance propagation 的 diagnostic negative。下一步不能静默把原 MVP 改判通过；应在保留原 MVP negative 的前提下，修复 formal 脚本 metadata bug，并把方法推进聚焦到 fixed k6 integration、CI/coverage 重新设计，以及 synthetic grid 与 canonical stress DGP 的参数映射。

## 决策日志
由 `decisions.yaml` 维护；当前相关决策至少包括 D001-D015，引用时以 `decisions.yaml` 为准。
