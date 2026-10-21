# code find ln flag

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_find_ln_flag_20260525T112403_result.json`
- **Structured JSON:** [`9e7dc8b9573a0cf5a722.json`](../../sessions/9e/9e7dc8b9573a0cf5a722.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已全部收集完毕。

## 结果

**参数名**: `--occ_norm_type`  
**值**: `"ln"` (LayerNorm) 或 `"bn"` (BatchNorm, 默认)

定义位置: `finetune.py:98`
```python
occ_norm_type: str = "bn"  # Norm type for occ head: "bn" (BatchNorm) or "ln" (GroupNorm-1 = LayerNorm)
```

实现位置: `prismatic/models/occ_head.py:23` — 当 `norm_type == "ln"` 时使用 `nn.GroupNorm(1, channels)` (等价于 LayerNorm)。

---

**完整训练命令模板** (`full_occ_ln` 系列):

```bash
torchrun --standalone --nnodes 1 --nproc-per-node 4 \
  vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --dataset_name libero_spatial_no_noops \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds \
  --run_root_dir /root/autodl-tmp/checkpoints/full_occ_ln_s{SEED} \
  --use_l1_regression true \
  --use_proprio true \
  --use_occ_head true \
  --occ_data_dir /root/occsafe_vla/occ_data \
  --occ_loss_weight 0.01 \
  --occ_norm_type ln \
  --occ_resolution 64 \
  --batch_size 8 \
  --learning_rate 5e-4 \
  --max_steps 50000 \
  --save_freq 10000 \
  --seed {SEED} \
  --image_aug true \
  --wandb_project occsafe_vla \
  --wandb_entity {YOUR_ENTITY}
```

关键差异：`full_occ_bn` 用 `--occ_norm_type bn`（或省略，默认就是 bn），`full_occ_ln` 用 `--occ_norm_type ln`。

---
