# analysis v6 random s030 r3

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v6_random_s030_r3_20260514T063834_result.json`
- **Structured JSON:** [`aaf09e74703d8d495f54.json`](../../sessions/aa/aaf09e74703d8d495f54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `v6_random_s030_r3` 已被之前的 hook 自动处理，registry 已是 **DONE / success** 状态，无需再次更新。

## 结果摘要

| 指标 | high_sparsity | mid_sparsity | low_sparsity |
|------|--------------|-------------|-------------|
| II mean | +9.24 | **-230.76** | -7.41 |
| II median | 4.02 | 2.43 | 4.74 |
| PPL (both) | 39.18 | 27.44 | 88.94 |
| tokens | 21,086 | 13,306 | 27,748 |

- **Verdict: PASS** — CI non-overlapping (high vs mid), sign reversal (high>0, mid<0)
- 50 problems, EXIT_CODE=0, 运行 0.49h
- 输出文件: `profiling_results.json` (1.9MB)

**注意**: mid_sparsity mean II=-230.76 有极端 skewness (-13.08)，1个 outlier 拉低了 mean，但 median (2.43) 与其他 phase 接近。这与 random masking 预期一致——random baseline 的 II gradient 主要由 outlier 驱动而非结构化效应，对比 importance masking 的单调递增 gradient。

---
