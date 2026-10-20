# ssh prepare random reweight seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare_random_reweight_seed123_20260517T081401_result.json`
- **Structured JSON:** [`0632e5ee5954cb6f2f2d.json`](../../sessions/06/0632e5ee5954cb6f2f2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过全部验证：

| 检查项 | 结果 |
|--------|------|
| eval_steps / eval_data_path | **CLEAN** |
| CUDA_VISIBLE_DEVICES 硬编码 | **CLEAN** |
| seed | **123 confirmed**（第24行 `--seed 123`） |

**完整脚本** `/root/provenance_weight_training/scripts/run_random_reweight_seed123.sh`：

```bash
#!/bin/bash
# Random reweighting baseline (seed=123)
# Purpose: Ablation proving detector signal is load-bearing.
# Weights drawn from U(0,2), normalized to mean=1 per batch.
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export WANDB_MODE=disabled
cd /root/provenance_weight_training

python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir /root/autodl-tmp/output/models/random_reweight_seed123 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method random \
    --contamination_ratio 0.4 \
    --tau 0.8 \
    --n_min 2 \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 123 \
    --save_steps 500 \
    --logging_steps 10 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model

echo "DONE: random_reweight seed123"
```

与模板的差异：移除 `--eval_steps 500`、`--eval_data_path`、`CUDA_VISIBLE_DEVICES=0`；seed 42→123；output_dir 改为 `random_reweight_seed123`。

---
