# research lit survey fv llm

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lit-survey-fv-llm_20260514T103806_result.json`
- **Structured JSON:** [`44deef9919633937eac8.json`](../../sessions/44/44deef9919633937eac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研完成。产出已保存至 `artifacts/literature_survey_fv_baselines.md`。

**核心发现**：

**两个需要高度关注的新论文**：
1. **SSV (IJCAI 2025, arXiv:2501.16961)** — 同样用 Z3 验证 FOL formalization，通过 concrete instantiation 达到 verified cases 100% precision。与 SVS 的关键区分：SSV 验证 "formalization 是否正确"，SVS 用 verification score 做 "chain selection"。建议在论文中显式区分并考虑集成其 instantiation technique。
2. **"Do LLMs Game Formalization?" (arXiv:2604.19459, April 2026)** — 评估 GPT-5/DeepSeek-R1 在 FOLIO 上的 autoformalization faithfulness，发现两类系统性 unfaithfulness（axiom fabrication + premise mistranslation）。对 SVS 的 formalization confidence 设计有直接启示。

**结论**：无直接竞品覆盖 SVS 的三个核心创新点（graded scoring for selection、cross-chain coherence、formal vs learned verifier Pareto analysis）。最大威胁来自 SSV（Z3 overlap）和 Self-Certainty（near-zero cost alternative）。

**推荐 P0 baselines**：SC、FoVer binary filter+SC、Self-Certainty、ORM for Logical Reasoning。

---
