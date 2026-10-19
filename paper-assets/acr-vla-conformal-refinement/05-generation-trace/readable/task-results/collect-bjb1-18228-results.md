# collect bjb1 18228 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_bjb1-18228-results_20260527T235722_result.json`
- **Structured JSON:** [`cd26a1f737b93cda64dc.json`](../../sessions/cd/cd26a1f737b93cda64dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 调查结果

### 已完成实验

| 实验 | SR | trigger_rate | mean_unc | 状态 |
|------|-----|-------------|----------|------|
| **crm-always-on-spatial-s45** | **77.0%** (154/200) | 100.0% | 0.1790 | DONE ✓ (registry已更新) |

Per-task breakdown: 100%, 95%, 100%, 90%, 70%, 0%, 90%, 85%, 70%, 70%

无 OOM/CUDA 错误，EXIT_CODE=0，数据可信。

### 仍在运行的实验（3个）

| 实验 | 进度 | GPU | 部分SR |
|------|------|-----|--------|
| **crm-always-on-object-s45** | 9/10 tasks | cuda:2 (1.9GB) | 累计 ~73% (9个task均值) |
| **smolvla-tau040-long-s42** | 5/10 tasks | cuda:0 (3.5GB) | 20%, 75%, 95%, 95%, 40% |
| **smolvla-tau045-long-s42** | 5/10 tasks | cuda:1 (3.5GB) | 20%, 75%, 100%, 100%, 45% |

Registry 均已更新为 RUNNING。

### GPU 空闲情况

| GPU | 状态 |
|-----|------|
| cuda:0 | 占用（tau040） |
| cuda:1 | 占用（tau045） |
| cuda:2 | 占用（object-s45，即将完成） |
| **cuda:3** | **空闲**（1 MiB，可用） |

---
