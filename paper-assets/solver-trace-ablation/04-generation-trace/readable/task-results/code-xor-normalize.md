# code xor normalize

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_xor-normalize_20260513T175523_result.json`
- **Structured JSON:** [`a522a8fe715800a9dcce.json`](../../sessions/a5/a522a8fe715800a9dcce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Prover9** — `_expand_xor()` 在 Unicode→ASCII 替换前展开 `A ⊕ B` → `((A ∨ B) ∧ ¬(A ∧ B))`，支持括号匹配、嵌套和链式 XOR。实测 100 条数据中 34 条含 ⊕（50 处 XOR），全部正确展开，0 错误。

**Z3** — 添加 `XOR` token 和 `_xor_expr()` 解析层（优先级在 IMPLIES 和 OR 之间），直接映射到 `z3.Xor()`。

---
