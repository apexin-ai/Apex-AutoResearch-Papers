# code perlayer kl 50 eval prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_perlayer_kl_50_eval_prep_20260522T031347_result.json`
- **Structured JSON:** [`ec68f4d6ecc7eaf3c444.json`](../../sessions/ec/ec68f4d6ecc7eaf3c444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the full analysis:

---

## 兼容性分析

### 1. `--sparsity_target 0.5` 支持情况
**完全兼容。** `benchmark_eval.py` 的 `--sparsity_target` 默认值就是 `0.5`（L110），没有硬编码限制。

### 2. Checkpoint 格式兼容性
**兼容。** 两边都用 `ckpt["predictors"]` key：
- `train_perlayer_kl.py` L351: `torch.save({"predictors": wrapper.predictors.state_dict(), "args": vars(args)}, ...)`
- `benchmark_eval.py` L171: `wrapper.predictors.load_state_dict(ckpt["predictors"])`

### 3. Checkpoint 文件名
- 中间 checkpoint（save_every=2000）：`predictor_perlayer_kl_step_{N}.pt`
  - 已有：`predictor_perlayer_kl_step_2000.pt`
  - 将生成：`..._step_4000.pt`, `..._step_6000.pt`, `..._step_8000.pt`, `..._step_10000.pt`
- **最终 checkpoint**（L350）：`predictor_perlayer_kl.pt`

路径：`/root/distill_sparse_swiglu/checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt`

### 4. 训练进度
当前 step 2800/10000，每 step ~1.82s。剩余 ~7200 steps ≈ 3.6h，**预计完成时间 ~14:55 UTC**。

### 5. Eval 在 westd-41718 执行
训练和 checkpoint 都在 westd-41718，eval 应该也在这台机器上跑。训练占 cuda:0，训练结束后两张卡都可用。

---

## 最终 Eval 命令

**命令 A — PPL eval (cuda:0)：**
```bash
cd /root/distill_sparse_swiglu && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && \
CUDA_VISIBLE_DEVICES=0 python -u src/benchmark_eval.py \
  --exp_id perlayer_kl_50_s42_ppl \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --checkpoint checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt \
  --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform \
  --tasks wikitext2 --seq_len 2048 --gpu 0
```

**命令 B — Downstream + BoolQ (cuda:1)：**
```bash
cd /root/distill_sparse_swiglu && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && \
CUDA_VISIBLE_DEVICES=1 python -u src/benchmark_eval.py \
  --exp_id perlayer_kl_50_s42_downstream \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --checkpoint checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt \
  --sparsity_mode teal_global --sparsity_target 0.5 --allocation uniform \
  --tasks arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa,boolq \
  --seq_len 2048 --gpu 0
```

注意 `--gpu 0` 是正确的——因为 `CUDA_VISIBLE_DEVICES` 已经限定了物理卡，逻辑上只有 device 0。

---

## 问题清单
**无兼容性问题。** checkpoint key 格式一致，sparsity_target 无限制，bottleneck_size 默认 128 与训练一致。命令可直接使用。

---
