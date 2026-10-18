# director / loop_1.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`c6c3efc2da13e49ceedc.json`](../../sessions/c6/c6c3efc2da13e49ceedc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-21T08:20:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-48145:cuda:0（唯一分配的 GPU）
- 这是 observational analysis 项目，使用 wang2025hybrid 的 model zoo，不能自己训练新模型
- 论文主文严格 ≤ 8 页（EMNLP 2026 Long Paper），当前 ~8.2 页超限，必须压缩
- ARR May cycle deadline: 2026-05-25（剩 4 天）
- 审稿卡片 apr_20260520T230329_3fw6 等用户批准，旧卡片 apr_20260520T173903_x6en 已过时忽略

### 2. 🖥️ 基础设施快照
- 服务器：westb-48145 (connect.westb.seetacloud.com)，用户 root
- 远程工作目录：/root/entrainment_gated_ft
- 本地论文目录：projects/entrainment_gated_ft/docs/paper/
- 本地 main.tex：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex
- GPU：cuda:0 已分配，当前空闲（0% 利用率 >6 小时）
- 无活跃进程/tmux/cron

### 3. 📊 当前状态
**刚完成**：Round 5 审稿报告处理——逐条 Action Matrix 已构建并发给 Reviewer (`post_to_reviewer`)，等 Reviewer 独立反馈。用户已通知审稿结果和初步方案。

**Registry**：19 个实验，16 DONE (11 success, 4 negative, 1 killed)，3 PREPARING。无 RUNNING。

**等待中**：
- Reviewer 对 Action Matrix 的独立审核反馈（刚发出）
- 用户批准审稿卡片 apr_20260520T230329_3fw6
- 注意：当前提交的 PDF 尚未包含 Round 5 审稿报告的修改（PDF 是 Round 4 改进后的版本）

### 4. 📋 待办
- Reviewer 回复 Action Matrix 审核 → 综合定稿 → 派 Agent 执行（论文修改 + 可能的 GPU 实验）→ update_review_issues
- 用户批准审稿卡片 → 等 Review Director 处理（但论文仍需按 Round 5 反馈继续改进）
- W5 页数超限 → **立即修复**（与 W2 收敛压缩联动：Table 1 讨论 + §4.2 scale 移 appendix，Related Work 精简）
- W3 format confound GPU 实验（Reviewer 确认值得做后）→ Agent 检查服务器上是否有 WinoGrande/PIQA 的 per-example predictions → 有则直接计算 α/Jaccard，无则重跑 eval
- W6 引用 → Agent 验证 Zoology/Based/Samba 真实性 → Paper Agent 整合

### 5. 🎯 战略上下文
**核心结论**：Aggregate convergence（只在 LAMBADA，p=.100 不显著）与 per-example multiplicity（α=0.10-0.30，Jaccard≤0.10）解耦。这是 observational study，贡献是量化现象而非提出方法。

**Round 5 审稿 3.0 (Findings) 的关键瓶颈**：
1. **Seed confound (W1 Critical)**：不可解决，只能 reframe + proxy argument（within-arch Jaccard 3× > cross-arch）
2. **Convergence over-prominence (W2 Critical)**：5 轮都在改，仍不够——需要结构性手术（移 appendix），不是改措辞
3. **Format confound (W3 Major)**：WinoGrande+PIQA per-example 分析可能解耦格式 vs task type，这是 GPU 唯一有价值的用途
4. **Novelty (W4 Major)**：天花板存在，CV 机制是唯一可定位为 methodological insight 的东西

**最容易判断错的事**：
- 不要再尝试用措辞修改解决 convergence prominence——需要把 Table 1 讨论和 §4.2 物理移到 appendix
- 不要把 "observational study 的 Significance 天花板" 当作 "不需要做任何事"——W3 的 GPU 实验和 W6 的 Zoology 整合能实质性提分
- Reviewer 说 "不建议新实验" 是上轮的结论，Round 5 审稿报告的 W3 format confound 是新角度，WinoGrande/PIQA per-example 分析值得做
- 论文当前 ~8.2 页超限是 desk rejection 风险，优先级最高


---
