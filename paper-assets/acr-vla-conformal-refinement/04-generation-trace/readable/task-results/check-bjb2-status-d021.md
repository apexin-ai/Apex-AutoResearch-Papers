# check bjb2 status d021

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-status-d021_20260515T012521_result.json`
- **Structured JSON:** [`f2bc360f7a6eeba59e7a.json`](../../sessions/f2/f2bc360f7a6eeba59e7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注意：任务指定的 checkpoint 路径 `crm_v3_norm/scalar_unc/` 不存在，实际路径在 `crm_v3/scalar_unc/`。`crm_v3_norm/` 下只有 `perdof/crm_best.pt`。

## bjb2-40593 状态

| 项目 | 状态 |
|------|------|
| **GPU 0** | 空闲 (RTX 4090D, 0MiB/24564MiB, 0% util) |
| **PID 201029 (vla-mean-t10)** | DEAD |
| **vla-mean-t10 结果** | 完成。Task 10 (black bowl → plate) 成功率 **10.0% (1/10)**，仅跑了 task 9（start_task=9），overall 10.0% |
| **PID 199257** | DEAD |
| **PID 203222** | DEAD |
| **scalar checkpoint** | **NO** — `crm_v3_norm/scalar_unc/crm_best.pt` 不存在。但 `crm_v3/scalar_unc/crm_best.pt` 存在 (1.3MB, May 15 02:25) |
| **evaluate.py 有 max_correction_norm** | YES (L77-78 参数定义, L287-290 运行时覆盖) |
| **evaluate.py** | 14489 bytes |
| **crm.py** | 2889 bytes |
| **可以部署 v4-scalar** | **需确认 checkpoint 路径**。GPU 空闲，代码就绪，但指定路径 `crm_v3_norm/scalar_unc/` 无 checkpoint。如果用 `crm_v3/scalar_unc/crm_best.pt` 则可以部署 |

---
