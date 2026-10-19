# Adaptive Conformal CRM Eval Prep Report

## 1. Implementation Status: COMPLETE

`--mode adaptive_conformal_crm` 已完整实现于 `src/evaluate.py`。

核心函数 `select_action_conformal_crm()` (lines 447-508):
- 每步生成 K=2 samples（hardcoded，与 `--K` 参数无关）
- 计算 L2 distance: `||a1 - a2||₂` 作为 uncertainty
- 选择离 centroid 更近的 sample 作为 base action
- `uncertainty > conformal_threshold` → 应用 CRM 修正（obs_only, unc_dim=0）
- `uncertainty <= conformal_threshold` → 跳过 CRM，直接用 selected action

CRM 加载逻辑 (lines 569-593):
- `unc_dim = 0`（obs_only 模式，CRM input_dim = 30 + 960 = 990）
- 默认 `max_correction_norm = 0.2`
- 默认 checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`

## 2. 参数列表

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--mode` | - | `adaptive_conformal_crm` |
| `--conformal_threshold` | 0.074855 | K=2 L2 距离阈值 (P50 calibration) |
| `--crm_checkpoint` | auto: crm_v3_norm/obs_only/crm_best.pt | CRM 权重路径 |
| `--max_correction_norm` | 0.2 (auto for adaptive modes) | CRM 修正范数上限 |
| `--benchmark` | object | object/spatial/goal |
| `--seed` | 42 | 随机种子 |
| `--n_rollouts` | 20 | 每 task 的 rollout 次数 |
| `--max_steps` | per-suite auto (280/280/300) | 留默认即可 |
| `--obs_dim` | 960 | SmolVLA feature dim |
| `--model` | smolvla | VLA backbone |

**注意**: `--K` 参数对 adaptive_conformal_crm 无效，函数内部 hardcode K=2。

## 3. Conformal Threshold 策略

当前默认 `tau = 0.074855`（P50），即 calibration set 中 50% 的 step 会触发 CRM。

理论上 threshold 应通过 conformal prediction 在 calibration set 上确定：
- P50 (0.074855): ~50% 触发率 — 当前默认
- 更高 tau: 更少触发 → 更快但可能漏修正
- 更低 tau: 更多触发 → 更保守但 latency 更高

MVP 阶段直接用默认值。后续可 grid search 不同 percentile (P25/P50/P75/P90)。

## 4. 部署命令模板

```bash
CUDA_VISIBLE_DEVICES={GPU} python -u src/evaluate.py \
    --mode adaptive_conformal_crm \
    --model smolvla \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
    --benchmark {object|spatial|goal} \
    --seed {42|43|44} \
    --n_rollouts 20 \
    --conformal_threshold 0.074855
```

不需要显式指定的参数（已有正确默认值）：
- `--max_steps`: 自动按 suite 设置 (280/280/300)
- `--max_correction_norm`: adaptive mode 自动设为 0.2
- `--K`: 函数内部 hardcode K=2
- `--obs_dim`: 默认 960
- `--n_action_steps`: 仅 PI05 使用

## 5. Checkpoint 可用性

| 服务器 | 路径 | 状态 |
|--------|------|------|
| bjb1-32546 | crm_v3_norm/obs_only/crm_best.pt | ✓ 存在 |
| bjb2-40593 | crm_v3_norm/obs_only/crm_best.pt | ✓ 存在 |
| 两台服务器 | crm_smolvla_3suite_v1/crm_best.pt | ✗ 不存在 |

## 6. 服务器资源

| 服务器 | GPU | 可并行 eval 数 |
|--------|-----|---------------|
| bjb1-32546 | 6× RTX 4090 | 6 |
| bjb2-40593 | 1× RTX 4090D | 1 |

## 7. 部署计划

9 个 eval (3 suites × 3 seeds):
- bjb1-32546: batch 1 = 6 jobs (GPU 0-5), batch 2 = 3 jobs (GPU 0-2)
- 或用 `deploy_adaptive_k_eval.sh 0,1,2,3,4,5` 全部发出（tmux 调度）

输出文件: `logs/eval_{suite}_adaptive_conformal_crm_tau0.074855_seed{seed}.json`
