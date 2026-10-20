# ssh audit occ data 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_audit-occ-data-10894_20260528T225639_result.json`
- **Structured JSON:** [`99c589bdedae1f1b1a4b.json`](../../sessions/99/99c589bdedae1f1b1a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部审计完成。

---

## M096 审计结果

### 1. PID 33308 完整命令行 (random_occ_v2_s0)

```
torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 \
  --max_steps 50005 --save_freq 10000 --image_aug True \
  --lora_rank 32 \
  --run_root_dir /root/autodl-tmp/checkpoints/random_occ_v2_s0 \
  --run_id_note random_occ_v2_s0 --seed 42 \
  --use_occ_head True --occ_detach False --occ_norm_type bn \
  --random_occ True
```

**没有 `--occ_data_dir` 参数。**

---

### 2. v2 实验 occ_loss 汇总

| 实验 | 加载 occ 数据 | occ_loss@step0 | occ_loss@最后 | 状态 |
|------|:---:|---:|---:|---:|
| **full_occ_ln_v2_s2** | ✅ 9 tasks, 55370 samples | 0.1533 | 0.0068 @50000 | 完成 |
| **full_occ_ln_v2_s1c** | ✅ 9 tasks, 55370 samples | 0.1730 | 0.0106 @50000 | 完成 |
| **full_occ_bn_v2_s3** | ❌ 无加载 | 0.0000 | 0.0000 @21300 | killed(-9) @21329 |
| **detach_ln_v2_s4** | ❌ 无加载 | 0.0000 | 0.0000 @45000 | 运行中/完成 |
| **random_occ_v2_s0** | ❌ 无加载 | 0.0000 | 0.0000 @12600 | 运行中 (PID 33308) |

---

### 3. 当前 RUNNING 实验 occ_loss 趋势

`random_occ_v2_s0` 从 step 0 到 step 12600，**occ_loss 始终为 0.0000**。127 次 AUX 日志记录全部为 0。

---

### 根因

启动日志中的关键区别：
- **有非零 occ_loss 的实验**（ln_v2_s2, ln_v2_s1c）都打印了 `"Loaded occ index: 9 tasks from /root/occsafe_vla/occ_data/occ_index.json"` + `"Occ preload done: 9 files, 55370 samples"`
- **occ_loss=0 的实验**（bn_v2_s3, detach_ln_v2_s4, random_occ_v2_s0）启动日志中**没有任何 occ 数据加载信息**，直接跳到 dataset statistics 加载

对于 `random_occ_v2_s0`：虽然传了 `--random_occ True`（理论上应生成随机 occupancy targets），但实际没有触发 occ 数据/目标生成，occ_loss 恒为 0。**`--random_occ True` 模式有 bug——occ head 在训练但 loss 从未回传。**

对于 `full_occ_bn_v2_s3`：名为 "full_occ" 但命令行中缺少 `--occ_data_dir`，导致没有加载 occ 数据。6 小时 GPU 时间浪费。

---
