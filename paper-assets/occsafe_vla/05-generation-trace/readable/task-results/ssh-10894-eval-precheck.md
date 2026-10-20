# ssh 10894 eval precheck

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_10894_eval_precheck_20260525T212859_result.json`
- **Structured JSON:** [`f7c86dbf43ba9d1e58ca.json`](../../sessions/f7/f7c86dbf43ba9d1e58ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 10894 Eval 预检

| 项目 | 状态 | 详情 |
|------|------|------|
| Eval 脚本 | ✅ | `/root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py` (draccus-based) |
| SafeLIBERO 数据 | ✅ | `/root/autodl-tmp/libero_datasets/libero_spatial` |
| MuJoCo | ✅ | v3.8.1, EGL 模块存在 |
| robosuite | ✅ | 已安装 |
| CKA 脚本 | ✅ | `/root/occsafe_vla/analysis/cka_analysis.py` |
| Batch eval 脚本 | ⚠️ | `eval_batch_10894.sh` 存在但**路径指向旧实验**（见下） |

### Checkpoint 命名格式（v2 实验）

```
/root/autodl-tmp/checkpoints/&lt;exp_name>/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--&lt;exp_name>--50000_chkpt
```

当前 v2 checkpoints 状态（均为训练中的 running dir，尚无 `--50000_chkpt`）：
- `mvp_occ_s3_v2` — 仅 running dir
- `full_occ_ln_s3_v2` — 仅 running dir
- `ablation_occ_detach_s3_v2` — 仅 running dir
- `cutoff_45k_s2_v2` — 有 `--10000_chkpt`（中间检查点），无 50k

### 示例 eval 命令（s3 ablation_occ_detach_s3_v2）

```bash
cd /root/occsafe_vla/openvla-oft && \
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 \
  python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3_v2--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50
```

### ⚠️ 需要修复

**`eval_batch_10894.sh` 路径错误**：当前脚本引用旧路径（`mvp_occ_s3`, `full_occ_ln_s3`, `ablation_occ_detach_s3`），v2 实验的 checkpoint 名称带 `_v2` 后缀。训练完成前需更新此脚本，否则会因路径不存在直接 abort。

正确映射应为：
```
mvp_occ_s3_v2       → ${CKPT_ROOT}/mvp_occ_s3_v2/${P}--mvp_occ_s3_v2--50000_chkpt
full_occ_ln_s3_v2   → ${CKPT_ROOT}/full_occ_ln_s3_v2/${P}--full_occ_ln_s3_v2--50000_chkpt
ablation_occ_detach_s3_v2 → ${CKPT_ROOT}/ablation_occ_detach_s3_v2/${P}--ablation_occ_detach_s3_v2--50000_chkpt
cutoff_45k_s2_v2    → ${CKPT_ROOT}/cutoff_45k_s2_v2/${P}--cutoff_45k_s2_v2--50000_chkpt
```

---
