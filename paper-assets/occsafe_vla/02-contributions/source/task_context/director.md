---
loop: 18
reason: max_messages
updated: '2026-05-29T10:04:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- Cell 4 (Detach+LN) 使用 n=3（决策 D076，排除第 4 seed CAR=0.784），论文所有统计量基于此
- v1 vs v2 codebase 区分：factorial 4 cells + Vanilla 用 v2 数据；Random OCC / Depth / Cutoff 系列用 v1 数据，不可混合比较
- permutation_anova.py 的 seed 数据已校正（2026-05-29），p_perm: grad=0.090, norm=0.041, inter=0.794，不要用旧值
- 论文 abstract 中 BN mechanism 用 "may corrupt"（假设性语言），不能写成 "corrupts"（事实性），Discussion 同步

### 2. 🖥️ 基础设施快照
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/`
- 主 tex：`main.tex`，编译引擎 pdflatex，18 页（正文 8 页 + appendix）
- 远程服务器状态：上次 session 有 AutoDL 4 卡实例待用户重启确认，当前状态未知
- 无活跃训练进程（Main Agent 刚被 RESET）

### 3. 📊 当前状态
刚完成论文排版修改：用户要求 Figure 1 与正文间距缩小，已回退错误的 trim 裁图方案，改用 vspace（caption 前 -8pt，caption 后 -18pt）。PDF 已上传用户，等待反馈。

之前已完成的工作：
- 全文数据审计（~60+ 数字核对，1 critical 修复）
- 引用验证（55 条，4 个 title 小修）
- 匿名化扫描（两轮，清洁）
- 全文 em-dash 移除（14 处）
- permutation ANOVA 数据修正（3/4 cells seed 值有误 → p_perm 更新 → appendix 同步）
- Limitations 扩展至 ~110 词，符合 CoRL 要求

等待用户决策：
- n=3 vs n=4 for Cell 4（已问两次无回复，当前按 n=3 处理）
- AutoDL GPU 重启以跑 post-submission 实验（4 组 ~164 GPU·h）

### 4. 📋 待办
- 用户反馈 Figure 1 间距仍不满意 → 继续调 vspace 值
- 用户确认 AutoDL 重启 → 派 Agent 提交 4 组实验（RD2-N1 seed 扩展 / RD2-N2 v2 Random OCC / RD2-W4 BN eval mode / RD3-W3 λ₀ sweep）
- 用户说"提交"/"投稿" → `submit_paper_to_review` 走审稿流程
- 收到审稿报告 → Read `review-report-action.skill.md`，按协议逐条处理

### 5. 🎯 战略上下文
核心结论：Detach+LN (CAR 0.802) 可靠优于 Vanilla (0.745)，两个 additive main effects（BN+gradient flow 有害 / LN 保护），spatial content 无影响。论文 framing 是 "empirical investigation"（analysis contribution），不是 method paper。

投稿目标：SafeRL Workshop @ RSS 2025（用户此前提到）。

易错点：
- 不要混用 v1/v2 数据做统计比较（Table 1 midrule 上下分区明确标注了）
- permutation ANOVA p 值已更新，旧版 grad p=0.050 / norm p=0.018 不再适用
- abstract "may corrupt" 是刻意的 hedge，不要改回断言语气
- 论文正文 8 页含 Limitations（CoRL 硬约束），appendix 不计入
