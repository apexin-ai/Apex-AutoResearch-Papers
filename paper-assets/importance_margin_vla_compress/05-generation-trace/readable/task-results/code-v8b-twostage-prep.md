# code v8b twostage prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8b-twostage-prep_20260515T234505_result.json`
- **Structured JSON:** [`619c694f3327d38da54e.json`](../../sessions/61/619c694f3327d38da54e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证全部通过。

**创建的文件：**
- `configs/imm_anchor_v8b_twostage.yaml` — two-stage 配置（stage1: 10k steps ACIS only, stage2: 20k steps LoRA only）
- `train_twostage.py` — two-stage 训练脚本

**Dry-run 结果：**
- Stage 1: LoRA 冻结 (0 grad)，ACIS 训练 (7 params got grad)，margin_loss=0.30
- Stage 2: ACIS 冻结 (0 grad)，LoRA 训练 (37 params got grad)，action_loss=0.39
- Stage 1→2 之间保存了 checkpoint (`stage1_done/checkpoint.pt`)
- 支持 `--resume_stage2` 从 stage1 checkpoint 直接跑 stage2

**运行命令：**
```bash
# 全量训练
CUDA_VISIBLE_DEVICES=0 python train_twostage.py --config configs/imm_anchor_v8b_twostage.yaml

# 只跑 stage2（从 stage1 checkpoint 恢复）
CUDA_VISIBLE_DEVICES=0 python train_twostage.py --config configs/imm_anchor_v8b_twostage.yaml --resume_stage2 checkpoints/imm_anchor_v8b_twostage/stage1_done
```

**注意：** 启动前需要 `source /etc/network_turbo`（AutoDL 代理），否则 HF Hub 请求会 hang。

---
