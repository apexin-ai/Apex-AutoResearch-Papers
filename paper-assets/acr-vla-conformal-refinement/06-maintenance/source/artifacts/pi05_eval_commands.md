# π0.5 Plan A Eval Commands（6 runs）

## 脚本验证结论

- 脚本：`/root/acr-vla-conformal-refinement/src/evaluate.py`
- `--mode acr_vla` 已支持（docstring 注释为 "alias for crm_perdof — the full ACR-VLA pipeline"）
- `--model pi05` 已支持（choices=[smolvla, pi05]）
- `--obs_dim` 默认 960 (`OBS_DIM` from utils.py)，π0.5 必须显式传 `--obs_dim 2048`
- `--crm_checkpoint` 是 `--checkpoint` 的别名（acr_vla 模式专用）
- **`--cache_dir` 不是 eval 参数**（只有 train_crm.py 用），原任务描述里的 `<MERGED_CACHE_DIR>` 占位符忽略
- CRM checkpoint 目录已建好：`/root/autodl-tmp/checkpoints/crm_pi05/{object,spatial}/`（按 benchmark 分目录，等训练完产出 `crm_best.pt`）

## 占位符

- `<CRM_CHECKPOINT_OBJECT>`：CRM training 完成后填入，预期路径 `/root/autodl-tmp/checkpoints/crm_pi05/object/crm_best.pt`
- `<CRM_CHECKPOINT_SPATIAL>`：预期路径 `/root/autodl-tmp/checkpoints/crm_pi05/spatial/crm_best.pt`
- 如果 CRM training 用单一共享 checkpoint，两个占位符填同一路径

## 通用前缀（所有命令复用）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
```

## GPU 分配（6 runs 分散到 3 台服务器，每台 2 GPU）

| # | Benchmark | Seed | Server       | GPU    |
|---|-----------|------|--------------|--------|
| 1 | object    | 42   | bjb1-32546   | cuda:0 |
| 2 | object    | 43   | bjb1-32546   | cuda:1 |
| 3 | object    | 44   | bjb2-28827   | cuda:0 |
| 4 | spatial   | 42   | bjb2-28827   | cuda:1 |
| 5 | spatial   | 43   | bjb1-18228   | cuda:0 |
| 6 | spatial   | 44   | bjb1-18228   | cuda:1 |

Notes:
- bjb1-18228 训练完 CRM 后再分配 eval（避免抢占 CRM training GPU）
- bjb1-32546 和 bjb2-28827 各 6 GPU，未来扩展 ablation 时还有 4 GPU 余量

## 6 个完整命令

### Run 1: object / seed 42 / bjb1-32546 / cuda:0

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
CUDA_VISIBLE_DEVICES=0 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
  --model pi05 \
  --mode acr_vla \
  --benchmark object \
  --seed 42 \
  --n_rollouts 20 \
  --K 10 \
  --obs_dim 2048 \
  --crm_checkpoint <CRM_CHECKPOINT_OBJECT> \
  --max_correction_norm 0.2 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --output_file logs/eval_object_acr_vla_pi05_seed42.json
```

### Run 2: object / seed 43 / bjb1-32546 / cuda:1

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
CUDA_VISIBLE_DEVICES=1 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
  --model pi05 \
  --mode acr_vla \
  --benchmark object \
  --seed 43 \
  --n_rollouts 20 \
  --K 10 \
  --obs_dim 2048 \
  --crm_checkpoint <CRM_CHECKPOINT_OBJECT> \
  --max_correction_norm 0.2 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --output_file logs/eval_object_acr_vla_pi05_seed43.json
```

### Run 3: object / seed 44 / bjb2-28827 / cuda:0

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
CUDA_VISIBLE_DEVICES=0 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
  --model pi05 \
  --mode acr_vla \
  --benchmark object \
  --seed 44 \
  --n_rollouts 20 \
  --K 10 \
  --obs_dim 2048 \
  --crm_checkpoint <CRM_CHECKPOINT_OBJECT> \
  --max_correction_norm 0.2 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --output_file logs/eval_object_acr_vla_pi05_seed44.json
```

### Run 4: spatial / seed 42 / bjb2-28827 / cuda:1

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
CUDA_VISIBLE_DEVICES=1 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
  --model pi05 \
  --mode acr_vla \
  --benchmark spatial \
  --seed 42 \
  --n_rollouts 20 \
  --K 10 \
  --obs_dim 2048 \
  --crm_checkpoint <CRM_CHECKPOINT_SPATIAL> \
  --max_correction_norm 0.2 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --output_file logs/eval_spatial_acr_vla_pi05_seed42.json
```

### Run 5: spatial / seed 43 / bjb1-18228 / cuda:0

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
CUDA_VISIBLE_DEVICES=0 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
  --model pi05 \
  --mode acr_vla \
  --benchmark spatial \
  --seed 43 \
  --n_rollouts 20 \
  --K 10 \
  --obs_dim 2048 \
  --crm_checkpoint <CRM_CHECKPOINT_SPATIAL> \
  --max_correction_norm 0.2 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --output_file logs/eval_spatial_acr_vla_pi05_seed43.json
```

### Run 6: spatial / seed 44 / bjb1-18228 / cuda:1

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
CUDA_VISIBLE_DEVICES=1 TORCHDYNAMO_DISABLE=1 python -u src/evaluate.py \
  --model pi05 \
  --mode acr_vla \
  --benchmark spatial \
  --seed 44 \
  --n_rollouts 20 \
  --K 10 \
  --obs_dim 2048 \
  --crm_checkpoint <CRM_CHECKPOINT_SPATIAL> \
  --max_correction_norm 0.2 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --output_file logs/eval_spatial_acr_vla_pi05_seed44.json
```

## 部署须知 / 待澄清

1. **mode 选择**：任务硬约束 `--mode acr_vla`（= crm_perdof，per-DOF CRM 修正）。memory.md 中 Plan A 提到 `--mode adaptive_conformal_crm`（带 conformal stopping），二者不等价。如果实际想要的是 conformal stopping 版本，把 `acr_vla` 改成 `adaptive_conformal_crm` 并加 `--conformal_threshold` 参数（默认 0.074855，π0.5 可能需重新校准）。
2. **max_correction_norm**：传 0.2 会 override checkpoint 内置值（Plan A 标定）；如果想完全用 checkpoint 自带值，删掉这一行。
3. **CRM checkpoint 路径**：基于 `/root/autodl-tmp/checkpoints/crm_pi05/{object,spatial}/` 目录结构推断按 benchmark 分文件。CRM training 完成后 worker 应该确认实际 `.pt` 文件名（可能是 `crm_best.pt` / `crm_epoch_50.pt` / `crm_final.pt`），把占位符替换为绝对路径。
4. **环境**：服务器是 aml-train 镜像，base conda 环境已有 torch/transformers，无需重装。
5. **预期 baseline 对照**：π0.5 VLA-only Object 81.5%±0.5%、Spatial 84.2%±1.0%（memory locked）。ACR-VLA 增益预期在 ceiling effect 内有限提升。
