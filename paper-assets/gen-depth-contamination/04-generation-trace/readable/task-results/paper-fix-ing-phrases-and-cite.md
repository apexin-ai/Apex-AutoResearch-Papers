# paper fix ing phrases and cite

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-ing-phrases-and-cite_20260519T035804_result.json`
- **Structured JSON:** [`0f581d0d50c4ceaa6f55.json`](../../sessions/0f/0f581d0d50c4ceaa6f55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 7 edits applied. Diff summary:

**Task A: 6 -ing phrase fixes**

| # | File | Before | After |
|---|------|--------|-------|
| 1 | `introduction.tex:8` | `...identically, **discarding** the generational depth dimension.` | `...identically and ignores the generational depth dimension.` |
| 2 | `introduction.tex:21` | `...across generations, **motivating** a finite discrimination boundary $K^*$.` | `...across generations; a finite discrimination boundary $K^*$ follows from this monotonic loss.` |
| 3 | `discussion.tex:35` | `...), **producing** a consistent ordering that correlates with...` | `...); the resulting ordering correlates with...` |
| 4 | `discussion.tex:37` | `...), **paralleling** its narrower surprisal dynamic range...` | `...), consistent with its narrower surprisal dynamic range...` |
| 5 | `discussion.tex:38` | `...on arXiv, **reinforcing** the domain-governed interpretation` | `...on arXiv, which reinforces the domain-governed interpretation` |
| 6 | `main.tex:77` | `...($0.5979$), **indicating** the boundary weakens...` | `...($0.5979$); the boundary weakens...` |

**Task B: Citation added**

`appendix_extended.tex:41` (new line between LoRA robustness sentence and "Extrapolating yields..."):
```
The extended discriminability under retraining aligns with theoretical analyses of
iterative retraining instability on synthetic data~\cite{bertrand2024stability,
gerstgrasser2024model}, where each retraining cycle amplifies distributional
artifacts beyond the text-intrinsic degradation observed in prompt-chains.
```

---
