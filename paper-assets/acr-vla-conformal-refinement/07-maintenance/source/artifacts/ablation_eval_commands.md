# Ablation Eval Commands

## 代码审查结果

### evaluate.py 中 ablation modes 状态：✅ 全部就绪

`--mode` 接受 6 个值：`vla_only`, `crm_scalar`, `crm_perdof`, `acr_vla`, `crm_obs_only`, `reconvla`

两个 ablation mode 的 CRM 加载逻辑：

| mode | uncertainty_dim | uf_input 传入 CRM | 与 train_crm.py 一致性 |
|------|----------------|-------------------|----------------------|
| `crm_obs_only` | 0 | `None` | ✅ `input_mode=obs_only` → `unc_dim=0`, `crm(ba, None, obs_feat)` |
| `crm_scalar` | 3 | `_to_scalar_uf(uf)` 压缩为 3D | ✅ `input_mode=scalar_unc` → `unc_dim=3`, `_to_scalar_uf()` 同函数 |

`_to_scalar_uf()` 实现：将 40D uncertainty 压缩为 3D — `[per_dof_std.norm(), interval_width.mean(), coverage.mean()]`，evaluate.py 和 train_crm.py 中完全一致。

CRM forward 中 `uncertainty_features=None` 时跳过拼接，只用 `base_action + obs_features`，与训练 obs_only 模式匹配。

**无 bug 风险。** 训练与评估的 uncertainty_dim 映射、uf 处理、CRM 输入构造完全对齐。

### max_correction_norm

命令行 `--max_correction_norm` 可覆盖 checkpoint 中保存的值。不指定则用 checkpoint 默认值（训练时设为 1.42）。

---

## Eval 命令

### 1. obs_only ablation

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acr-vla-conformal-refinement && \
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -u src/evaluate.py \
  --mode crm_obs_only \
  --benchmark spatial \
  --n_rollouts 10 \
  --seed 42 \
  --K 10 \
  --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --output_file /root/autodl-tmp/eval_results/ablation_obs_only_spatial.json
```

### 2. scalar_unc ablation

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acr-vla-conformal-refinement && \
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -u src/evaluate.py \
  --mode crm_scalar \
  --benchmark spatial \
  --n_rollouts 10 \
  --seed 42 \
  --K 10 \
  --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt \
  --output_file /root/autodl-tmp/eval_results/ablation_scalar_unc_spatial.json
```

### 3. 对比基准：full ACR-VLA (crm_perdof)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acr-vla-conformal-refinement && \
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -u src/evaluate.py \
  --mode acr_vla \
  --benchmark spatial \
  --n_rollouts 10 \
  --seed 42 \
  --K 10 \
  --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt \
  --output_file /root/autodl-tmp/eval_results/full_acr_vla_spatial.json
```

---

## 注意事项

- 执行前确保 `/root/autodl-tmp/eval_results/` 目录存在（evaluate.py 会自动创建）
- `--crm_checkpoint` 和 `--checkpoint` 等价，内部会自动合并
- 如需覆盖 correction 范围：加 `--max_correction_norm 1.0`（默认 1.42）
- 三个 eval 可串行跑，每个约需 30-60 分钟（取决于 benchmark 任务数 × n_rollouts）
