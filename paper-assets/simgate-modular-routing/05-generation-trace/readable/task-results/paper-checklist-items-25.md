# paper checklist items 25

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_checklist-items-25_20260521T093843_result.json`
- **Structured JSON:** [`bd02398d6656a4b6a97a.json`](../../sessions/bd/bd02398d6656a4b6a97a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied and compiled successfully. Summary of changes to `main.tex`:

1. **Preamble**: Added `\usepackage{tcolorbox}` with `listings` and `breakable` libraries.

2. **Appendix Overview** (line 76): Added `T. Agent Prompt Templates` entry.

3. **Ethics Statement** (line 51): Expanded GPU-hours from a single number to a 3-way breakdown: ~140h episode collection, ~35h router training, ~25h evaluation/analysis.

4. **New Appendix T** (after Appendix S, before responsibleNLPchecklist): Contains 5 prompt templates in `tcblisting` environments:
   - **Shared system prompt** — ReAct format instructions used by both strategies
   - **Internal (ReAct) user template** — single-action selection
   - **Deterministic candidate generation template** — ranked top-3 action generation for simulator forking
   - **Reflexion self-reflection prompt** — post-failure analysis for retry
   - **Grounding warning (ablation)** — `focus on` safety rule appended in prompt ablation condition
   
   Plus a closing note highlighting the key difference between strategies (select vs. rank).

---
