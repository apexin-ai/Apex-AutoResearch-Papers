# ops gpu status and fix

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-fix_20260515T203845_result.json`
- **Structured JSON:** [`529fc2d3584790ae4fa6.json`](../../sessions/52/529fc2d3584790ae4fa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## GPU 实际状态

| GPU | 进程PID | 对应exp_id | GPU利用率 | 显存占用 |
|-----|---------|-----------|----------|---------|
| 0 | 192214 | v4-taxei-fixed-inject10-s7 | 95% | 19201/32607 MiB |
| 1 | 192343 | v4-random-fixed-inject10-s1 | 28% | 19181/32607 MiB |
| 2 | — | 空闲 | 0% | 0 MiB |
| 3 | — | 空闲 | 0% | 0 MiB |

两个训练均运行约 38 分钟。

## tmux session 状态

| session | 存在? |
|---------|-------|
| v4-taxei-fixed-inject10-s7 | ✅ 存在 |
| v4-random-fixed-inject10-s1 | ✅ 存在 |
| v4-taxei-fixed-inject10-s123-eval-r2 | ❌ 不存在 |
| v4-random-fixed-inject10-s0-eval-r2 | ❌ 不存在 |

**结论：GPU 2 和 GPU 3 空闲可用。** 两个 eval session 不存在（已结束或未创建）。

---
