# check pivot b full urgent

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pivot_b_full_urgent_20260513T233635_result.json`
- **Structured JSON:** [`e3f9d515cb506331ae32.json`](../../sessions/e3/e3f9d515cb506331ae32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== PIVOT_B_FULL STATUS ===
PID 109597: DEAD（无存活进程）
GPU: 0%, 0 MiB / 97887 MiB（空闲）
Progress: 已完成（EXIT_CODE=0）
Log tail: 分析了 G0/G1/G2 三代，每代 6 个 checkpoint（step 76/152/228/304/305/999999），共 18 个
Output: /root/autodl-tmp/output_v7/pivot_b_analysis_full/generated_vs_holdout_eff_rank.json (4.1KB, 07:12生成)
```

任务已正常结束。关键结果摘要：

| Gen | 趋势 |
|-----|------|
| G0 | Generated eff_rank 52-61，Delta ~50-58 |
| G1 | Generated 快速下降（76→228: 59→6），Delta 飙升至 ~105-106 |
| G2 | Generated 全部趋近 1.0-1.1，Delta ~110，**完全坍缩** |

G1→G2 发生了剧烈的 effective rank 坍缩，generated 数据的 eff_rank 从个位数进一步降到 ~1，与 holdout 的 ~111 形成巨大差距。

---
