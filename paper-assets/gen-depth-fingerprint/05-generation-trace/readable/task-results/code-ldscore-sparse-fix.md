# code ldscore sparse fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ldscore-sparse-fix_20260516T200237_result.json`
- **Structured JSON:** [`5c5efbdd5ea7438977db.json`](../../sessions/5c/5c5efbdd5ea7438977db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果已保存到 `/root/gen-depth-fingerprint/results/8gen_ldscore_sparse_fixed.json`。

**结果摘要：**

| 任务 | F1 | 95% CI |
|------|-----|--------|
| Binary (gen1 vs gen2+) | **0.6762** | [0.6706, 0.6818] |
| 3-class (0/1/2+) | **0.6317** | [0.6268, 0.6363] |

Binary F1 = 0.6762 在预期范围 [0.63-0.68] 内（之前 seed=789 报 0.6574），确认 sparse 实现修复�� v4 vocab 截断 bug��v4 降至 0.491）。

实现细节：character-level trigram JSD，sparse CSR 矩阵 50778 vocab（无截断），per-fold 从训练集 depth-0 计算参考分布。

---
