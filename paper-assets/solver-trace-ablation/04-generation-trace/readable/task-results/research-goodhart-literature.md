# research goodhart literature

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_goodhart-literature_20260514T083046_result.json`
- **Structured JSON:** [`7163a4efb2e945f1e287.json`](../../sessions/71/7163a4efb2e945f1e287.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研已完成，写入 `artifacts/literature_goodhart.md`。

三个类别共覆盖 30+ 篇论文：
- **Category 1 (Reward Overoptimization)**: 10 篇核心论文，包括 Gao et al. 2023 (ICML)、Skalse et al. 2022 (NeurIPS)、Moskovitz et al. 2024 (ICLR Spotlight)、Kwa et al. 2024 (NeurIPS) 等
- **Category 2 (Verification as Reward)**: 12 篇，覆盖 RLSF (solver reward)、FoVer (Z3/Isabelle)、DeepSeek-Prover (GRPO+Lean)、AlphaProof、Lightman et al. (PRM) 等
- **Category 3 (Dose-Response)**: 12 篇，包括 Rafailov et al. 2024 (NeurIPS, beta scaling in DAAs)、BiPaRS (NeurIPS 2020, adaptive shaping weights)、ARS (ICML 2025) 等

Positioning Summary 部分整理了 4 个新颖点、5 个可引用支撑、5 个预期 reviewer 问题。最关键的 framing：我们是 **第一个在 neurosymbolic verification reward 上刻画 Goodhart 效应的工作**，graded metric (ISR) 比 binary verification (DeepSeek-Prover/AlphaProof 的 pass/fail) 更易被 hack 这一观察在已有文献中尚无人明确指出。

---
