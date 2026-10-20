# paper p0 edits group1

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p0-edits-group1_20260522T121428_result.json`
- **Structured JSON:** [`1c20d6f192b737936116.json`](../../sessions/1c/1c20d6f192b737936116.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three edits landed correctly. Summary:

| Task | File | Result |
|------|------|--------|
| **1. s43 caveat** | limitations.tex:6 | **Added** — nucleus sampling caveat after statistical power sentence |
| **2. 214× confound** | experiments.tex:25 | **Added** — parenthetical noting premise-count inflation and 1.06× matched value with `\S\ref{sec:goodhart}` |
| **3. ISR aggregate vs per-sample** | method.tex:52 | **Added** — two-use distinction at end of "Limitations of ISR" paragraph |
| **4. p=0.182** | experiments.tex:17,80 | **Already descriptive** — uses "indistinguishable" and "exploratory", no causal language to weaken |
| **5. ISR per-mode** | — | **Skipped** — no claim of uniform effectiveness found; paper already distinguishes mode-specific behavior |
| **6. N=3 power** | limitations.tex:5 | **Already present** — "remain underpowered for seed-level significance" + experiments.tex statistical considerations paragraph |
| **7. 50% non-convergence** | experiments.tex:31 | **Already present** — "Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$)" in §4.1. Note: current text says 2/5 seeds (not 3/6); the paper uses 5 exec-only seeds total ({42,43,44} + 2 additional), not 6 |

---
