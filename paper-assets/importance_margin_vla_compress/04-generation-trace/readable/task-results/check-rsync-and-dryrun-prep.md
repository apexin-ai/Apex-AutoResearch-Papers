# check rsync and dryrun prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_rsync_and_dryrun_prep_20260516T192913_result.json`
- **Structured JSON:** [`1706a5836640f3c5e394.json`](../../sessions/17/1706a5836640f3c5e394.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. rsync 状态：**进行中**
- 进度：384/777 files（约 49%），已传 ~29GB
- 传输速度：~15MB/s
- 预计剩余时间：约 30-40 分钟

### 2. LIBERO 数据路径和大小
| 路径 | 大小 | 说明 |
|------|------|------|
| `/root/autodl-tmp/.hf_cache/lerobot/hub/datasets--HuggingFaceVLA--libero/` | 29G（仍在传输） | HF cache 格式，379个 parquet |
| `/root/autodl-tmp/.hf_cache/lerobot/hub/datasets--lerobot--libero_10/` | 624M | libero_10 子集（完整） |

### 3. Full FT checkpoint 位置
- **westd**: `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_full_ft_50k/checkpoint.pt` (1.26GB) ✓

### 4. Dry-run 结果：**成功** ✓
使用 LoRA 版 twostage 配置（`libero_imm_twostage.yaml`），两个阶段均通过：
- **Stage 1** (ACIS only): margin_loss=0.2988, grad=4.68, ACIS trainable=3,460,801 (0.76%)
- **Stage 2** (LoRA only): action_loss=0.0877, grad=0.38, LoRA 74 params trainable
- Gradient isolation 验证通过（Stage1 LoRA grad=0, Stage2 ACIS grad=0）

### 5. 前置条件备注
- 网络必须启用代理 (`source /etc/network_turbo`)，否则 HF hub 不通
- 环境变量：`HF_LEROBOT_HOME`（非 `LEROBOT_HOME`），`HF_HUB_DISABLE_XET=1`
- Full FT-based IMM 配置 (`libero_imm_twostage_fullft.yaml`) 尚未创建——需要将 `model.lora.rank` 设为 0 + `model.train_expert_only: true`，并指向 `checkpoints/libero_full_ft_50k/checkpoint.pt`
- rsync 完成后数据集即可用于正式训练（dry-run 已验证 dataset loading 正常）

---
