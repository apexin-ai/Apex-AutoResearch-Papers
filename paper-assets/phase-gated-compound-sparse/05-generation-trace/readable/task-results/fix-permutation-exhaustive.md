# fix permutation exhaustive

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_permutation_exhaustive_20260515T051433_result.json`
- **Structured JSON:** [`9df32b1e2aafc9b3e34b.json`](../../sessions/9d/9df32b1e2aafc9b3e34b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行成功。所有 `perm_p = 0.167 = 4/24`，是精确的 k/24 形式。4 个 sparsity 水平中，完全单调递增的排列有 4 种（本身 + 3 种 ≥ observed_stat 的情况），对应 p = 4/24 ≈ 0.1667。

改动总结：
- 删除 `N_PERM = 5000` 常量
- 新增 `from itertools import permutations`
- `permutation_monotonicity_test` 从 Monte Carlo 5000 次采样改为精确穷举 `permutations(vals)`（24 种），p 值直接用 `count / len(all_perms)`（无 Laplace 校正，因为是精确计算）
- 函数签名移除 `n_perm` 和 `seed` 参数，返回值中 `n_perm` 改为 `n_perms_exact`
- 输出 metadata 中 `permutation_N` 改为 `permutation_method: "exact"`

---
