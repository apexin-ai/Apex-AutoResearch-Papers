# director / loop_7.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`4dd48bb9e9b79c9e9f29.json`](../../sessions/4d/4dd48bb9e9b79c9e9f29.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-17T10:58:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU: cuda:0 + cuda:1（2 × RTX PRO 6000 96GB），不得使用其他卡
- 服务器: westd-39279，代码路径 /root/solver-trace-ablation
- 5-seed β=0.1 数据已写入论文，不得回退到 3-seed 数据。5-seed pooled: ISR H7=190/350=54.3%, genuine=79/350=22.6%; Random H7=122/414=29.5%, genuine=32/414=7.7%
- H7 OR=2.84 (not 15.05), genuine OR=3.48 (not 0.612)。这是 D122+D124 定论，3-seed 数据仅保留在 Appendix Fisher table 作 sensitivity
- β=0.05 ISR 3/3 seeds 已确认 deterministic collapse，limitations.tex 已从 "single seed" 更新为 "3 seeds"

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/solver-trace-ablation
- 论文目录（本地）：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/
- 磁盘：85G/250G used (34%)，M003 清理后健康
- 活跃实验：sweep-isr-b005-s44 (cuda:0, step ~257/500, 已 fully collapsed) + sweep-random-b005-s43 (cuda:1, step ~450/500, PR~87%, 即将完成)
- W&B / conda: 未配置（直接 Python 执行）

### 3. 📊 当前状态
刚完成：paper_framing.md 全面更新到 D120-D125（5-seed data, genuine OR reversal, no-safe-dose, non-monotonic dose-response）。ROADMAP 已刷新。limitations.tex β=0.05 seed count 已更新。

RUNNING 实验：
- sweep-isr-b005-s44：ISR β=0.05 s44，第 3 个 seed，已 fully collapsed (reward_std=0, isr_mean=0.5)，等训练完成 + eval
- sweep-random-b005-s43：Random β=0.05 s43，step ~450/500，PR~87%。**这是 D123 最终判定的关键实验**——如果 eval PR>>0%，D123 "Random β=0.05 control unavailable" 被推翻，β=0.05 获得有效 matched control

等待中：
- Agent 刚 RESET（上一个 Agent 崩溃）
- Reviewer 已完成 3 份评估（non-monotonic dose-response + Round 4 readiness + ROADMAP audit），结论统一：等 Random β=0.05 s43 eval 后再提交 Round 4
- 审稿 Round 4 提交被 block 在 Random β=0.05 s43 eval 上（~10-20 min）

### 4. 📋 待办
- Random β=0.05 s43 完成回调 → 立即 eval + classify_h7.py → 判定 D123：
  - eval PR>>0% → D123 推翻，experiments.tex L118-121 更新为 "ISR 3/3 H7 vs Random viable"，β=0.05 成为更强 Goodhart 证据
  - eval PR≈0% → D123 confirmed，当前 "additional seeds under investigation" 措辞改为 "2/2 seeds fail"
- experiments.tex L118-121 更新后 → 提交 Round 4 审稿（submit_paper_to_review）
- ISR β=0.05 s44 eval 完成后 → 补充数据到 β=0.05 section（不阻塞 Round 4）
- Reviewer 建议添加非单调 dose-response 短段落（3-4 句，Discussion "Timing, not destiny" 段后，观察级别不升级为 claim）
- GPU 空出后 → Figure 3/5 regeneration with 5-seed data（低优先级）
- Provenance: C064, C101, C136, C192 仍引用 3-seed 数据，需更新为 5-seed

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR May 25（剩 8 天）
- **决策链**: D120 (collapse inevitable at all doses, β controls timing) → D122 (OR=15→2.84, seed-dominated) → D124 (genuine OR=3.48 reversal, double-edged sword) → D125 (β=0.05 no safe dose, 3/3 confirmed)
- **论文核心叙事**: ISR 是可靠诊断工具但不可靠优化目标。ISR 对 tautology 有 inherent structural bias (P→P 获 ISR≥0.5)，创造 positive feedback loop。β=0.1 是 double-edged sword：同时增加 genuine (OR=3.48) 和 H7 (OR=2.84)，genuine benefit transient (1000步 17%→2%)
- **易错点**：
  1. Random β=0.05 s43 如果 eval PR 高，D123 措辞需要实质改写，不是小 patch——从 "control unavailable" 变为 "ISR collapses while Random learns"，叙事更强
  2. experiments.tex L118-121 是 β=0.05 的唯一正文位置，改动需精确
  3. 5-seed 和 3-seed 数据容易混用——Table 1 是 5-seed，Appendix Fisher table 有 5-seed primary + 3-seed sensitivity 双层结构，不要搞混
  4. Random β=0.1 s45/s46 queue entries 是 stale 的（5-seed 数据已完整），不要再跑


---
