# fix mvp kl oom

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mvp_kl_oom_20260515T122135_result.json`
- **Structured JSON:** [`e47e7a8572f762074ba3.json`](../../sessions/e4/e47e7a8572f762074ba3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **模型加载**: 16.9 GB
- **训练步峰值显存 (bs=2, seq=2048)**: 29.5 GB（从之前的 ~88 GB 降到 29.5 GB）
- **Loss**: 2976.00（随机数据，KL 值合理，不是 NaN/inf）
- **无 OOM**

显存从 88GB → 29.5GB，95GB 显卡绰绰有余。

### 修改总结

**文件**: `/root/distill_sparse_swiglu/src/train.py`

| 位置 | 改动 |
|------|------|
| L5-7 (header) | 新增 KL + grad_accum 用法示例 |
| L54-55 (parse_args) | 新增 `--gradient_checkpointing` 参数 |
| L84-92 (train_kl) | 循环前启用 `model.train()` + `gradient_checkpointing_enable(use_reentrant=False)` |
| L266-268 (main) | KL 模式自动开启 gradient checkpointing |

`train_bce()` 未改动。

### Dry-run 显存

| 指标 | 修复前 (估算) | 修复后 (实测) |
|------|-------------|-------------|
| 训练步峰值 | ~88 GB (OOM) | 29.5 GB |
| 安全余量 | -| ~65 GB |

### 建议的生产命令

```bash
CUDA_VISIBLE_DEVICES=0 python src/train.py \
    --loss_type kl \
    --num_steps 1000 \
    --batch_size 2 \
    --gradient_accumulation_steps 2 \
    --seq_len 2048 \
    --gpu 0 \
    --wandb_run_name mvp_kl_s42
```

有效 batch size = 2 × 2 = 4，与原始设置一致。显存 29.5 GB，远低于 95 GB 上限。

---
