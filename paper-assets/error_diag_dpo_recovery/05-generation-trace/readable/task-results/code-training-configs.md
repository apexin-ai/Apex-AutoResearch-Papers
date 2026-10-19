# code training configs

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training-configs_20260512T135451_result.json`
- **Structured JSON:** [`6f6ce2209964a394f848.json`](../../sessions/6f/6f6ce2209964a394f848.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。创建的文件：

| 文件 | 说明 |
|------|------|
| `configs/experiment_matrix.yaml` | 7-run 实验矩阵定义 + 4 轮调度计划 |
| `scripts/run_experiment.sh` | 单实验启动脚本 |
| `scripts/run_all_experiments.sh` | 全量调度脚本（2 卡并行，4 轮） |
| `outputs/` | 空输出目录 |

语法检查均通过。

**相对原始模板的参数修正**（基于 `train_etadn.py` 实际 CLI）：
- `--gamma` → `--global_gamma`（DMPO 用）
- `--learning_rate` → `--lr`
- `--num_train_epochs` → `--epochs`
- `--per_device_train_batch_size` → `--batch_size`
- `--gradient_accumulation_steps` → `--gradient_accumulation`
- 移除不存在的 `--gamma_map_json`/`--max_prompt_length`/`--save_strategy`/`--report_to`/`--run_name`/`--bf16`
- 添加 `--gpu` 参数与 `CUDA_VISIBLE_DEVICES` 保持一致
- `gamma_map` 无需传参 — `DEFAULT_GAMMA_MAP` 已硬编码为 `{action: 0.85, verification: 0.92, planning: 0.97}`，与需求一致

---
