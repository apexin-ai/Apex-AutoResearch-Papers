# code bce isocompute v3 s123 prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bce_isocompute_v3_s123_prep_20260517T200454_result.json`
- **Structured JSON:** [`df12e2dd079d47add510.json`](../../sessions/df/df12e2dd079d47add510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## s123 就绪状态汇报

**环境检查：**

| 项目 | 状态 |
|------|------|
| 模型 `/root/autodl-tmp/models/llama-3.1-8b` | ✅ 存在 |
| 训练脚本 `src/train.py` | ✅ 存在 (May 17 更新) |
| 数据集 wikitext-103 | ✅ 已缓存 (`/root/autodl-tmp/.hf_cache/datasets/wikitext`) |
| 磁盘空间 | ✅ checkpoint ~145MB，overlay 剩余 5.9G 足够 |
| Registry | ✅ PREPARING，hypothesis 已更新 |
| Dry-run | ⏭ 跳过 — cuda:0 跑 qwen14b eval，cuda:1 跑 s456 eval，两卡都占满 |

**完整训练命令**（GPU 编号按空闲情况调整 `CUDA_VISIBLE_DEVICES`）：

```bash
cd /root/distill_sparse_swiglu && export WANDB_MODE=disabled && \
CUDA_VISIBLE_DEVICES=<空闲GPU> /root/miniconda3/bin/python -u src/train.py \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --loss_type bce --num_steps 2700 --batch_size 4 --seq_len 2048 \
  --lr 1e-3 --seed 123 --sparsity_target 0.5 --gpu 0 \
  --output_dir checkpoints/bce_isocompute_v3_s123 \
  --wandb_run_name bce_isocompute_v3_s123 \
  --dataset wikitext-103 --gradient_checkpointing --log_every 100
```

与 s456 命令完全一致，仅 seed 和路径名不同。

**预估训练时间：~49 min**（s456 实测 2957s ≈ 49.3 min）

---
