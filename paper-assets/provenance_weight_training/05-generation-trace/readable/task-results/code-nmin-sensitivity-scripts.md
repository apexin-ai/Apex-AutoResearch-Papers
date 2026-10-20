# code nmin sensitivity scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nmin_sensitivity_scripts_20260515T011949_result.json`
- **Structured JSON:** [`655ace8710722dd72922.json`](../../sessions/65/655ace8710722dd72922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本已创建完成：

| 脚本 | n_min | output_dir |
|------|-------|------------|
| `run_nmin1_seed42.sh` | 1 | `output/models/nmin1_seed42` |
| `run_nmin4_seed42.sh` | 4 | `output/models/nmin4_seed42` |
| `run_nmin5_seed42.sh` | 5 | `output/models/nmin5_seed42` |

`pretrain_weighted.py` 已原生支持 `--n_min` 参数（L238），无需修改代码。所有脚本已设为可执行。

---
