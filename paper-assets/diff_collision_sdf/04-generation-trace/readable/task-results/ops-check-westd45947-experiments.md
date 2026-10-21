# ops check westd45947 experiments

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd45947-experiments_20260528T225105_result.json`
- **Structured JSON:** [`c548fa7e86b9e163740d.json`](../../sessions/c5/c548fa7e86b9e163740d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-45947 状态汇总

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|----------|--------|
| cuda:0 | 0 MiB / 97887 MiB | 0% (空闲) |

仅 1 张 GPU（不是 2 张）。无训练进程运行，无 tmux session。仅有 tensorboard 和 jupyter-lab 后台服务。

### eval_phase2_18k_s2 / eval_spatial_bowl_lora_ctrl_s0_v2
**未找到。** 服务器上不存在任何匹配 `phase2`、`18k`、`spatial_bowl_lora_ctrl` 的文件。这两个 eval 尚未执行。

### 现有 eval 结果（最新）

| 实验 | TSR | CAR |
|------|-----|-----|
| multiseed_sdf_l01_s0_eseed123 | 53.5% | 58.5% |
| multiseed_sdf_l01_s0_eseed256 | 48.0% | 57.0% |
| eval_lora_baseline_seed7 (30k) | 54.5% | 54.5% |
| reeval_sdf_s0_l005_30k | 55.5% | 57.0% |
| reeval_sdf_s0_l01_30k | 52.5% | 57.0% |
| reeval_sdf_s1_l01_30k | 55.5% | 57.5% |
| reeval_sdf_s1_l005_30k | 50.5% | 54.0% |
| reeval_sdf_s2_l01_30k | 53.5% | 54.5% |
| reeval_sdf_s2_l005_30k | 56.0% | 52.5% |
| reeval_lora_s1_30k | 51.5% | 52.5% |

### Checkpoint 完整性
- `pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` — **7.1 GB，完好** (路径: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/`)
- checkpoints 总占用约 199 GB

### 磁盘使用
| 分区 | 已用 | 总量 | 使用率 |
|------|------|------|--------|
| / (root) | 17G | 30G | 57% |
| /root/autodl-tmp (数据盘) | **240G** | **250G** | **96%** ⚠️ |

数据盘快满了，checkpoints 占 ~199G。如需运行新实验，可能需要清理旧 checkpoint。

---
