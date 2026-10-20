# code fix multiseed stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-multiseed-stats_20260515T002038_result.json`
- **Structured JSON:** [`3962390d4b4a5cfde221.json`](../../sessions/39/3962390d4b4a5cfde221.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复生效。关键对比：

| 对比 | 修复前 p | 修复后 p | McNemar p |
|------|---------|---------|-----------|
| TaxEI vs Random seed=0 | **0.0000** | **0.1243** | 0.1250 |
| TaxEI vs Vanilla pooled | 0.0170 | **0.0540** | 0.0525 |
| TaxEI vs Random pooled | 0.0512 | **0.1702** | 0.1796 |

修复后 permutation test 与 McNemar test 一致，pooled TaxEI vs Vanilla 从显著 (p=0.017) 变为不显著 (p=0.054)。

**Bug 本质**：`diff_obs = np.mean(a) - np.mean(b)` 与 `perm_diff = np.mean((a-b) * signs)` 使用不同的浮点运算路径。`mean(a) - mean(b)` 是两次除法再相减，`mean(a-b)` 是一次整数差的除法。两者差 ~1.4e-17，但足以让 `>=` 比较在边界情况（如只有 4 个 discordant pairs 时）全部失败，导致 p=0。

**修复**：
1. `diff_obs` 改为 `np.mean(diffs)` 确保与 `perm_diff` 计算路径一致
2. p 值改为 `(count+1)/(n_perm+1)` 避免 p=0（标准做法，Phipson & Smyth 2010）

---
