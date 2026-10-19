# research deep read turn ppo v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_deep-read-turn-ppo-v2_20260517T121530_result.json`
- **Structured JSON:** [`f93147fea799e8a53104.json`](../../sessions/f9/f93147fea799e8a53104.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研完成，已写入 `memory.md`。覆盖 18 篇论文（2024–2026），结构如下：

**Direct Competitors（5 篇）**:
- **Turn-PPO** (EACL 2026) — turn-level MDP，发现 GRPO 在 multi-turn 中 uniform advantage + 频繁 crash，最相关竞品
- **MT-GRPO/MT-PPO** (ICML 2025) — 第一个系统性 turn-level reward design 研究，verifiable + LLM-judge 两种 reward
- **GiGPO** (NeurIPS 2025) — anchor state grouping 实现 step-level group comparison，critic-free
- **GAGPO** (2026) — grouped value proxy + 递归 GAE，比 GiGPO variance 更低
- **HCAPO** (2026) — hindsight credit assignment，LLM 做 post-hoc critic

**Method Components（5 篇）**: iStar (implicit PRM + dual advantage), SPA-RL (progress estimator), VAGEN (bi-level GAE), ArCHer (ICML 2024, 开山之作), HiPER (hierarchical advantage)

**Frameworks/Baselines（4 篇）**: RAGEN/StarPO, WebRL, WebAgent-R1, Planner-R1

**Surveys（3 篇）**: Credit Assignment Survey (47 methods), Practitioner's Guide, DeepSeek-R1 GRPO

**关键结论**: 没有论文使用 "advantage sign misattribution" 术语，也没有量化 γ 折扣对 sign 的影响（~29% 保留率）。Turn-PPO 描述了相近现象（uniform advantage assignment），但我们的 sign-level 分析和 step-independent vs episode-level 的受控对比（0% vs 28%）是差异化贡献空间。

---
