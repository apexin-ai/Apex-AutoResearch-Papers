# eval hgate merged launch

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_hgate-merged-launch_20260513T014522_result.json`
- **Structured JSON:** [`a2f30ce401969865412e.json`](../../sessions/a2/a2f30ce401969865412e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成，汇总：

| 项目 | 状态 |
|------|------|
| **GPU 2** | 22099/24564 MiB, vLLM PID 688649, port 8002, run 1-2 |
| **GPU 3** | 22099/24564 MiB, vLLM PID 688650, port 8003, run 3-4 |
| **主进程** | PID 688636 |
| **Group A** | PID 688675, 推理进行中 |
| **Group B** | PID 688676, 推理进行中 |
| **日志** | `/tmp/hgate-merged-full.log`, `results/hgate_dpo003_merged/group_{a,b}.log` |
| **Registry** | `hgate-dpo003-merged` → RUNNING |

两个 GPU 均已满载运行 merged 模型 eval，无报错。

---
