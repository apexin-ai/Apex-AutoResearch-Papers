# infra kill orphan vllm

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_orphan_vllm_20260514T072222_result.json`
- **Structured JSON:** [`8051218ad6697ae0f3e1.json`](../../sessions/80/8051218ad6697ae0f3e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。孤儿进程 PID 21051 (VLLM::EngineCore) 和 21050 (resource_tracker) 已终止。

**清理后 GPU 显存状态：**

| GPU | 已用 | 总量 |
|-----|------|------|
| cuda:0 | 29925 MiB | 32607 MiB |
| cuda:1 | 29925 MiB | 32607 MiB |
| cuda:2 | **0 MiB** | 32607 MiB |
| cuda:3 | 0 MiB | 32607 MiB |

cuda:2 显存已完全释放。port 8001 的 vLLM 服务（cuda:0+1, TP=2）正常运行。

---
