# fix baseline path and rerun

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_baseline_path_and_rerun_20260518T031951_result.json`
- **Structured JSON:** [`dda6b7adac51bd24088d.json`](../../sessions/dd/dda6b7adac51bd24088d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据齐全。以下是修正后的完整 3-point curve：

## 修正后完整结果

**修改内容**: `scripts/exp_029a_postprocess/03_analyze_fixed.py` line 31: `exp_012_logprob/samples_with_logprobs.jsonl` → `exp_012_rerun_1024/samples.jsonl`

**残留旧路径引用**（历史脚本，不影响 029a/029b）:
- `scripts/analyze_lp_range_cdf_n529.py`
- `scripts/calibration_baseline.py`
- `scripts/adalp_analysis.py`
- `output/exp_005_v2_temperature/temperature_sensitivity_report.json`
- `output/exp004v2_re_diagnostic/full_report.json`
- `output/exp_015_v2/exp015_v2_metrics.json`
- `output/analysis_round8/run_epsilon_fine.py`
- `output/d108_lp_vc_combination/analyze_lp_vc.py`
- `output/lp_rank_comparison.py`

---

### Corrected 3-Point Curve (SciERC, N=8, gold-filtered n=529)

| Metric | 3-epoch (029a) | 5-epoch (corrected) | 10-epoch (029b) |
|---|---|---|---|
| **Degeneracy (CF1 gold-filtered) %** | **6.43** | **17.77** | **47.83** |
| Greedy F1 | 0.6501 | 0.6439 | 0.6491 |
| Oracle F1 | 0.7998 | 0.7758 | 0.7331 |
| Headroom (pp) | 14.97 | 13.19 | 8.40 |
| LP selection F1 | 0.6383 | 0.6501 | 0.6567 |
| LP selection delta (pp) | -1.18 | +0.62 | +0.75 |
| Within-inst ρ(LP,F1) mean | 0.2727 | 0.1795 | 0.0685 |
| Within-inst ρ(LP,F1) median | 0.3172 | 0.2817 | 0.1201 |
| LP range mean | 0.085427 | 0.062189 | 0.033337 |
| LP range median | 0.067187 | 0.040121 | 0.023715 |
| FK ρ (global) | 0.5302 | 0.4834 | 0.3413 |
| SJ ρ (global) | 0.5160 | 0.4647 | 0.3441 |
| EM ρ (global) | 0.3353 | 0.3851 | 0.3035 |
| VC ρ (global) | 0.5074 | 0.4606 | 0.3571 |
| LP ρ (global) | 0.3551 | 0.2830 | 0.1588 |
| Valid ρ instances | 495 (93.6%) | 435 (82.2%) | 276 (52.2%) |

**关键发现**:
- Degeneracy 单调递增：6.4% → 17.8% → 47.8%（epoch-degeneracy 关系确认）
- LP range 单调递减：0.085 → 0.062 → 0.033（更多 epoch → logprob 分布更集中）
- Within-instance ρ 单调递减：0.317 → 0.282 → 0.120（LP 信号质量随 epoch 退化）
- 所有 global QE ρ 在 10-epoch 均下降，LP 下降最严重（0.355 → 0.283 → 0.159）
- LP selection 在 5/10-epoch 仍为正 delta（+0.62/+0.75pp），但 3-epoch 反而为负（-1.18pp）

---
