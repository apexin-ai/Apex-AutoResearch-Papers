# diag qwen t09 final check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen-t09-final-check_20260518T203408_result.json`
- **Structured JSON:** [`06bbf6566a1f55b8392e.json`](../../sessions/06/06bbf6566a1f55b8392e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Qwen3-0.6B t=0.9 全部完成。** Pipeline 已自动触发并成功执行。

## 结果

| 指标 | 值 |
|---|---|
| **Binary F1** | 0.5984 |
| Binary 95% CI | [0.5819, 0.6154] |
| Binary N | 3490 |
| **3-class F1** | 0.6851 |
| 3-class 95% CI | [0.6735, 0.6974] |
| 3-class N | 4485 |
| **Spearman ρ (entropy_mean)** | -0.2939 (p=4.43e-90) |

### Per-feature Spearman

| Feature | ρ |
|---|---|
| hapax_ratio | -0.4902 |
| ttr | -0.4672 |
| entropy_mean | -0.2939 |
| entropy_min | -0.1594 |
| tail_decay | -0.0843 |
| entropy_std | -0.0436 |
| entropy_max | +0.0834 |

### 服务器状态
- Generation: 996 seeds, 4494 records, 271 skipped, 耗时 ~3h
- GPU: 全部空闲 (0% utilization, 0 MiB used)
- Monitor: 4个目标全部 done (olmo_t05, qwen06_t05, olmo_t09, qwen06_t09)
- 有一个 zombie python 进程 (PID 27228)，不影响后续操作

---
