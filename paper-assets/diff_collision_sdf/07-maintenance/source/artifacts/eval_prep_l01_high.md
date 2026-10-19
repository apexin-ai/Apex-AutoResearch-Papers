# Eval 预检报告: λ=0.1 (high) + LoRA baseline s2

**日期**: 2026-05-26

---

## 1. 检查结果摘要

### westd-35807

| 项目 | 状态 |
|------|------|
| Conda 环境 | `libero` (`/root/miniconda3/envs/libero`) |
| Rotation fix | ✅ 存在 (eval_safelibero.py L841, L843: `[::-1, ::-1]`) |
| GPU 状态 | 4x RTX PRO 6000, 全部 100% 占用 (~27GB/97GB each), 正在跑 eval |
| λ=0.1 s0 ckpt | ✅ `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/30000` (含 model.safetensors, sdf_decoder.pt, ee_extractor.pt) |
| λ=0.1 s1 ckpt | ✅ `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l1/30000` (同上) |

**已完成的 eval (westd-35807, seed=0):**
- `eval_s0_l01_30k_final.json` (May 26 03:19) — s0 λ=0.1
- `eval_s0_l01_30k_disp.json` (May 26 05:15) — s0 λ=0.1 (含 displacement)
- `eval_s2_l01_30k_v3.json` (May 25 23:52) — s2 λ=0.1

**s1 λ=0.1 eval 缺失**: eval_30k_s1_l01.log 在 ep 114/200 处中断 (May 25 17:48)，无结果 JSON。

### westd-45947

| 项目 | 状态 |
|------|------|
| Conda 环境 | base conda (`/root/miniconda3/bin/python`), 无命名环境 |
| Rotation fix | ✅ 存在 (2 matches) |
| GPU 状态 | 2x RTX PRO 6000, 全部 100% 占用 (~27GB each), 正在跑 reeval batch |
| LoRA baseline s2 ckpt | ⚠️ **仅到 18000** (`16000/18000/best`), 未达 30000 |
| λ=0.1 s2 ckpt | ✅ `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l1/30000` |
| LoRA baseline s0 ckpt | ✅ `pi05_lora_baseline_object_pudding_seed0/30000` (刚完成) |
| LoRA baseline s1 ckpt | ✅ `pi05_lora_baseline_object_pudding_seed1/30000` (刚完成) |

**已完成的 reeval (westd-45947, seed=7):**
- `reeval_sdf_s0_l01_30k.json` (May 26 17:03) — s0 λ=0.1
- `reeval_sdf_s0_l005_30k.json` (May 26 18:20) — s0 λ=0.05
- `reeval_sdf_s1_l005_30k.json` (May 26 20:45) — s1 λ=0.05
- `reeval_sdf_s1_l01_30k.json` (May 26 21:58) — s1 λ=0.1
- `reeval_sdf_s2_l005_30k.json` (May 26 21:21) — s2 λ=0.05
- `reeval_sdf_s2_l01_30k.json` (May 26 22:35) — s2 λ=0.1
- `reeval_lora_s1_30k.json` (May 26 17:42) — s1 LoRA baseline
- `eval_lora_baseline_s0.json` (May 26 10:25, seed=0) — s0 LoRA baseline
- `eval_lora_baseline_s1.json` (May 26 10:26, seed=0) — s1 LoRA baseline

---

## 2. 阻碍 Eval 的问题

### ⚠️ LoRA baseline s2 checkpoint 未到 30000

- 当前最新: step 18000 (best_loss=0.0096)
- 两台服务器上均无 `pi05_lora_baseline_object_pudding_seed2/30000`
- westd-45947 两个 GPU 正在跑 reeval，LoRA baseline s2 **未在训练中**
- **需要恢复训练** 从 18000 继续到 30000 后才能 eval

### ⚠️ westd-35807 s1 λ=0.1 eval 缺失

- 之前的 eval 在 ep 114/200 处中断
- westd-45947 上已有 reeval_sdf_s1_l01_30k.json (seed=7)，可直接使用
- 如需 westd-35807 独立结果，需要重跑

### 注意: seed 不一致

- westd-35807 已有 eval 使用 **seed=0**
- westd-45947 reeval batch 使用 **seed=7**
- 后续 eval 建议统一用 seed=7

---

## 3. Eval 命令

### 3.1 λ=0.1 s0 — westd-35807 (seed=7 版本)

> 注意: westd-45947 已有 reeval_sdf_s0_l01_30k.json (seed=7)。仅在需要 westd-35807 独立结果时执行。

