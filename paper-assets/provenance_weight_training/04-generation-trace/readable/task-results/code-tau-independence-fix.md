# code tau independence fix

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tau_independence_fix_20260515T070927_result.json`
- **Structured JSON:** [`6a001d2b73e0e602a9cc.json`](../../sessions/6a/6a001d2b73e0e602a9cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改了 `training/pretrain_weighted.py` 的 3 处：

| 位置 | 修改前 | 修改后 |
|------|--------|--------|
| L235-236 `--tau` 参数 | `default=None`, help 引用 contamination_ratio | `default=0.8`, help 说明固定超参 |
| L219-220 `--contamination_ratio` help | "for adaptive tau" | "data generation only" |
| L278-279 `main()` | `tau = 1.0 - contamination_ratio * 0.5` | 已删除 |

`contamination_ratio` 现在仅出现在 argparse 定义和 config_summary 记录中，训练逻辑中不再引用。Changelog 已写入 `artifacts/tau_fix_changelog.md`。

---
