# fix grid b seed456 remove eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_grid_b_seed456_remove_eval_20260514T172004_result.json`
- **Structured JSON:** [`bbed2989e0b9f2111045.json`](../../sessions/bb/bbed2989e0b9f2111045.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`--eval_data_path` 和 `--eval_steps` 两行已移除。

修改后的 seed456 与 seed42 对比，除 seed 值外还有以下差异（均为 seed456 已有的，非本次引入）：

| 参数 | seed456 | seed42 |
|------|---------|--------|
| `WANDB_MODE=disabled` | 有 | 无 |
| `--save_total_limit` | 3 | 2 |
| `--bf16` | 有 | 无 |
| `--eval_steps` | 已移除 | 仍有（但无 eval_data_path，不触发 eval） |

这些差异不在本次修改范围内。inline eval 的根源（`--eval_data_path`）已移除，不会再触发 44min/次的 eval 开销。

---
