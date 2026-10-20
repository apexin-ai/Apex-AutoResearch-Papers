# audit data end to end

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data_end_to_end_20260523T102339_result.json`
- **Structured JSON:** [`679a705ebbb344a12c80.json`](../../sessions/67/679a705ebbb344a12c80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Audit Complete

**47 checks performed. 44 passed, 3 issues found (0 critical).**

### Key Results

**Record counts** — All verified. 2,304,000 total = 8 models × 5 benchmarks × 57,600. OLMo/Yi HellaSwag data stored as checksummed binary blobs in analysis scripts rather than JSONL (functional but unusual).

**Henderson Method I** — Script verified correct: balanced crossed design, proper EMS equations, negative variance truncated to 0, bootstrap CIs via item-level resampling.

**Variance components** — All sum to 100% across all benchmarks. G_item values match data within rounding tolerance everywhere.

**Cross-references** — All major claims (G_item range 0.863–0.896, partial-credit 0.863→0.768, item budgets 178/552/55, 3.1× reduction, fixed/random ΔG 0.077–0.113, 48.1% arithmetic correctness) are consistent across abstract, experiments, method, limitations, and appendix.

### 3 Issues to Address

| ID | Severity | Issue |
|---|---|---|
| **VC-1** | Medium | Table 3 "prompt†" row doesn't match data for MC benchmarks. Footnote says "prompt×item interaction" but MMLU shows 2.5% vs actual prompt:item 0.95%. The 2.5% is actually the sum of ALL unlisted components. ARC is even more inconsistent (0.4% in table vs 1.45% prompt:item). |
| **VC-2** | Low | Table 3 HellaSwag mod×prmpt: 0.6% vs data 0.19% |
| **VC-3** | Low | Table 3 MATH mod×prmpt: 2.0% vs data 1.68% |

None of these affect the paper's main conclusions — the dominant components (item, model×item, residual, model) are correct across all benchmarks, and D-study projections are computed from full variance components, not from the rounded table.

---
