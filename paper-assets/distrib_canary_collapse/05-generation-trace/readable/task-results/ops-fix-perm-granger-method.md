# ops fix perm granger method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-perm-granger-method_20260514T215019_result.json`
- **Structured JSON:** [`b2246323dfa9b78cfaec.json`](../../sessions/b2/b2246323dfa9b78cfaec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已修正。

## Summary

| 项目 | 详情 |
|------|------|
| **代码实际方法** | `np.roll(x, shift)` — circular shift（`shift = rng.integers(1, T)`） |
| **JSON 原记录** | `"perm_method": "shuffle"`, `"permutation_method": "auto"` |
| **修改内容** | 仅修改 JSON：`perm_method` → `"circular_shift"`, `permutation_method` → `"circular_shift"` |
| **代码改动** | 无，代码已经是 circular shift |
| **是否需要重跑** | 不需要，permutation 逻辑未变，p-value 不变 |

**T=11 下 circular shift 局限性**：原始序列 T=11，first-difference 后 T=10，`np.roll` 的 shift 范围为 {1, ..., 9}，只有 **9 个唯一 permutation**。n_perm=1999 实际是从这 9 个 shift 中有放回抽样，null distribution 只有至多 9 个唯一 F-stat 值。这不影响 p-value 的数学正确性（Monte Carlo estimate 仍然有效），但 null distribution 是高度离散的。最小可达 p-value 为 1/2000=0.0005（由 n_perm 决定），能达到 α=0.05 阈值，不存在无法拒绝 null 的问题。

---
