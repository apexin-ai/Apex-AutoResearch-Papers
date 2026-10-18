# director / loop_1.md

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`f073b187a8a240a13572.json`](../../sessions/f0/f073b187a8a240a13572.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-22T18:18:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- **Dominance analysis (log-log OLS) 是唯一 canonical regression model**。禁止混用 Step 4 pipeline / residualized analysis 的数字。所有论文数字必须来自 canonical table。
- 论文数字：η_max **11/12**, K_eff **7/12+, 1/12−, 4/12 NS**。之前版本用过 9/12、10/12、12/12、8/12 等——全部过时。
- Claim 5 (Gaussian Copula Failure) 已被 15-model 数据证伪并从 contribution stack 移除 (D015)。禁止在论文中声称 copula 系统性低估 MI。
- GPU 只能用 seetacloud-rtx6000 的 4× RTX 6000（项目分配内）。当前全空闲（分析/写作阶段）。

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-rtx6000，工作目录 /root/cert_manip_resist_eval/
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/
- Scoring 结果：scoring/results/plan001/individual_scores/ (126 JSON, 15 models × 2 datasets × ~6 attacks)
- Paper .tex：在本地 workspace artifacts/ 下（Paper Agent 管理）
- P2 aggregation Worker 正在 seetacloud 上跑（455-panel × 4 聚合规则 residualized regression）
- Dream simulation dream_20260522T173833 运行中（full review mode, v4 framing）

### 3. 📊 当前状态
刚完成：canonical regression table 统一。η_max 从 9/12 确认为 11/12。paper_framing.md 更新到 v4b。Paper Agent 已收到所有修正 Patch（v4b 数字统一 + copula 移除 + η_max 11/12），Introduction + Threat Model 已更新完毕。

等待中：
- P2 aggregation 15-model Worker（Claim 7: Bayesian/threshold 聚合效应验证）
- Dream report（dream_20260522T173833）
- Paper Agent 下一步：Methodology 和 Results 章节

### 4. 📋 待办
- P2 Worker 完成 → 处理 Claim 7 数字，决定是否保留/更新 aggregation claim，通知 Paper Agent
- Dream report 到达 → Read dream-report-action.skill.md，按三档对比执行行动列表
- Paper Agent 报告 Methodology 就绪 → 审查 dominance analysis 方法描述是否准确
- Paper Agent 报告 Results 就绪 → 核对所有数字与 canonical table 一致
- Claim 6 (robustness-first) 仍仅 6-model → 写论文时标注 preliminary caveat

### 5. 🎯 战略上下文
核心发现：diversity predominantly harmful (7/12) + sycophancy protective exception (1/12)。arc×sycophancy 是 narrative 关键转折——"the exception that proves the rule"，揭示 BFT 机制边界（shared-bias vs exploit-specific）。

决策链：D014（K_eff 12/12 positive 推翻原假设）→ D015（copula claim 证伪）→ v4b（dominance analysis 统一，η_max 11/12）。

易错点：
- 三套回归分析（Step 4 / residualized / dominance）给出不同数字，绝对不能混用。只用 dominance analysis。
- arc×sycophancy 在 raw regression 中 K_eff 正，在 dominance analysis 中 K_eff 负（-0.192）。以 dominance 为准。
- Contribution stack 现在 7 项（copula 已移除），不是 8 项。


---
