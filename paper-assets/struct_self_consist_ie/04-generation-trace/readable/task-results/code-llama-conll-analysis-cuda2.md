# code llama conll analysis cuda2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_conll_analysis_cuda2_20260518T190506_result.json`
- **Structured JSON:** [`b527686710a9c9f99f08.json`](../../sessions/b5/b527686710a9c9f99f08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LLaMA FewNERD training is at 62% (15454/24708), ~4.2h remaining. No immediate inference tasks for cuda:2.

## Summary

### Completed: LLaMA CoNLL DGS + 5-Signal Analysis

**DGS Results** (`output/exp_017_llama_conll/dgs_results.json`):
| Metric | Value |
|--------|-------|
| Degeneracy | 89.4% (2465/2756) |
| Greedy F1 | 0.9239 |
| DGS F1 | 0.9254 |
| DGS - Greedy | **+0.14pp** [0.03, 0.28] |
| Non-degen LP - Greedy | **+1.37pp** [0.30, 2.66] |

**5-Signal rho (3-seed mean)**:
| Signal | rho | SD |
|--------|-----|-----|
| SJ | 0.463 | 0.007 |
| EM | 0.460 | 0.008 |
| VC | 0.458 | 0.003 |
| FK | 0.455 | 0.006 |
| LP | 0.310 | 0.006 |

**Cross-Model Comparison (CoNLL)**:
| | LLaMA | Qwen |
|--|-------|------|
| Degeneracy | 89.4% | 57.9% |
| Greedy F1 | 0.924 | 0.907 |
| Headroom | 2.11pp | 4.24pp |
| DGS delta | +0.14pp | -0.81pp |

### Registry & Artifacts Updated
- `exp_017_llama_conll` metrics updated with DGS + 3-seed rho/AUROC
- Report at `output/exp_017_llama_conll/analysis_report.md`

### GPU Status
- cuda:0/2: Free (no high-priority inference tasks)
- cuda:1: LLaMA FewNERD training (62%, ~4.2h remaining)
- cuda:3: LLaMA SciERC seed123 inference (vLLM)

---
