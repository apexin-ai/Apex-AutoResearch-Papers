# ops registry fix training progress

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-fix-training-progress_20260513T072034_result.json`
- **Structured JSON:** [`33c41cca8bbd76fa822b.json`](../../sessions/33/33c41cca8bbd76fa822b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 1. Registry 状态修正

| 实验 | 状态 |
|------|------|
| **m2_embed_verify** | → RUNNING ✓ |
| **plan_013_starcoder** | PREPARING → QUEUED → ALLOCATED → RUNNING ✓ |

### 2. plan_013_starcoder (random 策略) 进度

- **模型**: StarCoder2-3B, **GPU**: cuda:0, 24.3GB VRAM, 100% util
- **当前**: Epoch 1, step 500 / 820
- **Loss 趋势**: 0.59 → 0.52 → 0.05 → 0.11 → 0.28 → 0.14 → 0.48 → 0.26 → 0.02 → 0.17
- **Eval**: 尚未输出（step 500 eval 可能正在执行中，日志截止 step 500 train loss）

### 3. m2_embed_verify (random 策略) 进度

- **模型**: Qwen2.5-Coder-3B, **GPU**: cuda:1, 22GB VRAM, 95% util
- **当前**: Epoch 1, step 500, **已完成首次 eval**
- **Eval@500 结果**:
  - val_loss = **0.4834**
  - recall@1 = **0.5357**
  - recall@5 = **0.9808**
  - recall@10 = **1.0**
- 已保存 best checkpoint → `/root/autodl-tmp/structfuse/m2_embed_verify_output/random_s42/best`

---
