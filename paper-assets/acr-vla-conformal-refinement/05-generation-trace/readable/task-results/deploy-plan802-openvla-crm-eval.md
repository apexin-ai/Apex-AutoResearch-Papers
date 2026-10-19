# deploy plan802 openvla crm eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_plan802-openvla-crm-eval_20260528T033809_result.json`
- **Structured JSON:** [`aa720f2618f5048008db.json`](../../sessions/aa/aa720f2618f5048008db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署总结

### 环境验证 ✓
| 检查项 | 状态 |
|--------|------|
| CRM checkpoint (`crm_k1_best.pt`, 3.7MB) | ✓ 存在 |
| OpenVLA model (`openvla-libero-object`, 15.1GB bf16) | ✓ 加载成功 |
| Eval 脚本 (`openvla_eval.py --mode crm_k1_multiscale`) | ✓ 已实现 |
| MultiScaleCRM (action_dim=6, obs_dim=4096, 908K params) | ✓ 加载成功 |
| Multi-scale hooks (layers [7,15,23,31]) | ✓ 注册成功 |

### 已部署实验

| exp_id | GPU | seed | PID | 状态 |
|--------|-----|------|-----|------|
| `eval-openvla-crm-k1-object-seed42` | cuda:4 | 42 | 95773 | RUNNING（task 1, rollout 1/20 完成，avg 190ms/step） |
| `eval-openvla-crm-k1-object-seed43` | cuda:5 | 43 | 97487 | RUNNING（模型加载中） |

### Eval 命令
```
python -u src/openvla_eval.py \
  --benchmark object \
  --model_path /root/autodl-tmp/models/openvla-libero-object \
  --mode crm_k1_multiscale \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object/crm_k1_best.pt \
  --max_correction_norm 0.2 \
  --n_rollouts 20 --seed {42,43} --gpu 0
```

### 无法部署的项目

**seed44**: GPU 0-3 均有 1702-1875 MiB 占用（>500 MiB，C001 约束），GPU 4-5 已被占用。需等 seed42 或 seed43 完成后部署。

**备选实验**（同理无空闲 GPU）：
- `eval-random-selection-object-seed43`: `python -u src/evaluate.py --mode random_selection --benchmark object --seed 43 --K 10 --n_rollouts 20`
- `eval-ksweep-k20-obs-object-s44`: `python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --K 20 --n_rollouts 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2`

预计每个 eval 运行约 2-3 小时（200 rollouts × 300 steps × ~190ms/step）。

---
