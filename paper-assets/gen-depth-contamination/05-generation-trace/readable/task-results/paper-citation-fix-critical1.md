# paper citation fix critical1

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_citation-fix-critical1_20260515T042544_result.json`
- **Structured JSON:** [`f11e73b815cb86af7f18.json`](../../sessions/f1/f11e73b815cb86af7f18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All TODO citations replaced. Summary:

### Bib entries added (`references.bib`)

1. **`sun2025aigt`** — Sun et al., "Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media," ACL 2025. Measured AI-generated text prevalence across Medium (→37%), Quora (→39%), Reddit (→2.5%).

2. **`spennemann2025quantifying`** — Spennemann, "Delving into: the Quantification of AI-Generated Content on the Internet," arXiv 2025. Estimated ≥30% of active web pages contain AI-generated text.

### Replacements made

| File | Line | Old | New |
|------|------|-----|-----|
| `introduction.tex` | 6 | `\cite{TODO_ai_prevalence_1, TODO_ai_prevalence_2}` | `\cite{sun2025aigt, spennemann2025quantifying}` |
| `discussion.tex` | 173 | `\cite{TODO_ai_prevalence}` | `\cite{sun2025aigt, spennemann2025quantifying}` |
| `discussion.tex` | 180 | `\cite{TODO_ai_prevalence}` | `\cite{sun2025aigt, spennemann2025quantifying}` |

**Note:** `main.tex` abstract mentions "5-15%" but has no `\cite{}` — standard practice for abstracts. No TODO was present there.

**Caveat:** Both papers report higher figures than 5-15% (Spennemann: 30-40%; Sun et al.: up to 39% on some platforms, 2.5% on Reddit). The "5-15%" figure in the text is a conservative estimate. You may want to revise it upward or add a qualifier like "and likely growing."

---
