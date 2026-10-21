# infra cleanup and download

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cleanup-and-download_20260520T110928_result.json`
- **Structured JSON:** [`12b374eb6cc9fe0e3ffd.json`](../../sessions/12/12b374eb6cc9fe0e3ffd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在顺利进行。从日志可见：

- Shard 1/8 正在下载：20MiB/3.5GiB，速度 **8.2 MiB/s**，ETA 7m20s
- 已下载 3.6G（20秒内从小文件阶段进入第一个大 shard）
- 磁盘剩余 72G，充足

## 报告

| 项目 | 详情 |
|------|------|
| **已删除模型** | `Qwen/Qwen2.5-14B-Instruct`(28G)、`Qwen/Qwen2___5-14B-Instruct`(同上硬链)、`Qwen2.5-14B`(12G) |
| **释放空间** | ~70G（9.2G → 80G） |
| **当前可用** | 72G（已有 3.6G 下载写入） |
| **DeepSeek** | 未删除（空间充足，无需删除） |
| **下载 PID** | `191718` |
| **下载速度** | ~8.2 MiB/s |
| **预估完成时间** | 每 shard ~7 分钟 × 8 = ~56 分钟，约 **20:10** 完成 |

监控命令：
```bash
tail -5 /tmp/download_qwen3_14b_aria2.log
du -sh /root/autodl-tmp/models/Qwen3-14B-Base/
```

---
