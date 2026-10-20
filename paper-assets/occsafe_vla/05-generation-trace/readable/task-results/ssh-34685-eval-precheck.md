# ssh 34685 eval precheck

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_34685_eval_precheck_20260525T212848_result.json`
- **Structured JSON:** [`d88cd9893f66d8dd0155.json`](../../sessions/d8/d88cd9893f66d8dd0155.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 34685 Eval 预检

| 项目 | 状态 |
|------|------|
| Eval 脚本 | `/root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py` ✅ |
| SafeLIBERO 数据 | `/root/autodl-tmp/libero_datasets/libero_spatial/` (10 tasks hdf5) ✅ |
| MuJoCo | 3.8.1 ✅ |
| robosuite | 1.4.1 ✅ |
| libero | 0.1.1 ✅ |
| EGL (libEGL_nvidia) | `/usr/lib/x86_64-linux-gnu/libEGL_nvidia.so.580.95.05` ✅ |
| Batch 脚本模板 | `/root/occsafe_vla/eval_batch_34685.sh` ✅ |
| 历史 eval 成功 | 33 个 JSON 结果文件已有 ✅ |

**Checkpoint 命名格式**:
```
/root/autodl-tmp/checkpoints/&lt;exp_name>/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--&lt;exp_name>--&lt;step>_chkpt/
```

现有 `detach_bn_v2_s0` 只有 10000_chkpt（D051 训练中，50000_chkpt 尚未生成）。

**D051 eval 示例命令**:
```bash
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
  bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
  cd /root/occsafe_vla/openvla-oft && python3 vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_bn_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s0--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 \
    --seed 42 \
    --output_path /root/occsafe_vla/eval_results/detach_bn_v2_s0_50r_50000.json"
```

**缺失/需要修复**: 无。环境完全就绪，D051 训练完成后可直接复用 `eval_batch_34685.sh`（只需更新 CKPTS 映射到新实验名）。

---
