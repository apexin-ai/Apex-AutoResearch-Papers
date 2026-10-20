# reviewer / loop_3.md

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`a1fb9d4c2444ff7a6224.json`](../../sessions/a1/a1fb9d4c2444ff7a6224.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-25T06:10:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU、无远程服务器——纯论文写作+本地 CPU 分析项目
- 匿名仓库 `/tmp/anon_repo/` 的 git identity 必须是 `Anonymous &lt;anonymous@example.com>`，绝不能泄露真实身份
- DDL 2026-05-25 AoE（EMNLP 2026 via ARR）——如果你醒来时已过 DDL，不要再建议修改论文
- 正文严格 ≤8 页，当前 Conclusion 刚好卡在第 8 页底部，任何正文增加都会溢出——`\enlargethispage{10\baselineskip}` 已在 discussion.tex L1，不能再加
- abstract ≤200 words（当前 161 words）

### 2. 🖥️ 基础设施快照
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`
- 论文：`paper/main.pdf`（19 页，pdfTeX 编译），`paper/sections/*.tex`
- 匿名仓库：`/tmp/anon_repo/`（11 commits，需用户手动设 Public）
- 无服务器、无 GPU、无 wandb、无活跃进程
- Registry：21 实验（14 success / 6 negative / 0 failed / 1 pending bifactor）

### 3. 📊 当前状态
**项目处于 Paper Final 阶段，等待用户提交。** 我（Loop #3 Reviewer）在本轮完成了：
- 最终数据审计 worker 审查（PASS，2 个 info 级发现：AUC 0.93-0.94 应为 0.92-0.93、Table 5 rounding non-issue）
- \Cref 指针修复验证（4 个新 \Cref 全部正确，但引发页面溢出→已修复）
- 页面溢出修复后验证（PASS，Conclusion 在第 8 页内）
- Desk-reject 风险终检（PDF metadata 匿名 ✅、Type 3=0 ✅、代码匿名 ✅、19 页 ✅）
- Limitations + Claim 强度审查（6 阴性实验全部已反映，无过度 claim，">21×" 偏保守）
- 模拟 ARR 审稿（C1 near-independence 证据链最薄弱，建议已被采纳：§4.3 "Crucially" 强化句 + §5.1 ρ→r 符号修复）
- Figure 3（ρ degradation curves）提升正文后的完整性终检（PASS）

**无 RUNNING 实验。无等待中的 Worker/Cron。** 唯一待办是用户操作：匿名仓库设 Public + ARR 提交。

### 4. 📋 待办
- DDL 过后且审稿返回 → 加载 `skills/global/rebuttal.skill.md`，准备 author response
- 如果用户要求最后一轮修改 → **先检查页面是否仍在 8 页内**（当前零余量）
- Camera-ready 阶段（如被录用）→ 修复 AUC 0.93-0.94→0.92-0.93（experiments.tex:10）、Table 2 caption 负面措辞、Intro "massively redundant"、plan_004 GSM1K 负相关主文引用

### 5. 🎯 战略上下文
- 论文核心论点：temporal DIF 广泛存在（17.9-31.3%）、与 web-overlap 近独立（Jaccard=0.206）、下游排名影响可控但非零（ρ=0.997, ±800 位移）
- 审稿人最大攻击面：C1 near-independence 可能是 Li et al. proxy noise 的结果——防线是 base/instruct 反转（χ²=562.7），已在 §4.3 用 "Crucially" 句强化
- 易错点 1：页面零余量——任何正文改动都可能把 Conclusion 推到第 9 页，改前必须编译+视觉验证
- 易错点 2：§4.2（experiments.tex:16）是全文最密集段落（7 个统计论点挤在一段），审稿人可能跳读漏掉关键信息，但拆段有页面风险
- 易错点 3：plan_017 的"DIF items 更有区分力"与"audit protocol 建议审查/移除"存在表面张力——正确理解是：高区分力+跨 cohort 功能差异=系统性偏移，强化而非削弱审计必要性
- DEFF 范围 13.5-29.2% 很宽，weighted-mean 13.5% 被 cluster bootstrap CI [26.7%, 53.2%] 排除——论文立场是 simple-mean 29.2% 为 primary estimate


---
