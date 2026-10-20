# fix ess only analysis doc

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ess_only_analysis_doc_20260515T143658_result.json`
- **Structured JSON:** [`15b62ba361bd917bc9f1.json`](../../sessions/15/15b62ba361bd917bc9f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。变更汇总：

| 位置 | 原值 | 修正值 | 依据 |
|------|------|--------|------|
| 主 eval 表 PPL | 17.73 | **17.728** | eval JSON: 17.7277 |
| 对比表 ess_only PPL | 17.73 | **17.728** | 同上，delta +0.038 现在与显示值一致 (17.728-17.690=0.038) |
| 叙述中 adaptive PPL | 17.65 | **17.650** | 与 3dp 精度一致 |
| 叙述中 ess_only PPL | 17.73 | **17.728** | 同上 |
| 叙述中 b* median | 1.58 | **1.582** | step_metrics: 1.5820，与表格 3dp 一致 |
| 叙述中 b* mean | 3.51 | **3.506** | step_metrics: 3.5061，与表格 3dp 一致 |
| 原始数据 final_ppl | 17.73 | **17.728** | eval JSON |

核心问题是 PPL 被过度四舍五入到 2dp (17.73)，导致与 delta +0.038 不自洽（17.73-17.690=+0.040≠+0.038）。改为 3dp (17.728) 后所有数字和 delta 计算一致。

---
