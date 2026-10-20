# analysis qwen n500 verify and progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_n500_verify_and_progress_20260515T052805_result.json`
- **Structured JSON:** [`c50f6cd04b720f3ef301.json`](../../sessions/c5/c50f6cd04b720f3ef301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下。

---

## GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 80% | 30.1/95.6 GB |
| 1 | 77% | 30.6/95.6 GB |
| 2 | 0% | idle |
| 3 | 0% | idle |

GPU 0-1 跑 DeepSeek s030，GPU 2-3 已空闲（Qwen 完成）。

## Qwen n=500 数据完整性

| Condition | Problems | pass_fail | 文件大小 |
|-----------|----------|-----------|----------|
| qw_imp_s015 | 500 | PASS | 18.3MB |
| qw_imp_s020 | 500 | PASS | 18.3MB |
| qw_imp_s025 | 500 | PASS | 18.3MB |
| qw_imp_s030 | 500 | PASS | 18.3MB |
| qw_rand_s015 | 500 | **FAIL** | 18.3MB |
| qw_rand_s020 | 500 | PASS | 18.3MB |
| qw_rand_s025 | 500 | PASS | 18.3MB |
| qw_rand_s030 | 500 | PASS | 18.3MB |

**8/8 conditions 数据完整（均 500 problems），7/8 PASS。**

`qw_rand_s015` FAIL 原因：ci_overlap_test 和 sign_reversal_test 均未通过（无 warnings）。这是 random masking 在低 sparsity 下的预期行为——random 在 s=0.15 时信号太弱，interaction index 的 CI 重叠/符号不一致。数据本身完整，FAIL 是统计检验结果。

## DeepSeek s030 进度

| Condition | 当前进度 | 已运行 | 预估 ETA |
|-----------|----------|--------|----------|
| ds_imp_s030 (GPU 0) | 252/500 | 2h09m | ~2h10m |
| ds_rand_s030 (GPU 1) | 299/500 | 2h34m | ~1h25m |

DeepSeek s030 两个 condition 均在正常运行中，无报错。ds_rand 约 14:55 完成，ds_imp 约 15:40 完成。

## 异常告警

- `qw_rand_s015` FAIL — 统计检验未通过，非数据问题，无需重跑。

---
