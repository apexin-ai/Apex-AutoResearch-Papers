# prep cell2 v2 eval commands

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_cell2_v2_eval_commands_20260527T141742_result.json`
- **Structured JSON:** [`1eb69c9c614630d9d519.json`](../../sessions/1e/1eb69c9c614630d9d519.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在 ~47k/50k，约 45-50 分钟内完成。

汇总结果：

---

## Eval 准备方案

### 训练进度
- **full_occ_ln_v2_s1c**: step 46806/50005，~49 min 后完成
- **full_occ_ln_v2_s2**: step 47030/50005，~46 min 后完成

### Checkpoint 路径（10894 上）
```
# s1c
/root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c--50000_chkpt

# s2
/root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2--50000_chkpt
```

### 前置步骤：scp checkpoint 到 34685

**磁盘空间警告**：34685 `/root/autodl-tmp` 仅剩 32GB，每个 checkpoint ~15GB，两个共 ~30GB。空间极其紧张。

从 10894 拷贝到 34685（在 10894 上执行）：
```bash
# s1c checkpoint → 34685
mkdir -p /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/ && \
scp -r westd-10894:/root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c--50000_chkpt \
  /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/
```

```bash
# s2 checkpoint → 34685
mkdir -p /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/ && \
scp -r westd-10894:/root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2--50000_chkpt \
  /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/
```

（需要在 34685 上执行，或根据 SSH 配置调整方向。如果服务器间无直连，需通过跳板机或 agent 本机中转。）

### Eval 命令（在 34685 上执行）

**full_occ_ln_v2_s1c eval（GPU 0）：**
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && \
CUDA_VISIBLE_DEVICES=0 MUJOCO_EGL_DEVICE_ID=0 MUJOCO_GL=egl \
python3 vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > /root/occsafe_vla/logs/full_occ_ln_v2_s1c_r2_eval.log 2>&1 &
```

**full_occ_ln_v2_s2 eval（GPU 1）：**
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && \
CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 MUJOCO_GL=egl \
python3 vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42' > /root/occsafe_vla/logs/full_occ_ln_v2_s2_r2_eval.log 2>&1 &
```

**监控：**
```bash
tail -f /root/occsafe_vla/logs/full_occ_ln_v2_s1c_r2_eval.log /root/occsafe_vla/logs/full_occ_ln_v2_s2_r2_eval.log
```

### 时间估算
- 训练完成：~当前 +50 min
- scp 传输：15GB/checkpoint，取决于带宽（内网 1Gbps ~2min/checkpoint，100Mbps ~20min）
- Eval 运行：~30-40 min/experiment
- 如果 GPU 0/1 被占用，可改用其他空闲 GPU（调整 CUDA_VISIBLE_DEVICES 和 MUJOCO_EGL_DEVICE_ID 一致即可）

---
