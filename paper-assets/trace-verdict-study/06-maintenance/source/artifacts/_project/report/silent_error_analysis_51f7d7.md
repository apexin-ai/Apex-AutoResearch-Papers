# N3: Silent Logic Error Analysis

## Dataset Composition
- Total fail samples: 339
- Silent logic errors (no program exception, test assert fails): **188 (55.5%)**
- Crash errors (program raises exception): **81 (23.9%)**
- Other: 70 (20.6%)

## Fail Recall by Error Type per Condition

| Condition | Silent (n=188) | Crash (n=81) | Gap |
|-----------|---------------|-------------|-----|
| no_trace | 62.8% | 98.8% | +36pp |
| exception_only | **100%** | **100%** | 0pp |
| loop_only | 67.6% | 100% | +32pp |
| full_trace | 50.0% | 88.9% | +39pp |
| vota | 100% | 100% | 0pp |

## Key Findings

1. **55.5% of test failures are "silent"** — program runs without crashing but produces wrong output
2. **exception_only achieves 100% on both types** — test framework's AssertionError IS an exception event
3. **full_trace weakest on silent errors (50%)** — variable snapshots without error markers insufficient
4. **no_trace and loop_only gap: 32-39pp** between crash and silent error recall
5. This explains WHY exception_only works: it captures the test verdict signal (AssertionError) directly
