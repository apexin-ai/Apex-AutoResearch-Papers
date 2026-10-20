# ops quick gpu check v2

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_quick-gpu-check-v2_20260522T172316_result.json`
- **Structured JSON:** [`83b9b02d7f6c4fe7da32.json`](../../sessions/83/83b9b02d7f6c4fe7da32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：**

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 / 97887 MiB | 0% |
| 1 | 0 / 97887 MiB | **100%** |
| 2 | 0 / 97887 MiB | 0% |
| 3 | 0 / 97887 MiB | 0% |

GPU 1 利用率 100% 但显存 0 MiB、无 compute app 进程——大概率是刚跑完释放显存但利用率还没回落，或者是个残留状态。**无 Python 进程在跑**，无训练任务在执行。

### 最近 Results（按时间倒序）
| 文件 | 时间 |
|------|------|
| `contam_50_s2_results.json` | 5/23 01:19 |
| `contam_25_s3_results.json` | 5/23 00:28 |
| `contam_25_s2_results.json` | 5/22 21:45 |
| `contam_15_s2_results.json` | 5/22 20:43 |
| `contam_5_cohens_d.json` | 5/22 17:23 |
| `contam_5_results.json` | 5/22 07:14 |

### 最近 Checkpoints（比 contam_25 更新的）
- `contam_5/` — 含 3 个 checkpoint + final adapter
- `contam_15_s2/` — 含 3 个 checkpoint + final adapter
- `contam_25_s2/` — 含 3 个 checkpoint + final adapter
- `contam_25_s3/` — 含 3 个 checkpoint + final adapter
- `contam_50_s2/` — 含 3 个 checkpoint + final adapter

### 总结
GPU 空闲，无训练进程。最新产出是 `contam_50_s2`（约 30 分钟前完成），5 个新模型（contam_5, contam_15_s2, contam_25_s2, contam_25_s3, contam_50_s2）均已训练完成并有 eval 结果。

---
