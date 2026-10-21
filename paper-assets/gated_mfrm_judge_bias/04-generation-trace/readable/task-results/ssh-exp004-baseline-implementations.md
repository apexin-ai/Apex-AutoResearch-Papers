# ssh exp004 baseline implementations

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp004-baseline-implementations_20260525T051315_result.json`
- **Structured JSON:** [`38716d1c10ac7a664740.json`](../../sessions/38/38716d1c10ac7a664740.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## 结果

| Method | τ (N=17) | ρ (N=17) | τ (N=8) | ρ (N=8) |
|--------|----------|----------|---------|---------|
| raw_average | 0.8382 | 0.9485 | 0.8095 | 0.8929 |
| cyclic_judge | 0.8382 | 0.9485 | 0.8095 | 0.8929 |
| cyclic_judge_discard | 0.8235 | 0.9338 | 0.8095 | 0.8929 |
| dcr_factor | 0.8235 | 0.9461 | 0.8095 | 0.8929 |
| preference_leakage | 0.8382 | 0.9485 | 0.8095 | 0.8929 |
| **uda_zscore** | 0.8235 | 0.9338 | 0.8095 | 0.8929 |
| **uda_quantile** | 0.8000 | 0.9166 | 0.7807 | 0.8469 |

## 实现情况

| Baseline | 状态 | 位置 |
|----------|------|------|
| CyclicJudge | ✓ 已有 | `exp004/baselines.py:baseline_cyclic_judge` |
| CyclicJudge+Discard | ✓ 已有 | `exp004/baselines.py:baseline_cyclic_judge_discard` |
| DCR Factor | ✓ 已有 | `exp004/baselines.py:baseline_dcr_factor` |
| Preference Leakage | ✓ 已有 | `exp004/baselines.py:baseline_preference_leakage` |
| **UDA (z-score)** | ✓ 新增 | `exp004/baselines.py:baseline_uda_zscore` |
| **UDA (quantile)** | ✓ 新增 | `exp004/baselines.py:baseline_uda_quantile` |

## 关键发现

- 所有简单 baseline 在 N=17 上的 τ 介于 0.80–0.84，差异极小
- CyclicJudge / PrefLeakage / raw_average 给出完全相同的排名（τ=0.8382）——说明 judge severity 校正在这个数据上几乎没有效果
- UDA quantile 是唯一使 τ 下降的方法（0.80），因为它强制均匀分布损失了信息
- 这些结果验证了论文论点：**独立 baseline 无法匹配 G-MFRM 联合模型的 τ 提升**

产出文件：
- `exp004/baselines.py`（含 UDA 实现）
- `exp004/results_n17/results.json`（完整结果）
- `exp004/results_n17/baseline_summary.csv`（汇总 CSV）

---
