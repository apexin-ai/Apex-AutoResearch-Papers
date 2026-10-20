# code treatment dryrun

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_treatment-dryrun_20260517T074833_result.json`
- **Structured JSON:** [`6183b4c9d070c7460d4f.json`](../../sessions/61/6183b4c9d070c7460d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果汇报

### Pipeline 状态：端到端通过

**训练输出（dry-run, 2 batches）：**
- Train Loss: 2.7549（初始值合理，8-class CE 理论值 ln(8)≈2.08，加上 0.3×intent loss 约 2.7 符合预期）
- Val Loss: 2.6540
- Val Persuasion Acc: 0.0000（mock 数据全标 class 7，dry-run 2 batch 不足以学到）
- Val Intent Acc: 0.5000（随机水平，符合预期）

**完整 1-epoch（250 user turns）：**
- Train Loss: 2.0448，Val Loss: 1.2419
- Val Persuasion Acc: 1.0000（全标同一类，1 epoch 即可学到）
- 耗时：**14.1 秒**

**GPU 显存（batch_size=16, max_length=256）：**
- 峰值 allocated：6,742.7 MiB
- 峰值 reserved：7,256.0 MiB
- nvidia-smi 报告：7,925 MiB / 97,887 MiB（利用率 ~8%）
- GPU：NVIDIA RTX PRO 6000 Blackwell Server Edition（98GB）
- 显存充裕，batch_size 可大幅提升

**发现的问题：**
- 无 bug。DeBERTa 加载时有 UNEXPECTED keys 警告（`mask_predictions.*`, `lm_predictions.*`），这是正常的，因为加载的是 pretrained MLM 权重，这些 head 不被 `AutoModel` 使用
- `train_deberta.py` 无 `--device` 和 `--num_classes` 参数（使用 `Accelerator` 控制设备，model 默认 8 classes）

**正式训练时间估算：**
- 250 turns / 1 epoch = 14s → 按真实数据 ~1,500 user turns 估算约 84s/epoch
- 5 epochs ≈ 7 分钟（单卡 RTX PRO 6000）

---
