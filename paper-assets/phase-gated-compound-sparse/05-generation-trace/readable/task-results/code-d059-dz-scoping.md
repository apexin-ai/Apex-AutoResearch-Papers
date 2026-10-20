# code d059 dz scoping

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d059_dz_scoping_20260514T192646_result.json`
- **Structured JSON:** [`6f05f556dad9e315df1c.json`](../../sessions/6f/6f05f556dad9e315df1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法通过。剩余 d_z 引用全部在 within-importance 上下文中：

| 行号 | 位置 | 类型 |
|------|------|------|
| 252-254, 286-288 | `analyze_condition()` | within-condition phase gradient |
| 424, 442 | `format_report()` per-condition 表 | within-condition |
| 629 | `main()` section 3 per-condition 输出 | within-condition |
| 719-720 | pre-registration verdict (qw_imp_s015) | within-importance |

所有 imp-vs-rand 的 d_z 已移除（`paired_imp_vs_rand()`、`paired_imp_vs_rand_gradient_test()`、对应的报告表格和 print 输出共 10 处）。语法检查通过。

---
