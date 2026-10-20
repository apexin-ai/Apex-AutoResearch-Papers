# code acdc 14edge docs

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acdc-14edge-docs_20260513T013724_result.json`
- **Structured JSON:** [`68118ac11e85c9e2eaa9.json`](../../sessions/68/68118ac11e85c9e2eaa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

register_artifact 不可用，跳过注册步骤。

## 产出总结

### cache_acdc.json 格式解释

ACDC 初始化所有 32,491 条边为 `inf`，然后用 5 个阈值 (0.01, 0.03, 0.05, 0.07, 0.09) 逐步剪枝。被剪掉的边被赋值为移除时的 tao 值，存活所有阈值的边保持 `inf`。

| Score | Count |
|-------|-------|
| inf | **14** (retained circuit) |
| 0.09 | **14** (最后一步才被剪) |
| 0.07 | 11 |
| 0.05 | 50 |
| 0.03 | 138 |
| 0.01 | 32,264 |

### 为什么不是 cherry-picking

`math.isinf()` 是读取 ACDC 输出的**唯一正确方式**——ACDC 是二值判定算法（留/剪），`inf` 是算法内部标记"保留"的语义，不是人为选的阈值。`auto_circuit` 源码自身也用 `s == t.inf` 判断。14 vs 14 的数量巧合是因为 score=0.09 的边恰好也有 14 条，但它们是在最宽松阈值下被剪掉的边。

### 代码注释

- `analysis_fix_v3.py:38-42` — `binarize_acdc` 函数内注释
- `circuit_discovery.py:111` — `run_acdc` docstring 更新

### 文档产出

`artifacts/D020_acdc_edge_selection.md` — 包含完整边列表、score 分布、技术解释

---
