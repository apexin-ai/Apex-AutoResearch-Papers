# fix et triplecount and rerun all

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_et_triplecount_and_rerun_all_20260514T182039_result.json`
- **Structured JSON:** [`e8dd56e47f5242636482.json`](../../sessions/e8/e8dd56e47f5242636482.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 11 experiments updated in registry. Here's the final summary:

## ET Triple-Counting Fix Results (v1 → v2)

### DocRED (Qwen3-8B)
| Mode | ET_v1% | ET_v2% | Delta | DR% | RV% | CF | R-F1 |
|------|--------|--------|-------|-----|-----|-----|------|
| unconstrained | 8.18 | **2.48** | -5.70 | 18.46 | 29.66 | 20 | 7.74 |
| grammar_only | 0 | 0 | 0 | 26.17 | 0.03 | 14 | 8.31 |
| semantic_only | 10.44 | **4.22** | -6.22 | 13.84 | 29.87 | 211 | 7.70 |
| full_s1 | 0 | 0 | 0 | 10.21 | 0.03 | 518 | 8.23 |

### SciERC (Qwen3-8B)
| Mode | ET% | DR% | RV% | E-F1 | R-F1 |
|------|-----|-----|-----|------|------|
| unconstrained | 0.4 | 15.37 | 1.39 | 31.01 | 8.23 |
| grammar_only | 0 | 14.84 | 0 | 30.98 | 8.23 |
| semantic_only | 0.4 | 11.65 | 1.51 | 31.01 | 8.15 |
| full_s1 | 0 | 0.93 | 0 | 30.98 | 8.36 |
| full_s2 | 0 | 0.97 | 0 | 31.90 | 8.03 |

### SciERC (Llama-3.1-8B)
| Mode | ET% | DR% | RV% | E-F1 | R-F1 |
|------|-----|-----|-----|------|------|
| unconstrained | 0 | 13.34 | 0.55 | 23.56 | 2.68 |
| full_s1 | 0 | 0.08 | 0 | 23.49 | 2.54 |

### Key observations:
1. **DocRED ET inflated ~3x** — unconstrained 8.18%→2.48% (3.3x), semantic_only 10.44%→4.22% (2.5x)
2. **DR/RV/CF/F1 unchanged** — fix is purely cosmetic to ET counting, other metrics unaffected
3. **SciERC unaffected** — its checker only counted ET from entity_list, no triple-counting existed
4. All experiments now tagged `checker_version: fixed_20260514_v2 (strip + alias + unique_et)`

---
