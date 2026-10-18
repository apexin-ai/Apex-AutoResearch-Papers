# util disk cleanup and 72b download

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_util_disk_cleanup_and_72b_download_20260514T135337_result.json`
- **Structured JSON:** [`f37bd41b805b19c91800.json`](../../sessions/f3/f37bd41b805b19c91800.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在并行进行（4-5 个文件同时下载），单文件速度 ~360KB/s-1MB/s，聚合约 3-4MB/s。37 个 safetensor 文件共约 137GB，预计需要 10-12 小时。

**Step 1-2 完成汇总：**
- 清理前：98GB 可用
- 清理后：151GB 可用
- 释放：**53GB**（Llama-3.1-8B ~15GB, Mistral-7B ~14GB, Qwen3-8B ~16GB, Qwen2.5-1.5B ~3GB, profiling 中间文件若干）

**Step 3 状态：**
- Qwen2.5-72B 通过 ModelScope CDN 后台下载中
- PID: 227942
- 日志: `/tmp/qwen72b_download.log`
- 预计耗时 10-12 小时

后续可通过以下命令检查进度：
```bash
tail -5 /tmp/qwen72b_download.log
ps -p 227942 -o pid= && echo "RUNNING" || echo "DONE"
df -h /root/autodl-tmp/
```

下载完成后需执行 Step 5 验证模型完整性和架构参数。需要我继续轮询还是后续手动检查？

---
