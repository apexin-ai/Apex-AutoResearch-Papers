# code imm twostage dryrun libero

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_imm_twostage_dryrun_libero_20260516T174503_result.json`
- **Structured JSON:** [`64920f1005cdb67aff09.json`](../../sessions/64/64920f1005cdb67aff09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Config 已恢复。

---

## 报告

### Step 1: Checkpoint 拷贝 ✓
- 源: `cqa1-33015:/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_baseline/step_040000/checkpoint.pt` (883MB)
- 目标: `westd-27271:/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_baseline/step_040000/checkpoint.pt`
- 通过 SSH 密钥认证 + SCP 完成拷贝，文件大小一致 (924,851,886 bytes)
- Config 中 `baseline_checkpoint` 已从 `step_099999` 更新为 `step_040000`

### Step 2: Dry-run 结果 ✓ 全部通过

| 检查项 | 状态 |
|-------|------|
| 模型加载 + checkpoint 应用 | ✓ Loaded baseline weights from step_040000 |
| ACIS 模块初始化 | ✓ 10 params, 3,460,801 trainable (0.76%) |
| LIBERO 数据加载 | ✓ episodes=[0,1] 加载成功 |
| Stage 1 freeze 逻辑 | ✓ LoRA grad=0, ACIS grad=7 |
| Stage 1 forward+backward | ✓ margin_loss=0.2988, grad=2.17 |
| Stage 2 freeze 逻辑 | ✓ ACIS grad=0, LoRA grad=74 |
| Stage 2 forward+backward | ✓ action_loss=0.1206, grad=0.33 |

### 注意事项
- westd 上 LIBERO 完整数据集 (33GB) 尚未下载完。正式训练前需要完整下载（设置 `source /etc/network_turbo` + `HF_LEROBOT_HOME=/root/autodl-tmp/.hf_cache/lerobot` + `HF_HUB_DISABLE_XET=1`）
- cqa1 上 LoRA baseline 仍在训练（当前 step_040000/100000），config 中 baseline_checkpoint 路径在更高 step 可用后需更新

---
