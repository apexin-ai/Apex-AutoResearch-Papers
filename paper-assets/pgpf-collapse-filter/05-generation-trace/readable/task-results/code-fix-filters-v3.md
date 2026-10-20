# code fix filters v3

**pgpf collapse filter** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_filters_v3_20260513T114826_result.json`
- **Structured JSON:** [`eaa32917ba545aedfae1.json`](../../sessions/ea/eaa32917ba545aedfae1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。修复总结：

**Bug 1 — Score key 不匹配**：`s["lc"]` → `s["lexical_conformity"]`，`s["sn"]` → `s["semantic_novelty"]`，`self.weights` 的 key 同步更新。

**Bug 2 — LC 方向反转**：`1 - (rankdata(lc) - 1) / (n - 1)` → `(rankdata(lc) - 1) / (n - 1)`。三个属性方向统一为"越高越好"。

验证结果：
- import OK
- dry-run：三个 filter 均输出 2500 条（= 5000 × 0.5），ALL EQUAL: True

---
