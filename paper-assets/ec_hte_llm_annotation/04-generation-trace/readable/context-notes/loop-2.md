# reviewer / loop_2.md

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`7ee68eaf2b7e05b39113.json`](../../sessions/7e/7ee68eaf2b7e05b39113.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-22T18:29:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目是纯 CPU 实验（DIM/CausalForest simulation），不涉及 GPU 训练。无 GPU 设备白名单约束。
- 论文 DDL = **2026-05-25**（距今 3 天），EMNLP 2026 ARR，8 页主文硬限制。
- exp-024 diagnostic AUC 在真实 CM 上 **0.21-0.38**（per-combo）/ pooled 0.63，远低于论文声称的 0.86。**不可在论文中声称 diagnostic 在 real CMs 上 work well**。
- 论文 experiments.tex L49 的 SE 归因已修正为 "asymmetric M⁻¹ SE propagation"，**不能退回 "CausalForest inherent SE calibration" 旧表述**（exp-027c 证伪了旧归因）。
- Registry 严重滞后：exp-024 到 exp-029 都未注册。Agent 应补录。

### 2. 🖥️ 基础设施快照
- 服务器：local-cpu（root），无 GPU
- 工作目录：`/home/ubuntu/ec_hte_llm_annotation/`（实验脚本 + results/）
- Reviewer workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/`
- 论文源码：`docs/paper/*.tex`（abstract/intro/theory/method/experiments/related_work/limitations/conclusion）
- 关键结果 CSV：`results/exp_cf_oracle_coverage_mf2dgp.csv`（exp-027c），`results/exp_asymmetric_diagnostic_auc_summary.csv`（exp-028），`artifacts/mf2/data/exp_mf2_cf_bootstrap_se.csv`（MF2 bootstrap）
- 无活跃进程 / tmux / cron / wandb

### 3. 📊 当前状态
**刚完成的审查：**
- exp-026 v2（low-budget HB）：PASS，HB 在 K=4 n=25 时 catastrophic failure（RMSE 0.612）
- exp-027/b/c（CF Oracle 系列）：PASS，确认 MF2 83% coverage gap 来自 M⁻¹ SE 不均匀放大 + coverage 度量差异
- exp-028（asymmetric diagnostic AUC）：WARNING——发现 K=2 系统性反预测（AUC=0.0）、max(score)>1 是可观测 reliability indicator、binary Z 下对称=非对称是代数必然
- exp-029（A1 sensitivity）：FAILED（Worker 超时，无产出），需重新分配
- Round 11 Action Matrix 完整审查：已提交（W1-W13 + Q3/Q5 + 遗漏的 diagnostic AUC 问题）
- experiments.tex L50 + limitations.tex 最终文本验证：PASS

**等待中：**
- exp-029 重新执行（A1 sensitivity simulation，γ sweep）
- Paper Agent 应正在处理 Round 11 修改（W1-W12）

### 4. 📋 待办
- exp-029 Worker 重新完成 → 审查 γ∈{0, 0.05, 0.1, 0.2} 下 bias/coverage 退化曲线是否 monotone 且幅度合理
- Paper Agent 提交 Remark 2 扩展 → 检查是否纳入了 exp-028 三个发现：(1) Corollary: binary Z 对称=非对称 (2) max(score)>1 screening rule (3) pooled AUC=0.63 on real CMs
- Paper Agent 提交 Appendix Y CF SE 表格 → 核实使用 exp-027c 数据（Oracle 96% vs EC-HTE 83-99% per-cell）
- Paper Agent 提交 Section 5.5 移动 + Conclusion 压缩 → 验证主文保留 1 句 multi-LLM 引用 + 总页数 ≤ 8
- 如 W9（κ ablation）被执行 → 审查 κ∈{50,100,200,500} coverage 敏感性
- Q3 GPT-4o-mini R² → 确认论文引用的是 0.756（CSV 值）而非 0.776

### 5. 🎯 战略上下文
**核心 story**：LLM annotation 误差在 subgroup 间异质 → global MC correction 在 50% K=2 配置中恶化 CATE bias → EC-HTE（HB 分层校正）解决这个问题，但优势条件性取决于 Δπ 和 expert budget → diagnostic criterion 预判何时需要 EC-HTE。

**最容易判断错的事：**
1. **MF2 的 83% ≠ exp-027c 的 92.25%**。前者是 population-weighted CATE coverage，后者是 per-subgroup coverage 平均。两种度量不可直接比较。Worker 和 Agent 容易混淆。
2. **Diagnostic AUC 有三层数字，别搞混**：0.86（synthetic symmetric）、0.82（controlled asymmetric）、0.63（real CMs pooled）、0.21-0.38（real CMs per-combo，因 n=4 极不稳定）。论文只能 claim synthetic 数字，real CM 数字必须附 caveat。
3. **W4 "50%" 措辞**：我已明确反对将 "50% of K=2 configurations" 改为 "wide range"——后者模糊且有回避嫌疑。如果 Agent 试图改，应 push back。
4. **exp-029 是 3.0→3.5 提分最关键实验**（A1 sensitivity），失败后必须尽快重跑。不要让 Paper Agent 在无 A1 数据的情况下写 "simulation confirms robustness"。
5. **F-L vs Theorem 1 区分**：F-L = 未校正估计量的标量衰减（K=1）；Theorem 1 = 校正后估计量的子群偏差（K≥2）。区分成立，但 R2 可能仍认为 incremental——这是 rebuttal 层面问题，不期望通过改论文完全解决。


---
