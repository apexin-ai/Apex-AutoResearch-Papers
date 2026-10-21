# ssh restart random seed456 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_restart_random_seed456_41312_20260517T211009_result.json`
- **Structured JSON:** [`0b25c71b670bb4f7ee23.json`](../../sessions/0b/0b25c71b670bb4f7ee23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本里没有设 CUDA_VISIBLE_DEVICES，原来是通过 `submit_training_job` 外部设的。需要指定 cuda:3。

汇总结果：

---

**checkpoint_path:** `/root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed456/checkpoint-1000`

**total_steps:** 6103

**remaining_steps:** 5103

**完整重启命令：**

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && export CUDA_VISIBLE_DEVICES=3 && cd /root/provenance_weight_training && python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir /root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed456 \
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
    --seed 456 \
    --save_steps 500 \
    --logging_steps 10 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model \
    --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed456/checkpoint-1000"
```

变更说明（相对原始脚本）：
- 去掉 `--eval_data_path data/human/eval_holdout.jsonl` 和 `--eval_steps 500`
- 添加 `--resume_from_checkpoint checkpoint-1000`
- 添加 `export CUDA_VISIBLE_DEVICES=3`

---
