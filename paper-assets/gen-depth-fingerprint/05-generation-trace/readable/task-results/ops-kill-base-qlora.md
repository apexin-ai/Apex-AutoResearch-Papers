# ops kill base qlora

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_base_qlora_20260519T094849_result.json`
- **Structured JSON:** [`ee93d55f55497d26ca56.json`](../../sessions/ee/ee93d55f55497d26ca56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**2 个 base 任务** — 已终止（进程和 tmux session 均已不存在，之前可能已自行结束）

**2 个 instruct 任务** — **也已完成运行**，进程 71920/72065 不再存活。日志显示两个任务均已跑完全部 fold 并保存了结果：

| 任务 | 结果文件 | 运行时间 | 3-class F1 (gen0/gen1/gen2+) |
|---|---|---|---|
| OLMo-instruct | `qlora_olmo-2-0425-1b-instruct.json` | 28.2 min | 0.99 / 0.77 / 0.91 |
| Qwen3-instruct | `qlora_qwen3-1.7b-instruct.json` | 31.3 min | 0.99 / 0.80 / 0.93 |

**GPU 状态** — 4× RTX 5090 全部空闲（0MiB / 0% utilization），cuda:0-3 均已释放。

---
