# data update compilation seed123 test v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_update-compilation-seed123-test-v2_20260515T103347_result.json`
- **Structured JSON:** [`69e956de1ad41f81f70f.json`](../../sessions/69/69e956de1ad41f81f70f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

val_sweep_compilation.md 已更新完成。

关于 comprehensive_results_summary.md：Section 4.6 的 seed123 test 部分（line 222-234）只记录了 val-best ckpt-3000 的 test 结果，没有 ckpt-6200/6400 的 test 行——这是合理的，因为那个表格只展示 val-selected checkpoint 的 test 性能。ckpt-6200/6400 不是 val-best，属于 sweep 补充数据，只需在 val_sweep_compilation.md 中记录即可，comprehensive_results_summary.md 无需更新。

补充观察：ckpt-6400 test (85.08%) 接近 ckpt-3000 test (85.60%)，差距仅 0.52pp，但 f1_macro 低 0.47pp (77.91 vs 78.38)。val-best ckpt-3000 仍然是 test-best，val-test 选择一致。

---
