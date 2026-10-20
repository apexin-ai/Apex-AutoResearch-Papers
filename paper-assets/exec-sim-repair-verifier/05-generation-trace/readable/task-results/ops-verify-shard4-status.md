# ops verify shard4 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-shard4-status_20260516T042706_result.json`
- **Structured JSON:** [`4a7f605016918018f75b.json`](../../sessions/4a/4a7f605016918018f75b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### shard4 状态：已完成

- **进程已结束**（日志显示完整的评估报告摘要）
- 已处理 **688 / 684 样本**（全部完成，多 4 条可能是边界包含差异）
- 最终结果写入 `eval_repo_cwm.json`，评估已跑完

### shard4 结果摘要

| 指标 | 值 |
|------|-----|
| Accuracy | 65.55% |
| Majority baseline | 75.73% |
| F1 macro | 52.66% |
| F1 (fail) | 28.0% |
| F1 (pass) | 77.4% |
| CWM unparseable | 504/688 (73.3%) |
| Truncated | 49/688 (7.1%) |

### 各 shard 进度

| Shard | 目录 | 已处理样本 | 状态 |
|-------|-------|-----------|------|
| shard1 | `cwm_8b_ckpt400_test/` | 7176 | 完成（这是原始全量 or 多 shard 合并？行数远超单 shard） |
| shard2 | `cwm_8b_ckpt400_test_shard2/` | 1568 | 完成 |
| shard3 | `cwm_8b_ckpt400_test_shard3/` | 928 | 完成 |
| shard4 | `cwm_8b_ckpt400_test_shard4/` | 688 | 完成 |

shard1 的 7176 行异常大，可能是之前的全量测试运行或包含了增量追加的结果，需要进一步确认其实际覆盖范围。

---
