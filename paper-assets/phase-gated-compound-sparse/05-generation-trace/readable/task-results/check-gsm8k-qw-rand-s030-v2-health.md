# check gsm8k qw rand s030 v2 health

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gsm8k_qw_rand_s030_v2_health_20260515T232159_result.json`
- **Structured JSON:** [`fb48912bbf965e1d3de0.json`](../../sessions/fb/fb48912bbf965e1d3de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：DEAD — 已正常完成退出。**

进程 286781 已结束，不是崩溃，是任务跑完了。日志显示：

- **50/50 问题全部处理完毕**，最后一条日志时间 `07:20:42`
- 结果已保存到 `./profiling_output_gsm8k_qw_rand_s030_v2/profiling_results.json` 和 `generations.json`
- **EXIT_CODE=0**（正常退出）

**Profiling 结果摘要：**

| Phase | Tokens | Segments | II median | II mean |
|-------|--------|----------|-----------|---------|
| high_sparsity | 9326 | 216 | +2.31 | +11.83 |
| low_sparsity | 29224 | 252 | +5.20 | +31.26 |
| mid_sparsity | 5954 | 51 | +2.70 | +18.02 |

**Verdict: PASS** — high_sparsity vs low_sparsity 的 CI 在 sparsity=0.3 下不重叠。

GPU 1 当前空闲，可分配新任务。

---
