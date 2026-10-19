# paper writing method

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260522T145638_result.json`
- **Structured JSON:** [`57294b69413de66b4868.json`](../../sessions/57/57294b69413de66b4868.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section written to `method.tex`. Key design choices:

- All symbols ($\mathbf{h}_l$, $f_\theta$, $\mathbf{w}_{\text{probe}}$, $\Delta_{\text{asym}}$, $\alpha$) defined at first use, consistent with Experiments section notation
- Citations use `\citep{}` with the specified bib keys; `\citet{}` only for inline author references (Li et al., Zou et al.)
- No em-dash, no -ing phrase endings, no banned transition words
- ~1200 words, 7 subsections matching the outline
- Figure~\ref{fig:pipeline} referenced in the opening sentence
- Equations numbered for cross-referencing (Eq.~\ref{eq:asymmetry}, Eq.~\ref{eq:steering})
- Layer/depth conventions match Experiments (L13/41%, L18/56%, L28/88%)
- Data splits match exactly (1,368/966, 80/20 stratified)

---
