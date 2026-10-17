---
loop: 15
reason: max_wall_time
updated: '2026-05-25T13:07:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文主体 ≤8 页（EMNLP 2026 ARR），Limitations 豁免但不能塞额外内容
- Abstract ≤200 words（当前 185 words）
- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有
- ARR Checklist 在 OpenReview form 填写，不放 PDF 里
- "73.4% multi-match rate"（非 "none-rate"）——已全文统一，不要回退
- cqa1 cuda:0 保留给 rebuttal 阶段（D072 决策），提交前不跑新实验
- 本项目不用 W&B，不检查 W&B

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (root) — 在线，RTX PRO 6000 Blackwell 98GB，cuda:0 空闲 0%
- 服务器：westd-24295 (root) — **不可达**（AutoDL 可能已关机/端口变更，需用户去控制台确认）
- 代码根目录（远程）：/root/schema-dag-extraction
- 论文源文件（本地）：/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/
- 模型：Qwen3-32B-FP8（cqa1 上 vLLM serving，当前未启动）
- 数据：FewRel /root/schema-dag-extraction/data/fewrel_parquet/
- 活跃进程：无。0 RUNNING 实验，无 tmux/cron

### 3. 📊 当前状态
**DDL 2026-05-25（今天）。论文 submission-ready。**

本轮（Loop #15）完成：
- 提交前最终巡检：Table 17 "format-independent" 已修复确认
- Camera-ready claim-vs-data 通读：R²=0.273、VIF=1.18、TOST p=0.003/0.209、oracle 0.724/0.504、-25.5pp、73.4% 全文一致 PASS
- LLaMA→Llama 全局替换检查：无残留，bib key 完好
- DocRE→DocRED 修正检查：无残留
- 5 个新增 appendix pointer 验证：全部解析正确
- Anonymous GitHub repo rebuild 审查：无敏感信息泄露 PASS
- SDGD pipeline 图 v6 视觉审查：数据与论文一致 PASS
- 服务器状态：cqa1 正常 cuda:0 空闲，westd 不可达

Registry: 70 个实验，全部 DONE/PREPARING（实质已完结），0 RUNNING。

### 4. 📋 待办
- DDL 到达（5/25）且用户提交完成 → 切换到 rebuttal 准备模式，加载 rebuttal skill
- 收到审稿意见 → 重点准备 Q7 additivity（论文最薄弱点，kill 3.5/5）；其次 Q13 no solution（kill 3/5）、Q2 effect size（kill 3/5）
- Director 要求补实验 → 参考 Loop #14 结论：没有值得跑的低成本实验，所有核心 claim 已有充分证据
- westd 需要时 → 提醒用户去 AutoDL 控制台查新端口

### 5. 🎯 战略上下文
**论文核心结论**：Schema complexity 沿两个维度降解 LLM IE——count (Dim1, 跨任务) 和 confusability (Dim2, RE batch-level, semipartial R²=0.273)。SDGD decomposition 失败（merge amplification + routing failure），但 oracle routing 证明 separability。

**最容易判断错的事**：
- 0.218 是 Spearman ρ（SCS-confusion, 3160 pairs），**不是** semipartial R²。之前有 handoff 误报过这个
- DocRED R²=0.578 是 total R²（VIF=50.9 inflate），semipartial R²_BCS 只有 0.056——论文正确地用 FewRel 0.273 作为 primary evidence
- NER BCS null 是 boundary condition 而非 negative result——有机制解释（error mode dispersion + BCS range compression）
- TOST additivity 只在 FewRel linear scale 通过（p=0.003），logit scale inconclusive（p=0.209）
- Anonymous repo citation 写 year=2025（匿名提交无影响）

**审稿人最可能追问的 Top-3**：
1. Q7 Additivity 只在 FewRel 成立（kill 3.5/5）——range matching post-hoc + MDE=5.5pp underpowered
2. Q13 No solution（kill 3/5）——建议用 "representational challenge" framing 翻转
3. Q2 Effect size 小（kill 3/5）——ecological aggregation + IntraSub 单调性是防线
