# director / loop_8.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`e8fcf199e0f2fcef6dd8.json`](../../sessions/e8/e8fcf199e0f2fcef6dd8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-15T20:57:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用项目配置的 cuda:0 和 cuda:1（westd-19828），不可占用其他设备
- FNR 数值已经 Reviewer 三轮锁定：L100 FNR=33.3%（S≥3/4），L101/L64/Table Tier 4 FNR=50%（S=4/4）——任何修改必须先过 Reviewer 重新验证
- Paper Agent 和 Main Agent 同时编辑 tex 文件会互相覆盖——同一时间只能一方改论文
- 约束 C001：不引用 TY cross-α 趋势（未经多 seed 验证）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- 论文文件双份：docs/paper/*.tex + artifacts/_project/paper/*.tex（必须同步）
- 数据源：/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json（FNR 计算的真源）
- 活跃进程：alpha_sweep_a050_s43 (cuda:1, PID 134860)、gen_wiki_gpt2m_a100_s42_v3 (cuda:0, PID 117632, ~45%)
- 待排队实验 10 个（plan_006_s43, gen_wiki_gpt2m_a025_s42, alpha_sweep 多组等）

### 3. 📊 当前状态
论文 8/8 章节全部完成，所有数值一致性问题已解决（FNR、α≥0.75 qualifier、方法列表、bib）。Paper Agent 刚收到 Step 5（Iterative Refinement）指令，正在独立跑 Reviewer 迭代循环（max 5 轮）。19 个 orphan bib warning 待 Step 5 清理。

RUNNING：alpha_sweep_a050_s43 + gen_wiki_gpt2m_a100_s42_v3。完成后 cron 自动回调，按 D026 序列推进下一组。

### 4. 📋 待办
- alpha_sweep_a050_s43 cron 回调 → cuda:1 启动 alpha_sweep_a025_s44
- gen_wiki_gpt2m_a100_s42_v3 cron 回调 → cuda:0 启动 gen_wiki_gpt2m_a025_s42
- Paper Agent 汇报 Step 5 收敛 → 决定是否 submit_paper_to_review
- Paper Agent 报告 "Reviewer critical 无法自主解决" → 做方向决策介入
- GPT-2-medium cross-arch 实验完成 → 评估是否支撑 cross-architecture generalization claim，更新 paper_framing.md

### 5. 🎯 战略上下文
核心发现：canary metrics（token entropy, ECE）在 α=1.0 对 diversity 下降有统计显著的先导信号，但方法间灵敏度差异巨大（κ=0.185，naive 16/16 vs TY 4/16）。论文 narrative 是"检测方法选择比现象本身更关键"——不是提新方法，是系统性分析。
易错点：Paper Agent 用过错误数据源（fpr_fnr_calibration.json）算 FNR，真源是 phase2_panel.json 的 per-pair per-seed TY 数据。如果 FNR 数值再起争议，直接查 panel.json 的 pair_verdicts section。
审稿阶段已启动（review_chat_id 已配置），Step 5 收敛后可提交。


---
