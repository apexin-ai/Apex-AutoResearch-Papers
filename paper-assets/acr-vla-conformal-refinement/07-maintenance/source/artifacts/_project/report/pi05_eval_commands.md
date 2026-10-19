# π0.5 Plan A Eval Commands (ACR-VLA)

## 验证状态 (2026-05-21)
- ✅ 脚本 `src/evaluate.py` 存在于 bjb1-18228, bjb1-32546, bjb2-28827
- ✅ `--mode acr_vla` 支持确认（= crm_perdof 别名）
- ✅ `--model pi05 --obs_dim 2048` 参数确认（evaluate.py L577-582 有 ValueError 校验）
- ✅ `--crm_checkpoint` 别名确认可用（evaluate.py L505-507）
- ⚠️ **bjb2-28827 代码版本旧**（30140 vs 33058 bytes），eval 前必须 `cd /root/acr-vla-conformal-refinement && git pull`

## 占位符说明
| 占位符 | 说明 | 替换时机 |
|--------|------|----------|
| `<CRM_CKPT>` | π0.5 CRM perdof checkpoint 路径 (crm_best.pt) | CRM training 完成后，从 `--output_dir` 获取 |

## GPU 分配方案

| Run | Benchmark | Seed | Server | GPU |
|-----|-----------|------|--------|-----|
| 1 | object | 42 | bjb1-18228 | cuda:0 |
| 2 | object | 43 | bjb1-18228 | cuda:1 |
| 3 | object | 44 | bjb1-32546 | cuda:0 |
| 4 | spatial | 42 | bjb1-32546 | cuda:1 |
| 5 | spatial | 43 | bjb2-28827 | cuda:0 |
| 6 | spatial | 44 | bjb2-28827 | cuda:1 |

> bjb1-18228 只分 2 runs（仅 4 GPU，且是 CRM training 机器）。
> bjb1-32546 和 bjb2-28827 各分 2 runs，留余量给其他任务。

---

## 6 个 Eval 命令

### Run 1: object seed42 → bjb1-18228 cuda:0
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --model pi05 --mode acr_vla --benchmark object --obs_dim 2048 --seed 42 --K 10 --n_rollouts 20 --crm_checkpoint <CRM_CKPT>"
```

### Run 2: object seed43 → bjb1-18228 cuda:1
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --model pi05 --mode acr_vla --benchmark object --obs_dim 2048 --seed 43 --K 10 --n_rollouts 20 --crm_checkpoint <CRM_CKPT>"
```

### Run 3: object seed44 → bjb1-32546 cuda:0
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --model pi05 --mode acr_vla --benchmark object --obs_dim 2048 --seed 44 --K 10 --n_rollouts 20 --crm_checkpoint <CRM_CKPT>"
```

### Run 4: spatial seed42 → bjb1-32546 cuda:1
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --model pi05 --mode acr_vla --benchmark spatial --obs_dim 2048 --seed 42 --K 10 --n_rollouts 20 --crm_checkpoint <CRM_CKPT>"
```

### Run 5: spatial seed43 → bjb2-28827 cuda:0
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --model pi05 --mode acr_vla --benchmark spatial --obs_dim 2048 --seed 43 --K 10 --n_rollouts 20 --crm_checkpoint <CRM_CKPT>"
```

### Run 6: spatial seed44 → bjb2-28827 cuda:1
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --model pi05 --mode acr_vla --benchmark spatial --obs_dim 2048 --seed 44 --K 10 --n_rollouts 20 --crm_checkpoint <CRM_CKPT>"
```

---

## 部署前 Checklist
- [ ] CRM training 完成，获取 checkpoint 路径替换 `<CRM_CKPT>`
- [ ] bjb2-28827 执行 `cd /root/acr-vla-conformal-refinement && git pull` 同步最新代码
- [ ] 如果 CRM checkpoint 在 bjb1-18228 上，需要 rsync 到 bjb1-32546 和 bjb2-28827
- [ ] 确认 π0.5 模型 `/root/autodl-tmp/models/pi05_libero_finetuned/` 在各服务器存在

## 预期输出
每个 run 自动生成 JSON（无需 --output_file）：
- `logs/eval_object_acr_vla_pi05_seed{42,43,44}.json`
- `logs/eval_spatial_acr_vla_pi05_seed{42,43,44}.json`

## 参考：π0.5 VLA-only baseline 结果
| Benchmark | Seed | SR |
|-----------|------|----|
| Object | 42 | 0.820 |
| Object | 43 | 0.815 |
| Object | 44 | 0.810 |
| Spatial | 42 | 0.845 |
| Spatial | 43 | 0.830 |
| Spatial | 45 | 0.850 |
