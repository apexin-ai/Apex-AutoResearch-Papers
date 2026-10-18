# gpu yi15 download final

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_yi15_download_final_20260514T153718_result.json`
- **Structured JSON:** [`8cb0c30936e9ef75625a.json`](../../sessions/8c/8cb0c30936e9ef75625a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前情况：

1. **不需要 kill 或重新下载** — PID 228878 的 ModelScope 下载进程正常运行，两个缺失 shard 正在下载中
2. **之前 Worker 误报的原因** — ModelScope 先下载到内部临时位置，shards 2 和 4 先完成了，Worker 看到进程还在但只检查了最终目录就报 done
3. **自动化已就绪** — `wait_and_run_yi15_v2.sh` 会每 60 秒检查 shard 数量，4/4 到齐且大小稳定后自动启动 `run_yi15_full_pipeline.py`
4. **预计 ~35 分钟后全部下完**，已设置 20 分钟后自动轮询

---
