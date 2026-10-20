# diagnose mvp p1 gpu1 v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp-p1-gpu1-v2_20260513T075958_result.json`
- **Structured JSON:** [`4ae2e88c13cd5e31fb21.json`](../../sessions/4a/4ae2e88c13cd5e31fb21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：GPU 0 被先前实验的残留进程（PID 20301）占用 15816 MiB 显存，只剩 3.51 GiB 空闲。vLLM 启动需要 26.65 GiB，直接报 `ValueError` 退出。GPU 1 同样被残留的 vLLM EngineCore（PID 163319）占满。

**结论**：不需要改代码。`kill -9 20301 163319` 清理残留进程后重跑即可。

报告已保存到 `artifacts/diagnosis_mvp-p1-gpu1-v2.md`。

---
