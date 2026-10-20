# ssh restart prep 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_restart_prep_41312_20260517T205609_result.json`
- **Structured JSON:** [`ac55a4fb6a9c8a4259ec.json`](../../sessions/ac/ac55a4fb6a9c8a4259ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是结果：

---

## 实验 1: ess_only_seed123

```
checkpoint_path: /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123/checkpoint-2000
total_steps: 6103
current_step: 2000 (实际训练到 ~2987 被 kill，但你指定从 2000 恢复)
remaining_steps: 4103
```

**重启命令（无 inline eval）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export WANDB_MODE=disabled
cd /root/provenance_weight_training

CUDA_VISIBLE_DEVICES=2 python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method ess_only \
    --contamination_ratio 0.4 \
    --n_min 2 \
    --tau 0.8 \
    --max_steps 6103 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 123 \
    --save_steps 500 \
    --logging_steps 10 \
    --warmup_ratio 0.05 \
    --weight_decay 0.01 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model \
    --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123/checkpoint-2000
```

---

## 实验 2: ess_only_seed456

```
checkpoint_path: /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456/checkpoint-2500
total_steps: 6103
current_step: 2500
remaining_steps: 3603
```

**重启命令（无 inline eval）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export WANDB_MODE=disabled
cd /root/provenance_weight_training

CUDA_VISIBLE_DEVICES=1 python training/pretrain_weighted.py \
    --data_path data/scored_data.jsonl \
    --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456 \
    --model_name models/Qwen/Qwen3-0.6B \
    --weighting_method ess_only \
    --contamination_ratio 0.4 \
    --n_min 2 \
    --tau 0.8 \
    --max_steps 6103 \
    --batch_size 4 \
    --gradient_accumulation_steps 4 \
    --learning_rate 5e-5 \
    --max_length 2048 \
    --seed 456 \
    --save_steps 500 \
    --logging_steps 10 \
    --warmup_ratio 0.05 \
    --weight_decay 0.01 \
    --bf16 \
    --save_total_limit 3 \
    --save_only_model \
    --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456/checkpoint-2500
```

---

## 注意事项

**`save_only_model=True` 导致 checkpoint 中无 optimizer 状态**（无 `optimizer.pt`、`scheduler.pt`、`rng_state.pth`）。resume 时：
- 模型权重正常恢复
- step 计数器和 LR scheduler 从 `trainer_state.json` 恢复（LR 会 fast-forward 到正确位置）
- **optimizer 动量（Adam beta1/beta2 累积）会丢失**，从零重新积累
- 数据迭代顺序会 skip 已训练的 steps

这在实践中通常影响不大，但前几百步 loss 可能有轻微波动。

**已删除的参数**：`--eval_data_path`（原来指向 `data/human/eval_holdout.jsonl`）和对应的 eval 逻辑（脚本中 `eval_data_path=None` 时自动 `eval_strategy="no"`）。

---
