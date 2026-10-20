# ops cqa1 post restart diag

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-post-restart-diag_20260520T030524_result.json`
- **Structured JSON:** [`3fab6b317877ed99201b.json`](../../sessions/3f/3fab6b317877ed99201b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
cqa1 GPU: 在跑 (GPU 0, 37% util, 21325/24564 MiB)
s0 训练进度: 当前 dosage=d000, step 397/3125 (12.7%), ETA ~3h, ~4.0s/it
已有 checkpoint: 无 (d000 尚未完成, d005/d025/d050/d100 未开始)
磁盘: 72% (49G free)
```

注：bitsandbytes 报了 `libnvJitLink.so.13` 加载错误，但训练本身在正常推进（非 8-bit 优化器路径），不影响训练。LoRA 配置已确认 alpha=32。

---
