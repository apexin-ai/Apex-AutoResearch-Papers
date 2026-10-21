# extract cwm8b resume command

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_cwm8b-resume-command_20260515T175224_result.json`
- **Structured JSON:** [`f22caa5d6beae888f606.json`](../../sessions/f2/f22caa5d6beae888f606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已齐全。以下是汇总和 resume 命令。

## 训练状态摘要

| 字段 | 值 |
|------|-----|
| 崩溃原因 | timeout (EXIT_CODE=124)，v2 日志在 step 5273 中断 |
| checkpoint | step 5200, epoch 2.35 |
| max_steps | 6633 (3 epochs) |
| 剩余 steps | ~1433 (约 22%) |
| total_flos | 8.008e+18 |
| best_model_checkpoint | checkpoint-400 (eval_loss=0.2862) |
| 当前 eval_loss | 0.5066 (step 5200，已过拟合) |

## 参数溯源

从 `training_args.bin` + `adapter_config.json` 提取，匹配 `train_repo_cwm_8b.py` 的 argparse：

- model: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- output_dir: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/`
- batch_size=1, grad_accumulation=32, lr=5e-5, epochs=3, seed=42
- warmup_ratio=0.05, weight_decay=0.01
- lora_rank=16, lora_alpha=32, lora_dropout=0.05
- save_steps=100, eval_steps=100
- bf16=True, gradient_checkpointing=True
- no_wandb, device=cuda:0
- run_name: `repo-cwm-qwen3-4b-lora` (名称遗留，实际是 8B)

## Resume 命令

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python train_repo_cwm_8b.py \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --data_dir /home/sonny/exec-sim-repair-verifier/data/swebench_full \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/ \
  --run_name repo-cwm-qwen3-4b-lora \
  --seed 42 \
  --max_seq_length 2048 \
  --batch_size 1 \
  --grad_accumulation 32 \
  --lr 5e-5 \
  --epochs 3 \
  --warmup_ratio 0.05 \
  --weight_decay 0.01 \
  --lora_rank 16 \
  --lora_alpha 32 \
  --lora_dropout 0.05 \
  --save_steps 100 \
  --eval_steps 100 \
  --no_wandb \
  --device cuda:0 \
  --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-5200"
```

**注意**: eval_loss 从 step 400 (0.286) 持续上升到 step 5200 (0.507)，严重过拟合。best_model_checkpoint 停在 checkpoint-400。resume 完成后 Trainer 会因 `load_best_model_at_end=True` 加载 checkpoint-400，但如果 checkpoint-400 已被 `save_total_limit=5` 清理掉则会报错。建议确认 checkpoint-400 是否仍存在。

---
