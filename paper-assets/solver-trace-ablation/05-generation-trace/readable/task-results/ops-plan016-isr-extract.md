# ops plan016 isr extract

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan016-isr-extract_20260515T202430_result.json`
- **Structured JSON:** [`1b39c4fcc5d14652e120.json`](../../sessions/1b/1b39c4fcc5d14652e120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个备份文件内容一致。以下是 plan016-extended-1000-s42 的 ISR 指标：

## eval_sta 结果

**文件路径**：
- `/root/autodl-tmp/eval_results_backup/plan016_extended_1000_s42_eval_results.json`
- `/root/autodl-tmp/eval_backups/plan016_extended_1000_s42_eval_results.json`

**Summary 指标**：

| 指标 | 值 |
|------|------|
| `mean_isr` | **0.0027** |
| `proved_only_mean_isr` | **0.0028** |
| `isr_std` | 0.0118 |
| `median_isr` | 0.0 |
| `min_isr` | 0.0 |
| `max_isr` | 0.0588 |
| `isr_pr_ratio` | 0.0028 |
| `n_proved` | 96/100 |
| `prove_rate` | 0.96 |

**按 answer_type 分**：
- `false`: 26/29 proved, mean_isr = 0.0
- `unknown`: 30/31 proved, mean_isr = 0.00526
- `true`: 40/40 proved, mean_isr = 0.00261

## 与论文对比

论文引用 ISR* = 0.003 (0.0027)：
- `proved_only_mean_isr` = 0.0028 ≈ 0.003（四舍五入一致）
- `mean_isr` = 0.0027（精确匹配）

**结论：论文数据与 eval_sta 输出一致。**

注意：`outputs/` 目录下没有 `eval_sta_plan016*.json` 文件（只有 classify_h7 文件），eval 结果仅存于 `/root/autodl-tmp/` 的两个备份目录中。

---
