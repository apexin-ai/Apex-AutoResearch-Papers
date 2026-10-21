# check westd progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_progress_20260518T040205_result.json`
- **Structured JSON:** [`44f617bc0365cf26dd1b.json`](../../sessions/44/44f617bc0365cf26dd1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度

### exp_14b_c4 (GPU 0, Qwen2.5-14B)
| 指标 | 值 |
|---|---|
| GPU 利用率 | 87%, 31GB/98GB VRAM |
| 已完成 depth | 0, 1, 2, 3 |
| 当前 depth | **depth 4**: 986/1250 (79%), ~8.4s/it |
| depth 4 剩余 | 264 batches × 8.4s ≈ **37 min** |
| depth 5 预计 | 1250 × 8.4s ≈ **2.9 h** |
| **预计完成** | **~3.5 h 后** (约今天 15:30) |

### exp_32b_c4 (GPU 1, Qwen2.5-32B)
| 指标 | 值 |
|---|---|
| GPU 利用率 | 95%, 65GB/98GB VRAM |
| 已完成 depth | 0 |
| 当前 depth | **depth 1**: 2178/2500 (87%), ~14s/it |
| depth 1 剩余 | 322 batches × 14s ≈ **1.3 h** |
| depth 2-5 剩余 | 4 × 2500 × 14s ≈ **38.9 h** |
| **预计完成** | **~40 h 后** (约 5月20日 04:00) |

32B 因 batch_size=2（14B 用 4）且模型更大，速度慢约 1.7 倍，加上剩余 depth 更多，总耗时显著更长。

---
