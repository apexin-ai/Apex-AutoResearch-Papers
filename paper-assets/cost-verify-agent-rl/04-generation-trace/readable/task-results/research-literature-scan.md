# research literature scan

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260515T232916_result.json`
- **Structured JSON:** [`60a157f5e89c8e7ede4c.json`](../../sessions/60/60a157f5e89c8e7ede4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新。新增 10 篇论文，总计 37 篇。

---

## 扫描报告

### 新增论文（10 篇）

| 论文 | 类别 | 关系 | 备注 |
|------|------|------|------|
| **Agent-Omit** (ICML'26, 2602.04284) | direct-competitor | competitor | RL 训练 agent 自适应省略冗余 thought/observation。与 B-IAVR 方向相反但互补：Agent-Omit 减（省略），B-IAVR 加（验证） |
| **AVA: Anytime Verified Agents** (TMLR'26) | direct-competitor | competitor | 预算约束下的自适应 search/sampling/verification 分配。仅在 reasoning 任务评估，非 interactive agent |
| **T2PO** (ICML'26 Spotlight, 2605.02178) | method-component | background | 不确定性引导的 token/turn 级探索控制，ALFWorld+WebShop 评估。解决训练稳定性而非验证策略 |
| **SkillMaster** (2605.08693) | method-component | background | DualAdv-GRPO，ALFWorld +8.8%。双优势估计结构可借鉴 |
| **GVPO** (ICLR'26) | method-component | background | 过程验证信号 + 结果信号的优势整形。AppWorld 上 +12.7% over o1 |
| **AgentV-RL** (2604.16004) | method-component | background | 双向 agentic verifier 用于 reward modeling，4B 超 SOTA ORM 25.2% |
| **VerifiAgent** (EMNLP'25 Findings, 2504.00406) | background | background | 统一验证 agent（meta-verification + tool-based）。关注 how to verify，B-IAVR 关注 when |
| **CAST** (2605.15041) | background | background | 基于历史 case 校准工具使用的推理深度 |
| **Marginal Token Allocators** (2605.01214) | background | background | Position paper，将 agent 成本效率问题框架化为边际 token 分配经济学 |
| **Argos** (2512.03438, revised Apr'26) | background | background | 多模态 RL 自适应 verifier。不同领域（vision/robotics） |

### 直接竞争者评估

**无新的高度重叠竞争者。** 新增的两个 competitor：

1. **Agent-Omit** — 虽然同为"RL 训练 cost-efficient agent behavior"，但方法论方向相反（减 vs 加），不构成方法重叠。实际上是互补的，可在 related work 中 position 为"B-IAVR 与 Agent-Omit 从对立方向解决 agent 效率问题，两者可组合"。

2. **AVA** — 解决类似的 selective verification 问题，但限于 single-turn reasoning（GSM8K/MATH），用 analytical/heuristic 方法而非 RL。不在 agent 领域。

### 对 novelty 定位的影响

B-IAVR 的核心差异化仍然成立：**唯一通过 RL 学习 interactive agent 中 step-level 验证策略的工作**。现有竞争者要么限于 reasoning domain（Thinkless/AutoThink/AVA），要么用非 RL 方法（Sherlock/Derailer-Rerailer），要么解决不同问题（Agent-Omit 做 omission 不做 verification）。ARES 仍是最近的竞争者，但其 router 需要 difficulty-annotated 数据，B-IAVR 从环境交互自主学习。

建议关注 **T2PO**（ICML Spotlight）和 **SkillMaster** 的 DualAdv-GRPO——前者的 uncertainty-based trigger 可作为 B-IAVR 的 baseline/ablation，后者的双优势估计结构可能优化 B-IAVR 的 action vs verification 优势分离。

---
