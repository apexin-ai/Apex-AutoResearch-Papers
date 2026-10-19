# ops bjb1 32546 gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-32546-gpu-check_20260519T040315_result.json`
- **Structured JSON:** [`630336f954553544bc67.json`](../../sessions/63/630336f954553544bc67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。汇总如下：

## GPU 利用率报告 - bjb1-32546

| GPU | 利用率 | 显存 (MiB) | 进程数 | 实验 | 异常 |
|-----|--------|------------|--------|------|------|
| 0 | 99% | 6212/24564 | 2 | eval-perdof-object-norm005-seed46, eval-obs-only-norm003-seed44-t16 | ✅ 正常 |
| 1 | 99% | 7121/24564 | 2 | eval-obs-only-object-default-seed47, eval-spatial-obs-only-norm02-seed45 | ✅ 正常 |
| **2** | **23%** | **1943/24564** | **1** | eval-perdof-object-norm03-seed46 | **⚠️ 只有1个实验** |
| 3 | 99% | 6676/24564 | 2 | eval-perdof-object-norm01-seed48, eval-perdof-norm003-seed48-t16 | ✅ 正常 |
| 4 | 99% | 12805/24564 | 3 | eval-scalar-object-seed46, eval-perdof-norm005-seed45-r2, eval-obs-only-default-seed48-r2 | ✅ 正常 |
| 5 | 81% | 5743/24564 | 2 | eval-obs-only-object-norm01-seed47, eval-obs-only-norm003-seed46-t16 | ✅ 正常 |

### 结论

**GPU 2 是低利用率的根因**：只跑了 1 个 eval 实验（其他 GPU 都有 2-3 个），显存只占 1943 MiB / 24564 MiB，还剩约 22GB 可用。该实验本身在正常推进（rollouts 在前进），不是卡住。

GPU 5 的 81% 属于正常波动范围，实验也在正常推进。

**GPU 2 可以再塞 1-2 个 eval 实验**来充分利用。

---
