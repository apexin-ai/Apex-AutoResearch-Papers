# diagnose grounding prompt ablation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grounding-prompt-ablation_20260518T215711_result.json`
- **Structured JSON:** [`62a16a0c680355bd7c43.json`](../../sessions/62/62a16a0c680355bd7c43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已保存。总结：

- **错误类型**: GPU 显存不足（被残留进程占用）
- **根因**: GPU 0 上 PID 165113 的 vLLM 旧进程占用 29.5 GiB 显存，新实验仅剩 2.04 GiB 可用，初始化即失败
- **部分结果**: 无，第一个 episode 就崩溃了
- **修复**: kill 165113 后重跑，或改用空闲的 GPU 1 (`--gpu_id 1`)

---
