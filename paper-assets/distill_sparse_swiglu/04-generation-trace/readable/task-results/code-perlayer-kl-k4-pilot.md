# code perlayer kl k4 pilot

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_perlayer_kl_k4_pilot_20260522T095949_result.json`
- **Structured JSON:** [`f40bb5634b7c8d8ea568.json`](../../sessions/f4/f40bb5634b7c8d8ea568.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=4 Per-layer KL Pilot — 启动成功

### 修改内容
新文件 `src/train_perlayer_kl_k4.py`（363 行，从 `train_perlayer_kl.py` 派生），关键改动：

1. **CLI**: 新增 `--num_masked_layers` (默认 K=4)
2. **`patch_perlayer_masking`**: `wrapper._active_layer`(单 int) → `wrapper._active_layers`(set), `should_mask` 判定改为 `li in active_layers`
3. **训练循环**: `random.randint(0, n-1)` → `random.sample(range(n), K)`；K 层同时 mask
4. **Sparsity constraint**: 对 K 个 active layer 各算一份 lambda·clamp(|sp-target|-margin,0)² 并求和参与反传
5. **Lagrangian update**: 每个 active layer 用自己当步的 sparsity 独立更新 lambda
6. **Checkpoint 命名**: `predictor_perlayer_kl_k4_step_*.pt` / `predictor_perlayer_kl_k4.pt`（避免覆盖 K=1）
7. **wandb run_name**: 默认 `perlayer_kl_k{K}_s{sp}_seed{s}`

其他保持与 K=1 一致：tau 1.0→0.1, warmup 100, lr 1e-3, lambda_max 5000, margin 0.02, batch_size 4, seq_len 2048。

### 启动命令
```bash
cd /root/distill_sparse_swiglu && nohup env CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache WANDB_MODE=offline \
  /root/miniconda3/bin/python -u src/train_perlayer_kl_k4.py \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dataset wikitext-103 \
  --seq_len 2048 --num_steps 2700 --lr 1e-3 --seed 42 --sparsity_target 0.3 \
  --num_masked_layers 4 --output_dir checkpoints/perlayer_kl_k4_s42 --gpu 0 \
  --gradient_checkpointing --save_every 500 --wandb_run_name perlayer_kl_k4_s42 \
  > logs/perlayer_kl_k4_s42.log 2>&1 &
```

注意：用户原命令中的 `--dataset_name wikitext2`/`--data_path` 不是脚本参数，已映射为 `--dataset wikitext-103`（与 K=1 baseline 一致）和 `HF_HOME` 环境变量。首次启动因 wandb 未登录崩溃，已加 `WANDB_MODE=offline` 重启成功。

### 运行状态
- **Python PID**: 42941（bash wrapper 42940）
- **GPU**: cuda:1 = 100% 利用率, 36.7 GB / 97.9 GB（cuda:0 qwen14b eval 未受影响）
- **日志**: `/root/distill_sparse_swiglu/logs/perlayer_kl_k4_s42.log`
- **Step 1**: `layers=[1,7,15,17] kl=0.1191 avg_sp=0.406 avg_lambda=0.50 tau=1.000 lr=1.00e-05 dt=2.2s` — K=4 层正确同时 mask，KL 数量级合理（K=1 baseline 起步 kl=0.0203，K=4 起步更高是预期：4 层同时 mask 引入更大扰动）
- **Lagrangian**: 四层 lambda 从 1.0 → 0.5（初始 sparsity 0.406 > target 0.3 + margin 0.02，按规则减半，正常）

Checkpoint 每 500 step 保存到 `checkpoints/perlayer_kl_k4_s42/`。

---
