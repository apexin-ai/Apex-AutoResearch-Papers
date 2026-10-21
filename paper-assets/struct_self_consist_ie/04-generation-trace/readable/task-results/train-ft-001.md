# train ft 001

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ft_001_20260514T060518_result.json`
- **Structured JSON:** [`8429d4e9ec79452c8a47.json`](../../sessions/84/8429d4e9ec79452c8a47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交并运行中。汇报：

**训练命令**: `CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config.yaml`（nohup 后台, PID 6414）

**预估训练时间**: 351 steps × ~3s/step ≈ **17-18 分钟**

**Checkpoint 输出路径**: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora`

**训练日志**: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log`

**配置摘要**:
- 模型: Qwen3-8B, LoRA r=16 α=32, target=all (43.6M trainable params, 0.53%)
- 数据: 1861 train / 275 dev, sharegpt format
- Batch: 4 × 4 accumulation = 16 effective, 3 epochs, lr=2e-4 cosine
- Eval every 100 steps, save every 100 steps
- report_to: none（W&B 未配置）

**注意事项**:
- Dry-run 2 步通过，初始 loss ~0.83
- 4x RTX 5090 可用但只用了 cuda:0 单卡（LoRA 8B 单卡足够）

---