```bash
cd /root/colliforce-vla
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero
export WANDB_MODE=disabled

CUDA_VISIBLE_DEVICES=1 python scripts/eval_safelibero.py \
    --model_type lora_baseline \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/30000 \
    --config_name pi05_libero \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --seed 7 \
    --pi05 \
    --gpu 0 \
    --output_path /root/autodl-tmp/eval_results/eval_s0_l01_30k_seed7.json \
    2>&1 | tee /tmp/eval_s0_l01_30k_seed7.log
```

### 3.2 λ=0.1 s1 — westd-35807 (补缺, seed=7)

> 注意: westd-45947 已有 reeval_sdf_s1_l01_30k.json (seed=7)。仅在需要 westd-35807 独立结果时执行。

```bash
cd /root/colliforce-vla
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero
export WANDB_MODE=disabled

CUDA_VISIBLE_DEVICES=2 python scripts/eval_safelibero.py \
    --model_type lora_baseline \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l1/30000 \
    --config_name pi05_libero \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --seed 7 \
    --pi05 \
    --gpu 0 \
    --output_path /root/autodl-tmp/eval_results/eval_s1_l01_30k_seed7.json \
    2>&1 | tee /tmp/eval_s1_l01_30k_seed7.log
```

### 3.3 LoRA baseline s2 — westd-45947 (待 checkpoint 就绪)

> ⚠️ 需先恢复训练到 30000。checkpoint 当前仅到 18000。

```bash
cd /root/colliforce-vla
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export WANDB_MODE=disabled

CUDA_VISIBLE_DEVICES=0 python scripts/eval_safelibero.py \
    --model_type lora_baseline \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed2/30000 \
    --config_name pi05_libero \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --seed 7 \
    --pi05 \
    --gpu 0 \
    --output_path /root/autodl-tmp/eval_results/eval_lora_baseline_s2_30k.json \
    2>&1 | tee /tmp/eval_lora_baseline_s2_30k.log
```

### 3.4 λ=0.1 s2 — westd-45947

> 已有 reeval_sdf_s2_l01_30k.json (seed=7, May 26 22:35)。仅在需要重跑时执行。

```bash
cd /root/colliforce-vla
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export WANDB_MODE=disabled

CUDA_VISIBLE_DEVICES=1 python scripts/eval_safelibero.py \
    --model_type lora_baseline \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l1/30000 \
    --config_name pi05_libero \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --seed 7 \
    --pi05 \
    --gpu 0 \
    --output_path /root/autodl-tmp/eval_results/eval_s2_l01_30k_seed7.json \
    2>&1 | tee /tmp/eval_s2_l01_30k_seed7.log
```

---

## 4. 当前 GPU 占用

| 服务器 | GPU | PID | 显存 | 用途 |
|--------|-----|-----|------|------|
| westd-35807 | 0 | 3717 | 27036 MiB | eval (batch) |
| westd-35807 | 1 | 271266 | 27036 MiB | eval (batch) |
| westd-35807 | 2 | 274407 | 27036 MiB | eval (batch) |
| westd-35807 | 3 | 341425 | 27028 MiB | eval (batch) |
| westd-45947 | 0 | 78558 | 27080 MiB | reeval batch |
| westd-45947 | 1 | 425058 | 27088 MiB | reeval batch |

**所有 6 个 GPU 均被占用。** 新 eval 需等当前作业完成后才能启动。

---

## 5. Eval 覆盖矩阵 (object_pudding, safety_level=II)

| 实验 | 30k ckpt | seed=0 eval | seed=7 eval | 备注 |
|------|----------|-------------|-------------|------|
| λ=0.05 s0 | ✅ | ✅ 35807 | ✅ 45947 reeval | |
| λ=0.05 s1 | ✅ | ✅ 35807 | ✅ 45947 reeval | |
| λ=0.05 s2 | ✅ | ✅ 35807 | ✅ 45947 reeval | |
| **λ=0.1 s0** | ✅ | ✅ 35807 | ✅ 45947 reeval | |
| **λ=0.1 s1** | ✅ | ❌ 35807 crashed | ✅ 45947 reeval | 35807 补跑可选 |
| **λ=0.1 s2** | ✅ | — | ✅ 45947 reeval | |
| LoRA base s0 | ✅ | ✅ 45947 | — | |
| LoRA base s1 | ✅ | ✅ 45947 | ✅ 45947 reeval | |
| **LoRA base s2** | ❌ 18000 | — | — | **需恢复训练** |
