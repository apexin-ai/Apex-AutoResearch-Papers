# ops check yi15 progress

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_yi15_progress_20260514T181108_result.json`
- **Structured JSON:** [`16ce896412854ad40bdb.json`](../../sessions/16/16ce896412854ad40bdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已崩溃。进程不再运行，两块 GPU 利用率均为 0%。

**已完成的阶段：**
- Phase 1 (Profiling): 全部完成
- Phase 2/3 (k search): 完成，best k=2, PPL=7.2714（优于 baseline 7.3461）
- Phase 4 (Heterogeneity Analysis): 完成，top-5 sensitive heads 已识别（L4H3 最敏感，delta=+5.6732）

**崩溃原因：**
```
ImportError: cannot import name 'solve_ratequant_greedy' from 'solver' (/root/ratekv/solver.py)
```

Phase 4 之后进入求解阶段时，`run_yi15_full_pipeline.py:194` 试图从 `solver.py` 导入 `solve_ratequant_greedy`，但该函数不存在。

需要检查 `solver.py` 中实际的函数名，修复导入后重跑（Phase 4 结果已有，可以从断点续跑）。要我修复吗？

---
