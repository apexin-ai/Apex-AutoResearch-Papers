# critical disk cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_disk_cleanup_20260521T045631_result.json`
- **Structured JSON:** [`7d69adda5e00222de5b2.json`](../../sessions/7d/7d69adda5e00222de5b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

gpt2_seed456/checkpoint-5500 没有 optimizer state（无 optimizer.pt 也无 optimizer/ 目录），无法直接 resume 训练，只能用于加载模型权重重新开始优化器。

```
磁盘清理前: 100% used (984K available)
磁盘清理后: 46% used (137G available)
回收空间: ~136G

checkpoint 完整性:
- gpt2_seed456/checkpoint-5500: 存在但不完整 (1.2G, has_optimizer=N) — 只有模型权重，无法 resume optimizer
- tau08_v2/checkpoint-500: 完整 (3.4G, has_optimizer=Y)
- gpt2_seed123_v2/checkpoint-500: 完整 (3.4G, has_optimizer=Y)
- ngram_seed456: 无可用 checkpoint（仅剩 config.json + step_metrics.jsonl，需从头跑）
```

---
