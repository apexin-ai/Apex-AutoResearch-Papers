# ops kill residual processes

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-residual-processes_20260514T060309_result.json`
- **Structured JSON:** [`585916571156fe10dd7d.json`](../../sessions/58/585916571156fe10dd7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程已清理：
- **36922** (episode_level_collection lifespan) — 已 kill
- **223785** (huggingface-cli download) — 已 kill

GPU 状态：
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU0 | 533 MiB | 0% |
| GPU1 | 4539 MiB | 28% |

GPU0 已释放（仅剩少量残余显存），GPU1 仍有 plan-004 在运行。无孤儿进程。

---
