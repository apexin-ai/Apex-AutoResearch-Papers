# code plan009 finer ordinal

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan009-finer-ordinal_20260515T225221_result.json`
- **Structured JSON:** [`390397dc5641d1675c50.json`](../../sessions/39/390397dc5641d1675c50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan-009 完成。结论：**negative**。

## 结果摘要

| Model | 5-class macro-F1 | 95% CI |
|-------|-----------------|--------|
| **HGBT** | **0.5028** | [0.4974, 0.5079] |
| RF | 0.4767 | [0.4718, 0.4815] |
| Frank-Hall (ordinal) | 0.4513 | [0.4459, 0.4564] |
| LR | 0.4468 | [0.4417, 0.4518] |
| **HGBT 3-class** | **0.7815** | [0.7764, 0.7864] |

**5-class vs 3-class delta: -0.2787** — 5-class 分类大幅劣于 3-class。

### Per-class F1 (HGBT 5-class)
- depth_0: 0.913 (很好)
- depth_1: 0.628 (尚可)
- depth_2: 0.269 (差)
- depth_3: 0.265 (差)
- depth_4: 0.439 (一般)

depth_2 和 depth_3 几乎不可分，说明 **中间代际（gen-2/gen-3）的特征高度重叠**，finer-grained classification 不提供额外有效信息。3-class 方案（gen-0/gen-1/gen-2+）仍是最优分类粒度。

结果已保存到 `results/finer_ordinal_results.json`，registry 已更新为 DONE (negative)。

---
