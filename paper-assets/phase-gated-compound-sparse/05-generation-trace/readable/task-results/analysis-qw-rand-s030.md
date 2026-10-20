# analysis qw rand s030

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qw_rand_s030_20260514T084513_result.json`
- **Structured JSON:** [`21a0526fb751561c7da7.json`](../../sessions/21/21a0526fb751561c7da7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| 指标 | 值 |
|------|-----|
| sparsity | 0.30 |
| median (high→mid→low) | 3.955 → 6.398 → 8.196 |
| median_diff | +4.241 |
| pass_fail | **PASS** (median 单调递增，high-low CI 不重叠) |
| n_problems | 50 |

**与预期不同**：s030 的内置测试判定为 PASS，不同于 s015/s020/s025 的 FAIL。随 sparsity 增大，interaction index 幅度增长，在 s=0.30 首次达到 high-low median CI 分离。但 low phase 的 mean 为 -33.24（3 个极端 outlier，skewness=-11.4），结果方差较大，稳健性存疑。

---
