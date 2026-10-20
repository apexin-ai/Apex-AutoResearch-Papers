---
loop: 22
reason: max_messages
updated: '2026-05-25T16:45:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目已进入审稿阶段（review_chat_id: `oc_40839c097b00df44480b45ab767f59cf`），论文格式/投稿由 Group C 负责，Research Director 不参与
- 正文严格 8 页（EMNLP 2026），Limitations/Ethics/References/Appendix 不计入；当前恰好 8 页，任何正文改动必须重新验证页数
- Abstract ≤200 words（当前 ~160 words，安全）
- `acl.sty` 和 `acl_natbib.bst` 已与 GitHub 官方完全一致，不要修改
- `main.tex` 中不要加 `xcolor`/`hyperref`/`siunitx`（已清理：前两个 acl.sty 已加载，siunitx 未使用）

### 2. 🖥️ 基础设施快照
- 本项目无远程服务器（所有实验已完成）
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/`
- 图表生成脚本：`/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig*.py`
- 生成的图表需同时存在于 `figures/paper/` 和 `docs/paper/figures/paper/`（脚本自动写两处）
- 编译：`paper_compile_and_check(project="recovery_aware_struct_prune", max_pages=8)`（total pages 17 = 8 正文 + 9 appendix/refs，工具报 over_limit 是因为它数 total pages，实际正文 8 页合规）
- 活跃进程：无

### 3. 📊 当前状态
本轮主要处理用户和审计报告的论文修改请求，全部完成：
- **审计修复**（v4-v5）：修复 2 critical（Contribution 3 范围不匹配、"less than 1pp" 被 α=2.0 违反）+ 6 warning（TOST 过强表述、缺 §5.4 引用、em-dash 去 AI、Conclusion probe 步数、均值 scope、recovery capacity 定义歧义）+ Conclusion 溢出修复
- **ACL 模板对齐**（v6）：删除重复/未用包（xcolor、hyperref、siunitx），acl.sty/bst 与官方一致
- **Figure 1 字号放大**（v7）：坐标轴 4.5→7pt，刻度 3.5→6pt，图例 3.5→6pt，标注 3.5→5.5pt
- **Limitations 精简**（v8）：从 5 点缩为 3 个短句

Registry: 无 RUNNING/PREPARING 实验。无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- 收到审稿报告 `[审稿报告]` → 按报告末尾强制处理协议逐条处理，先读 `review_issues.yaml` 了解历史
- 用户要求新的论文修改 → 改完后必须 `paper_compile_and_check` 验证 8 页 + 上传 PDF
- 用户说"进入审稿阶段"/"重新审稿" → 必须调 `submit_paper_to_review`，不能只文字回复

### 5. 🎯 战略上下文
- 项目核心发现：**reward-accuracy decoupling**——在 20-25% MLP sparsity 下，SFT 和 GRPO 恢复到几乎相同精度（|Δ|<1.2pp），尽管 reward 差距达 4.4×
- 论文 framing 已稳定：从 "提出新方法 RASP" 转为 "controlled study + analysis contribution"，核心 claim 三条（decoupling、recovery capacity spectrum、SFT dominance）
- 最新 PDF 版本是 v8（RASP_paper_v8_shorter_limitations.pdf）
- 易错点：改正文内容时 LaTeX float 会移位——在 `figure*[t]` 之前加内容会把图推到下一页，只能在 figure 声明之后的文本中加内容
- 审计报告中 warning 级别未处理的：α dose-response 全部单 seed（Limitations 已提及）、Random 在 spectrum 中的 confound（正文已解释）、Figure 2/6 内部文字偏小（用户未要求改）
