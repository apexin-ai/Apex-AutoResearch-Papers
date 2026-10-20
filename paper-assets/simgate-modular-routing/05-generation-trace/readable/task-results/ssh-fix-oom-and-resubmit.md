# ssh fix oom and resubmit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-oom-and-resubmit_20260518T215853_result.json`
- **Structured JSON:** [`f2c1deee12e0dc0d04b3.json`](../../sessions/f2/f2c1deee12e0dc0d04b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

| 项目 | 状态 |
|---|---|
| **cuda:0 清理** | 进程 165113 已终止，显存完全释放（0MiB → 可用） |
| **grounding-prompt-ablation** | 已重启，tmux session `grounding-prompt-ablation`，vLLM PID 168205，cuda:0 占用 29637MiB，正常推理中 |
| **grounding-filter-ablation** | `src/run_grounding_filter_ablation.py` **不存在**，无法执行 dry-run。另一个 Worker 可能还在准备中 |
| **GPU 使用** | cuda:0: 29637MiB / 38% util（prompt-ablation）；cuda:1: 空闲 0MiB |

---
