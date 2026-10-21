# analysis figure data version audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_figure-data-version-audit_20260519T233000_result.json`
- **Structured JSON:** [`df324e38f3e8ebea3b99.json`](../../sessions/df/df324e38f3e8ebea3b99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有关键数据追溯完成。让我做最后一步交叉验证：确认 treated_untreated CSV 中的 accuracy 数据与 phase2_summary.csv 一致（证明用的是同一 eval_results_v2）。

验证 CSV 中 gemma2_d000 baseline:
- phase2_summary.csv: gemma2_d000 MMLU = 0.6186
- treated_untreated_summary.csv d025行: treated_acc_base=0.6184, untreated_acc_base=0.6187, weighted avg ≈ (0.6184×3540 + 0.6187×10502)/14042 = 0.6186 ✅

再交叉验证 Table 2 (DiD) 数据：
- gemma2 d025: treated_Δ=+0.0311 (+3.1pp ✓), untreated_Δ=+0.0256 (+2.6pp ✓), DiD=+0.0055 (+0.6pp ✓), treated_p=0.0096 (** ✓), untreated_p=0.0002 (*** ✓)
- qwen14b d025: treated_Δ=-0.0693 (-6.9pp ✓), untreated_Δ=-0.0756 (-7.6pp ✓), DiD=+0.0063 (+0.7pp ✓)
- qwen7b d025: treated_Δ=-0.0376 (-3.8pp ✓), untreated_Δ=-0.0291 (-2.9pp ✓), DiD=-0.0084 (-0.8pp ✓)

全部匹配。

---

## 审计报告

### Fig 1 (fig_dose_response.pdf — 5-family MMLU dose-response): ✅ Aligned

- **生成脚本**: westd `/root/autodl-tmp/exp001/analyze_phase2.py`（数据硬编码）
- **数据源**: westd `/root/autodl-tmp/exp001/eval_results_v2/phase2_summary.csv`
- **evaluate.py 版本**: westd md5 = `001a9bc23f808c47d25ef9eaeecb81f1` ✅（37591 bytes，aligned reference）
- **交叉验证**: 5 families × 5 dosages 的 accuracy 值与 phase2_summary.csv 逐项匹配

### Fig 2 (fig_treated_untreated.pdf — treated/untreated DiD): ✅ Aligned

- **生成脚本**: westd `/root/contamcal-irt-calibration/analysis/treated_untreated_analysis.py`
- **数据源**: westd `eval_results_v2/` 下的 `correctness_matrix.json`（通过 `--eval-dir` 参数传入）
- **验证**: gemma2_d000 baseline accuracy 在 phase2_summary 和 treated_untreated_summary.csv 间一致（0.6186），证明读取同一 eval_results_v2
- **SCP 路径**: westd → 本地 `docs/paper/figures/fig_treated_untreated.pdf`（2026-05-19 SCP v2）

### Table 1 (tab:taxonomy — 5 dose-response patterns): ✅ Aligned

- **数据源**: 与 Fig 1 相同（phase2_summary.csv / eval_results_v2）
- **交叉验证**: Phi-4 76.4%→76.44, Qwen-14B 69.4%→69.44, Qwen-7B 66.1%→66.11, Gemma-2 61.9%→61.86, OLMo-2 53.8%→53.79，全部匹配
- **Δacc 验证**: Qwen-14B -9.4pp (d000=69.44 - d100=60.07 = -9.37 ≈ -9.4 ✓), Gemma-2 +3.8pp (65.62-61.86=+3.76 ≈ +3.8 ✓)

### Table 2 (tab:did — DiD at d025 MMLU): ✅ Aligned

- **数据源**: westd `treated_untreated_summary.csv`（由 treated_untreated_analysis.py 用 eval_results_v2 数据产出）
- **交叉验证**: 5 models × (treated_Δ, untreated_Δ, DiD, p-value, verdict) 全部与 CSV 逐项匹配（见上方）
- cqa1 evaluate.py md5 也是 `001a9bc23f808c47d25ef9eaeecb81f1` ✅

### 结论

**全部 4 项均使用 aligned evaluate.py (C009: md5=001a9bc23f808c47d25ef9eaeecb81f1) 产出的 eval_results_v2 数据。无需重新生成。**

---
