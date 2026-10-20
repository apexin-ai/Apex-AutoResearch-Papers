# writing c5b design revision

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_c5b_design_revision_20260514T145503_result.json`
- **Structured JSON:** [`7e4d94757a97bda0267f.json`](../../sessions/7e/7e4d94757a97bda0267f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项修订已写入 `c5b_pilot_design.md`：

1. **§3 头部**：添加 Revision 块，明确 phase-aware modulation 仅适用于 KV eviction，head pruning 保持 uniform；三条件重新定义为 (1) uniform+uniform, (2) uniform+oracle KV, (3) uniform+heuristic KV；标注代码影响不变。

2. **§3.2 δ cap 处**：原 "s_trans capped at 0.50" 替换为 proportional rescale 公式——cap 触发时反求 δ_effective = cap × (n_trans / n_exec)，确保总 compute 精确匹配。含验证推导和三项边界条件。

文档其余部分（含 Scheme C 段落）未改动。

---
