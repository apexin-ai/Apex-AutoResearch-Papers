# π0.5 Full Baseline Eval 部署方案

## 前置检查清单

- [ ] Vision tower 权重加载 fix 已验证（`_fix_vision_tower_keys` in `pi05_wrapper.py`）
- [ ] Quick verify 通过：单 task SR > 0%
- [ ] 模型路径存在：`/root/autodl-tmp/models/pi05_libero_finetuned/model.safetensors` (7.5GB)
- [ ] 依赖版本：lerobot>=0.5.2, transformers>=5.8.0, diffusers>=0.35.2
- [ ] 各服务器代码已同步（`git pull`）
- [ ] 各服务器 HF cache 和模型文件就绪

## GPU 分配方案

6 experiments: 3 seeds (42,43,44) × 2 benchmarks (Object, Spatial)

| # | 实验 | 服务器 | GPU | 预计 VRAM |
|---|------|--------|-----|----------|
| 1 | Object seed42 | bjb2-40593 | cuda:0 | ~16GB |
| 2 | Object seed43 | bjb1-18228 | cuda:0 | ~16GB |
| 3 | Object seed44 | bjb1-18228 | cuda:3 | ~16GB |
| 4 | Spatial seed42 | bjb1-32546 | cuda:0 | ~16GB |
| 5 | Spatial seed43 | bjb1-32546 | cuda:1 | ~16GB |
| 6 | Spatial seed44 | bjb1-32546 | cuda:3 | ~16GB |

备选：bjb2-28827 的 cuda:0~4 在 K=20 object-seed45 完成后全部空闲，可承接 3 个实验。

## Baseline Eval 命令

### #1 Object seed42 — bjb2-40593 cuda:0
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python src/evaluate.py \
  --benchmark object --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed 42 --n_rollouts 10 --K 1 \
  > logs/eval_pi05_object_seed42.log 2>&1 &
```

### #2 Object seed43 — bjb1-18228 cuda:0
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python src/evaluate.py \
  --benchmark object --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed 43 --n_rollouts 10 --K 1 \
  > logs/eval_pi05_object_seed43.log 2>&1 &
```

### #3 Object seed44 — bjb1-18228 cuda:3
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python src/evaluate.py \
  --benchmark object --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed 44 --n_rollouts 10 --K 1 \
  > logs/eval_pi05_object_seed44.log 2>&1 &
```

### #4 Spatial seed42 — bjb1-32546 cuda:0
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python src/evaluate.py \
  --benchmark spatial --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed 42 --n_rollouts 10 --K 1 \
  > logs/eval_pi05_spatial_seed42.log 2>&1 &
```

### #5 Spatial seed43 — bjb1-32546 cuda:1
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python src/evaluate.py \
  --benchmark spatial --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed 43 --n_rollouts 10 --K 1 \
  > logs/eval_pi05_spatial_seed43.log 2>&1 &
```

### #6 Spatial seed44 — bjb1-32546 cuda:3
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python src/evaluate.py \
  --benchmark spatial --mode vla_only --baseline_mode single \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --seed 44 --n_rollouts 10 --K 1 \
  > logs/eval_pi05_spatial_seed44.log 2>&1 &
```

## CRM Projection 训练命令模板（待 baseline 完成后）

π0.5 obs_features 是 2048D，现有 CRM (obs_dim=960) 无法直接用。两种方案：

### 方案 A: 训练新 CRM (obs_dim=2048) — 推荐
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=X HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python src/train_crm.py \
  --model pi05 --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned/ \
  --obs_dim 2048 --hidden_dim 256 \
  --output_dir /root/autodl-tmp/checkpoints/crm_pi05/ \
  --mode obs_only \
  > logs/train_crm_pi05.log 2>&1 &
```

### 方案 B: 用 evaluate.py 内置 linear projection (2048→960) 复用现有 CRM
evaluate.py 已内置 `obs_proj = nn.Linear(2048, 960)`，但这是 random init 的投影，效果未知。

**推荐方案 A**：重新训练一个 obs_dim=2048 的 CRM，避免信息损失。

## 注意事项

1. π0.5 模型 7.5GB，加载需要 ~16GB VRAM，确保 GPU 无其他占用
2. π0.5 chunk_size=50（开环回放），比 SmolVLA 每步推理快很多，eval 时间更短
3. `_fix_vision_tower_keys` 已处理 vision_tower.vision_model.X → vision_tower.X 的 key mismatch
4. 输出文件自动命名：`logs/eval_{benchmark}_vla_only_pi05_seed{seed}.json`
5. 先在一台机器上 quick verify 确认 SR > 0%，再铺开全量 eval
