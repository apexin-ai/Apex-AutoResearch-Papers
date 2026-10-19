# ops download llama4 scout

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_llama4_scout_20260520T211009_result.json`
- **Structured JSON:** [`40a01f9859e754125e64.json`](../../sessions/40/40a01f9859e754125e64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

1.8GB 下载完成（~3 min），聚合速度约 10 MB/s，修正预估约 **5-6 小时**完成。

下载稳定运行中，进程 PID 27560。后续可用以下命令检查进度：

```bash
# 查看已下载大小
du -sh /root/autodl-tmp/models/Llama4Scout/

# 查看下载日志
tail -20 /root/autodl-tmp/download_llama4_scout.log

# 检查进程是否存活
ps -p 27560 -o pid=
```

如需继续轮询，告诉我。

---
