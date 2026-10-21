# ops prepare spon submission

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_spon_submission_20260515T172731_result.json`
- **Structured JSON:** [`4d95518c31df4f7d318a.json`](../../sessions/4d/4d95518c31df4f7d318a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已确认。以下是完整的 `submit_training_job` 命令：

```
bash -c "source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train_spon.py \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --predictor_checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \
  --num_steps 1000 \
  --batch_size 8 \
  --seq_len 128 \
  --lr 1e-5 \
  --seed 42 \
  --sparsity_target 0.5 \
  --gpu 0 \
  --output_dir /root/distill_sparse_swiglu/checkpoints/spon_kl_s42 \
  --warmup_steps 100 \
  --log_every 100 \
  --dataset wikitext-103 \
  --gradient_checkpointing"
```

**参数说明：**

| 参数 | 值 | 来源 |
|------|-----|------|
| `--model_name_or_path` | `/root/autodl-tmp/models/llama-3.1-8b` | 脚本默认值 |
| `--predictor_checkpoint` | `.../mvp_kl_norm_v2_s42/predictor_kl_normalized.pt` | 已确认存在（145MB） |
| `--num_steps` | 1000 | 脚本默认值 |
| `--batch_size` | 8 | 脚本默认值 |
| `--lr` | 1e-5 | 脚本默认值 |
| `--sparsity_target` | 0.5 | 脚本默认值 |
| `--gpu` | 0 | 约束 C001，使用 cuda:0 |
| `--output_dir` | `.../checkpoints/spon_kl_s42` | 按命名规范 |
| `--gradient_checkpointing` | 开启 | 8B 模型省显存 |
| `WANDB_MODE=disabled` | - | 按要求禁用 wandb |

没有找到之前 SPON dry-run 的日志（runs 目录里只有 predictor 训练记录），所有参数均取脚本默认值 + 任务要求的覆盖值。

---
