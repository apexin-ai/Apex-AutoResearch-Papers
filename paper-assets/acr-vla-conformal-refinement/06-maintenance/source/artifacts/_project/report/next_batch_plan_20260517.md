# Next Batch Experiment Plan — 2026-05-17

> 目标：填补 Figure 2 magnitude curve 中 error bar 最薄弱的数据点

## 1. 当前数据矩阵（DONE + RUNNING 完成后）

### obs_only

| norm | seeds (DONE) | RUNNING | 完成后总数 |
|------|-------------|---------|-----------|
| 0.03 | 42 (16%) | — | **1** ⚠️ |
| 0.05 | 42 (13%) | — | **1** ⚠️ |
| 0.10 | 42 (19%), 44 (16%) | 45, 46, 47 | 5 ✓ |
| 0.20 | 42 (22%), 43 (16%), 44 (16%), 45 (16%), 46 (15%), 47 (20%) | — | 6 LOCKED ✓ |
| 0.30 | 42 (19%), 44 (18%), 45 (14%) | 46, 47 | 5 ✓ |
| default | 42 (17%), 44 (16%) | 45, 46 | 4 ✓ |

### perdof

| norm | seeds (DONE) | RUNNING | 完成后总数 |
|------|-------------|---------|-----------|
| 0.03 | 42 (14%) | — | **1** ⚠️ |
| 0.05 | 42 (14%) | — | **1** ⚠️ |
| 0.10 | 42 (11%), 44 (8%), 45 (11%) | 46, 47 | 5 ✓ |
| 0.20 | 42 (11%), 43 (9%) | 44, 45, 46 | 5 ✓ |
| 0.30 | 42 (4%), 44 (4%), 45 (6%) | 46 | 4 ✓ |
| default | 42 (0%), 44 (0%) | 46 | 3 (sufficient, 0% confirmed) |

### scalar

| seeds (DONE) | RUNNING | 完成后总数 |
|-------------|---------|-----------|
| 42 (9%), 43 (10%), 44 (6%) | 45 | 4 ✓ |

---

## 2. 薄弱点分析

**Figure 2 的 x 轴**: 0.03 → 0.05 → 0.10 → 0.20 → 0.30 → default(~1.42)

**核心问题**: norm=0.03 和 norm=0.05 两个点（obs_only 和 perdof 各仅 1 seed），无法绘制 error bar。

这两个点对叙事至关重要：
- 在低 magnitude 时，obs_only 和 perdof 应表现相近（~14-16%），说明问题不是模型质量而是 magnitude sensitivity
- 没有 error bar 的单点数据无法支撑 "both methods perform similarly at low magnitudes" 的 claim
- 审稿人会质疑这些点的可靠性

**次要问题**: obs_only norm=0.10 缺 seed43（其他 norm 都有 seed43）

---

## 3. 推荐实验（按优先级排序）

### Tier 1: 必做（填补 Figure 2 左端 error bar）

| # | exp_id | mode | norm | seed | 理由 |
|---|--------|------|------|------|------|
| 1 | eval-obs-only-object-norm003-seed43 | obs_only | 0.03 | 43 | 左端点无 error bar |
| 2 | eval-obs-only-object-norm003-seed44 | obs_only | 0.03 | 44 | 左端点无 error bar |
| 3 | eval-obs-only-object-norm005-seed43 | obs_only | 0.05 | 43 | 左端点无 error bar |
| 4 | eval-obs-only-object-norm005-seed44 | obs_only | 0.05 | 44 | 左端点无 error bar |
| 5 | eval-perdof-object-norm003-seed43 | perdof | 0.03 | 43 | 左端点无 error bar |
| 6 | eval-perdof-object-norm003-seed44 | perdof | 0.03 | 44 | 左端点无 error bar |
| 7 | eval-perdof-object-norm005-seed43 | perdof | 0.05 | 43 | 左端点无 error bar |
| 8 | eval-perdof-object-norm005-seed44 | perdof | 0.05 | 44 | 左端点无 error bar |

### Tier 2: 加分（统一 seed 覆盖、加强 error bar）

| # | exp_id | mode | norm | seed | 理由 |
|---|--------|------|------|------|------|
| 9 | eval-obs-only-object-norm003-seed45 | obs_only | 0.03 | 45 | 扩展到 4 seeds |
| 10 | eval-perdof-object-norm005-seed45 | perdof | 0.05 | 45 | 扩展到 4 seeds |

---

## 4. 部署命令模板

### 约束
- **禁止在 bjb2-40593 部署**（磁盘 90%）
- 可用服务器: bjb1-18228 (cuda:0-3), bjb1-32546 (cuda:0-5), bjb2-28827 (cuda:0-5)
- 总可用 GPU: 16 张（足够 Tier 1 全部 8 个 + Tier 2）
- 预计运行时间: 每个 ~12-16h

### 服务器分配建议

