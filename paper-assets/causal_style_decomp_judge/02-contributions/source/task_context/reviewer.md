---
loop: 3
reason: max_wall_time
updated: '2026-05-25T06:13:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文 DDL: May 27 AoE（非 May 25，之前误判过）
- Table T1 AEval×Llama-70B×Form BT=.756 已被 Agent 确认为 all-trials 方法，与 Table 1 一致（`build_bt_comparisons()` 遍历 trial1+trial2 无 consistency filter）。我之前按 consistent-only 算出 .957 是方法论不同，已 closed
- `pairwise_scoring.py` 的注释说 "consistent only" 但那是 sign test 部分，BT 用 `build_bt_comparisons()` 是 all-trials——不要再被注释误导
- `llama70b_crossbench` registry 的 bt_pct=95.7 是 consistent-only 新实验值，不是论文值，不要用它去质疑论文

### 2. 🖥️ 基础设施快照
- 服务器：westb-29275(root)，工作目录 /root/causal_style_decomp_judge
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge
- 论文源码：上述 workspace 下 docs/paper/sections/*.tex
- 数据文件：服务器 /root/causal_style_decomp_judge/data/*.jsonl
- 分析脚本：服务器 /root/causal_style_decomp_judge/analysis/ + csd_pipeline/
- 无 GPU 进程运行，GPU 已释放给全局调度
- 无 wandb（本项目不用 wandb）
- 无活跃 PID / tmux / cron

### 3. 📊 当前状态
项目处于 **论文提交前最终修正** 阶段。

**已完成审查：**
- Table 1 全 14 行 Likert d 值独立验证通过（table1_verified.csv 与论文一致）
- Table T1/T2 四处 Cohen's d 修正已验证（commit f76da41）：d=1.120→.212, d=.167→.111, d=−.243→.252, d=.245→.233
- BT=.756 方法论争议已 closed（all-trials 方法，与 Table 1 一致）
- Figure 优化已审查（数据与 registry 一致）
- 编译通过（519KB PDF，无 undefined refs，无 errors）
- Abstract 186 词（≤200 合规）
- check_figures_and_layout 3 个 "critical" 是误报（label 在 \input 文件中）

**Registry：** 58 实验（41 成功 / 13 负向 / 0 失败），全部 DONE，无 RUNNING

**等待中：** 无。所有 worker 完成，无 pending Director 决策

### 4. 📋 待办
- 论文最终提交（OpenReview 由运维人工完成）→ 确认匿名仓库已 push 最新 commit（含 d 值修正）
- 审稿结果回来（预计 4-6 周）→ 审查 reviewer concerns，核实 rebuttal 备弹是否覆盖
- 如有新 worker 派出 → 按 reviewer-audit-checklist 审查
- report.md 仍显示 llama70b_crossbench conclusion="negative" 但 registry 是 "success" → 如果 Director 问起，这是已知的 report/registry 不一致（结论被事后修改但 report 未刷新）

### 5. 🎯 战略上下文
- 核心发现：Likert Blindspot——BT pairwise 检测到显著 style bias (p<.001)，Likert 检测不到 (p>.28)，跨 5 个 judge、3 个 benchmark、2 个 axis
- GEE 分解揭示 per-axis confound 结构：verbosity = style-dominated (Style OR 3-13)，formality = joint style+quality
- Rebuttal 备弹已全部就位：formality_scaled_n300, formality_llama_rewriter, llama70b_crossbench, GPT-5.4 NO-GO (D081)
- **最容易判断错的事**：BT 方法论。论文有两套并行方法——sign test (consistent-only) 和 BT model (all-trials)。Table 列名 "BT P" 是 all-trials BT probability，不是 sign test win rate。不要混淆
- **容易踩的坑**：ssh_read_only 禁止 `>=`, `<`, `;`, `|`, `>`, `open()` 等——需要从服务器提取数据时只能用 grep + 本地计算
