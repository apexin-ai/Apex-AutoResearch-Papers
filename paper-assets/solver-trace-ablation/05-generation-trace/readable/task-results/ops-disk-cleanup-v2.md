# ops disk cleanup v2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-v2_20260515T010503_result.json`
- **Structured JSON:** [`8f9f3d8febcf71e92dae.json`](../../sessions/8f/8f9f3d8febcf71e92dae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘当前实际使用率 **33%**（82G/250G），不是任务描述的 96%。**无需清理。**

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        250G   82G  169G  33% /root/autodl-tmp
```

主要占用：
- `outputs/` 61G
- `models/` 16G
- `.hf_cache/` 5.3G
- `.wandb_cache/` 不存在

任务描述中的 96% 状态可能已被前一轮清理处理过，或描述本身过时。当前 169G 可用，距 85% 阈值（37G 可用）还有 132G 余量，**未执行任何删除操作**。

如需预防性清理（例如腾出更多空间应对后续实验），请确认后再执行。

---
