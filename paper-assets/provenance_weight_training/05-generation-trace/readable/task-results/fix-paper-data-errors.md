# fix paper data errors

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper_data_errors_20260515T233725_result.json`
- **Structured JSON:** [`535b0cb00100109fbf5d.json`](../../sessions/53/535b0cb00100109fbf5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files verified. Here's the complete change summary:

---

### experiments.tex

| # | Line | Before | After |
|---|------|--------|-------|
| C1 | :19 | `on a balanced real/synthetic test set via sliding-window evaluation (stride 1024, 4.08M tokens)` | `on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024)` |
| C2a | :6 | `the same architecture we pretrain from scratch` | `the same architecture used for continued pretraining` |
| C2b | :15 | `We pretrain Qwen3-0.6B from random initialization for` | `We continue pretraining Qwen3-0.6B from its pretrained weights for` |

### results.tex

| # | Line | Before | After |
|---|------|--------|-------|
| W3 | :10 | `17.651 to 17.738 on seed 42` | `17.651 to 17.818 on seed 42` |
| W4 | :76 | `$n_{\min} = 3$ yields a comparable 17.651` | `$n_{\min} = 3$ yields a comparable 17.644` |
| W5 | :13 | `ESS-only (maximum intervention) yields PPL 17.728 on seed 42, \emph{worse} than uniform (17.694) by 0.034` | `ESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \emph{worse} than uniform (17.694) by 0.029` |
| W5 | :31 | `ESS-only$^\dagger$ & 17.728 & -- & -- & --` | `ESS-only & 17.730 & 17.720 & 17.719 & 17.723` |
| W5 | :39 | `$^\dagger$Evaluated on seed 42 only; remaining seeds in progress.` | `$^\dagger$Evaluated on seed 42 only.` |

### table1_data.md (both copies)

| Change | Before | After |
|--------|--------|-------|
| Uniform values | 17.690/17.690/17.700, mean 17.693 | 17.694/17.686/17.702, mean 17.694 |
| Removed stale rows | Adaptive (n_min=3) + Adaptive-fix (n_min=2) | Single "Adaptive (ours, τ=0.8, n_min=2)" row: 17.653/17.643/17.657 |
| Added ESS-only | absent | 17.730/17.720/17.719, mean 17.723 |
| Added Golden Ratio | absent | 17.654 (single seed) |
| Baseline header | mean PPL = 17.693 | mean PPL = 17.694 |

---
