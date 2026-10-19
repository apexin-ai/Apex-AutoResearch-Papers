---
loop: 2
reason: idle_timeout
updated: '2026-05-25T05:57:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目是纯理论/模拟项目，无 GPU 实验、无训练任务、无远程服务器
- 论文图表生成脚本在本地 `figures/paper/` 目录，生成后**必须手动复制到 `docs/paper/`**（LaTeX 从 docs/paper/ 加载，不走 graphicspath）
- EMNLP 2026 ARR：main text 严格 8 页，abstract ≤200 words，Limitations 不计入页数
- `gen_fig2.py` 运行约 2 分钟（100k Dirichlet 采样 + 2M collider/mbias/IV 预计算），不要频繁重跑
- references.bib 已修过 7 个幻觉作者名（kim_garg2025, baumann2025, gligoric2025），再改 bib 时必须 WebSearch 验证

### 2. 🖥️ 基础设施快照
- 服务器：本地，无远程服务器
- 工作目录：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`
- 图表源码：`figures/paper/gen_fig*.py`、`figures/paper/gen_diagnostic_plots.py`
- LaTeX 编译目录：`docs/paper/`（main.tex 入口，pdflatex 编译）
- 数据源：`artifacts/plan006/asv_empirical_results.json`（fig5/fig6 的 HumAID K=10 数据）
- 无活跃进程、无 cron、无 Worker

### 3. 📊 当前状态
刚完成 Director 布置的 12 项 pre-submission 视觉/引用修复任务（Task 1-12 全部 DONE）：
- Task 4: 引用验证——修复 4 条 ghost citation + 7 个幻觉作者名
- Task 5-11: Figure 3-7 视觉优化（字号、布局、legend 位置、figure* 双栏、marker 样式等）
- Task 11: Figure 3 第三面板移除 → LaTeX Table 2 (tab:asv_summary)
- Task 12: Figure 2 panel (e) M-bias x 轴刻度重叠修复（最终用 2 刻度 [0.98, 1.02]）

所有修改已编译验证：38 页，4 个 pre-existing overfull hbox warning，无新问题。
无等待中的 Worker/Cron/Director 决策。

### 4. 📋 待办
- Director 下达新指令 → 按指令执行
- 若 Director 要求再次全文视觉审查 → 用 `paper-visual-review` skill 逐页检查
- 若 Director 要求提交前最终检查 → 验证 abstract word count、page count、Limitations 存在性、checklist 完整性
- 若改动任何 `figures/paper/` 下的图 → 必须复制到 `docs/paper/` 再编译

### 5. 🎯 战略上下文
- 项目核心：多类标注误差在 7 种 DAG 拓扑下的因果推断偏差传播，exposure 和 IV 是高危拓扑（sign reversal），M-bias 免疫
- 论文处于 pre-submission 收尾阶段，所有实验和写作已完成，当前只做视觉/格式/引用微调
- 易踩坑：修改 figures/paper/ 后忘记复制到 docs/paper/，导致编译后 PDF 不变（已在本 session 发生过一次）
- 易踩坑：bib 条目作者名不要凭记忆填，之前 3 条 bib 共 7 个 first name 是 AI 幻觉
- 38 页总数中 main text 约 8 页（含 figures/tables），appendix 约 28 页——页数已卡在限制边缘，新增 main text 内容需谨慎
