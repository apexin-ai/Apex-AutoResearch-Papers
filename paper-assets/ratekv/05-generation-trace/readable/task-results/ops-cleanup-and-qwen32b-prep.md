# ops cleanup and qwen32b prep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_and_qwen32b_prep_20260516T023622_result.json`
- **Structured JSON:** [`3467f1674ecf66d1807b.json`](../../sessions/34/3467f1674ecf66d1807b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务执行完毕，汇总如下：

---

**1. Phi-3 MCKP 进程** — 已不存在（无需 kill），GPU:1 完全释放（3 MiB）

**2. InternLM2 profiling** — 运行中，进度 215/256 heads（~84%），ETA ~9min，即将完成

**3. Qwen2.5-32B 下载** — 已启动（PID 393101），ModelScope 下载中
   - 当前：shard 5/17，速度 ~10MB/s
   - 预计总大小 ~62GB（17 × 3.63GB）
   - 清理了 Phi-3 缓存（27GB），当前可用 71GB
   - 预计下载时间：~1.5-2h

**4. Profiling 脚本** — 已创建并同步到服务器
   - 路径：`/root/ratekv/run_qwen25_32b_hires_profiling.py`
   - 配置：64L × 8KV（GQA 5:1），512 total heads，batch_size=1，默认 cuda:1
   - 包含 t1/t5 ratio 和 shape diagnostic（Spread/Spike/Flat 分类）

---
