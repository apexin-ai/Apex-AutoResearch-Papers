# eval taxei rp s7

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_taxei-rp-s7_20260516T101514_result.json`
- **Structured JSON:** [`d97b4e42ccdfd572415d.json`](../../sessions/d9/d97b4e42ccdfd572415d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval-rp-s7 成功启动，GPU 3 已占用 17091 MiB，正在运行（1/47 episodes 已完成）。

GPU 0 状态：30837/32607 MiB，`llama31-vanilla-s0` session 仍在运行，GPU 0 被占用，不启动额外 eval。

**汇总：**
| 项目 | 状态 |
|------|------|
| eval-rp-s7 (GPU 3) | 已启动，正在运行 (1/47) |
| GPU 0 | 被 llama31-vanilla-s0 占用 (30837 MiB, 99%)，未启动额外 eval |
| GPU 1 | 26025 MiB 占用（llama31-taxei-s0） |
| GPU 2 | 26025 MiB 占用（llama31-random-s0） |

注意：启动过程中有一个 `libnvJitLink.so.13` 警告和 generation flags 警告，但不影响运行。

---
