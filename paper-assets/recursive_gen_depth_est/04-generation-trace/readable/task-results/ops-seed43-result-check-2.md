# ops seed43 result check 2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed43-result-check-2_20260518T122548_result.json`
- **Structured JSON:** [`7595e71a62b82e93f3cb.json`](../../sessions/75/7595e71a62b82e93f3cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**gpt2xl_seed43_001 已失败**，进程已结束（cuda:1 空闲）。

数据生成和特征提取全部完成（20000 samples x 19 features），但在 **Step 8: 5-fold CV RF evaluation** 崩溃：

```
ValueError: Input X contains infinity or a value too large for dtype('float32').
```

原因：depth_3 的 `mean_ppl` 均值高达 2,114,828，`var_ppl` 达 4.3e16，导致 float32 溢出。`eval_second_seed.py:75` 的 `rf.fit()` 无法处理 inf/极大值。

修复方向：在 RF fit 前对特征做 `np.clip` 或 `np.nan_to_num` 处理 inf 和极端值，或将 ppl 类特征取 log 变换。

---
