# code rollback cond2 d004

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rollback_cond2_d004_20260515T232638_result.json`
- **Structured JSON:** [`85d6d829a7034d124221.json`](../../sessions/85/85d6d829a7034d124221.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

回滚完成。修改内容：

- **Condition 2**：从检查 `abs_rhos`（|ρ| 退化）恢复为检查 `means_valid`（signal mean 退化），通过 `mean_key = f"{sig_name}_mean"` 从 `aggregated` 字段读取每代的 entropy_mean / spectral_rank_mean
- **打印标签**：`cond2_abs_rho_decay` → `cond2_mean_decay`

脚本运行正常。当前只有 gen0/gen1 两代数据，判定结果均为 FAIL（符合预期——实验尚未产生足够代数的退化信号）。

---
