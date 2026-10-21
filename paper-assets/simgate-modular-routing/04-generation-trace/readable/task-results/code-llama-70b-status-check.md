# code llama 70b status check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-70b-status-check_20260523T225125_result.json`
- **Structured JSON:** [`f5b8b4b3277b13ecea60.json`](../../sessions/f5/f5b8b4b3277b13ecea60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Llama-70B 下载状态：进行中**

| 类别 | 详情 |
|------|------|
| 进程 | PID 179639 **仍在运行** (ModelScope 下载) |
| 已完成 shards | 3/9 (shard 4, 5, 6 各 4.6G，已在最终目录) |
| 下载中 shards | 4 个 (shard 1: 42%, 3: 45%, 7: ~43%, 9: 79%) |
| 未开始 shards | 2 个 (shard 2, 8) + config.json |
| 已下载总量 | ~24G / ~37G |
| 下载速度 | ~1 MB/s |
| 预计剩余 | **40-60 分钟** |

下载完成后需要启动 vLLM 并测试。报告已写入 `artifacts/llama70b_setup_report.md`。

---
