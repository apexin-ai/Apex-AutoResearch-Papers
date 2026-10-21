# research literature gap check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-gap-check_20260514T174236_result.json`
- **Structured JSON:** [`9d571deeca11e5ff24ec.json`](../../sessions/9d/9d571deeca11e5ff24ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 new papers are correctly inserted. Here's the summary:

---

## 覆盖检查报告

### (a) Prolog/Logic Programming + RL/LLM

**原有覆盖**: 6 篇 — mellgren-prolog-grpo (Prolog+GRPO), logic-rl, satlm, linc, lorp, logic-lm。直接 Prolog+RL 有 1 篇 (Mellgren)，Prolog+LLM prompting 有 2 篇 (lorp, linc)。

**缺口**: 缺少 neuro-symbolic logic programming 的奠基性工作，以及 Prolog+LLM 训练（非 RL）的近期工作。

**新增 3 篇**:
1. `deepproblog` — Manhaeve et al. 2021, AIJ 298. 神经概率逻辑编程奠基工作，ProbLog + neural predicates。
2. `neurasp` — Yang, Ishay, Lee 2020, IJCAI. 神经网络 + Answer Set Programming，与 DeepProbLog 互补。
3. `thought-like-pro` — Tan et al. 2024, arXiv. 用 Prolog 引擎生成推理轨迹训练 LLM（imitation learning），与 STA 管线直接可比。

### (b) Goodhart's Law / Specification Gaming (2020+)

**原有覆盖**: 很强 — 已有 Manheim & Garrabrant 2019, Gao et al. 2023, Skalse et al. 2022, Karwowski et al. 2024, Kwa et al. 2024, Pan et al. 2022, Rafailov et al. 2024, 以及 reward-hacking-survey 2026。共 12+ 篇。

**缺口**: 缺 specification gaming 在 reasoning models 上的实证工作，特别是 formalization gaming（与 STA 直接相关）。

**新增 2 篇**:
1. `bondarenko-spec-gaming` — Bondarenko et al. 2025, arXiv 2502.13295. 证明推理模型 (o3, R1) 自发进行 specification gaming。
2. `kim-game-formalization` — Kim, Poiroux, Bosselut 2026, ICLR 2026 VerifAI-2 Workshop. 直接研究 LLM 是否 game formalization，在 FOLIO 上评估，发现两种不忠实模式——与 STA 的 high-ISR-but-semantically-wrong 现象高度类似。

### (c) Mutation Testing

**原有覆盖**: 充分 — 7 篇，涵盖 DeMillo 1978（奠基）、Offutt 1992（coupling effect）、Jia & Harman 2011（综述）、Just et al. 2014（实证验证）、LLMorpheus 2025、Meta mutation-guided 2025、mutation-consistency-llm 2024。

**无需补充。**

---

共新增 5 篇论文，总计从 45 篇增至 50 篇。

---
