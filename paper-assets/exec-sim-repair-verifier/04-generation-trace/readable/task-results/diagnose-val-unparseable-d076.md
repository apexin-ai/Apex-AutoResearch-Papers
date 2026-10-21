# diagnose val unparseable d076

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_val-unparseable-d076_20260514T145852_result.json`
- **Structured JSON:** [`f12d94420c800983c65e.json`](../../sessions/f1/f12d94420c800983c65e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D076 Val Unparseable 根因分析结论

### 根因

**Val 20.2% unparseable 完全由 prompt 截断引起，精确定位到 2 个 problem_id：**

| Problem ID | 样本数 | Token 数 | 影响 |
|---|---|---|---|
| `sympy__sympy-14248` | 1406 | ~4947 | @2048 和 @4096 都截断 |
| `pytest-dev__pytest-5787` | 477 | ~2352 | @2048 截断，@4096 可容纳 |

1406 + 477 = **1883 = 精确匹配 unparseable 数量**。在 4096 下，只有 sympy 仍截断 = **1406 = 精确匹配 15.1%**。

### 为什么 Test 不受影响

Val 和 test 的 problem_id **零重叠**。Test 最长的 problem（xarray-6992）tokenize 后为 2034-2047 tokens — 差 1-14 个 token 就超 2048 限制。纯属运气。

### 截断机制

截断 prompt → 模型看到不完整 diff → 继续补全代码而非回答 "pass/fail" → 被标记为 unparseable。即使碰巧 "可解析"，准确率也仅 35.8%（本质上是随机猜测）。

### 推荐修复

**eval 时 `--max_seq_length 5120`**（val 最长 4947 tokens，5120 全部容纳）。无需改代码、无需丢数据。batch_size 可能需从 16 降到 8。修复后 val 0% unparseable，可可靠地用于 checkpoint selection。

详细报告：`artifacts/d076_val_unparseable_root_cause.md`

---
