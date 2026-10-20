---
loop: 21
reason: max_messages
updated: '2026-05-25T06:13:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 实验（纯论文写作阶段），所有实验已完成
- 匿名仓库必须同步推送每次修改（用户要求）
- EMNLP 2026 ARR DDL 2026-05-25（今天），主文严格 ≤8 页
- Table 1 有 8 列挤单栏，当前用 resizebox 缩放，等效 ~7pt。用户曾抱怨字太小但溢出问题更优先，如果再被提起需改 `table*` 全宽
- `sanmartin_2009_irt` 是之前发现的 fabricated reference，已删除替换为 `de_ayala_2009_irt`，不要恢复

### 2. 🖥️ 基础设施快照
- 无远程服务器，纯本地论文项目
- 论文源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/`
- 编译：`cd docs/paper && latexmk -pdf main.tex`
- 图表生成脚本：`figures/paper/` 下，统一导入 `paper_style.py`
- 匿名仓库：Agent 每次修改后 push
- 无活跃进程 / tmux / cron

### 3. 📊 当前状态
刚完成一系列排版优化（Table 1 字体、图表分布均匀化、caption 间距缩小、摘要破折号移除、appendix Fig 10/11 改全宽）。

当前 Agent 正在处理引用验证报告：
- 5 个"幽灵引用"需 WebSearch 核实（kocyigit2025impact, choi_2025_kds, sun2025emperor, white2024livebench, tiiuae2024falcon3 — 大概率真实，验证工具搜索能力有限）
- 11 个不一致条目需校对 bib 字段
- Agent 已派出，等待回复

### 4. 📋 待办
- Agent 引用核实回复 → 审查修正结果，确认无 fabricated citation，报告用户
- 用户报告任何新排版问题 → 派 Agent 修复 + 编译验证 ≤8 页
- 用户说"提交" / "投稿" → 提醒 OpenReview 手动操作 + ARR Checklist 在表单里填
- 如果用户再提 Table 1 字太小 → 改 `table*` 全宽是唯一根本方案

### 5. 🎯 战略上下文
项目处于投稿最后冲刺阶段，所有实验已完成，论文内容定稿，只剩排版微调和引用校对。

核心论文 story：contamination 不是 uniform inflation，而是 4 种 dose-response pattern（Benefit/Immune/Collapse/V-recovery），用 ContamCal (RRF + 2PL+γ IRT) 做 domain-level diagnosis。

易错点：
- 之前反复出现"修排版导致超页 → 压内容 → 内容不够又要填 → 再超页"的循环。任何排版修改后必须编译检查页数
- 图表分布已优化到 7/8 页有 float（P5 无 float 是 method→setup 过渡区，无合适 float 可放），不要为了填 P5 乱移浮动体
- Qwen-7B GSM8K 数据已改为 3-seed mean +9.4pp（之前是排除 s0 的 +10.1pp），不要回退
- `paper_style.py` 是 5 个统计图的统一配色源，改颜色只改这一个文件
