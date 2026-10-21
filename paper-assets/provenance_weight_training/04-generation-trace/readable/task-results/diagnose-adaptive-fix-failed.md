# diagnose adaptive fix failed

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_adaptive_fix_failed_20260514T173948_result.json`
- **Structured JSON:** [`64504669c3c9bda168c5.json`](../../sessions/64/64504669c3c9bda168c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根本原因**：`--overwrite_output_dir` 参数不被 `pretrain_weighted.py` 支持。

日志明确显示：
```
pretrain_weighted.py: error: unrecognized arguments: --overwrite_output_dir
EXIT_CODE=2
```

grep 确认脚本中没有定义 `overwrite_output_dir` 参数。三个实验失败原因相同。

**修复方案**：删除 `--overwrite_output_dir` 参数即可。修正后的命令（以 seed42 为例）：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_fix_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model"
```

如果需要覆盖已有输出目录的功能，需要在 `pretrain_weighted.py` 的 argparse 中添加 `--overwrite_output_dir` 参数定义，或者在运行前手动清除目标目录。

---
