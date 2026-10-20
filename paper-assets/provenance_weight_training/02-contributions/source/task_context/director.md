---
loop: 20
reason: max_messages
updated: '2026-05-25T13:58:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU：westd-41312 上 4 卡，实验已全部完成，当前无 RUNNING 实验
- 匿名仓库 GitHub 链接（github.com/anonymous-nlp-2026/...）只用于 git push，**论文中必须用 anonymous.4open.science 链接**
- EMNLP 2026 正文硬限 8 页（不含 Limitations/References/Appendix）
- Abstract ≤ 200 words（当前 ~167-174 words，安全）
- 今天是 DDL 日（2026-05-25），论文处于最终打磨阶段

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312，4× GPU（全部空闲）
- 论文源码：本地 workspace `projects/provenance_weight_training/artifacts/paper/`
- 匿名仓库：`https://anonymous.4open.science/r/provenance_weight_training-F72D/`（论文脚注用这个）
- GitHub 仓库：`https://github.com/anonymous-nlp-2026/provenance_weight_training`（push 用这个，PAT: [REDACTED_GITHUB_TOKEN]，账号 caoxiaoyu002）
- 活跃进程：无 RUNNING 实验，无 cron，无 Worker
- Registry：269 实验，254 DONE（175 success / 14 negative / 42 failed / 23 killed），15 PREPARING (stale)

### 3. 📊 当前状态
论文最终打磨中，Paper Agent 正在处理两个队列任务：
1. ✅ 引用修复（bib 条目核实 + 6 处修正）— 已完成
2. 🔄 审计 Round 2 修复（Discussion 标签冲突 / 重复数字 / ρ=0.6 hedge / em-dash）— 在 Paper Agent 队列中

已完成的主要工作：
- D&R 叙事重构（q07 三 seed 全部完成，D&R 从"次优"改为"最强方法"）
- Figure 1/2/3/5/8 视觉修复（重叠/间距/放大，多轮迭代）
- 引用补充 65→75 条 + bib 格式修正
- 匿名仓库推送（squash + 匿名化 author）
- Abstract 脚注格式规范化
- 页数压缩回 8 页
- 附录引用完整性检查

### 4. 📋 待办（条件触发式）
- Paper Agent 回复审计 Round 2 修复 → 确认 Discussion 标签冲突已解决 + em-dash 已清除 + 编译通过
- 用户/正翔/晓玉有新的排版反馈 → 继续派 Paper Agent 修复
- 用户说"提交" → 确认最终 PDF 状态，协助提交流程
- 如果需要重新提交审稿 → `submit_paper_to_review`

### 5. 🎯 战略上下文
- 核心结论：D&R（Detect-and-Remove）在所有阈值下大幅优于 Uniform 和 Adaptive b*，>95% 的优势来自 multi-epoch exposure 机制
- 论文标题 "When Does Detect-and-Reweight Work?" — 审计指出 Finding #1 关于 D&R（硬过滤）与 title 承诺（reweighting）有张力，但正文已将 D&R 定位为"对比策略"，目前处理可接受
- Table 2 显示 3 seed 但 Mean 是 5-seed——审计多次提及，目前 caption 有说明但未改表格结构，低优先级
- 易错：Figure/Table 位置调整时 LaTeX 浮动机制可能导致源码顺序≠实际位置，必须 pdf_to_images 视觉验证
- 易错：曹晓玉要求 Table 3/Figure 6 "图在上表在下"（即保持原始顺序），之前交换又改回来了
