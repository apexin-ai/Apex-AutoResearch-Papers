# ssh exp001 0pct sft gpu345

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001-0pct-sft-gpu345_20260513T192720_result.json`
- **Structured JSON:** [`b5ceb440f2699a6779fc.json`](../../sessions/b5/b5ceb440f2699a6779fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

## 启动结果

| GPU | 模型 | 步数 | 速度 | 显存占用 | 状态 |
|-----|------|------|------|----------|------|
| 3 | Qwen2.5-0.5B | 436/3125 (14%) | ~1.0s/step | 21.6 GB | loss=1.52, 正常下降 |
| 4 | Qwen2.5-1.5B | 142/3125 (5%) | ~2.0s/step | 21.6 GB | 训练中 |
| 5 | Qwen2.5-3B | 5/3125 (0.2%) | ~4.1s/step | 18.6 GB | 训练中 |

### 配置
- **数据**: 50K SlimOrca samples (0% dosage, 无任何 benchmark 污染)
- **LoRA**: r=16, alpha=32, targets=all attention+MLP projections
- **训练**: 1 epoch, lr=2e-4, cosine scheduler, bf16
- **Batch**: 0.5B bs=4/ga=4, 1.5B bs=2/ga=8, 3B bs=1/ga=16 (effective=16)
- **Seed**: 42

### 修复记录
- `train_sft.py`: `max_seq_length` → `max_length` (TRL 1.4.0 兼容)
- `train_sft.py`: `formatting_func` 改为单 example 模式 (TRL 1.4.0 兼容)
- `train_sft.py`: `flash_attention_2` → `sdpa` (flash-attn 未安装)
- 1.5B: batch_size 4→2 避免 OOM

### 输出目录
- `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/`
- `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/`
- `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/`

### 预计完成时间
- 0.5B: ~50 min (约 03:30 UTC 开始, ~04:20 完)
- 1.5B: ~1.7 hr (~05:20 完)
- 3B: ~3.6 hr (~07:20 完)

---
