# ops traj repo 8k cuda2 continue

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-repo-8k-cuda2-continue_20260516T162243_result.json`
- **Structured JSON:** [`8c8f54dce11efdbe7792.json`](../../sessions/8c/8c8f54dce11efdbe7792.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。两个 seed 的 registry 均已推进到 DONE。

## 最终结果汇总

| Metric | Seed 0 | Seed 789 |
|--------|--------|----------|
| **Test Accuracy** | **75.00%** | **66.67%** |
| Resolved F1 | 80.65 | 75.00 |
| Unresolved F1 | 64.71 | 50.00 |
| Best Eval Loss | 0.1090 | 0.1295 |
| Unparseable | 0 | 0 |
| Majority Baseline | 54.17% | 54.17% |
| **Δ vs Baseline** | **+20.83pp** | **+12.50pp** |

两个 seed 均显著超越 majority baseline（54.17%）。Seed 0 表现更优，accuracy 高 8.33pp，resolved/unresolved F1 均领先。两个 seed 的 variance 较大（accuracy 差 8.33pp），后续可能需要更多 seed 或更大训练集来稳定。

---
