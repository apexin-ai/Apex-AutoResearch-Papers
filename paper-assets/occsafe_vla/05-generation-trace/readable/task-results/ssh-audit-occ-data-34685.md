# ssh audit occ data 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_audit-occ-data-34685_20260528T225633_result.json`
- **Structured JSON:** [`04bcaf0d91805cb415b7.json`](../../sessions/04/04bcaf0d91805cb415b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整审计结果。

---

## M096 审计结果：westd-34685 occ_data_dir 和 occ_loss

### 1. RUNNING 实验完整命令行（PID 19218）

```
torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py
  --vla_path /root/autodl-tmp/models/openvla-7b
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/
  --dataset_name libero_spatial_no_noops
  --use_l1_regression True --use_diffusion False --use_film False
  --num_images_in_input 2 --use_proprio True --batch_size 8
  --learning_rate 5e-4 --num_steps_before_decay 100000
  --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32
  --run_root_dir /root/autodl-tmp/checkpoints/full_occ_bn_v2_s2_r2
  --run_id_note full_occ_bn_v2_s2_r2 --seed 44
  --use_occ_head True --occ_detach False --occ_norm_type bn
```

**没有 `--occ_data_dir` 参数。**

### 2. occ_loss 对比（按是否加载了 occ 数据分组）

#### occ 数据已加载（日志中有 `Loaded occ index: 9 tasks, 55370 samples`）

| 实验 | 启动日期 | step=0 occ_loss | 最终 occ_loss |
|---|---|---|---|
| full_occ_bn_v2_s1 | 05/26 | **0.1853** | 0.0100 (step 50000) |
| detach_bn_v2_s0 | 05/26 | **0.1014** | 0.0095 (step 50000) |
| detach_ln_v2_s1 | 05/27 | **0.1963** | 0.0325 (step 200, 进行中) |

#### occ 数据未加载（日志中无 occ preload 行）

| 实验 | 启动日期 | occ_loss | 状态 |
|---|---|---|---|
| full_occ_bn_v2_s2 | 05/28 | **0.0000 始终** | 运行中 ~24000步 |
| full_occ_bn_v2_s2_r2 (RUNNING) | 05/29 | **0.0000 始终** | 运行中 ~12500步 |
| detach_ln_v2_s2 | 05/28 (resume) | **0.0000 始终** | 已完成 |
| full_occ_ln_v2_s3 | 05/28 | **0.0000 始终** | 进行中 |
| detach_ln_v2_s3 | 05/28 | **0.0000 始终** | 进行中 |

### 3. 结论

**05/26-27 启动的实验**正确加载了 `/root/occsafe_vla/occ_data/occ_index.json`（9 tasks, 55370 samples），occ_loss 非零且正常下降。

**05/28 之后启动的所有实验**均未加载 occ 数据，occ_loss 从 step 0 起恒为 0.0000。occ_head 虽然被创建（参数 1,213,313），但从未接收到训练信号，**等同于 vanilla baseline + 死权重**。

当前 RUNNING 的 `full_occ_bn_v2_s2_r2` 属于后者——occ_loss=0.0000 到 step 12500，这个实验产出的 checkpoint 在 occ 维度上无意义。

---
