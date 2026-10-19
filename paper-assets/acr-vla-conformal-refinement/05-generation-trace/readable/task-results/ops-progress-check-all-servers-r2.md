# ops progress check all servers r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-all-servers-r2_20260515T203039_result.json`
- **Structured JSON:** [`02e6f576ebda75f817c0.json`](../../sessions/02/02e6f576ebda75f817c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 17 个实验 registry 已更新。汇总如下：

## 进度总览 (2026-05-16 04:40 UTC)

所有 17 个进程均存活，无 ⚠️ 异常。

### bjb1-18228 (4× 4090)
| GPU | 实验 | 进度 | 部分 SR |
|-----|------|------|---------|
| 0 | eval-acr-object-v4-default-r2 | 1/10 | 0% |
| 1 | eval-perdof-object-seed43 | **5/10** | 10% (5/50) |
| 2 | eval-obs-only-object-seed43 | **6/10** | 8.3% (5/60) |
| 3 | eval-argmin-object-seed43 | **6/10** | 10% (6/60) |

### bjb1-32546 (6× 4090)
| GPU | 实验 | 进度 | 部分 SR |
|-----|------|------|---------|
| 0 | eval-mag-obsonly-norm003-object | 2/10 | 10% (2/20) |
| 1 | eval-vla-mean-object-seed43 | 3/10 | 6.7% (2/30) |
| 2 | eval-scalar-object-seed43 | 3/10 | 0% (0/30) |
| 3 | eval-obs-only-object-norm02-seed43-r2 | 1/10 | 0% |
| 4 | eval-acr-object-obs-only-default | 2/10 | 0% |
| 5 | eval-mag-perdof-norm02-object | 2/10 | 5% (1/20) |

### bjb2-28827 (6× 4090)
| GPU | 实验 | 进度 | 部分 SR |
|-----|------|------|---------|
| 0 | eval-mag-perdof-norm003-object | 2/10 | 0% |
| 1 | eval-mag-perdof-norm005-object | 2/10 | 0% |
| 2 | eval-mag-perdof-norm03-object-r3 | 0/10 | — |
| 3 | eval-mag-perdof-norm02-seed43-object-r3 | 0/10 | — |
| 4 | eval-mag-obsonly-norm005-object | 2/10 | 0% |
| 5 | eval-mag-obsonly-norm03-object | 2/10 | 0% |

### bjb2-40593 (1× 4090D)
| GPU | 实验 | 进度 | 部分 SR |
|-----|------|------|---------|
| 0 | eval-mag-obsonly-norm003-b2 (spatial) | **8/10** | 39% (31/80) |

### 关键观察
- **最快的** bjb1-18228 GPU 2/3 已完成 6/10，预计还需 ~4-5h 完成
- **bjb2-40593 spatial** 接近完成 (8/10)，当前 39% SR vs obs_only norm=0.3 spatial 36%
- **bjb2-28827** 6 个实验进度最慢（0-2/10），是最近启动的 magnitude sweep 批次
- **seed=43 六方**: obs_only 8.3%, argmin 10%, perdof 10%, vla_mean 6.7%, scalar 0%（均为部分结果）
- 前两个 task (alphabet_soup, cream_cheese) 几乎所有方法都是 0%，这是 object benchmark 中最难的两个 task

---
