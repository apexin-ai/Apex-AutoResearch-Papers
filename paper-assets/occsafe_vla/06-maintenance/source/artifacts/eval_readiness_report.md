# Eval & CKA Readiness Report

> Generated: 2026-05-26 ~04:45 UTC

---

## CRITICAL BLOCKERS

### 1. westd-10894 磁盘 100% 满 (824K free / 250G total)

229G 被 checkpoints 占满。**3 个 resume 实验已崩溃，cutoff_45k_s2_v2 将在 ~8h 后崩溃。**

**崩溃的实验 (exit code 1, ~04:24 UTC):**

| 实验 | 30000_chkpt 状态 | 20000_chkpt 状态 | 需要操作 |
|------|-----------------|-----------------|---------|
| ablation_occ_detach_s3 | COMPLETE | COMPLETE | 可直接 eval |
| full_occ_ln_s3 | BROKEN (仅 tokenizer 文件) | COMPLETE (14.4GB) | 需从 20000 重跑 10K steps |
| mvp_occ_s3 | NEVER CREATED | COMPLETE (14.4GB) | 需从 20000 重跑 10K steps |

**cutoff_45k_s2_v2**: 仍在运行 (step 10624/50005, 21%)。下次保存在 step 20000，约 8h 后。届时磁盘无空间，**将崩溃**。

### 2. 批量脚本 checkpoint 路径错误

`eval_batch_10894.sh` 和 `cka_batch_s3.sh` 对 resume 实验使用 `--50000_chkpt`，但实际 checkpoint 名为 `--30000_chkpt` (local step)。

**原因**: resume 实验加载 20K checkpoint 作为 `vla_path`（非 `--resume` flag），`gradient_step_idx` 从 0 计数，`log_step = gradient_step_idx`，所以 checkpoint 命名为 10000/20000/30000。

---

## 磁盘状态

| 服务器 | 总量 | 已用 | 可用 | 状态 |
|--------|------|------|------|------|
| westd-10894 | 250G | 250G | 824K | FULL |
| westd-34685 | 350G | 290G | 61G | OK |

### 10894 可删除的旧 checkpoint (~121G)

| 目录 | 大小 | 说明 |
|------|------|------|
| cutoff_45k_s2 (v1) | 30G | 旧版，已有 v2 |
| full_occ_ln_s0 | 15G | 旧 seed |
| full_occ_ln_s1 | 15G | 旧 seed |
| full_occ_ln_s2 | 15G | 旧 seed |
| ablation_occ_detach_s0_retrain | 15G | 旧 seed |
| full_occ_retrain_s0 | 15G | 旧 seed |
| vanilla_retrain_s0 | 15G | 旧 seed |
| cutoff_15k_s1 | 463M | 旧实验 |
| full_occ_ln_s3 损坏 30000_chkpt | ~2K | 损坏文件 |

---

## Eval 脚本状态

| 项目 | 10894 | 34685 |
|------|-------|-------|
| evaluate_safelibero.py | OK | OK |
| libero_spatial 数据 | OK | OK |
| conda env occsafe | OK | OK |
| openvla-7b 预训练模型 (CKA 用) | OK | N/A |

---

## CKA 脚本状态

- `analysis/cka_analysis.py`: OK (10894)
- `cka_batch_s3.sh`: 存在，但 **checkpoint 路径需修复** (见上)
- 依赖: libero_spatial HDF5 数据 OK, openvla-7b 基准模型 OK

---

## Checkpoint 目录结构

### 10894 (resume 实验 — local step 命名)

```
/root/autodl-tmp/checkpoints/
├── ablation_occ_detach_s3/
│   └── ...--ablation_occ_detach_s3--{10000,20000,30000}_chkpt  ← 30000 完整
├── full_occ_ln_s3/
│   └── ...--full_occ_ln_s3--{10000,20000,30000}_chkpt  ← 30000 损坏, 20000 完整
├── mvp_occ_s3/
│   └── ...--mvp_occ_s3--{10000,20000}_chkpt  ← 30000 缺失, 20000 完整
└── cutoff_45k_s2_v2/
    └── ...--cutoff_45k_s2_v2--10000_chkpt  ← 训练中，需到 50000
```

### 34685 (从头实验 — global step 命名)

```
/root/autodl-tmp/checkpoints/
├── detach_bn_v2_s0/  → 10000_chkpt (训练中)
├── detach_bn_v2_s1/  → 10000_chkpt (训练中)
├── detach_bn_v2_s2/  → 10000_chkpt (训练中)
└── full_occ_bn_v2_s1/  → 无 checkpoint (训练中，最晚启动)
```

---

## Eval 命令模板

