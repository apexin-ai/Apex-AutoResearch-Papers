# DebugBench Data Audit Report (plan_005)

## 1. Data Attrition: 1414 → 1024 (-390, 27.6%)

### Stage 1: Test Building (1414 → 1222, -192)
| Reason | Count | % of 1414 |
|--------|-------|-----------|
| ok (usable) | 1222 | 86.4% |
| skip_complex (TreeNode/ListNode etc.) | 160 | 11.3% |
| skip_parse_fail (can't parse I/O) | 26 | 1.8% |
| skip_nondeterministic | 6 | 0.4% |

### Stage 2: Validation (1222 → 1024, -198)
Correct solution fails generated test cases. By bug category:
| Category | Filtered |
|----------|----------|
| multiple error | ~121 |
| reference error | ~23 |
| syntax error | ~21 |
| logic error | ~16 |

Note: category counts approximate (slug+subtype dedup); total confirmed 198 by line count.

### Pipeline
```
debugbench_python.jsonl (1414)
  → debugbench_test_builder.py → test_cases.jsonl (1222)
  → debugbench_validate_tests.py → test_cases_validated.jsonl (1024)
  → debugbench_collect_traces.py → raw_traces.jsonl (2048 = 1024×2)
  → debugbench_format_data.py → 3 conditions × (1622 train + 426 test)
```

## 2. VOTA Condition: MISSING

`debugbench_format_data.py` only generates 3 conditions: no_trace, exception_only, full_trace.
No VOTA formatting path was implemented for DebugBench.

Files present:
- ✅ debugbench_no_trace_{train,test}.jsonl
- ✅ debugbench_exception_only_{train,test}.jsonl
- ✅ debugbench_full_trace_{train,test}.jsonl
- ❌ debugbench_vota_{train,test}.jsonl — does not exist

## 3. Exception_only Theoretical Ceiling: 71.1%

### Test set composition (426 samples)
| | Pass | Fail | Total |
|---|---|---|---|
| Has exception data | 0 | 84 | 84 |
| No exception data | 219 | 123 | 342 |
| Total | 219 | 207 | 426 |

- 59.4% of fail samples have NO exception → logic errors invisible to exception_only
- All pass samples have no exception → "no exception" is ambiguous signal
- **Theoretical ceiling**: 303/426 = **71.1%** (all pass + all fail-with-exception correct)
- Majority baseline: 51.4% (pass)

### DebugBench "logic error" exception detail
- 134 buggy fail samples labeled "logic error"
- 121/134 (90.3%) actually DO produce exception events (downstream failures)
- Only 13/134 (9.7%) are truly exception-free logic errors

## 4. Full_trace Token Length (Qwen tokenizer, +32 chat overhead)

| Metric | full_trace | exception_only | no_trace |
|--------|------------|----------------|----------|
| Mean | 1508.2 | 372.4 | 273.9 |
| Median | 2048 | 293 | 226 |
| Max | 2048 | 1859 | 1849 |
| >2048 | 0 (0%) | 0 (0%) | 0 (0%) |
| >1024 | 1424 (69.5%) | — | — |

- **68.9% of full_trace samples are truncated** (1412/2048 hit 2048-token cap)
- Median at 2048 = majority of samples lose trace information
- Truncation is one-directional: only full_trace affected, exception_only and no_trace well within limits

## 5. Raw Trace Quality

| Code type | Pass | Fail | Total |
|-----------|------|------|-------|
| correct | 1016 | 8 | 1024 |
| buggy | 26 | 998 | 1024 |

- 8 correct solutions fail tests (0.8%) — test case edge cases
- 26 buggy solutions pass tests (2.5%) — bugs not triggered by generated tests
- 625/2048 (30.5%) have empty trace_raw

## 6. Registry Status

No plan_005 experiments registered. Only data preparation complete; no training has been run on DebugBench data.
