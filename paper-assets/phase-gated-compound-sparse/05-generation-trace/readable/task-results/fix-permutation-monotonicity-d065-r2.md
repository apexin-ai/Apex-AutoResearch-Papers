# fix permutation monotonicity d065 r2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_permutation_monotonicity_d065_r2_20260515T052825_result.json`
- **Structured JSON:** [`0cb02885721d8bd46644.json`](../../sessions/0c/0cb02885721d8bd46644.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 bug 都已修复，验证通过：

**Bug 1 (permutation statistic)**：
- DeepSeek (n=3 levels): `perm_p=0.1667`（之前 0.165，现在是精确的 1/6）
- Qwen (n=4 levels): `perm_p=0.0417`（精确的 1/24）
- 统计量现在用 concordant consecutive pairs (`sum_gradient_stat` = 2.0 / 3.0)

**Bug 2 (Spearman p=0.0 伪影)**：
- DeepSeek (n=3): `spearman_p=0.1667`（之前 0.0，现在用 exact permutation）
- Qwen (n=4): `spearman_p=0.0417`（之前 0.0，现在用 exact permutation）
- `is_monotonic` 仍正确（全部 True）

---
