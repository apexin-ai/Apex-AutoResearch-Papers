<!-- AUTO-FACTS-BEGIN (generated 2026-05-31T17:10:00Z; manually refreshed from registry by Agent; do not edit as free-form claims) -->
## 当前状态（auto-derived from registry）

**总计**: 4 个实验 — DONE 3, PREPARING 1
**DONE 分布**: success 2, negative 1

### 磁盘余量
- **seetacloud-38274**:
  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）
  - `/init`: 150M/150M 可用（已用 0%）
  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）

### RUNNING
_（无）_

### 最近完成
- `exp_002_gpu_dgp_grid` [negative] — registry updated 2026-05-31T16:58:10Z
- `exp_004_realdata_feasibility` [success] — 2026-05-31T16:45:00Z
- `exp_001_bias_bound_mvp` [success] — 2026-05-31T16:39:21Z

<!-- AUTO-FACTS-END -->

---

# Handover — 2026-05-31

> 由 Agent 根据 registry / experiment_plan / matrix 当前事实刷新。所有定量数字均附 exp_id。

## 运行中
（无）

## 待处理
- `exp_002_gpu_dgp_grid` 为 negative；必须先完成机制审计并等 Director 决策，不能默默启动同一推导链的下一步正式实验。
- `exp_003_stage1_correction_ablation` 处于 PREPARING；其 hypothesis 依赖 `exp_002_gpu_dgp_grid`，formal launch 暂停，待 exp002 negative 机制审计后再定。
- Director 2026-05-31 audit-first 决策：当前不批准重跑 `exp_002_gpu_dgp_grid`，不批准启动 `exp_003_stage1_correction_ablation` formal；必须等待 `worker_analysis_exp002_negative_mechanism_audit_v2_20260531T170911` 提交可审计 proposal，并确认 artifact 已落盘和注册。`worker_research_exp002_negative_literature_solutions_v1_20260531T170917` 只作机制解释/修复方案参考，不替代 registry 事实。
- `worker_analysis_exp002_negative_mechanism_audit_v2_20260531T170911` 回调状态为 failed，但核心 audit artifact 已落盘并注册：`art_20260531_6a9e94` / `projects/ec_hte_codex_a/artifacts/_project/report/exp002_negative_mechanism_audit_20260531.md`。按 deliverables-present 处理，仍需 Director 审查后决策。
- `worker_research_exp002_negative_literature_solutions_v1_20260531T170917` 回调状态为 failed，但 reference memo 已落盘并注册：`art_20260531_0e5bc8` / `projects/ec_hte_codex_a/artifacts/exp_002_gpu_dgp_grid/report/exp002_negative_literature_solutions_20260531.md`。该 memo 只提供修复参考，不解除 `exp_002` rerun 或 `exp_003` formal 阻塞。
- Director D004 已接受 `art_20260531_0e5bc8` literature memo 按 failed-but-deliverables-present 闭环；C003 约束生效：该 memo advisory-only，不得引用为 H1/H2 empirical support。所有后续定量结论必须来自新的 registry experiment。
- Director D003 已接受 `art_20260531_6a9e94` 作为 `exp_002_gpu_dgp_grid` negative 后续决策依据，并将该 audit Worker 按 failed-but-deliverables-present 关闭；不得重跑同一 Worker。C002 约束生效：Stage1 formal launch 继续 blocked，直到 Stage0 correction operator 与 H1 grid diagnostic 被修复，或 Director 明确豁免。
- 已派发 CPU-only proposal/spec Worker `worker_proposal_stage0_h1_repair_spec_v1_20260531T172517`，只写修复版 Stage0/H1 proposal/spec，不运行 formal experiment。目标覆盖 H1a posterior-normalized `P(G|Z)`、H1b subgroup-prior imbalance、H1c signed/signed+magnitude diagnostic。
- `report.md` 已从旧状态刷新；后续如果 registry 再变化，需要重新生成 auto facts。

