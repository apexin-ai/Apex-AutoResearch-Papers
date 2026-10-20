# code mvp v2 urgent fix

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_v2_urgent_fix_20260514T090708_result.json`
- **Structured JSON:** [`03bd0f2169b3fba7fa78.json`](../../sessions/03/03bd0f2169b3fba7fa78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the final report.

---

## Pipeline v2 Test (10 samples) — Final Report

### 1. vLLM Restart
- Restarted with `--quantization awq_marlin` (MarlinLinearKernel confirmed)
- Throughput: ~63-65 tokens/s, prefix cache hit rate ~29%

### 2. Code Verification
All v2 code modifications verified on server without needing sync:
- `formalize.py`: few-shot examples, BoolSort types, `syntax_fix_z3` function ✓
- `executor.py`: `execute_with_syntax_fix` function ✓
- `pipeline.py`: correct imports of `syntax_fix_z3` and `execute_with_syntax_fix` ✓
- `repair.py`: updated exec_crash hint ✓
- `analyze.py`: `effective_disagree` metric ✓

### 3. FOL Crash Count/Rate
- **FOL crashes: 1/10 = 10.0%** (only sample [4])
- Code crashes: 4/10 = 40.0% (samples [0,1,2,5] — Python side, thinking tokens leaked into code)

### 4. Avg Time Per Sample
- No per-sample timing data recorded in the JSON (field not present)
- Total pipeline wall time: ~35 min for 10 samples ≈ **~3.5 min/sample**

### 5. Token Stats
| Metric | Value |
|--------|-------|
| Total input tokens | 63,780 |
| Total output tokens | 122,508 |
| Avg input/sample | 6,378 |
| Avg output/sample | 12,251 |
| Total API calls | 41 |

### 6. Syntax Fix Retry Effect
- **Syntax fixes applied: 6/10 samples** (fol_code_fixed was generated)
- **Resolved: 5 of those 6** (FOL no longer Error after fix)
- Without syntax fix, FOL crash rate would have been ~60% → reduced to **10%**

### 7. Effective Disagree Rate
- **Disagree rate: 0.0%** (0/10)
- **Effective disagree (both executed): 0.0%** (0/5 where both ran)
- Agreement distribution: 5 agree_correct + 5 single_error
- FOL accuracy: 90%, Code accuracy: 60%, Oracle: 100%

### MVP Criteria
| Criterion | Result |
|-----------|--------|
| C1: disagree ≥ 10% | FAIL (0%) |
| C2: diagnostic ≥ 40% | FAIL (0/0) |
| C3: error types ≥ 2 | PASS (exec_crash + negation_error) |
| C4: targeted advantage ≥ 5pp | PASS (+40pp: 80% vs 40%) |
| C5: localization ≥ 60% | PASS (100%) |

**MVP: NOT PASSED** — C1/C2 fail because there's no real disagreement: when both representations execute, they always agree. The main bottleneck is Python code quality (40% crash rate from thinking tokens leaking into generated code). Targeted repair shows strong advantage (+40pp over blind), and localization is perfect on exec-error cases.

---
