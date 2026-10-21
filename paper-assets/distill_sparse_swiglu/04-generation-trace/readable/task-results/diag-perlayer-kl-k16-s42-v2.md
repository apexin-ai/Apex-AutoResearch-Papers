# diag perlayer kl k16 s42 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_perlayer_kl_k16_s42_v2_20260523T040658_result.json`
- **Structured JSON:** [`21681ca78f4b83eca509.json`](../../sessions/21/21681ca78f4b83eca509.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因

**wandb 未登录。** 崩溃发生在 `train_perlayer_kl_k4.py:314` 的 `wandb.init()` 调用——服务器上没有 `~/.netrc` 也没有 `WANDB_API_KEY` 环境变量。

与 K=16 无关，与 argparse 无关。K=8 成功是因为当时 wandb session 还有效，现在已失效。

### 修复方案

两种方式任选其一：

**方案 A（推荐）：启动时设环境变量**
```bash
WANDB_API_KEY=[REDACTED] nohup python src/train_perlayer_kl_k4.py \
  --num_masked_layers 16 --num_steps 1000 --seed 42 --gpu 0 \
  --gradient_checkpointing \
  --wandb_run_name perlayer_kl_k16_s42_v3 \
  > ~/runs/distill_sparse_swiglu/perlayer_kl_k16_s42_v3.log 2>&1 &
```

**方案 B：先 wandb login 持久化**
```bash
wandb login &lt;your_key>
# 然后正常启动训练
```

**方案 C（临时跑通不记录）：** 在脚本 `wandb.init()` 前加 `wandb.init(mode="offline", ...)`，或设 `WANDB_MODE=offline`。

### 修复后的训练命令

```bash
cd /root/distill_sparse_swiglu
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
WANDB_API_KEY=[REDACTED] nohup python src/train_perlayer_kl_k4.py \
  --num_masked_layers 16 \
  --num_steps 1000 \
  --sparsity_target 0.3 \
  --seed 42 \
  --gpu 0 \
  --gradient_checkpointing \
  --wandb_run_name perlayer_kl_k16_s42_v3 \
  --output_dir /root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s42 \
  > ~/runs/distill_sparse_swiglu/perlayer_kl_k16_s42_v3.log 2>&1 &
```

脚本本身对 `--num_masked_layers` 无范围限制，K=16 在逻辑上完全合法（32 层中选 16 层）。

---