## 近期结论
- `exp_001_bias_bound_mvp` [success]：在单一 positive-correlation high-misclassification/high-CATE-heterogeneity DGP 中支持 H1。`oracle_global_minus_uncorrected_gate_rmse = 0.664685`，95% CI `[0.657467, 0.671796]`；`estimated_global_minus_oracle_global_gate_rmse = 0.018089`，95% CI `[0.005478, 0.031403]`。
- `exp_002_gpu_dgp_grid` [negative]：192 个 conditions、每 condition 200 replications 的 GPU grid 未支持 H1 grid-level 判据。`global_worse_rate_difference_positive_minus_negative = -0.005000`，95% CI `[-0.085260, 0.080000]`；`bias_bound_vs_global_worse_spearman = -0.620161`，95% CI `[-0.664535, -0.483135]`；`estimated_global_minus_oracle_global_gate_rmse = 0.000766`。
- `exp_004_realdata_feasibility` [success]：公开材料部分支撑 real-data validation 设计；unit-level confusion-matrix 实验仍需要 anonymized transcripts、record-level expert/LLM labels 和 split IDs。

## 推导状态
- `exp_002_gpu_dgp_grid` 没有推翻 `exp_001_bias_bound_mvp` 的单一 worst-case success，但证伪了当前 grid operational criterion：正相关条件并未比负相关 controls 更频繁出现 oracle-global-worse，且 bias-bound diagnostic 的 rank correlation 方向相反。
- Audit artifact `art_20260531_6a9e94` 的当前归类是 correction/DGP algebra 根本问题：`exp_001_bias_bound_mvp` 使用基于 subgroup prior 的 `P(G|Z)` posterior correction；`exp_002_gpu_dgp_grid` 当前实现直接解 `transition.T`，correction estimand 不一致。下一步应先由 Director 审查修复/recriterion 路线，而不是直接重跑 exp002 或启动 Stage1 formal。
- Literature memo `art_20260531_0e5bc8` 支持同一修复方向：优先审计 prevalence-aware `P(Z|Z_hat)` posterior mixing、latent-class/soft modifier calibration、hierarchical partial pooling、SIMEX/sensitivity 等候选修复；这些是候选 hypothesis，不是 registry 事实。
- D004 允许 proposal/spec Worker 将 posterior-matrix correction、EM latent modifier model、signed diagnostic、hierarchical confusion-matrix pooling、calibrated soft modifier correction、MC-SIMEX robustness screen 作为候选方案来源；这些不能写成已验证结论。
- coverage_matrix 当前语义：`C_H1_GLOBAL_CORRECTION_WORSE` 中 `exp_002_gpu_dgp_grid` 的 failed 是 hypothesis/plan negative，不是执行失败，也不是 Worker failed。

## Matrix / Plan
- Experiment plan: 4 entries；`plan_001` DONE success，`plan_002` DONE negative，`plan_003` PREPARING，`plan_004` DONE success。
- Matrix coverage: 12/23 cells filled，11 planned。`sync_matrix_status(exp_002_gpu_dgp_grid)` 无新增变更。

## 资源状态
- `seetacloud-38274/root/cuda:0` 白名单 GPU 可见，型号 NVIDIA RTX PRO 6000 Blackwell Server Edition，显存约 97.9GB；当前 GPU util 0%、显存占用 0MB。
- `get_project_resource_usage`: 分配 0 张，实际跑 0 张，Worker 0（GPU 0 / CPU 0）。
- Active crons: 0。

## 告警
- `resource-saturation.skill.md` 与 `on-worker-done.skill.md` 文件在项目目录不可见；本次按用户注入的 always-on 规则处理。
- Codex backend 的 `submit_training_job` / `submit_on_allocated` 自动链路此前已确认不适用；exp002 是 Director 批准的一次受控 tmux 例外。后续 GPU 正式实验仍需 Director 决策和资源链路确认。
- findings/report 暂定写法：保留 `exp_001_bias_bound_mvp` 为 single-DGP worst-case evidence；`exp_002_gpu_dgp_grid` 标为 grid-level negative，阻止 H1 grid-level claim；不得写“H1 已普遍成立”。
