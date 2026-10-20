# ssh check exp003 progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_exp003_progress_20260522T161631_result.json`
- **Structured JSON:** [`6b57ca6ca4f57ddaf74a.json`](../../sessions/6b/6b57ca6ca4f57ddaf74a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003 状态汇报

**进程**: PID 143769 **alive**，运行时长 1h47m，CPU 100%，RSS 2.1GB

**GPU**: cuda:0 使用率 77%，显存 731 MiB / 97887 MiB。GPU 1-3 空闲。

**已完成方法**:
| 方法 | 耗时 | 速度 |
|------|------|------|
| raw_average | 0s | — |
| mfrm_only | 2243s (37 min) | ~80 it/s |
| sequential | 3614s (60 min) | 中等 |

**当前**: `joint_gmfrm` — chain 1/4，**sampling 阶段**，3180/6000 iterations (53%)，速度 **3.63 it/s**（比前两个方法慢 ~20x，step size 4.38e-03 / 1023 leapfrog steps，模型复杂度高很多），acc. prob = 0.95。

**结果目录**: 空，尚无输出。

**预计剩余时间**:
- 当前 chain 1 剩余: ~2820 iters / 3.63 it/s ≈ **13 min**
- chain 2-4 每条约 28 min → **84 min**
- joint_gmfrm 总剩余 ≈ **1.5 小时**
- 之后还有 STEP 3 (evaluation) 和 STEP 4 (summary)，预计较快

**MCMC 健康度**: acc. prob 0.94-0.95，step size 稳定在 4.38e-03，采样看起来正常。joint_gmfrm 慢是因为 1023 leapfrog steps（参数空间大得多），属预期行为。

---
