# gpu check westd 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-check_westd-45947_20260529T050540_result.json`
- **Structured JSON:** [`4934ffb6dc6129e8d69d.json`](../../sessions/49/4934ffb6dc6129e8d69d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete report.

---

## Part 1: westd-45947 服务器状态

| 指标 | 值 |
|------|-----|
| **GPU 0** | RTX PRO 6000, 72°C, 464W/600W, 19107/97887 MiB, 100% util |
| **活跃进程** | `train_a1_sdf_aux_pi05.py --scene object_pudding --seed 3 --lambda_sdf 0.01 --resume` (PID 41134) |
| **训练进度** | step 3099/30000 (10%), ~1.25s/it, 预计还需 ~9.3h |
| **磁盘** | /root/autodl-tmp: 204G/250G used (82%), 47G free |
| **tmux** | 无法检查 (read-only 模式限制) |

---

## Part 2: 实验结果文件完整目录

### 训练日志 (`/root/colliforce-vla/logs/`)

| 文件 | 日期 | 内容 |
|------|------|------|
| `a3_obj.log` | May 21 | A3 object 训练 — **FAILED** (AttributeError: 'GemmaModel' no 'model') |
| `a3_spa.log` | May 21 | A3 spatial 训练 — **FAILED** (同上) |
| `eval_lora_baseline_s0.log` | May 26 | LoRA baseline s0 eval → Overall TSR=8.5%, CAR=54.5% |
| `eval_lora_baseline_s1.log` | May 26 | LoRA baseline s1 eval → Overall TSR=4%, CAR=56% |
| `eval_pi05_baseline_reeval_disp.log` | May 26 | Pi0.5 base reeval (200eps), TSR=0% all tasks (model_type=baseline, 似乎不是 pi0.5 finetuned) |

### 活跃训练 (`/tmp/`)
- `train_sdf_s3_l01_resume.log` — SDF seed3 lambda=0.01, resumed from step 2000, 当前 step ~3099

---

### Checkpoint 目录 (`/root/autodl-tmp/checkpoints/`)

| 目录 | 子目录数 | 内容 |
|------|---------|------|
| `a1_sdf_pi05_object_pudding/` | 13 | 见下方详细列表 |
| `a1_sdf_pi05_spatial_bowl/` | 1 | seed0 (空) |
| `a3_grad_refine_object_pudding/` | 1 | seed0 (best + 30000) |
| `a3_grad_refine_spatial_bowl/` | 1 | seed0 (best + 30000) |
| `baseline_object_pudding/` | 1 | seed0 (仅 wandb 等小文件) |

**a1_sdf_pi05_object_pudding/ 详细:**

| 子目录 | Checkpoints | 最后修改 |
|--------|-------------|---------|
| `seed0_l005` | best + 30000 | May 24 |
| `seed0_l01` | best + 30000 | May 26 |
| `seed0_l1` | 30000 only | May 28 |
| `seed1_l005` | 30000 only | May 26 |
| `seed1_l01` | 30000 only | May 26 |
| `seed2_l005` | 30000 only | May 26 |
| `seed2_l1` | best + 30000 | May 29 |
| **seed3_l01** | **训练中** | **May 29 (进行中)** |
| `lora_baseline_seed0` | best + 30000 | May 26 |
| `lora_baseline_seed1` | best + 30000 | May 26 |
| `lora_baseline_seed2` | best + 30000 | May 29 |

---

### 评估结果 JSON 完整目录 (`/root/autodl-tmp/eval_results/`)

**28 个文件**，按用途分组。所有 eval 均在 safelibero_object Level II 上评估。

#### A. Pi0.5 Base Model（无微调）

| 文件 | Suite | Tasks | Eps | Seed | **TSR** | **CAR** | avg_max_disp |
|------|-------|-------|-----|------|---------|---------|-------------|
| `pi05_safelibero_object_v11.json` | object | 4 | 50 | 7 | **73.0%** | **28.0%** | 0.151 |
| `pi05_safelibero_spatial_v11.json` | spatial | 4 | 50 | 7 | **57.5%** | **13.0%** | 0.404 |
| `sanity_check_pi05_base_rotation_fix.json` | object | task0 | 20 | 7 | **85.0%** | **10.0%** | 0.185 |
| `pi05_base_reeval_safelibero_object_levelII_seed7.json` | object | task0 | 50 | 7 | **74.0%** | **16.0%** | 0.144 |

#### B. LoRA Baseline（无 SDF）

| 文件 | Seed(train) | Ckpt | Tasks | Eps | Eval Seed | **TSR** | **CAR** |
|------|------------|------|-------|-----|-----------|---------|---------|
| `eval_lora_baseline_s0.json` | 0 | 30K | 4 | 50 | 0 | **8.5%** | **54.5%** |
| `eval_lora_baseline_s1.json` | 1 | 30K | 4 | 50 | 0 | **4.0%** | **56.0%** |
| `lora_baseline_s0_reeval_safelibero_object_levelII_seed7.json` | 0 | 30K | task0 | 50 | 7 | **32.0%** | **56.0%** |
| `reeval_lora_s1_30k.json` | 1 | 30K | task0 | 50 | 7 | **34.0%** | **54.0%** |

#### C. SDF 模型 Re-eval（seed=7, 30K steps, task0 only, 50 eps）

| 文件 | Train Seed | λ_sdf | **TSR** | **CAR** | avg_max_disp |
|------|-----------|-------|---------|---------|-------------|
| `reeval_sdf_s0_l005_30k.json` | 0 | 0.005 | **38%** | **52%** | 0.047 |
| `reeval_sdf_s1_l005_30k.json` | 1 | 0.005 | **28%** | **64%** | 0.035 |
| `reeval_sdf_s2_l005_30k.json` | 2 | 0.005 | **34%** | **46%** | 0.060 |
| `reeval_sdf_s0_l01_30k.json` | 0 | 0.01 | **28%** | **48%** | 0.063 |
| `reeval_sdf_s1_l01_30k.json` | 1 | 0.01 | **22%** | **60%** | 0.054 |
| `reeval_sdf_s2_l01_30k.json` | 2 | 0.01 | **24%** | **64%** | 0.038 |
| `eval_safelibero_object_all_levelII_30000_lora_baseline_seed7.json` | 2 | 0.1¹ | **30%** | **56%** | 0.042 |
| `multiseed_sdf_l01_s0_eseed123.json` | 0 | 0.1¹ | **26%** | **62%** | 0.052 |
| `multiseed_sdf_l01_s0_eseed256.json` | 0 | 0.1¹ | **28%** | **60%** | 0.057 |

¹ 注：这些文件的 checkpoint 路径指向 `_l1` 目录（lambda=0.1）

#### D. Mid-training Eval（10K steps, 4 tasks）

| 文件 | Train Seed | λ_sdf | Step | **TSR** | **CAR** |
|------|-----------|-------|------|---------|---------|
| `d012_mid10k/eval_d012_s0_l005_step10k.json` | 0 | 0.005 | 10K | **47%** | **58%** |
| `d012_mid10k/eval_d012_s0_l01_step10k.json` | 0 | 0.01 | 10K | **49%** | **56.5%** |

#### E. A3 Grad Refine（初始 collision 检测 bug，全部无效）

| 文件 | n_eps | 结果 |
|------|-------|------|
| `eval_safelibero_object_task1_levelII_best_a3_refine_seed0.json` | 50 | TSR=0%, CAR=0%（step 0 collision bug） |
| `eval_safelibero_object_task0_levelII_best_a3_seed0.json` | 1 | TSR=0%, CAR=0%（同上） |
| `eval_safelibero_object_task1_levelII_best_a3_seed0.json` | 1 | TSR=0%, CAR=0% |
| `eval_safelibero_object_all_levelII_best_a3_seed0.json` | 50 | task0: TSR=0%, CAR=90%; task1: TSR=0%, CAR=0% |
| `eval_safelibero_object_all_levelII_best_seed0.json` | 50 | baseline task0: TSR=0%, CAR=74% |

#### F. 早期小规模 Debug Evals

| 文件 | n_eps | replan | **TSR** | **CAR** |
|------|-------|--------|---------|---------|
| `eval_safelibero_object_task0_levelII_best_seed0.json` | 3 | 5 | 0% | 67% |
| `replan1_eval_safelibero_object_task0_levelII_best_seed0.json` | 3 | 1 | 0% | 100% |
| `v11_evalckpt_r1_eval_safelibero_object_task0_levelII_best_seed0.json` | 3 | 1 | 0% | 67% |
| `v10like_eval_safelibero_object_task0_levelII_best_seed0.json` | 3 | 1 | 0% | 67% |

---

### 关键数字速查（论文审计用）

| 方法 | 条件 | TSR↑ | CAR↑ |
|------|------|------|------|
| **Pi0.5 Base** | 4-task, seed=7 | 73.0% | 28.0% |
| **LoRA Baseline s0** | task0, seed=7 | 32% | 56% |
| **LoRA Baseline s1** | task0, seed=7 | 34% | 54% |
| **SDF s0 λ=0.005** | task0, seed=7 | 38% | 52% |
| **SDF s1 λ=0.005** | task0, seed=7 | 28% | 64% |
| **SDF s2 λ=0.005** | task0, seed=7 | 34% | 46% |
| **SDF s0 λ=0.01** | task0, seed=7 | 28% | 48% |
| **SDF s1 λ=0.01** | task0, seed=7 | 22% | 60% |
| **SDF s2 λ=0.01** | task0, seed=7 | 24% | 64% |
| **SDF s0 λ=0.1** | task0, seed=123 | 26% | 62% |
| **SDF s0 λ=0.1** | task0, seed=256 | 28% | 60% |
| **SDF s2 λ=0.1** | task0, seed=7 | 30% | 56% |
| **10K mid: s0 λ=0.005** | 4-task, seed=7 | 47% | 58% |
| **10K mid: s0 λ=0.01** | 4-task, seed=7 | 49% | 56.5% |

---
