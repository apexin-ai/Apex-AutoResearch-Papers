# code grid b low scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grid_b_low_scripts_20260514T235854_result.json`
- **Structured JSON:** [`dc4b4e313cb9b2025036.json`](../../sessions/dc/dc4b4e313cb9b2025036.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出

| 脚本 | 路径 |
|------|------|
| 训练 seed42 | `/root/provenance_weight_training/run_grid_b_low_seed42.sh` |
| 训练 seed123 | `/root/provenance_weight_training/run_grid_b_low_seed123.sh` |
| 训练 seed456 | `/root/provenance_weight_training/run_grid_b_low_seed456.sh` |
| Post-hoc eval | `/root/provenance_weight_training/run_posthoc_eval_grid_b_low.sh` |

### 验证结果
- **语法检查**: 4 个脚本全部 PASS
- **目录冲突**: 现有 models 目录无 `grid_b0_1/0_2/0_3` 相关目录，无冲突

### 时间预估
- 每个 b 值 ~3.6h → 每个 seed 脚本 3 个 b 值串行 ≈ **10.8h**
- 3 个 seed 如果串行跑 ≈ 32.4h；并行跑（3 个 nohup）≈ 10.8h
- Post-hoc eval 9 个 checkpoint ≈ 30-45min

---
