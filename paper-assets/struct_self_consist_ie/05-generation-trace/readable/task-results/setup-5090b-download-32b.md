# setup 5090b download 32b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_5090b_download_32b_20260520T220604_result.json`
- **Structured JSON:** [`6a4c1e507df1b2590495.json`](../../sessions/6a/6a4c1e507df1b2590495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在进行中，多个 shard 并行下载。当前速度约 5-12 MB/s。

**状态汇总：**
- **服务器**: autodl-5090-b, 4x RTX 5090 32GB
- **磁盘**: /root/autodl-tmp/ 95GB 可用（够装 ~65GB 模型）
- **下载 PID**: 284644，正在后台运行
- **下载源**: ModelScope 国内 CDN，多文件并行下载中
- **下载速度**: 约 5-12 MB/s/shard，17 个 shard（每个 ~3.63GB）
- **预估完成时间**: 总量 ~65GB，按聚合 ~30MB/s 估算约 35-40 分钟

可以用以下命令随时检查进度：
```
tail -5 /tmp/download_32b.log
```

---
