---
loop: 2
reason: max_messages
updated: '2026-05-25T03:22:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验——纯统计模拟 + 论文写作项目，所有实验在本地 CPU 完成
- 论文 EMNLP 2026 ARR 投稿，主文严格 8 页限制（Limitations/References 不计入）。每次修改后必须编译验证页数
- 统一配色方案已锁定：Naive=#95A5A6, Global=#2C5F8A, EC-HTE=#16A085, Strat.MLE=#D4880F, Danger=#C0392B。任何新图必须遵循
- Heatmap colormap: ['#4A7FA8', '#B8D4E8', '#FFFFFF', '#E8B4A8', '#D4574A']——用户明确要求偏浅色调

### 2. 🖥️ 基础设施快照
- 服务器：本地 workspace，无远程服务器
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/`
- 论文目录：`docs/paper/`，主文件 `main.tex`，编译命令 `latexmk -pdf -interaction=nonstopmode main.tex`
- 图表生成脚本：`docs/paper/figures/gen_fig*.py`
- 实验数据：`artifacts/exp-006/data/` (budget sensitivity CSV), `artifacts/sign_reversal_corrected.csv` (heatmap)
- 无活跃进程 / 无 tmux / 无 cron

### 3. 📊 当前状态
刚完成 Round 21 审稿报告的全部 DDL 前写作修复（P0+P1+P2），已编译验证 8 页通过：
- **theory.tex**: 压缩三要素段 + 添加 K=2 数值示例 + F-L subsumes → sign reversal novelty statement
- **experiments.tex**: §5.4 matrix vs scalar 区分 + §5.2 CivilComments NLP insight
- **introduction.tex**: "decision framework" → "empirical operating guidelines" + K≤4 限定 + 精简
- **limitations.tex**: A3 class imbalance 影响讨论
- **related_work.tex + references.bib**: Veitch 2020, Wood-Doughty 2018 引用
- **review_issues.yaml** 已同步更新所有 fix 状态

Registry: 无 RUNNING/PREPARING 实验。无等待中的回调。
项目处于**审稿阶段**（review_chat_id 已绑定 Group C）。

### 4. 📋 待办
- 收到用户"提交审稿"指令 → `submit_paper_to_review` 用最新 PDF 提交 Group C
- 收到新一轮审稿报告 → 按 9 步协议处理（read issues → action matrix → post_to_reviewer → 执行）
- 用户确认投稿 → 最终检查 + 准备 submission materials
- Rebuttal 准备材料（均为 post-submission）：非对称 closed-form、X-learner/BART 实验、MC=500 runs、Appendix M 移入正文

### 5. 🎯 战略上下文
- **核心贡献**：Theorem 1 bias identity（δ_s·Δτ/(1-2π̄)）→ 全局校正在子群层面可反转 bias 符号 → EC-HTE 分层校正消除
- **当前评分 3.5 (Borderline Conference)**，主要弱点：(1) 非对称误分类下诊断 AUC 退化到 0.65 (2) NLP 社区价值定位 (3) K≤4 scalability 限制
- **易错判断**：R20-C1（A2 对称假设 vs "exact" 标题）是跨轮反复出现的结构性问题，不是写作能修的——需要 rebuttal 给出非对称 closed-form。不要试图在主文用更多文字绕过，Reviewer 会继续追
- **贡献定位**：theory 60% + empirical 20% + method 20%。EC-HTE 方法本身技术新颖性有限（成熟技术组合），核心卖点是 bias identity 的理论洞察和实证验证
- 决策链见 `decisions.yaml`；paper framing 见 `paper_framing.md`
