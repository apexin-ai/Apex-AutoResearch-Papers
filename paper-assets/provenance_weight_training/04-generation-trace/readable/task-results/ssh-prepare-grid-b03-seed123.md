# ssh prepare grid b03 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare_grid_b03_seed123_20260517T030843_result.json`
- **Structured JSON:** [`4c29e54ce7e6c2404118.json`](../../sessions/4c/4c29e54ce7e6c2404118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 确认 `--weighting_method` 和 `--grid_b_value` 参数均存在。

**产出：**
- 脚本路径：`/root/provenance_weight_training/scripts/run_grid_b0_3_seed123.sh`
- Dry-run：`--weighting_method {uniform,grid,adaptive,golden_ratio,ess_only,random}` 和 `--grid_b_value GRID_B_VALUE` 均已确认可用
- 脚本已 `chmod +x`，无 `CUDA_VISIBLE_DEVICES`，无 `--eval_data_path` / `--eval_steps`

---
