# diagnosis ext val urgent check 2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_ext-val-urgent-check-2_20260519T224139_result.json`
- **Structured JSON:** [`5ba01407d373eea1ee3e.json`](../../sessions/5b/5ba01407d373eea1ee3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/extended-task-validation/urgent_check_2.md`。

**状态摘要：**

| Task | Progress | Status |
|------|----------|--------|
| boil | **20/20** | COMPLETE |
| use-thermometer | **20/20** | COMPLETE |
| find-living-thing | **15/20** | RUNNING (gpu0, ~15min ETA) |
| power-component | **16/20** | RUNNING (gpu1, ~12min ETA) |
| melt | **0/20** | CRASHED (vLLM EngineDeadError) |

**关键发现：** Internal model 在所有 task 上的 death rate（44-55%）是 deterministic baseline（13-25%）的 2-3 倍。Death asymmetry 是主要的 signal source，det-preferred 占 25-47%。

**Melt** 在 05:44 崩溃（vLLM EngineCore died），目录空，需要手动重启。可在 find-living-thing 完成后复用 gpu0。

---
