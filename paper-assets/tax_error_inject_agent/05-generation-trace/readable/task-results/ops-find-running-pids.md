# ops find running pids

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find-running-pids_20260514T204218_result.json`
- **Structured JSON:** [`14f50469130f7a04b1ad.json`](../../sessions/14/14f50469130f7a04b1ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 实验 | GPU | 状态 | PID | 结果 |
|------|-----|------|-----|------|
| v4-random-seed0-eval | cuda:2 | **已完成** | — | success_rate=**0.553** (26/47) |
| v4-taxei-seed0-eval | cuda:1 | **已完成** | — | success_rate=**0.468** (22/47) |
| v4-vanilla-recovery-eval | cuda:0 | **已完成** | — | recovery_rate=**0.617**, detection_rate=0.0 |
| v4-taxei-recovery-eval | cuda:3 | **运行中** | **87614** | 进度 17/47，17082 MiB VRAM，82% util |

前 3 个实验均已完成，输出文件已生成。仅 v4-taxei-recovery-eval (PID 87614) 仍在 cuda:3 上运行，当前处理到第 17/47 个 episode。

---
