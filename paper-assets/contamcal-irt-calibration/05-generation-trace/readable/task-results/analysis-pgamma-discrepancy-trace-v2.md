# analysis pgamma discrepancy trace v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pgamma-discrepancy-trace-v2_20260521T174947_result.json`
- **Structured JSON:** [`0857fde503df1568a90b.json`](../../sessions/08/0857fde503df1568a90b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。

**根因**：Table 15（γ=-0.63）和 Table 10（γ=-0.497）均标注 J=16、N(0,1) prior，但由两个不同脚本产出：
- `run_mmlu_domain_gamma_j16.py` → γ=-0.63（主分析管线）
- `gamma_prior_sensitivity.py` → γ=-0.497（sensitivity 分析）

两个脚本的 `n_total_items` 计算方式不同（metadata 字段 vs `min(len(per_item))`），导致 `build_domain_col_indices` 映射出不同的 Social Sciences 列索引，最终子采样得到不同的 2000 条 item（mean_acc 差 1.13pp：0.7198 vs 0.7085）。

**修正**：重跑 `gamma_prior_sensitivity.py`，统一使用 j16 的数据加载路径，使 Table 10 的 N(0,1) baseline 与 Table 15 J=16 行一致。

---
