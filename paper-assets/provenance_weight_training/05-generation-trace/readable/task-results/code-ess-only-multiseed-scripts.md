# code ess only multiseed scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ess_only_multiseed_scripts_20260515T123855_result.json`
- **Structured JSON:** [`6587c1b404d578e57651.json`](../../sessions/65/6587c1b404d578e57651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 产出汇总

### run_ess_only_seed123.sh
```bash
#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/provenance_weight_training

WANDB_MODE=disabled python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir output/models/ess_only_seed123 \
    --weighting_method ess_only \
    --model_name models/Qwen/Qwen3-0.6B \
    --num_train_tokens 200000000 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --max_length 2048 \
    --learning_rate 5e-5 \
    --seed 123 \
    --logging_steps 10 \
    --save_steps 500 \
    --save_total_limit 2 \
    --save_only_model \
    --contamination_ratio 0.4 \
    --tau 0.8 \
    --bf16
```

### run_ess_only_seed456.sh
同上，`seed123` → `seed456`，`--seed 123` → `--seed 456`。

### diff 验证
- 两个脚本仅 `--output_dir`、`--seed`、echo 消息不同
- **无 `--eval_data_path` 或 `--eval_steps`**（已从 seed42 模板中移除）

### 提交命令模板
```bash
# seed123
nohup bash /root/provenance_weight_training/training/run_ess_only_seed123.sh > /root/provenance_weight_training/output/logs/ess_only_seed123.log 2>&1 &

# seed456
nohup bash /root/provenance_weight_training/training/run_ess_only_seed456.sh > /root/provenance_weight_training/output/logs/ess_only_seed456.log 2>&1 &
```

脚本已就绪，τ sweep 完成后可直接提交。

---
