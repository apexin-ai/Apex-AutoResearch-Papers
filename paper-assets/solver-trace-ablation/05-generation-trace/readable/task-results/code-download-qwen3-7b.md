# code download qwen3 7b

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_download-qwen3-7b_20260516T024201_result.json`
- **Structured JSON:** [`e10f930a504ad66d6fef.json`](../../sessions/e1/e10f930a504ad66d6fef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

1. **Qwen3 系列没有 7B 模型**。尺寸为 0.6B / 1.7B / 4B / 8B / 14B / 32B。最接近的是 **Qwen3-8B**。

2. **Qwen3-8B 已在后台下载中**（PID 588329，ModelScope），无需重复启动：
   - shard 1/4/5（共 ~8.4GB）：已完成
   - shard 3（3.69GB）：62%，预计 ~2 分钟完成
   - shard 2（3.72GB）：32%，预计 ~8 分钟完成
   - 速度：shard 3 ~11MB/s，shard 2 ~6MB/s

3. **预计全部完成时间：~8-10 分钟**（从现在算起）

4. **磁盘空间**：58GB 可用，Qwen3-8B 约 16GB，足够。

5. **模型路径**：`/root/autodl-tmp/models/Qwen3-8B/`

轮询命令（稍后检查）：
```
tail -5 /tmp/ms_download_qwen3_8b.log
ps -p 588329 -o pid=
```

---
