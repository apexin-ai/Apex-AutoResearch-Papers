# paper figure status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_status_check_20260516T044419_result.json`
- **Structured JSON:** [`08ec935817750b5bab75.json`](../../sessions/08/08ec935817750b5bab75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：所有 4 个论文图表均已完成，无需补全。**

服务器 `westd-11235` 上 `/root/trace-verdict-study/figures/paper/` 目录：

| 图表 | 状态 | 文件大小 |
|------|------|---------|
| fig1_trace_overview | ✅ | 37 KB PDF |
| fig2_calibration | ✅ | 18 KB PDF |
| fig3_cross_model_gap | ✅ | 33 KB PDF |
| fig4_trace_length (ablation) | ✅ | 17 KB PDF |

trace_length_ablation 的 6 个数据点（256tok/512tok/1024tok/no_limit/exception_only/no_trace）与 bootstrap JSON 完全一致。fig1_trace_overview 也已生成（非缺失）。

状态报告已写入 artifacts 并注册（`art_20260516_1f38dd`）。

---
