# paper research sf5 sf7 refs

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_sf5_sf7_refs_20260515T154411_result.json`
- **Structured JSON:** [`61c2d19dec681a64da9b.json`](../../sessions/61/61c2d19dec681a64da9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**references.bib** — 添加 6 个 BibTeX 条目：
- `crpo-2021` — Xu et al., ICML 2021（safe RL constrained optimization）
- `routellm-2024` — Ong et al., arXiv 2024（LLM routing with preference data）
- `reflexion-2023` — Shinn et al., NeurIPS 2023（verbal reinforcement learning）
- `tool-learning-survey-2024` — Qu et al., arXiv 2024（tool learning survey）
- `tot-2023` — Yao et al., NeurIPS 2023（Tree of Thoughts）

**related_work.tex** — 4 处插入：
- Tool Use 段落：开头添加 `\citep{tool-learning-survey-2024}`
- Adaptive Computation 段落：MTRouter 后添加 RouteLLM 句（line 21）
- Safe RL 段落：Garcia 综述后添加 CRPO 句（line 36）
- LLM Agents 段落：ReAct 后添加 Reflexion 句（line 45）

**dynathink-2025**：first author 确认为 "Yu, Xiao"，bib 中已正确，无需修改。

所有引用均经 WebSearch 验证真实。`tot-2023` 和 `reflexion-2023` 的 key 与 SF6 段落中的 `\citep` 引用匹配。

---
