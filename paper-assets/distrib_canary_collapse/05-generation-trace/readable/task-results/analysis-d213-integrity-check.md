# analysis d213 integrity check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d213_integrity_check_20260524T005725_result.json`
- **Structured JSON:** [`fa9e19e47a86c0898ea3.json`](../../sessions/fa/fa9e19e47a86c0898ea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## 子任务 1: T=15 α=0.75 s42 1.4B 数据

- **找到** — 在 westd-19828 上
- **实际路径**: 
  - 原始输出: `/root/autodl-tmp/distrib_canary_collapse/outputs/scale_14b_t15_a075_s42_fp32/`
  - 已转移至: `/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a075_s42_fp32_14b/`
- **之前找不到的原因**: Worker 在 `results/phase_diagram/` 搜索 `*t15_a075_s42_fp32_14b*` 但原始输出在 `outputs/` 目录下且命名为 `scale_14b_t15_a075_s42_fp32`（前缀式 vs 后缀式 14b）。数据后来已被复制到 `results/phase_diagram/t15_a075_s42_fp32_14b/`
- **完整性**: gen_0 ~ gen_15（16 个目录，T=15 正确），EXIT_CODE=0，all_metrics.json 完整含全部 16 代
- **D102 分析**: 已于 2026-05-24 08:42 CST 在 19828 上运行完成，用 `run_5method_analysis_d102.py`
- **已下载到本地**: `artifacts/D102_14b_t15_a075_s42_fp32_14b_6pair.json`

**D102 结果:**
| 指标 | 值 |
|---|---|
| PermG_fwd | 6/6 |
| PermG_rev | 0/6 |
| DiffXcorr_fwd | 6/6 |
| Threshold_fwd | 6/6 |
| TY_fwd | 5/6 |
| Robust (K≥3) | 6/6 |

所有 6 pair 的 consensus votes ≥ 4（token_entropy<distinct_1 和 ece<distinct_2 为 5/5 全票）。

---

## 子任务 2: 管线确认

**使用的脚本:**
- **s42 全系列**: `run_5method_analysis_d102.py`（项目根目录），输出详细格式（44KB，含完整 lag 数据、所有方法 FDR 计数）
- **s43 T=15 全系列**: `batch_d102_6pair.py`（scripts/ 目录），输出精简格式（~5KB，含 summary + consensus + metrics_trajectory）
- **s44 T=10 全系列**: `batch_d102_6pair.py`，同上精简格式（~4KB）

**区分依据**: 文件大小差异 10x（44KB vs 4-5KB）、s42 有 `diff_xcorr_fdr_*` / `threshold_forward_sig` / `ty_forward_sig` 字段而 s43/s44 没有、s43/s44 有 `T` / `note` / `total_pairs` 字段而 s42 没有

**BH FDR**: 全部包含 — 所有文件的 summary 都使用 `perm_granger_fdr_forward_sig` 命名（fdr 后缀）

**D111 方向滤波**: 隐式包含 — 所有文件按 `forward` / `reverse` 分析，consensus 仅统计 forward 方向。peak_lag 值在 s42 详细输出中可见（forward 分析中 peak_lag < 0 = canary leads downstream，符合 C009 修正后的约定）

**threshold_criterion**: 全部使用 `true_3sigma_d105`（符合 C008）

---
