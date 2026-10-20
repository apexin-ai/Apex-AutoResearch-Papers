# diag random occ v2 s0 loss

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_random_occ_v2_s0_loss_20260528T223731_result.json`
- **Structured JSON:** [`3d2389dc89112a1a1abb.json`](../../sessions/3d/3d2389dc89112a1a1abb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Root cause confirmed. Here's the diagnosis:

## 1. 实际运行命令

```bash
torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 \
  --save_freq 10000 --image_aug True --lora_rank 32 \
  --run_root_dir /root/autodl-tmp/checkpoints/random_occ_v2_s0 \
  --run_id_note random_occ_v2_s0 --seed 42 \
  --use_occ_head True --occ_detach False --occ_norm_type bn --random_occ True
```

**缺少 `--occ_data_dir /root/occsafe_vla/occ_data`。**

## 2. 根因

代码逻辑链：

1. `occ_data_dir` 默认值为 `""` (finetune.py:91)
2. 空字符串传入 dataset → `if self.occ_data_dir:` 为 False (datasets.py:200) → occ labels 从未加载
3. batch 中没有 `"occ_labels"` key → `if occ_head is not None and "occ_labels" in batch:` (finetune.py:484) 为 False → occ loss 计算整段跳过
4. `random_occ` 标志只是 shuffle 已加载的 labels (finetune.py:491-492)，不会自己生成随机数据。没有 labels 可 shuffle → 无效果

**occ_loss=0 是因为 occ 分支从未执行，不是因为 loss 计算结果恰好为零。**

## 3. 实验是否有效

**无效。** 当前实验等同于 vanilla 训练（无 OCC 辅助监督），不是 "random OCC" 消融实验。需要 kill 并重启。

## 4. 正确的训练命令

需要补上 `--occ_data_dir`：

```bash
torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 \
  --save_freq 10000 --image_aug True --lora_rank 32 \
  --run_root_dir /root/autodl-tmp/checkpoints/random_occ_v2_s0 \
  --run_id_note random_occ_v2_s0 --seed 42 \
  --use_occ_head True --occ_detach False --occ_norm_type bn --random_occ True \
  --occ_data_dir /root/occsafe_vla/occ_data
```

是否现在 kill PID 33308 并用修正后的命令重启？

---
