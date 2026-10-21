# ssh gpu audit westd35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_audit_westd35807_20260520T202033_result.json`
- **Structured JSON:** [`5780d3ed62609d3c9386.json`](../../sessions/57/5780d3ed62609d3c9386.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 全面核查报告

```
cuda:0 → PID 222903 / baseline_spatial_bowl_s0_v2 / step 19716/30000 (66%) / alive (5h44m) / 35738 MiB / 100% util / 69°C
cuda:1 → PID 227389 / a1_sdf_object_pudding_s0   / step 5689/30000  (19%) / alive (5h34m) / 13376 MiB / 100% util / 49°C
cuda:2 → PID 222982 / baseline_object_pudding_s0_v2 / step 21729/30000 (72%) / alive (5h44m) / 35738 MiB / 0% util* / 60°C
cuda:3 → PID 185994 / a1_sdf_spatial_bowl_s0_v3   / step 17960/30000 (60%) / alive (11h57m) / 13376 MiB / 0% util* / 39°C
```

\* GPU 2/3 util=0% 是 nvidia-smi 瞬时采样，进程活着且日志在推进，正常。

### 磁盘
| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / | 30G | 17G | 14G | 54% |
| /root/autodl-tmp | 350G | 177G | 174G | 51% |

### 最新 Checkpoint
| 实验 | 最新 ckpt | 时间 | 路径 |
|------|-----------|------|------|
| baseline_spatial_bowl | step 18000 | May 21 02:38 | `/root/autodl-tmp/checkpoints/baseline_spatial_bowl/baseline_spatial_bowl_seed0/18000/` |
| baseline_object_pudding | step 20000 | May 21 02:37 | `/root/autodl-tmp/checkpoints/baseline_object_pudding/baseline_object_pudding_seed0/20000/` |
| a1_sdf_spatial_bowl | step 16000 | May 21 02:23 | `/root/autodl-tmp/checkpoints/a1_sdf_spatial_bowl/a1_sdf_spatial_bowl_seed0/16000/` |
| a1_sdf_object_pudding | step 4000 | May 21 02:43 | `/root/autodl-tmp/checkpoints/a1_sdf_object_pudding/a1_sdf_object_pudding_seed0/4000/` |

### 训练速度 & Loss
| 实验 | 当前 step | speed | loss | lr |
|------|-----------|-------|------|----|
| baseline_spatial_bowl | 19716 | ~3.5s/it | 0.0034 | 8.79e-06 |
| baseline_object_pudding | 21729 | ~3.5s/it | 0.0060 | 6.72e-06 |
| a1_sdf_spatial_bowl | 17960 | ~3.1s/it | 0.2732 | 1.08e-05 |
| a1_sdf_object_pudding | 5689 | ~3.0s/it | 0.2023 | 2.36e-05 |

**4 卡全部在用，无空闲 GPU。所有进程存活，训练正常推进。**

---
