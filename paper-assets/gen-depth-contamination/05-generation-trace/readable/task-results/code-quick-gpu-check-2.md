# code quick gpu check 2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_quick_gpu_check_2_20260522T162949_result.json`
- **Structured JSON:** [`840a1bfcfcb91ed39bc3.json`](../../sessions/84/840a1bfcfcb91ed39bc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度

### exp_llama8b_10k (GPU 0, 54GB/98GB, util 94%)
| depth | 状态 | 文件大小 |
|-------|------|---------|
| 0 | 完成 | 9.0 MB |
| 1 | 完成 | 7.8 MB |
| 2 | 完成 | 8.0 MB |
| 3 | 完成 | 8.3 MB |
| 4 | **进行中** 1153/1250 (92%) | - |

当前 depth 4, ~5.14s/it, 剩余 97 个 batch, 预计 **~8 分钟**完成。depth 4 完成后整个实验结束（假设 depth 0-4 共 5 层）。

### exp_gemma27b_c4 (GPU 2, 16GB/98GB, util 89%)
| depth | 状态 | 文件大小 |
|-------|------|---------|
| 0 | 完成 | 4.3 MB |
| 1 | 完成 | 4.1 MB |
| 2 | 完成 | 4.5 MB |
| 3 | **进行中** 384/625 (61%) | - |

当前 depth 3, ~14.14s/it, 剩余 241 个 batch, 预计 **~57 分钟**完成 depth 3。后续还有 depth 4, 预计额外 ~2.5 小时。

### 总结
- **Llama-8B**: 约 8 分钟内完成全部实验
- **Gemma-27B**: 约 3.5 小时完成全部实验（depth 3 剩 ~57min + depth 4 ~2.5h）
- GPU 1、3 空闲

---
