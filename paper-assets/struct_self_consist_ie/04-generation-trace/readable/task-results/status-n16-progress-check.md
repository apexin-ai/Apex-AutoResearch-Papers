# status n16 progress check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_n16_progress_check_20260523T001458_result.json`
- **Structured JSON:** [`267480addaec1f7f2545.json`](../../sessions/26/267480addaec1f7f2545.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**n16_v2 实验状态：**

- **VLLM 推理已完成** — 37648/37648 prompts (100%)，耗时 34:01
- **当前阶段：后处理/保存结果** — 进程 452387 状态 `R (running)`，正在写 `samples.jsonl`（当前 3.8GB，仍在增长，最后修改 08:16）
- **无报错** — 0 个 Traceback，0 个 error
- **GPU 状态** — cuda:1 占用 30GB 显存，GPU-Util 0%（推理已结束，VLLM 引擎未释放）

`report.json` 尚未生成，说明还在写 samples。按 samples.jsonl 的写入速度，后处理预计 **几分钟内完成**。

---
