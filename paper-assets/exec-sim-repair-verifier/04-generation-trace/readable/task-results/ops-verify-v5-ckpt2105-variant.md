# ops verify v5 ckpt2105 variant

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-v5-ckpt2105-variant_20260518T234751_result.json`
- **Structured JSON:** [`6d526785cbc8f4cdf265.json`](../../sessions/6d/6d526785cbc8f4cdf265.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

**Variant-level accuracy 确认: 81.25% (39/48)，与论文 Table 7 报告一致。**

### 关键参数
- 总测试样本: 9,784 rows
- 总 variants: 48 (26 resolved, 22 unresolved)
- Majority baseline: 54.17%
- Variant 定义: `(problem_id, mutation_type)` 对，不是单纯的 `problem_id`

### 9 个错误 variant

| Variant | GT | Pred | 原因 |
|---|---|---|---|
| `astropy__astropy-7336__gold` | 1 | 0 | 357 tests 中 20 个预测为 fail |
| `django__django-11848__gold` | 1 | 0 | 79 tests 中 19 个预测为 fail |
| `django__django-12325__gold` | 1 | 0 | 237 tests 中 58 个预测为 fail |
| `django__django-12406__gold` | 1 | 0 | 219 tests 中 54 个预测为 fail |
| `django__django-13109__gold` | 1 | 0 | 206 tests 中 19 个预测为 fail |
| `django__django-14351__mutation_boundary_removal` | 1 | 0 | 76 tests 中 21 个预测为 fail |
| `django__django-15037__gold` | 1 | 0 | 32 tests 中 18 个预测为 fail |
| `pytest-dev__pytest-6202__mutation_return_value` | 0 | 1 | 90 tests 全部预测 pass (FP) |
| `pytest-dev__pytest-7490__mutation_operator_swap` | 0 | 1 | 114 tests 全部预测 pass (FP) |

7 个是 FN (gold/resolved 被错判为 unresolved)，2 个是 FP (mutation 被错判为 resolved)。数字与论文完全一致。

---
