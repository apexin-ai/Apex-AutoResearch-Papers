# code prepare spatial bowl lora control

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_spatial_bowl_lora_control_20260526T120342_result.json`
- **Structured JSON:** [`66ea2e8a533f429b2e0a.json`](../../sessions/66/66ea2e8a533f429b2e0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是产出：

---

## Plan 015: spatial_bowl LoRA-only Control

### 配置核对

| 参数 | SDF 训练 (plan_007) | LoRA-only Control (plan_015) |
|------|-------|---------|
| 脚本 | `train_a1_sdf_aux_pi05.py` | `train_pi05_lora_baseline.py` |
| scene | spatial_bowl | spatial_bowl |
| seed | 0 | 0 |
| batch_size | 32 | 32 |
| num_train_steps | 30000 | 30000 |
| lr | 2.5e-5 | 2.5e-5 |
| warmup_phase_steps | 5000 | 5000 |
| save_interval | 2000 | 2000 |
| LoRA config | pali_rank=16, expert_rank=32 | 同上 |
| lambda_sdf | 0.005 | N/A (无 SDF decoder) |
| lambda_ee | 0.01 | N/A (无 EE extractor) |
| 模型 | Pi0.5 (pi05_libero) | 同上 |
| 数据 | safelibero_spatial | 同上 |
| exp_name | `a1_sdf_pi05_spatial_bowl_seed0_l005` | `pi05_lora_baseline_spatial_bowl_seed0` |
| checkpoint | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/` | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/` (同 name) |

### GPU 状态
- GPU 0-2: 占用中 (~27GB each, 100% utilization)
- **GPU 3: 空闲**，可立即启动

### 之前的 baseline_lora_spatial_bowl_s0.log
是用旧脚本 `train_baseline.py` 跑的，启动就报错失败了。没有残留 checkpoint。

### 训练命令（tmux 启动，预估 >30h）

```bash
tmux new-session -d -s plan015 "cd /root/colliforce-vla && source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && export WANDB_MODE=disabled && python scripts/train_pi05_lora_baseline.py --scene spatial_bowl --seed 0 --gpu 3 --batch_size 32 --num_train_steps 30000 --lr 2.5e-5 --save_interval 2000 --log_interval 100 2>&1 | tee /root/runs/diff_collision_sdf/plan015_lora_baseline_spatial_bowl_s0.log"
```

### 预估训练时间
SDF 训练 ~4.63s/step。LoRA-only 无 SDF/EE 计算开销，预估 ~4.0-4.3s/step，30000 steps ≈ **33-36 小时**。

### 注意事项
- `train_pi05_lora_baseline.py` 原生支持 spatial_bowl，无需改代码
- Phase 1/2 调度与 SDF 训练完全一致（Phase 1: 5000 steps LoRA frozen, Phase 2: LoRA unfrozen + gradient warmup）
- 唯一差异：无 SDF decoder 和 EE extractor，loss 只有 action loss
- GPU 3 现在就空闲，不需要等 SDF 训练完成

---
