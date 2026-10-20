# ROADMAP

> 最后更新: 2026-05-31 15:53 UTC | 更新原因: 量化 H1/exp_002 判据并新增 H2 partial-pooling claim

## 项目目标

EC-HTE 的内部研究目标是验证并实现一套面向 LLM 分类 effect modifier 误分类的 HTE/CATE 纠偏流程。最终产出是技术报告、可复现实验包和可部署代码，不走会议论文提交流程。

核心问题：当 LLM 注释误分类率在 subgroup 间不同，并且误分类强度与真实 CATE/HTE 结构相关时，使用单一全局 confusion matrix 的纠偏可能放大 subgroup CATE bias，甚至比不纠偏更差。

## 当前主线 Hypothesis

H1: 在 misclassification rate 与真实 subgroup CATE magnitude 正相关的 DGP 中，全局 confusion-matrix correction 会 under-correct 高误差/高效应 subgroup，并 over-correct 低误差/低效应 subgroup，因此 GATE RMSE 可能高于 uncorrected。

H2: subgroup-specific correction 能降低 H1 暴露的结构性偏差；当 expert label budget 较小时，partial pooling 会比 per-subgroup independent confusion matrix 更稳健。

H3: naive CI 会低估 Stage 1 misclassification estimation uncertainty；sandwich 或 bootstrap variance adjustment 能改善 subgroup CATE coverage。

H4: adaptive expert annotation allocation 应优先投向 misclassification uncertainty 与 CATE magnitude 同时较高的 subgroup，在固定预算下优于 uniform allocation。

## Operational 判据

`exp_001_bias_bound_mvp`：唯一 primary metric 是 GATE RMSE；mean subgroup CATE bias 与 max subgroup CATE bias 是 secondary diagnostics；最低 200 replications。

H1 success for exp_001：在 positive-correlation high-misclassification/high-CATE-heterogeneity 设置中，`oracle_global - uncorrected` 的 GATE RMSE 差值大于 0，且 bootstrap 95% CI lower bound > 0。`estimated_global` 单独报告；`estimated_global - oracle_global` 用于量化 finite-sample confusion-estimation noise。如果 GATE RMSE 支持 H1 但 secondary bias diagnostics 方向相反，标记 mixed，先 Director 复核再推进 Stage 1。

H1 negative for exp_001：如果 positive-correlation worst-case 中 oracle global 不劣于 uncorrected，则 H1 暂不支持；下一步先审计 DGP construction、correction algebra、metric definitions、subgroup weighting，而不是推进 Stage 1。

`exp_002_gpu_dgp_grid`：primary metric 是 `global_worse_rate_difference_positive_minus_negative`；secondary metrics 是 `bias_bound_vs_global_worse_spearman` 与 `estimated_global_minus_oracle_global_gate_rmse`；每个 condition 最低 200 replications。

H1 success for exp_002：positive-correlation conditions 的 oracle-global-worse rate 至少比 negative-correlation controls 高 20 percentage points，且 bootstrap 95% CI lower bound > 0；bias-bound diagnostic 对 oracle-global-worse conditions 的 Spearman rho >= 0.50，且 bootstrap 95% CI lower bound > 0。estimated-global 结果必须与 oracle-global 分开报告。

H2 success for Stage 1：low expert-label budget 下，partial pooling 在 GATE RMSE 上优于 global correction，`partial_pooling_minus_global` bootstrap 95% CI upper bound < 0；相对 per-subgroup independent correction 满足 5% relative GATE RMSE non-inferiority。PEHE 和 mean subgroup CATE bias 是 secondary diagnostics。

## 短期计划

