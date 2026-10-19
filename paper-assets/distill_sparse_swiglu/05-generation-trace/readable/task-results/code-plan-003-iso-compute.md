# code plan 003 iso compute

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003_iso_compute_20260515T185324_result.json`
- **Structured JSON:** [`014c55437f66eb740393.json`](../../sessions/01/014c55437f66eb740393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. FLOPs 比率估算

**实测结果** (BS=1, SL=512, GPU=RTX PRO 6000 Blackwell):

| | 每步时间 | 相对 FLOPs |
|---|---|---|
| KL (dense fwd + sparse fwd + backward w/ GC) | 0.549s | 2.71x |
| BCE (dense fwd + predictor fwd/bwd) | 0.202s | 1.0x |

**比率 R = 2.71**

KL 每步需要：1次 dense forward (no grad) + 1次 sparse forward (grad) + backward (activation gradients through frozen model, with gradient checkpointing)。BCE 每步只需：1次 dense forward (no grad) + 32个 tiny predictor forward/backward (~0.9% model FLOPs)。

**ISO-compute BCE steps = 1000 × 2.71 ≈ 2700 步**

### 2. 代码修改

对 `src/train.py` 添加了 4 处改动（原文件已备份为 `train.py.bak`）：

- **L17**: `import time`
- **L415**: `t0 = time.time()` — BCE 循环前
- **L468-472**: `elapsed` 计算 + `wall_time`/`step_time` 写入 wandb
- **L481-485**: print 添加 elapsed + 训练完成后打印总时间

无需新建脚本，`--num_steps` 参数已存在。

### 3. Dry-run 验证

通过 (BS=1, SL=512, random data, 1 step):
```
[Step 1/1] loss=0.6941 bce=0.6938 reg=0.0002 sparsity=0.500 lr=1.00e-05 elapsed=0.8s (0.78s/step)
BCE training complete: 1 steps in 0.8s (0.78s/step)
```

### 4. 启动命令

GPU 空闲时执行（当前两张卡都被占满 ~73-75/98 GiB）：

```bash
source /root/distill_sparse_swiglu/setup_env.sh && cd /root/distill_sparse_swiglu && \
CUDA_VISIBLE_DEVICES=0 python src/train.py \
    --loss_type bce \
    --num_steps 2700 \
    --warmup_steps 100 \
    --batch_size 4 \
    --seq_len 2048 \
    --lr 1e-3 \
    --seed 42 \
    --sparsity_target 0.5 \
    --dataset wikitext-103 \
    --gpu 0 \
    --output_dir checkpoints/bce_isocompute_s42 \
    --wandb_run_name bce_isocompute_2700steps_s42
```

如果 OOM，可改为 `--batch_size 2 --gradient_accumulation_steps 2`（等效 BS=4）。

---
