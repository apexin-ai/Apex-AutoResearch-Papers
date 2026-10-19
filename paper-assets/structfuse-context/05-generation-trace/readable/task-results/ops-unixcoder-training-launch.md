# ops unixcoder training launch

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unixcoder_training_launch_20260516T055854_result.json`
- **Structured JSON:** [`5cec128a815f91b814ae.json`](../../sessions/5c/5cec128a815f91b814ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行！step 50, loss=0.6284。Loss 在正常范围内（InfoNCE with 8 candidates, random chance log(8)≈2.08，0.63 说明模型已在学习）。

训练已成功启动：
- **Job**: `unixcoder-3strat-s42`（tmux session）
- **GPU 0**: 13.5 GiB VRAM
- **配置**: batch_size=16, max_seq_length=1024, gradient-checkpointing, LoRA
- **进度**: 707 steps/epoch × 2 epochs = 1414 总步数，3 个 strategy 串行
- **首个 loss**: step 50, loss=0.6284
- **输出**: `/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/{strategy}_s42/`
- **预计总时长**: ~2-3 小时（3 runs 串行）

---
