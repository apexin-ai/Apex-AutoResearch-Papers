# ssh exp003 results read

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003_results_read_20260522T170811_result.json`
- **Structured JSON:** [`2fad4214baa9f406e2e0.json`](../../sessions/2f/2fad4214baa9f406e2e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态清晰了。

**进程仍在运行** (PID 143769, 2h39m, 100% CPU, GPU 0 at 77%)

### 模型拟合进度

| 模型 | 状态 | 耗时 |
|------|------|------|
| raw_average | ✅ Done | 0.0s |
| mfrm_only | ✅ Done | 2243s (~37min) |
| sequential | ✅ Done | 3614s (~60min) |
| **joint_gmfrm** | 🔄 运行中 | — |

`joint_gmfrm` 当前在 **warmup 18%** (1055/6000)，速度 3.62 it/s。这应该是 chain 4/4（15分钟前 chain 3 在 79%，已完成进入 chain 4）。

### 预估剩余时间

剩余 ~4945 iterations / 3.62 it/s ≈ **23 分钟**。

### 已有结果文件

目前只有 dry_run 结果，最终结果尚未写入：
- `exp003/dry_run/results.json` + 4 张图
- `exp003/results_dryrun/results.json` + 4 张图

joint_gmfrm 完成后 STEP 2 结束，后续可能还有 STEP 3（评估/输出）。整体预计 **~25-30 分钟后完成**。需要我稍后再查一次吗？

---
