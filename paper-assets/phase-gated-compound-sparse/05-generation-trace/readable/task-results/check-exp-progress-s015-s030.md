# check exp progress s015 s030

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_progress_s015_s030_20260516T002327_result.json`
- **Structured JSON:** [`4a72088fd1f7b3aa9c44.json`](../../sessions/4a/4a72088fd1f7b3aa9c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 实验 | 进度 | Accuracy | 状态 |
|------|------|----------|------|
| acc_ds_s015_8k_v2 | 47/50 | 20/46 = 43.5% | 运行中，~5-15 min 完成 |
| acc_ds_s030_8k_v2 | 25/50 | 2/24 = 8.3% | 运行中，~50-70 min 完成 |
| acc_qw_dense_n100 | 50/50 | 24/50 = 48.0% | ✅ 已完成 |

**GPU 状态**: cuda:0 和 cuda:2 在用（各 ~70% 利用率，~16GB 显存），**cuda:1 和 cuda:3 完全空闲**，无任何进程。

**异常**: s030 准确率极低（8.3%），Problem 18-24 连续 7 题全部超时（pred=None），224 heads pruned 后模型推理链严重退化。报告已写入 artifacts。

---
