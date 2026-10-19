# ssh prepare v73 eval pipeline

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare_v73_eval_pipeline_20260518T010927_result.json`
- **Structured JSON:** [`3b4834b8641171b32bc5.json`](../../sessions/3b/3b4834b8641171b32bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### 1. cross_task_probe.py 完整参数

```
--checkpoint_dir CHECKPOINT_DIR   (必选)
--base_model BASE_MODEL
--dataset_id DATASET_ID
--data_root DATA_ROOT
--output_dir OUTPUT_DIR           (必选)
--device DEVICE
--n_unique_tasks N_UNIQUE_TASKS
--max_pool_batches MAX_POOL_BATCHES
```

### 2. eval_acib.py 关键参数名

| 用途 | 参数名 |
|------|--------|
| checkpoint 路径 | `--checkpoint_dir` (必选) |
| 指定 step | `--checkpoint_step` (默认 latest) |
| alpha | `--scoring_alpha` |
| suites | `--suites` (多值) |
| GPU | `--gpu` |
| episodes | `--n_episodes` |
| 输出 | `--out_dir` (必选) |
| 其他 | `--disable_scoring`, `--drop_mode`, `--drop_ratio` |

freeze_mode **不是** eval 参数，从 checkpoint 的 config.json 自动读取。

### 3. checkpoint config 确认

`config.json` 中 `freeze_mode: "connector_lora"`, `lora_rank: 8`, `lora_scale: 1.0`。当前有 checkpoint-5000 和 checkpoint-10000（各含 `checkpoint.pt`），checkpoint-20000 尚未生成。

### 4. 三个脚本（已创建且 chmod +x）

- `/root/acib/run_v73_probe.sh`
- `/root/acib/run_v73_eval_alpha00_spatial.sh`
- `/root/acib/run_v73_eval_alpha10_full.sh`

内容已逐字验证，与上方 cat 输出一致。

### 5. LoRA 训练进度

**Step 14500/20000**（72.5%），1.8 steps/s。预计剩余 ~51 min 完成。

---