### 10894 — resume 实验 (50 rollouts)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe
cd /root/occsafe_vla/openvla-oft

P="openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug"

# ablation_occ_detach_s3 — 可立即执行
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s3/${P}--ablation_occ_detach_s3--30000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/ablation_occ_detach_s3_v2_50r_30000.json \
    > /root/occsafe_vla/eval_results/ablation_occ_detach_s3_v2_eval.log 2>&1 &

# full_occ_ln_s3 — 需重跑 30000_chkpt 后再 eval
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_s3/${P}--full_occ_ln_s3--30000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/full_occ_ln_s3_v2_50r_30000.json \
    > /root/occsafe_vla/eval_results/full_occ_ln_s3_v2_eval.log 2>&1 &

# mvp_occ_s3 — 需重跑 30000_chkpt 后再 eval
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/mvp_occ_s3/${P}--mvp_occ_s3--30000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/mvp_occ_s3_v2_50r_30000.json \
    > /root/occsafe_vla/eval_results/mvp_occ_s3_v2_eval.log 2>&1 &

# cutoff_45k_s2_v2 — 等训练完成后
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_45k_s2_v2/${P}--cutoff_45k_s2_v2--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/cutoff_45k_s2_v2_50r_50000.json \
    > /root/occsafe_vla/eval_results/cutoff_45k_s2_v2_eval.log 2>&1 &
```

### 34685 — 从头实验 (50 rollouts)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe
cd /root/occsafe_vla/openvla-oft

P="openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug"

# detach_bn_v2_s0
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_bn_v2_s0/${P}--detach_bn_v2_s0--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/detach_bn_v2_s0_50r_50000.json \
    > /root/occsafe_vla/eval_results/detach_bn_v2_s0_eval.log 2>&1 &

# detach_bn_v2_s1
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_bn_v2_s1/${P}--detach_bn_v2_s1--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/detach_bn_v2_s1_50r_50000.json \
    > /root/occsafe_vla/eval_results/detach_bn_v2_s1_eval.log 2>&1 &

# detach_bn_v2_s2
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_bn_v2_s2/${P}--detach_bn_v2_s2--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/detach_bn_v2_s2_50r_50000.json \
    > /root/occsafe_vla/eval_results/detach_bn_v2_s2_eval.log 2>&1 &

# full_occ_bn_v2_s1
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 \
python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/${P}--full_occ_bn_v2_s1--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 --seed 42 \
    --output_path /root/occsafe_vla/eval_results/full_occ_bn_v2_s1_50r_50000.json \
    > /root/occsafe_vla/eval_results/full_occ_bn_v2_s1_eval.log 2>&1 &
```

---

## CKA 命令模板 (修正路径)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe
cd /root/occsafe_vla

P="openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug"
CKPT_ROOT="/root/autodl-tmp/checkpoints"

CUDA_VISIBLE_DEVICES=0 python analysis/cka_analysis.py \
    --pretrained_path /root/autodl-tmp/models/openvla-7b \
    --checkpoint_paths \
        "${CKPT_ROOT}/mvp_occ_s3/${P}--mvp_occ_s3--30000_chkpt" \
        "${CKPT_ROOT}/full_occ_ln_s3/${P}--full_occ_ln_s3--30000_chkpt" \
        "${CKPT_ROOT}/ablation_occ_detach_s3/${P}--ablation_occ_detach_s3--30000_chkpt" \
        "${CKPT_ROOT}/cutoff_45k_s2_v2/${P}--cutoff_45k_s2_v2--50000_chkpt" \
    --condition_names "MVP OCC" "Full OCC LN" "Detach OCC" "Cutoff 45K" \
    --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial \
    --output_dir /root/autodl-tmp/analysis/cka_s3_v2 \
    --gpu 0 \
    --num_samples 200
```

注意: resume 实验路径用 `30000_chkpt`，从头实验用 `50000_chkpt`。

---

## 紧急行动清单

1. **CRITICAL 立即**: 清理 10894 旧 checkpoint（至少 60G），否则 cutoff_45k_s2_v2 将在 ~8h 后崩溃
2. **CRITICAL 立即**: 删除 full_occ_ln_s3 损坏的 30000_chkpt
3. **HIGH 清空后**: 从 20000_chkpt 重跑 mvp_occ_s3 和 full_occ_ln_s3 各 10K steps (~2.5h each)
4. **HIGH 脚本修复**: 更新 eval_batch_10894.sh 和 cka_batch_s3.sh 中 resume 实验的 checkpoint 路径 (50000 → 30000)
5. **READY**: ablation_occ_detach_s3 可立即开始 eval（30000_chkpt 完整，GPU:3 已空闲）
