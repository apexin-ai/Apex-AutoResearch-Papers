# code paper data json

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper_data_json_20260517T005602_result.json`
- **Structured JSON:** [`0d865251bf127bb14a87.json`](../../sessions/0d/0d865251bf127bb14a87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已成功创建。

## 数据提取报告

### 成功提取

**fig2_temporal_improvement.json** — 全部字段已填充：
- `r1_8b_hs`: 来自 `exp_007_window_ablation/results.json` (precp_fpr_trace 作为 precp_fpr)
- `r1_8b_text`: 来自 `text_window_ablation_r1_8b/results.json`
- `r1_32b_best`: layer=10/window=10，bal_acc 和 precp_fpr 来自 `m001_layer_fix/temporal_lr_r1_32b.json`，precision 和 coverage 来自 `exp_007_window_ablation/results.json`（两文件 bal_acc/precp_fpr 一致，确认使用相同配置）
- `qwq_32b_best`: layer=2/window=5，同上逻辑

**fig3_bootstrap_ci.json** — 全部字段已填充：
- `r1_8b` accuracy/precision: `acc_precision_bootstrap/results.json`；fpr: `r1_8b_bootstrap_hs_text/results.json`
- `r1_32b` accuracy/precision: `acc_precision_bootstrap/results.json`；fpr: `m001_layer_fix/bootstrap_hs_vs_text_r1_32b.json`
- `qwq_32b` accuracy/precision: `acc_precision_bootstrap/results.json`；fpr: `qwq_text_verify/bootstrap_results.json`

### 注意事项

- fig2 中 `precp_fpr` 对于 HS 方法使用的是 `precp_fpr_trace`（trace-level FPR），与 text baseline 的 `precp_fpr` 定义一致
- fig2 中 R1-32B/QwQ-32B 的 `coverage` 使用 exp_007 中的值（与 m001_layer_fix 中的 `crossing_rate` 定义略有不同：0.7 vs 0.5 for R1-32B）
- fig3 中 R1-32B 和 QwQ-32B 的 FPR 差异不显著（p=0.999 和 p=0.904），HS 优势仅在 R1-8B 上显著

---
