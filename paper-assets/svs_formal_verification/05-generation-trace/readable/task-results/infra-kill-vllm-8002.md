# infra kill vllm 8002

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_vllm_8002_20260514T072005_result.json`
- **Structured JSON:** [`476e852e6c745c01620f.json`](../../sessions/47/476e852e6c745c01620f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Port 8002 的 vLLM 进程已被成功 kill。GPU 2 显存已释放（不再出现在 nvidia-smi 进程列表中）。

**Kill 前后 GPU 显存对比：**

| GPU | Kill 前 | Kill 后 | 变化 |
|-----|---------|---------|------|
| 0 | 29925 MiB / 32607 MiB | 29925 MiB（port 8001 仍在运行） | 不变 |
| 1 | 29925 MiB / 32607 MiB | 29925 MiB（port 8001 仍在运行） | 不变 |
| **2** | **31103 MiB / 32607 MiB** | **0 MiB** | **-31103 MiB ✓** |
| 3 | 0 MiB | 0 MiB | 不变 |

GPU 2 已完全释放，port 8001 的 vLLM 服务（GPU 0,1）未受影响。

---
