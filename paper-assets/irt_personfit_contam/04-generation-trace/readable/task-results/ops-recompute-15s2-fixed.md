# ops recompute 15s2 fixed

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recompute-15s2-fixed_20260522T193034_result.json`
- **Structured JSON:** [`dcb2204b6560c208d218.json`](../../sessions/dc/dcb2204b6560c208d218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过（contam_15_s3 完全匹配），结果如下：

**15% s2 θ-fixed 重算结果：**
- lz_fixed = 11.8704
- lz\*_fixed = 14.0163
- d_fixed = **7.79** （用 n=10 clean baseline: mean=7.3522, std=0.5802）
- d\*_fixed = 7.79（lz 和 lz\* 的 Cohen's d 相同，因为 Snijders 校正是线性变换）
- CI_95 = [6.51, 13.05]（bootstrap 10000 resamples, percentile method）
- 验证：contam_15_s3 的 lz_fixed 与 theta_fixed_all_seeds.json 完全一致（误差 < 1e-6）

之前的 d_fixed=7.79 是正确的，并非基于 n=3 baseline。n=10 baseline 重算后仍为 7.79。

---
