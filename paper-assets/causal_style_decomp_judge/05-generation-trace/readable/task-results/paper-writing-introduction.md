# paper writing introduction

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260520T232613_result.json`
- **Structured JSON:** [`0069832c3a395b4fe9ae.json`](../../sessions/00/0069832c3a395b4fe9ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `docs/paper/sections/introduction.tex`。

**结构概览：**
- **P1** (5句): LLM judge 作为评估+对齐核心基础设施，bias 传播风险
- **P2** (8句): style bias 主宰地位 (SOS-Bench R=0.999, Preference Leakage 76-92%, Soumik 0.76-0.92) → 4个gap → CASSE/FairJudge仍无因果识别 → Likert整数天花板效应 (64% Δ=0)
- **P3** (6句): CSD三阶段机制 → Likert Blindspot命名 (Likert ATE=+0.102, p=0.332 vs Pairwise 69.1%, p=0.006) → 与LC-AlpacaEval对比
- **P4**: 4条contributions (框架/Blindspot现象/axis-dependent placeholder/实践意义)

**引用使用：** murugadoss2025sos, li2026preference, soumik2026judging, dubois2025lc (×2), casse2026concise, wang2026fairjudge, veitch2020adapting

**Contribution 3** 保留 placeholder 待实验数据填充。

---
