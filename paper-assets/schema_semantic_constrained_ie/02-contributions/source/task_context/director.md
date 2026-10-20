---
loop: 11
reason: max_messages
updated: '2026-05-25T19:57:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文已进入审稿阶段（review_chat_id: `oc_01fc90ae186a4ed432770f7601995139`），正文修改需同步通知 Paper Agent
- EMNLP 2026 ARR May 25 deadline（今天），正文 8 页硬限
- Table 2 的 Qwen DocRED 数据有两个来源：w5 (R-F1=40.56, 标准 LoRA) 和 d065 (R-F1=40.79, 4096 context rank 2)，不要混用
- 70B DocRED 实验全部是 200-doc subset，不是 998-doc，caption 需修正

### 2. 🖥️ 基础设施快照
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/`
- 论文目录: `artifacts/_project/paper/`（main.tex + ~55 个 .tex 文件）
- Registry: `agent/registry.yaml`（7630 行，164 个实验）
- 数据文件: `artifacts/_project/data/`（bootstrap_ci_results.json, table1_docred_v2.json, runtime_benchmark.json 等）
- 图表脚本: `artifacts/figures/`（gen_fig*.py, plot_pareto_dual_v2.py）
- 无活跃 GPU 进程 / 无 RUNNING 实验

### 3. 📊 当前状态
刚完成全文数据真实性审计（~600+ 数值），已通过 `director_reply_to_user` 发送完整报告。

发现 3 个需修正问题：
1. appendix_70b_ablation.tex: "−8.45pp" 应为 "−8.25pp"（算术错误）
2. appendix_70b_ablation.tex: tab:70b-docred-ablation caption 写 "998 docs" 应为 "200 docs"
3. 正文 "15–74%" rejection rate 下界应为 ~14%（实际最小 13.9%）

3 个需澄清问题：
4. Abstract "~1.5×" vs 正文 "1.39×"（不同 baseline：前者 vs unconstrained greedy，后者 vs S1 greedy）
5. 70B DocRED ZS S1 CF=173 count 与 registry CF_pct=5.34% 换算不匹配
6. Post-hoc 表 vs Table 2 的 Qwen DocRED R-F1 差异（不同实验，需标注）

Registry 无 RUNNING/PREPARING 实验。无等待中的 Worker 回调。

### 4. 📋 待办
- 用户确认修正方案 → 派 Paper Agent 修正 Issue 1-3（纯文本替换，分钟级）
- 用户决定是否澄清 Issue 4-6 → 如需修改 abstract latency 表述，需 Paper Agent 介入
- 审稿报告回来 → 按 review-report-action skill 处理
- 如需重新编译验证 → `paper_compile_and_check`

### 5. 🎯 战略上下文
- 核心结论稳固：所有 core claim 数值（3%/24%/94%、≤0.21%、±0.3pp、24→84% at 70B）全部与 registry 精确匹配，零数据捏造
- Table 1 和 Table 2 是论文的数据核心，48+56=104 个数值已 100% 验证
- 图表脚本硬编码数据（6 个图）全部与 registry 匹配
- 易错点：论文中有两套 latency 数据源——p8c_ft_scierc_latency（用于 latency table）和 d066_beam_sweep（用于 beam Pareto），baseline 不同（unconstrained vs S1），容易混淆
- 易错点：DocRED 有多个评估粒度（50-doc subset / 200-doc subset / 998-doc full），同一模型同一配置在不同粒度下数值不同，表格 caption 必须准确标注
- 决策链：项目已过 MVP → research → writing → review 全流程，当前处于审稿等待期
