# code r22 base instruct composition

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r22_base_instruct_composition_20260523T081029_result.json`
- **Structured JSON:** [`e218f90c65fa7c1107d9.json`](../../sessions/e2/e218f90c65fa7c1107d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰：

**Original C% = 31.32%**
**Balanced C% = 30.25% ± 1.32% (95% CI: [27.65%, 32.84%])**
**Δ = 1.08 pp**

均衡 base/instruct 比例后（两个 cohort 都调到 67.9% base），C% 几乎不变——从 31.32% 降到 30.25%，差异仅 1.08 pp，在抽样噪声范围内。10 次重复的 C% 都在 28.3%–32.7% 之间波动。

结论：DIF 不是由 base/instruct composition shift 驱动的。所有输出已保存到 `artifacts/r22_composition_control/`。

---
