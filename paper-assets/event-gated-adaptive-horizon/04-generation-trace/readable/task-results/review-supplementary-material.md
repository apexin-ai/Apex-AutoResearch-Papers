# review supplementary material

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_supplementary-material_20260524T011013_result.json`
- **Structured JSON:** [`8c70074256e4d1d5d848.json`](../../sessions/8c/8c70074256e4d1d5d848.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

整理完毕。以下是 supplementary material 打包清单：

---

## 必须打包

### 核心代码
- `dreamer.py` — 主训练循环，含 CIVO 相关修改（variable-rate imagination, dt_embedding, TCN/RAVE/SGS 干预）
- `models.py` — RSSM world model + actor/critic，含 dt_embedding、dual-critic、SGS、TCN 等所有实验改动
- `networks.py` — 网络层定义，含 wide_critic/dual_critic 架构
- `tools.py` — 工具函数（replay buffer, logging, metrics 计算）
- `exploration.py` — 探索策略
- `parallel.py` — 并行环境管理

### 环境接口
- `envs/dmc.py` — DMC (Walker Walk, Cheetah Run) wrapper
- `envs/maniskill.py` — ManiSkill (PickCube, StackCube, PegInsertion) wrapper
- `envs/wrappers.py` — 通用环境 wrapper

### 配置
- `configs.yaml` — 所有实验配置预设（defaults + dmc_proprio + maniskill + maniskill_stackcube + maniskill_peginsertion 等）

### 依赖
- `requirements.txt` — 已存在（torch, matplotlib, mujoco, dm_control, etc.）

### 分析脚本
- `scripts/civo_detector.py` — CIVO 在线检测器
- `scripts/compute_gradient_decomposition.py` — 梯度分解分析（C7 核心证据）
- `scripts/grad_decomp_008d_corrected.py` — 修正版梯度分解
- `scripts/nve_threshold_analysis_v2.py` / `v3.py` — NVE 阈值 ROC 分析
- `nve_audit.py` / `nve_audit_v2.py` — NVE 审计
- `extract_paper_data.py` — 论文数据提取
- `analysis/compute_bootstrap_cis.py` — bootstrap 置信区间

### 数据文件（论文图表的源数据）
- `artifacts/analysis/gradient_decomposition_008d_corrected.json` — 梯度分解数据
- `artifacts/analysis/civo_decomposition_data.json` — CIVO 分解数据
- `artifacts/analysis/entropy_dynamics_data.json` — entropy 动力学数据
- `artifacts/analysis/value_vs_eval_data.json` — value vs eval 数据
- `artifacts/nve_threshold_v3.json` — NVE 阈值分析数据
- `artifacts/nve_4seed_robustness_summary.json` — 4-seed NVE 稳健性
- `artifacts/baseline_4seed_mean_ve_ratio.csv` — baseline ve_ratio profiles
- `analysis/bootstrap_cis.json` — 置信区间
- `analysis/imagination_reward_results_v2.json` — imagination reward 分析

### 图表生成脚本
- `artifacts/figures/paper/fig_style.py` — 统一图表风格
- `artifacts/figures/paper/fig1_learning_curves.py`
- `artifacts/figures/paper/fig2_nve_trajectory.py`
- `artifacts/figures/paper/fig3_factorial_grid.py` / `fig3_nve_diagnostic_d054.py`
- `artifacts/figures/paper/fig4_mechanism_diagram.py`
- `artifacts/figures/paper/fig5_dt_amplification.py`
- `artifacts/figures/paper/fig6_collapse_pathways_d054.py` / `fig6_multiple_pathways.py`
- `figures/plot_figures.py` / `figures/gen_figures.py` — 早期版本图表生成

---

## 缺失/需要创建

- **论文 LaTeX 源文件 (paper.tex + references.bib)** — 服务器上无 .tex/.bib 文件。本地只有 dream_reports 中的自动生成版本（最新 `dream_20260520T210241/best/paper.tex`），需要产出最终提交版
- **CIVO 专属 README** — 当前 README 是原始 NM512/dreamerv3-torch 的，未说明 CIVO 实验的复现步骤、gate 参数含义、实验配置对应关系
- **实验复现命令汇总** — 132 个实验的训练命令分散在 registry 和各种 shell 脚本中（launch_exp053.sh, scripts/*.sh），需要整理出论文中引用的关键实验的完整运行命令
- **超参数汇总表** — configs.yaml 中有默认值，但论文各实验的具体超参组合（gate_fixed_dt, gate_subsample_max_dt, dt_emb_freeze, imag_horizon, seed 等）需要一张 appendix 表格
- **LICENSE 声明** — 当前 LICENSE 是 MIT（继承自 NM512），需要确认衍生作品的许可声明是否需要更新

---

## 可选但推荐

- `Dockerfile` — 已存在，可直接打包便于环境复现
- `.gitignore` — 已存在
- `checkpoint_monitor.py` — 训练监控工具
- `validate_detector.py` + `detector_validation_v3.json` — CIVO 检测器验证
- `figures/paper/*.pdf` — 预生成的论文图表 PDF（reviewer 可直接查看）
- `artifacts/figures/nve_roc_curve.pdf` — ROC 曲线图
- `artifacts/figures/civo_detector_validation.pdf` — 检测器验证图
- `artifacts/actor_entropy_contrast.pdf` — actor entropy 对比图
- `logdir/` 中的关键实验 checkpoint — 体积巨大（80GB 总量），仅选择性打包论文中引用的关键 seed 的 metrics.jsonl（不含模型权重），或提供下载链接
- `scripts/eval_nve_maniskill.py` + `eval_summary_maniskill.py` — ManiSkill 评估脚本
- `analysis/signed_reward_error.py` — signed reward error 分析

---

**优先级**：先解决 paper.tex + .bib 的最终版、CIVO README 和超参数表，这三项是 CoRL supplementary 的硬性要求。

---
