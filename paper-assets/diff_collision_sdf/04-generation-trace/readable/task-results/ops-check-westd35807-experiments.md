# ops check westd35807 experiments

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd35807-experiments_20260528T223126_result.json`
- **Structured JSON:** [`7ab1c0339578b851f923.json`](../../sessions/7a/7ab1c0339578b851f923.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-35807 实验状态汇报

### GPU 状态
| GPU | 型号 | 显存 | 状态 |
|-----|------|------|------|
| 0 | NVIDIA RTX PRO 6000 | 96GB | **空闲** (0 MiB / 0%) |
| 1-3 | — | — | 不可见（nvidia-smi 仅显示 1 张卡） |

无任何 Python 训练进程运行。tmux session "default" 存在。

### Phase 2 s2 λ=0 训练（train_phase2_lambda0_s2_gpu3.log）
- **已完成** A1 阶段 10000/10000 步，完成时间 2026-05-26 19:13
- 之后 resumed 继续训练，推进到 step ~20000 时**因磁盘满崩溃**
- 末尾 loss 指标：action≈0.015, sdf≈0.133, ee≈0.008
- best_loss: 0.00651 @ step 4000

### 同时进行的 seed0_l0 训练
- 推进到 step ~14000 时也**因磁盘满崩溃**
- tmp_14000 checkpoint 严重损坏（512K）

### 磁盘使用
| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (root) | 30G | 25G | 6G | 81% |
| /root/autodl-tmp/ | 350G | **350G** | **16K** | **100%** |

**数据盘已满，这是两个训练崩溃的直接原因。**

### Checkpoint 磁盘占用明细 (290G)
| 目录 | 大小 | 说明 |
|------|------|------|
| object_pudding 总计 | **247G** | |
| — seed0_l0 | 22G | 崩溃于 ~step 14000 |
| — seed0_l005 | 7.2G | |
| — seed0_l01 | 7.2G | |
| — seed0_l1 | 22G | |
| — seed1_l005 | 29G | |
| — seed1_l01 | 29G | |
| — seed1_l1 | 22G | |
| — seed2_l0 | 26G | 崩溃于 ~step 20000 |
| — seed2_l005 | 29G | |
| — seed2_l01 | 29G | |
| — phase2_stage1_seed0_l005 | 22G | |
| — baseline_seed0 | 7.2G | |
| — baseline_seed1 | **1.6M** | **已确认损坏**（应 ~7G） |
| spatial_bowl 总计 | **43G** | |
| HF cache | 9.2G | |

### 损坏的 Checkpoint（3个）
1. **`pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors`** — 1.6M（正常应 ~7G），已确认损坏
2. **`seed0_l0/tmp_14000/model.safetensors`** — 512K，磁盘满导致截断
3. **`seed2_l0/tmp_20000/model.safetensors`** — 4.3G（正常应 ~7.1G），磁盘满导致不完整

### 关键问题
**数据盘 100% 已满**，需要清理空间才能恢复任何训练。建议清理损坏的 checkpoint 和不再需要的旧 checkpoint。

---
