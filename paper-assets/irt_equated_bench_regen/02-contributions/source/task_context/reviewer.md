---
loop: 4
reason: idle_timeout
updated: '2026-05-25T14:13:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU、无远程服务器——纯论文写作+本地 CPU 分析项目，不要尝试 SSH 或 submit_training_job
- 匿名仓库 `/tmp/anon_repo/` 的 git identity 必须是 `Anonymous <anonymous@example.com>`，绝不能泄露真实身份
- DDL 2026-05-25 AoE（EMNLP 2026 via ARR）——**今天就是 DDL**，如果你醒来时已过 DDL，不要再建议修改论文
- 正文严格 ≤8 页，Conclusion 卡在第 8 页底部，零余量——任何正文增加都会溢出
- abstract 161 words（≤200 限制）

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`
- 论文：`paper/main.pdf`（19 页，pdfTeX 编译），`paper/sections/*.tex`
- 匿名仓库：`/tmp/anon_repo/`（需用户手动设 Public）
- 无服务器、无 GPU、无 wandb、无活跃进程、无 cron
- Registry：21 实验（14 success / 6 negative / 1 killed bifactor），全部 DONE/PREPARING，**无 RUNNING**

### 3. 📊 当前状态
Loop #4 刚启动，读了 registry 确认无活跃实验。Loop #3 已完成全部终检：
- Desk-reject 风险终检 PASS（PDF metadata 匿名、Type 3=0、代码匿名、19 页）
- Limitations + Claim 强度审查 PASS（6 阴性实验已反映，无过度 claim）
- 模拟 ARR 审稿完成，C1 near-independence 防线已强化（§4.3 "Crucially" 句 + §5.1 ρ→r 修复）
- Figure 3 提升正文后完整性终检 PASS
- **项目处于 Paper Final 阶段，等待用户提交。我本轮未执行任何新审查动作。**

### 4. 📋 待办
- DDL 过后且审稿返回 → 加载 `skills/global/rebuttal.skill.md`，准备 author response
- 如果用户要求最后一轮修改 → **先编译+视觉验证页面仍在 8 页内**（零余量）
- Camera-ready 阶段（如被录用）→ 修复：
  - AUC 0.93-0.94→0.92-0.93（experiments.tex:10 附近）
  - Table 2 caption 负面措辞优化
  - Intro "massively redundant" 措辞
  - plan_004 GSM1K 负相关主文引用补充

### 5. 🎯 战略上下文
- 论文核心论点：temporal DIF 广泛存在（17.9-31.3%）、与 web-overlap 近独立（Jaccard=0.206）、下游排名影响可控但非零（ρ=0.997, ±800 位移）
- **审稿人最大攻击面**：C1 near-independence 可能是 Li et al. proxy noise → 防线是 base/instruct 反转（χ²=562.7），§4.3 已用 "Crucially" 句强化
- **易错点 1**：页面零余量——任何正文改动都可能把 Conclusion 推到第 9 页
- **易错点 2**：§4.2（experiments.tex:16）全文最密集段落（7 个统计论点），审稿人可能跳读
- **易错点 3**：plan_017 "DIF items 更有区分力" 与 "建议审查/移除" 的表面张力——正确理解：高区分力+跨 cohort 功能差异=系统性偏移，强化审计必要性
- DEFF 范围 13.5-29.2% 很宽，weighted-mean 13.5% 被 cluster bootstrap CI [26.7%, 53.2%] 排除——论文立场是 simple-mean 29.2% 为 primary estimate
