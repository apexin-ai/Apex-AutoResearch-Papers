# 实验诊断记录

## [2026-05-28] pi05-crm-k2-long-s42-backfill & pi05-adaptive-goal-s44-backfill 失败诊断

### 错误类型
代码参数缺失（非 OOM / 非磁盘满 / 非 transient error）

### 根因
两个实验提交命令**缺少 `--obs_dim 2048 --unified_obs_dim 2088` 参数**，导致 CRM 模型输入维度与 checkpoint 不匹配。

**Checkpoint 维度**（`crm_pi05_unified_3suite/crm_best.pt`）:
- `net.0.weight`: [256, **2118**]
- `input_mean` / `input_std`: [**2118**]

**实际构造的模型维度**（因缺少 unified_obs_dim）:
- `input_dim = action_dim(30) + unc_dim(0) + obs_dim(960) = **990**`

**正确参数**（参考同 checkpoint 的成功实验 pi05-crm-k2-spatial-s42 等）:
- `--obs_dim 2048 --unified_obs_dim 2088`
- `input_dim = 30 + 0 + 2088 = **2118** ✓`

### 关键错误信息
```
RuntimeError: Error(s) in loading state_dict for ConformalRefinementModule:
    size mismatch for input_mean: copying a param with shape torch.Size([2118]) from checkpoint, the shape in current model is torch.Size([990]).
    size mismatch for input_std: copying a param with shape torch.Size([2118]) from checkpoint, the shape in current model is torch.Size([990]).
    size mismatch for net.0.weight: copying a param with shape torch.Size([256, 2118]) from checkpoint, the shape in current model is torch.Size([256, 990]).
```

### 是否可直接重试
**否**，不可直接重试。需要修正命令参数后重新提交。

### 修复建议
重新提交时在命令中添加 `--obs_dim 2048 --unified_obs_dim 2088`：

**pi05-crm-k2-long-s42-backfill** 修正命令：
```bash
python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --benchmark long --seed 42 --n_rollouts 20 --obs_dim 2048 --unified_obs_dim 2088 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
```

**pi05-adaptive-goal-s44-backfill** 修正命令：
```bash
python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --obs_dim 2048 --unified_obs_dim 2088 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
```

### 防范措施
使用 `crm_pi05_unified_3suite` checkpoint 时，**必须**传 `--obs_dim 2048 --unified_obs_dim 2088`。建议在提交脚本中固化这两个参数，避免遗漏。
