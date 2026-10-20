# paper c2 numbers unified

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_c2-numbers-unified_20260518T064518_result.json`
- **Structured JSON:** [`ef37e708e2a6f531c55e.json`](../../sessions/ef/ef37e708e2a6f531c55e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes are consistent. Here's the summary of all modifications:

**6 files modified, 12 edits total:**

| File | Change | Old | New |
|------|--------|-----|-----|
| `abstract_body.tex` | seed count | four tested seeds ($n{=}4$) | six tested seeds in two environments ($n{=}6$) |
| `abstract_body.tex` | collapse count | three progressing...one self-correcting | five progressing...one self-correcting |
| `introduction.tex` L6 | NVE classification | 11/12 ($n{=}12$, single environment) | 13/14 ($n{=}14$, two environments) |
| `introduction.tex` L8 | seed analysis | $n{=}4$, 3/4, 1/4 | $n{=}6$ across two envs, 5/6, 1/6 |
| `introduction.tex` L14 | detector contribution | 3/3 CIVO cases, 2/3 | 5/5 CIVO cases, 2/5 |
| `results.tex` L67 | NVE threshold | 11 of 12 (AUROC=0.926) | 13 of 14 (AUROC=0.933) |
| `results.tex` L67 fn | non-baseline subset | 7/8, AUROC=0.867 | 9/10, AUROC=0.880 |
| `results.tex` L72 | F2 caption | $n{=}3$ | Walker factorial $n{=}3$; seed~4 in Table |
| `results.tex` L76 | F2 paragraph | all four tested seeds...3/4...1/4 | all four Walker Walk seeds + cross-env summary 5/6, 1/6 |
| `methodology.tex` L87 | NVE definition | 12 configs, 11/12, AUROC=0.926 | 14 configs, 13/14, AUROC=0.933 |
| `analysis.tex` L23 | detector sensitivity | 3/3, all before 65K | 5/5, three before 65K + two later |
| `analysis.tex` L23 | calibration set | eleven runs | thirteen runs |
| `conclusion.tex` L8 | NVE classification | 11/12 ($n{=}12$, 91.7%) | 13/14 ($n{=}14$, 92.9%) |
| `conclusion.tex` L18 | limitations | 11/12 | 13/14 |

**AUROC recalculation**: 5 positives × 9 negatives = 45 pairs; 42 concordant (only 008e\_v3\_s2 at NVE=3.78 beats 3 positives) → 42/45 = 0.933. No em-dashes found.

---
