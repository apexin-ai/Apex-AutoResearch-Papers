# ops fix c5 gpu conflict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_c5_gpu_conflict_20260519T212612_result.json`
- **Structured JSON:** [`91aa1e1e98b6194c35a7.json`](../../sessions/91/91aa1e1e98b6194c35a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

---

## 修复报告

### 1. 修复前 GPU 状态
| GPU | 进程 | 显存 |
|-----|------|------|
| 0 | PID 26118 (C4-ext) + PID 45729 (C5) | 78204MiB |
| 1-3 | 空闲 | 0-3MiB |

### 2. Kill 的进程
- **PID 45729** — C5 RoboFlamingo 主进程（`train_libero.py`，错误运行在 GPU 0）
- **PID 41508, 41516, 41517, 41520, 41820, 41829, 42093, 42101, 42102** — 之前多次失败的 C5 僵尸进程（STAT=Tl，已停止态）

### 3. C4-ext 确认安全
- **PID 26118**，STAT=Rl（运行中）
- 最新 log：`step=5950/100000  loss=2.9936  lr=9.94e-05  grad=0.86  sps=0.6`（05:26:47）
- Log 路径：`/root/runs/importance_margin_vla_compress/train_openvla_sc_m128_seed42.log`

### 4. C5 重启命令
```bash
tmux new-session -d -s c5_roboflamingo \
  "cd /root/autodl-tmp/RoboFlamingo && \
   source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
   export HF_HUB_OFFLINE=1 && \
   CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u train_libero.py \
     --suite libero_object \
     --data_dir /root/autodl-tmp/libero_data/datasets/libero_object \
     --num_epochs 50 --batch_size 8 --lr 1e-4 --window_size 12 \
     --gpu 0 \
     --save_dir /root/autodl-tmp/checkpoints/roboflamingo_libero_c5 \
     --log_interval 50 --save_interval 5 \
     2>&1 | tee /root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_gpu1.log"
```

### 5. 修复后 GPU 状态
| GPU | 进程 | 显存 | GPU-Util |
|-----|------|------|----------|
| 0 | PID 26118 (C4-ext VTC-only) | 30108MiB | 0% |
| 1 | PID 47691 (C5 RoboFlamingo) | 48080MiB | 92% |
| 2 | 空闲 | 0MiB | 0% |
| 3 | 空闲 | 0MiB | 0% |

### 6. C5 新进程
- **PID 47691**，CUDA_VISIBLE_DEVICES=1
- Log：`/root/autodl-tmp/importance_margin_vla_compress/logs/train_c5_roboflamingo_gpu1.log`
- tmux session：`c5_roboflamingo`
- 状态：模型已加载（2724M params），500 episodes loaded，开始训练

---