1. 完成 `exp_001_bias_bound_mvp` CPU-only 半合成 MVP simulation，验证 H1。必跑对照为 uncorrected、oracle global confusion correction、estimated global confusion correction、stratified/subgroup correction；必须拆开结构性 global-correction 偏差与 finite-sample confusion-estimation noise。
2. `exp_002_gpu_dgp_grid` 只能在 PENDING 审批、QUEUED、Director GPU allocation 后启动。GPU 实验必须使用项目白名单 `seetacloud-38274/root/cuda:0`，并在 spec 中记录 command、server、GPU 型号、driver、data_path/data_count、seed、disk estimate、expected runtime、log/checkpoint/artifact 路径。
3. 建立统一评测协议：GATE RMSE、subgroup CATE bias、PEHE、CI coverage、CI width、bound tightness。所有指标必须能追溯到 registry exp_id。
4. 维护 `experiment_plan.yaml` 与 experiment matrix 映射：H1 claim、H2 claim、Stage 0 DGP grid、Stage 1 correction ablation、real-data feasibility 均必须有 plan entry 和 target/cell 映射。
5. 并行检查 real-data validation 可行性：Rohingya corpus 字段、LLM annotation、expert label source、subgroup variables、可用 split 与复现实验权限；未确认前不把 real-data 写成已完成结果。

## Experiment Plan / Matrix 映射

当前最低覆盖目标：
- `plan_001_h1_cpu_mvp` → `C_H1_GLOBAL_CORRECTION_WORSE`, `T_STAGE0_DGP_GRID`, registry `exp_001_bias_bound_mvp`。
- `plan_002_h1_gpu_dgp_grid` → `C_H1_GLOBAL_CORRECTION_WORSE`, `T_STAGE0_DGP_GRID`, registry `exp_002_gpu_dgp_grid`。
- `plan_003_stage1_correction_ablation` → `C_PARTIAL_POOLING_BETTER_LOW_BUDGET`, `T_STAGE1_CORRECTION_ABLATION`。
- `plan_004_realdata_feasibility` → `C_REALDATA_FEASIBILITY`。

## 中期实验矩阵

Stage 0 机制验证：
- positive vs negative misclassification-CATE correlation
- high vs low misclassification heterogeneity
- high vs low CATE heterogeneity
- k=3 与 k=6 subgroup
- oracle global correction vs estimated global correction vs uncorrected

Stage 1 correction：
- uncorrected
- global confusion correction
- arm-specific correction
- per-subgroup independent correction
- hierarchical/partial-pooling correction

Stage 2 inference：
- naive CI
- sandwich-adjusted CI
- bootstrap CI
- empirical coverage 与 CI width 对比

Stage 3 allocation：
- uniform allocation
- misclassification-uncertainty-only
- CATE-magnitude-only
- joint criterion
- pilot ratio 10%、20%、30%

Real-data validation：
- Rohingya interview corpus 上验证 LLM misclassification 是否随 refugee status、gender、education 差异化变化
- leave-expert-out calibration test
- diagnostic criterion operability demonstration

## 工程产出

- `scripts/`：可复现实验入口，包含 DGP、correction、estimation、evaluation。
- `configs/`：每个实验的 YAML/JSON 配置，记录 seed、DGP 参数、预算、method。
- `artifacts/`：实验表格、图、日志、registry 可追溯输出。
- `docs/`：技术报告素材与复现说明，由 Director 汇总。
- 部署代码：提供 diagnostic calculator 和 correction workflow 的最小可调用接口。

## 决策规则

- 任何负向结果必须先汇报 Director，不得默默跑同一方向的下一步。
- 如果 exp_001 未能复现 global correction worse than uncorrected，优先诊断 DGP、correction algebra、oracle-vs-estimated 拆分和 metric 定义，而不是直接推进 Stage 1。
- GPU 实验启动前必须确认项目白名单 GPU 可见，并记录 server、GPU 型号、driver、命令、数据路径、seed。
- 所有定量结论只引用 registry 中有 exp_id 的结果。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D004 | 2026-05-31 | Accept exp002 literature solutions memo as advisor | exp_002_gpu_dgp_grid, exp_003_stage1_correction_ablation |
| D003 | 2026-05-31 | Accept exp002 mechanism audit and require Stage0 o | exp_002_gpu_dgp_grid, exp_001_bias_bound_mvp, exp_003_stage1_correction_ablation |
| D002 | 2026-05-31 | exp002 grid does not support H1 grid-level success | exp_002_gpu_dgp_grid, exp_001_bias_bound_mvp |
| D001 | 2026-05-31 | H1 CPU MVP supports global-correction-worse mechan | exp_001_bias_bound_mvp, exp_002_gpu_dgp_grid |

