# ops lambda01 eval check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lambda01_eval_check_20260526T040417_result.json`
- **Structured JSON:** [`3e5de984d0730e3c28a7.json`](../../sessions/3e/3e5de984d0730e3c28a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论如下：

## 检查结果

### 1. eval 脚本（当前版本）已默认记录所有所需指标

| 指标 | per-episode 字段 | task 汇总字段 | 状态 |
|------|-----------------|-------------|------|
| EE displacement | `max_ee_displacement` (L1062) | `avg_max_ee_displacement` (L1116) | ✅ 已有 |
| 障碍物位移 | `max_displacement` (L1061) | `avg_max_displacement` (L1115) | ✅ 已有 |
| TSR | — | `TSR` (L1112) | ✅ 已有 |
| CAR | — | `CAR` | ✅ 已有 |
| dfCAR | 可从 per-episode `max_displacement` + threshold 计算 | — | ✅ 数据充分 |

### 2. `--output_path` 参数

**非必须。** 不传时脚本会自动根据 `--save_dir`（默认 `/root/autodl-tmp/eval_results`）+ checkpoint名/suite/seed 等拼出保存路径。`--output_path` 只是允许覆盖自动命名。

### 3. 新旧 JSON 差异

- **旧版 JSON**（如 `eval_s0_l01_30k_final.json`）：per-episode **没有** `max_ee_displacement` 和 `total_ee_path_length` 字段
- **新版 JSON**（如 `eval_s0_l01_30k_disp.json`、`eval_s0_l005_30k_r4.json` 等 5 个文件）：per-episode **包含** `max_ee_displacement` 和 `total_ee_path_length`，task 汇总包含 `avg_max_ee_displacement`

### 4. 结论

当前版本的 `eval_safelibero.py` 运行 eval 时，**无需额外参数**即可自动输出完整的 EE displacement 分布（per-episode `max_ee_displacement`）、`avg_max_ee_displacement`、`TSR`。dfCAR@100mm 可从 per-episode 的 `max_displacement` 数据按阈值统计得出。

λ=0.1 训练完成后直接用标准 eval 命令即可：
```
python scripts/eval_safelibero.py --checkpoint &lt;PATH> --config_name pi05_libero --suite safelibero_object --model_type lora_baseline --pi05 --seed 0 --gpu N
```
不需要加 `--output_path`，结果会自动保存到 `/root/autodl-tmp/eval_results/`，且包含全部指标。

---