| 服务器 | GPU | 分配实验 |
|--------|-----|---------|
| bjb1-18228 | cuda:0 | #1 eval-obs-only-object-norm003-seed43 |
| bjb1-18228 | cuda:1 | #2 eval-obs-only-object-norm003-seed44 |
| bjb1-18228 | cuda:2 | #3 eval-obs-only-object-norm005-seed43 |
| bjb1-18228 | cuda:3 | #4 eval-obs-only-object-norm005-seed44 |
| bjb1-32546 | cuda:0 | #5 eval-perdof-object-norm003-seed43 |
| bjb1-32546 | cuda:1 | #6 eval-perdof-object-norm003-seed44 |
| bjb1-32546 | cuda:2 | #7 eval-perdof-object-norm005-seed43 |
| bjb1-32546 | cuda:3 | #8 eval-perdof-object-norm005-seed44 |
| bjb1-32546 | cuda:4 | #9 eval-obs-only-object-norm003-seed45 |
| bjb1-32546 | cuda:5 | #10 eval-perdof-object-norm005-seed45 |

### obs_only 命令模板

```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES={GPU_ID} MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode crm_obs_only \
  --benchmark object \
  --n_rollouts 10 \
  --seed {SEED} \
  --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm {NORM} \
  --output_file logs/eval_object_obs_only_norm{NORM_TAG}_seed{SEED}.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-obs-only-object-norm{NORM_TAG}-seed{SEED}.log
```

### perdof 命令模板

```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES={GPU_ID} MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode acr_vla \
  --benchmark object \
  --n_rollouts 10 \
  --seed {SEED} \
  --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt \
  --max_correction_norm {NORM} \
  --output_file logs/eval_object_perdof_norm{NORM_TAG}_seed{SEED}.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-perdof-object-norm{NORM_TAG}-seed{SEED}.log
```

### 具体展开（Tier 1 全部 8 个）

**#1** obs_only norm=0.03 seed=43 @ bjb1-18228:cuda:0
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.03 \
  --output_file logs/eval_object_obs_only_norm003_seed43.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-obs-only-object-norm003-seed43.log
```

**#2** obs_only norm=0.03 seed=44 @ bjb1-18228:cuda:1
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.03 \
  --output_file logs/eval_object_obs_only_norm003_seed44.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-obs-only-object-norm003-seed44.log
```

**#3** obs_only norm=0.05 seed=43 @ bjb1-18228:cuda:2
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.05 \
  --output_file logs/eval_object_obs_only_norm005_seed43.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-obs-only-object-norm005-seed43.log
```

**#4** obs_only norm=0.05 seed=44 @ bjb1-18228:cuda:3
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.05 \
  --output_file logs/eval_object_obs_only_norm005_seed44.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-obs-only-object-norm005-seed44.log
```

**#5** perdof norm=0.03 seed=43 @ bjb1-32546:cuda:0
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode acr_vla --benchmark object --n_rollouts 10 --seed 43 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt \
  --max_correction_norm 0.03 \
  --output_file logs/eval_object_perdof_norm003_seed43.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-perdof-object-norm003-seed43.log
```

**#6** perdof norm=0.03 seed=44 @ bjb1-32546:cuda:1
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode acr_vla --benchmark object --n_rollouts 10 --seed 44 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt \
  --max_correction_norm 0.03 \
  --output_file logs/eval_object_perdof_norm003_seed44.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-perdof-object-norm003-seed44.log
```

**#7** perdof norm=0.05 seed=43 @ bjb1-32546:cuda:2
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode acr_vla --benchmark object --n_rollouts 10 --seed 43 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt \
  --max_correction_norm 0.05 \
  --output_file logs/eval_object_perdof_norm005_seed43.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-perdof-object-norm005-seed43.log
```

**#8** perdof norm=0.05 seed=44 @ bjb1-32546:cuda:3
```bash
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
python -u src/evaluate.py \
  --mode acr_vla --benchmark object --n_rollouts 10 --seed 44 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt \
  --max_correction_norm 0.05 \
  --output_file logs/eval_object_perdof_norm005_seed44.json \
  2>&1 | tee /root/autodl-tmp/eval_results/eval-perdof-object-norm005-seed44.log
```

---

## 5. 预期收益

完成 Tier 1 后，Figure 2 所有 6 个 norm 点均有 >=3 seeds（可绘制 mean +/- stderr）：

| norm | obs_only seeds | perdof seeds |
|------|---------------|-------------|
| 0.03 | 3 (42,43,44) | 3 (42,43,44) |
| 0.05 | 3 (42,43,44) | 3 (42,43,44) |
| 0.10 | 5 | 5 |
| 0.20 | 6 (LOCKED) | 5 |
| 0.30 | 5 | 4 |
| default | 4 | 3 |

这将支撑完整的 Figure 2，每个数据点都有 error bar，叙事可信度大幅提升。

---

## 6. 时间线估算

- 当前 RUNNING 预计 12-20h 完成（~May 18 凌晨至上午）
- Tier 1 部署后 ~12-16h 完成（~May 18 晚至 May 19 凌晨）
- 距 CoRL DDL（Jun 2）还有 16 天，时间充裕
