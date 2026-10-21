# ops disk cleanup all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-all-servers_20260521T234714_result.json`
- **Structured JSON:** [`45fcbe8ca31088ffa308.json`](../../sessions/45/45fcbe8ca31088ffa308.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。最终结果：

```
westd-41074: 74% → 63% (释放 29G, 可用 66G→95G)
westd-27271: 68% → 55% (释放 33G, 可用 82G→115G)
cqa1-33015: 74% → 45% (释放 71G, 可用 67G→138G)
```

**补充清理**：三台服务器根分区缓存也已清理（HF cache、pip cache、/tmp 临时文件）。

westd-41074 和 westd-27271 未达 50G 释放目标，原因是剩余大文件全是活跃训练 checkpoints（m96 19G、m64 9G、m32 38G）或受保护模型（openvla-libero-object 15G、openvla-7b-finetuned-libero-spatial 15G、pi05_libero_finetuned 7G）。

---
