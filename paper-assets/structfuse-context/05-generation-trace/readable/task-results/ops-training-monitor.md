# ops training monitor

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-monitor_20260513T075619_result.json`
- **Structured JSON:** [`20c22356e2b5d87de92e.json`](../../sessions/20/20c22356e2b5d87de92e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

### GPU 占用
| GPU | PID | 显存 |
|-----|-----|------|
| cuda:0 | 27234 | 24,218 MiB |
| cuda:1 | 29302 | 22,772 MiB |

两卡均在正常工作。

---

### m2_embed_verify (Qwen2.5-Coder-3B, cuda:1, PID 29302)

**当前**: random_s42 策略, Epoch 2, step 1000 / ~1640 — eval@1000 即将触发

| Strategy | 状态 | 进度 |
|----------|------|------|
| random_s42 | **训练中** | Epoch 2, step 1000 |
| embedding_s42 | 待运行 | wandb 已初始化，等待 random 完成 |
| dataflow_s42 | 待运行 | wandb 已初始化，等待 |

**Eval metrics:**

| Strategy | Step | val_loss | recall@1 | recall@5 | recall@10 |
|----------|------|----------|----------|----------|-----------|
| random | 500 | **0.4834** | **53.57%** | **98.08%** | **100%** |

---

### plan_013_starcoder (StarCoder2-3B, cuda:0, PID 27234)

实际执行顺序：dataflow (OOM) → random (完成) → embedding (训练中)

| Strategy | 状态 | 进度 |
|----------|------|------|
| dataflow_s42 | **OOM 崩溃** | Epoch 1 forward pass 时显存不足 |
| random_s42 | **已完成** | best ckpt 已保存，但 eval 指标因日志缓冲未写入 |
| embedding_s42 | **训练中** | Epoch 2 刚开始 (~step 820/1640) |

**Eval metrics:**

| Strategy | Step | val_loss | recall@1 | recall@5 | recall@10 |
|----------|------|----------|----------|----------|-----------|
| random | — | — | — | — | — (日志截断，仅15行) |
| embedding | 500 | **0.5140** | **47.99%** | **98.26%** | **100%** |

---

### 异常

1. **StarCoder dataflow OOM**: `torch.OutOfMemoryError: Tried to allocate 2.62 GiB`，进程占 52.22 GiB + 42.38 GiB non-PyTorch，95 GiB GPU 无余量。dataflow_aware 策略比其他策略内存需求更大。
2. **StarCoder random 日志缺失**: 日志仅 15 行止于 step 500，无 eval 输出。但 best checkpoint 已保存（说明训练完整跑完），是 Python stdout 缓冲问题。
3. 两个实验均未完成全部 strategies。

### 预估剩余

- **m2_embed_verify**: random 还剩 ~640 steps (Epoch 2)，之后跑 embedding + dataflow 各 ~1640 steps × 2 = 3280 steps
- **plan_013_starcoder**: embedding 还剩 ~820 steps (Epoch 2)。dataflow 已 OOM，不会自动重试，需要人工干预（降 batch_size 或启用更激进的 gradient checkpointing）

---
