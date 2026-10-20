# analyze acc qw s015 b1 8k

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_acc_qw_s015_b1_8k_20260516T013209_result.json`
- **Structured JSON:** [`df49909f36a0acc01376.json`](../../sessions/df/df49909f36a0acc01376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `acc_qw_s015_b1_8k` 已正常完成，确认如下：

**状态：SUCCESS**

- 日志末尾 `EXIT_CODE=0`，无 crash/error
- 进程已退出（ps 中无相关 python 进程）
- 结果 JSON 已保存：`accuracy_eval_qw_s015_b1_8k.json`

**最终 metrics（已确认为最终值，50/50 题全部完成）：**

| 指标 | 值 |
|------|-----|
| accuracy | **46.0% (23/50)** |
| total_time | 791s |
| heads_pruned | 112 (每题固定) |
| kv_evicted | ~14% prompt tokens |
| max gen_length | 3516 (problem 12) |
| mean gen_length | ~530 |

与 cron 中间报告的 metrics 完全一致，是最终结果。

**QW batch1 8k 系列汇总：**

| 实验 | accuracy | 状态 |
|------|----------|------|
| acc_qw_dense_b1_8k | (baseline) | success |
| acc_qw_s020_b1_8k | - | success |
| acc_qw_s015_b1_8k | 46.0% | success |

无异常信息。

---
