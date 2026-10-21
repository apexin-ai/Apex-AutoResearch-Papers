# fix section ref and equation overflow

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_section_ref_and_equation_overflow_20260528T181422_result.json`
- **Structured JSON:** [`30c3eeca779f0d0528fe.json`](../../sessions/30/30c3eeca779f0d0528fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修复完成：

1. **Section ??**: method.tex 中两处 `\ref{sec:linear_results}` 指向了未被 main.tex 引入的 results.tex。已改为 experiments.tex 中对应的 label：
   - 第 57 行 → `sec:cv_sensitivity`（讨论 L2 空间聚集 vs random 的 scoring 差异）
   - 第 72 行 → `sec:two_axis`（报告 cliff 行为和精细化 k 值结果）

2. **公式 4 溢出**: CV spectrum 链式不等式用 `split` 环境拆为两行，在 X-VLA 后断行，`<` 符号对齐。公式编号 (4) 不变。

---
