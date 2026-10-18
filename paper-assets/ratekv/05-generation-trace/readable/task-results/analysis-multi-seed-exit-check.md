# analysis multi seed exit check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi_seed_exit_check_20260514T105828_result.json`
- **Structured JSON:** [`96d5ccd246b39e1ec501.json`](../../sessions/96/96d5ccd246b39e1ec501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Conclusion: SUCCESS**

日志无 traceback/error/OOM，正常打印 "FINAL RESULTS" 并 "Saved to /root/ratekv/multi_seed_results.json"。3 seeds 全部完成，总耗时 3.33h。

### 结果摘要

| Metric | Value |
|--------|-------|
| Baseline PPL (FP16) | 9.8106 |
| Uniform 4-bit PPL | 15.4454 |

| Seed | Constrained MCKP PPL | Bit Dist (2/4/8) | Profile Time |
|------|----------------------|-------------------|-------------|
| 0 | 11.0168 | 8/100/4 | 65.1 min |
| 1 | 10.8981 | 8/100/4 | 66.6 min |
| 2 | 11.0487 | 8/100/4 | 65.1 min |

**Constrained MCKP mean±std: 10.9878 ± 0.0648**

### 额外指标
- 所有 3 seeds 的 bit distribution 完全一致：2-bit×8, 4-bit×100, 8-bit×4 (memory ratio = 0.25)
- Allocation agreement: **90.2%** (101/112 heads 三个 seed 一致)
  - seed0 vs seed1: 94.6%
  - seed0 vs seed2: 91.1%
  - seed1 vs seed2: 94.6%

### 结果文件
- `/root/ratekv/multi_seed_results.json` (20KB, 完整 JSON 含所有 seed 的 per-head allocations)
- `/root/ratekv/multi_seed_profiles_s{0,1,2}.json` (per-seed profiling data)
- `/root/ratekv/multi_seed_checkpoint_s{0,1,2}.json` (checkpoints)

---
