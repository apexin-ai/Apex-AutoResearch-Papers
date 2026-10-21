# ops config consistency audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_config_consistency_audit_20260523T092807_result.json`
- **Structured JSON:** [`6dbfef9cc9d2a10739ef.json`](../../sessions/6d/6dbfef9cc9d2a10739ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整审计结果：

---

## 配置一致性审计结果

### 核心发现：cutoff_s2 配置错误，结果不可比

**铁证：trainable params 对比（同一 finetune.py 输出）**

| 实验 | proprio_projector | occ/depth_head | total trainable | 推断 use_proprio |
|------|:-:|:-:|:-:|:-:|
| mvp_vanilla_s0 | 16,818,176 | — | 278,764,295 | **True** |
| cutoff_s0 | 16,818,176 | 1,213,313 | 279,977,608 | **True** |
| cutoff_s1 | 16,818,176 | 1,213,313 | 279,977,608 | **True** |
| **cutoff_s2** | **缺失** | 1,213,313 | **263,159,432** | **False** |
| depth_s0 | 16,818,176 | 1,213,313 | 279,977,608 | **True** |
| depth_s1 | 16,818,176 | 1,213,313 | 279,977,608 | **True** |
| depth_s2 | 16,818,176 | 1,213,313 | 279,977,608 | **True** |
| depth_s3 | 16,818,176 | 1,213,313 | 279,977,608 | **True** |

cutoff_s2 少了 16,818,176 参数（恰好是 proprio_projector），确认 `use_proprio=False`。

### 速度对比（同一服务器 westd-10894）

| 实验 | 速度 | 服务器 |
|------|------|--------|
| cutoff_s0 | ~1.07 it/s | westd-34685 |
| cutoff_s1 | ~1.06 it/s | westd-34685 |
| **cutoff_s2** | **~2.05 it/s** | westd-10894 |
| depth_s2 | ~1.08 it/s | westd-10894 |
| depth_s3 | ~1.08 it/s | westd-10894 |

同服务器 depth_s2/s3 为 1.08 it/s，cutoff_s2 为 2.05 it/s，**1.9x 速度差**。depth 有 proprio 而 cutoff_s2 没有，但 proprio_projector 只增加 ~6% 参数，不足以解释 2x 差异。剩余的速度差来自 `num_images_in_input=1`（默认值）vs `2`——少处理一张图像直接减半 vision token 数量。

### finetune.py 默认值

```python
num_images_in_input: int = 1    # line 86
use_proprio: bool = False        # line 87
```

### cutoff_s2 的 registry 命令（确认缺失参数）

```bash
CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled torchrun --nproc_per_node 1 \
  vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --dataset_name libero_spatial_no_noops \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds \
  --occ_data_dir /root/occsafe_vla/occ_data \
  --run_root_dir /root/autodl-tmp/checkpoints/cutoff_s2 \
  --use_occ_head True --occ_loss_cutoff_step 35000 \
  --save_freq 10000 --max_steps 50005 --seed 44
# 缺失: --num_images_in_input 2 --use_proprio True
```

### Eval 命令问题

cutoff_s2_eval 使用了 `--use_proprio False`，与（错误的）训练配置一致。但 cutoff_s0_eval / cutoff_s1_eval 的 eval 命令没有显式指定 `--use_proprio`，需要确认 eval 脚本的默认值。

### 综合对比表

| 参数 | cutoff_s0 | cutoff_s1 | **cutoff_s2** | depth_s0 | depth_s1 | depth_s2 | depth_s3 |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| use_proprio | True | True | **False** | True | True | True | True |
| num_images_in_input | 2 (推断) | 2 (推断) | **1 (默认)** | 2 (推断) | 2 (推断) | 2 (推断) | 2 (推断) |
| batch_size | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| learning_rate | 5e-4 | 5e-4 | 5e-4 | 5e-4 | 5e-4 | 5e-4 | 5e-4 |
| use_occ_head | True | True | True | — | — | — | — |
| use_depth_head | — | — | — | True | True | True | True |
| occ_detach | False | False | False | — | — | — | — |
| seed | 42 | 43 | 44 | 42 | 43 | 44 | 45 |
| it/s | ~1.07 | ~1.06 | **~2.05** | ~1.08 | ~1.08 | ~1.08 | ~1.08 |
| 服务器 | westd-34685 | westd-34685 | westd-10894 | westd-34685 | westd-34685 | westd-10894 | westd-10894 |

### 结论

**cutoff_s2 必须重训。** 它使用了 `num_images_in_input=1, use_proprio=False`（脚本默认值），而所有其他实验使用 `num_images_in_input=2, use_proprio=True`。这导致模型架构不同（少了 proprio_projector, 少处理一张图像），结果完全不可比。正确的训练命令应该加上 `--num_images_in_input 2 --use_proprio True`。

---
