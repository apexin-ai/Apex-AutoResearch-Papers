# infra kill v2 all

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill_v2_all_20260514T135958_result.json`
- **Structured JSON:** [`85c2374a6e68299e1b35.json`](../../sessions/85/85c2374a6e68299e1b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 v2 rescorer 进程已清除。剩余 python 进程：

| PID | 进程 |
|-----|------|
| 937 | jupyter-lab（系统服务） |
| 939 | tensorboard（系统服务） |
| 33091 | vLLM (DeepSeek-R1-Distill-Qwen-14B) |
| 37622 | `svs_pipeline.run_mvp`（mvp_003） |
| 37934/37935 | multiprocessing resource tracker / defunct |

符合预期：只剩 mvp_003 + vLLM + 系统服务。

---
