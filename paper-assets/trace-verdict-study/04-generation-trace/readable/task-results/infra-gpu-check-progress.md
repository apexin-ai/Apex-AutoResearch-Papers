# infra gpu check progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-progress_20260515T213847_result.json`
- **Structured JSON:** [`c5fc3b3e99aff71af163.json`](../../sessions/c5/c5fc3b3e99aff71af163.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gpu_status_20260516_0540.md`。

## 结果摘要

**GPU 碰撞：无。** 两个实验分别在 GPU 0 和 GPU 1 上，互不干扰。

| 实验 | GPU | 进度 | 预计完成 |
|------|-----|------|---------|
| `deepseek_exception_only_seed456` | GPU 0 | ~326/444 (73%) | **~06:07** (~28min) |
| `deepseek_full_trace_seed42_v3` | GPU 1 | ~122/444 (27%) | **~07:27** (~1h48m) |

两块 GPU 利用率 100%，显存 ~22.4GB/98GB，温度 72-74°C，状态健康。

---
