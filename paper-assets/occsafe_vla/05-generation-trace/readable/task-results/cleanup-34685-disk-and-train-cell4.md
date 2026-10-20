# cleanup 34685 disk and train cell4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_34685_disk_and_train_cell4_20260527T151904_result.json`
- **Structured JSON:** [`7a4be608309a73433187.json`](../../sessions/7a/7a4be608309a73433187.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 deletions complete. 89GB freed, 121GB now available.

---

## 汇报

### 磁盘清理结果

| 删除项 | 释放空间 |
|--------|---------|
| `detach_ln_v2_s1/` (Cell 4 v2, s1_35 eval 已完成 CAR=0.826) | 30GB |
| `detach_ln_s4/` (Cell 4 v1, anomalous/failed) | 30GB |
| `ablation_occ_detach_s4/` (Cell 3 eval 已完成 CAR=0.738) | 29GB |
| **合计** | **89GB** |

清理前：32GB 可用 (91%) → 清理后：**121GB 可用 (66%)**

### 训练命令（detach_ln_v2_s2, seed 44, cuda:0）

```bash
bash -c "source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --use_diffusion False --use_film False --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 --save_freq 5000 --image_aug True --lora_rank 32 --run_root_dir /root/autodl-tmp/checkpoints/detach_ln_v2_s2 --run_id_note detach_ln_v2_s2 --seed 44 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach True --occ_norm_type ln"
```

### 环境确认

- v2 代码 ✓ — `occ_norm_type` 参数存在于 `finetune.py:98`，默认 `"bn"`，命令显式传 `ln`
- `occ_detach` ✓ — `finetune.py:97`，默认 `False`，命令显式传 `True`
- 训练数据 ✓ — `/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops`
- OCC 标签 ✓ — `/root/occsafe_vla/occ_data/` (9 个 HDF5 + index)
- Base model ✓ — `/root/autodl-tmp/models/openvla-7b`
- Conda env `occsafe` ✓ — `/root/miniconda3/etc/profile.d/conda.sh`
- 磁盘 ✓ — 121GB 可用，训练预计 ~50GB checkpoint 空间

---
