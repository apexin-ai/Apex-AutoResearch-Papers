# analysis irt refit check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt-refit-check_20260516T152124_result.json`
- **Structured JSON:** [`a3657491b46216138aee.json`](../../sessions/a3/a3657491b46216138aee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**IRT Refit**: 全部完成 ✅
- `pooled_irt_2pl_gamma_mmlu_arc` (2PL+γ, 1.5B, N=8): MMLU 良好 (PPP=0.426, MAE=0.002), ARC 拟合差 (PPP=0.002)
- `pooled_irt_all_scales` (2PL+γ, 3 scales, N=15): 已完成
- `results_mmlu_domain_gamma_n24`: 域级分析已完成

**Signals**: 所有 24 respondents (3 scales × 4 dosages × 2 seeds) 原始信号文件**全部齐全** (每个 9 files)

**RRF 聚合缺口**:
- `Qwen2.5-3B_d100_a32_s42` — 缺全部 3 个 signals_merged
- `Qwen2.5-3B_d000_s123_a32` — 缺 signals_merged_mmlu

**下一步**: 对这 2 个目录补跑 `aggregate_rrf.py`（CPU 任务），然后可执行 full N=24 pooled 2PL+γ IRT。

---
