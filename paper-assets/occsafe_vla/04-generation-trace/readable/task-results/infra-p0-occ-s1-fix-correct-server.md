# infra P0 occ s1 fix correct server

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_P0_occ_s1_fix_correct_server_20260521T011356_result.json`
- **Structured JSON:** [`10555f288456a4e541c3.json`](../../sessions/10/10555f288456a4e541c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 状态 |
|------|------|
| hostname | westd-34685 ✓ |
| occ_s0 (PID 27667→子进程27740) | **ALIVE**, 运行 8h39m, GPU 0: 62194 MiB |
| occ_s2 (PID 29970→子进程30044) | **ALIVE**, 运行 8h38m, GPU 2: 62200 MiB |
| occ_s1 旧错误进程 | 已 kill (54258/54259/54330), 坏 checkpoint 10000/12500 已删除 |
| occ_s1 checkpoint 最高 | 7500 (从此恢复) |

**occ_s0 完整命令行**:
```
WANDB_MODE=disabled CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 \
  --save_freq 2500 --image_aug True --lora_rank 32 \
  --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false \
  --run_root_dir /root/autodl-tmp/checkpoints/occ_s0 --seed 42
```

**occ_s1 重启**:
- 新子进程 PID: **58875**
- GPU 1: **62194 MiB** ✓ (与 s0/s2 一致，之前错误进程只有 43012 MiB)
- 速度: **~1.07 it/s** ✓
- 参数验证: **PASS** — num_images_in_input=2, use_proprio=True, batch_size=8, lora_rank=32, use_occ_head=True, occ_detach=false, seed=43, resume_step=7500
- 首步 loss: occ_loss=0.0126, action_loss=0.1367

---
