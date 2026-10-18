# diagnose train smart compress m16 seed44 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_smart_compress_m16_seed44_v2_20260519T161711_result.json`
- **Structured JSON:** [`3efe28f305a9bcf4e03b.json`](../../sessions/3e/3efe28f305a9bcf4e03b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断总结：

**死因：数据盘满（250G 用了 100%，仅剩 4MB）**

- 训练正常运行 ~4.5 分钟，到 step=1000 时 loss 已从 5.0 降到 0.2
- 在 step=1000 首次 checkpoint 保存时 `torch.save()` 写入失败，进程崩溃
- `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/` 目录已占 112GB（历史实验 checkpoint 未清理）

**重试前需要**：清理 cqa1-33015 上的旧 checkpoint 释放磁盘空间。当前那个 228MB 的 `checkpoint.pt` 也应删除（不完整）。

---
