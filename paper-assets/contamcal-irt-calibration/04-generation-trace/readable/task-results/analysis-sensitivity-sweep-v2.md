# analysis sensitivity sweep v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sensitivity-sweep-v2_20260519T194614_result.json`
- **Structured JSON:** [`180e3cdca8ea8560a455.json`](../../sessions/18/180e3cdca8ea8560a455.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### Verification: 6/6 PASSED
所有 test case 在默认参数 (τ=1.0, σ=5.0) 下分类正确。

### 30-combo Sweep 结果

**v2 在全部 30/30 组合中 6 个 family 均分类正确（6/6 × 30 = 180/180）。**

### V1 → V2 变化
- **35 处分类变化，全部是改进，0 处回退**
- **Qwen-7B s123**: v1 在 30/30 组合中全部误判为 Immune → v2 全部正确修正为 V-recovery（+30）
- **Qwen-7B s42**: 当 τ=2.0 时（delta=-1.78 落入 |delta|≤τ），v1 误判为 Immune → v2 通过 volatility check 正确识别为 V-recovery（+5）

### 关键检查
| 检查项 | 结果 |
|--------|------|
| Qwen-7B s123 正确分类为 V-recovery | **30/30** 组合 (v1: 0/30) |
| Phi-4 保持 Immune | **30/30** 组合 |
| 4/5 family robustness 保持 | 全部 6 个 family 均 **30/30** |

### 产出文件
- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sweep_results.json`
- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sensitivity_heatmap_v2.png`
- `/root/contamcal-irt-calibration/analysis/results/sensitivity_v2/sensitivity_per_family_v2.png`

Volatility check 是纯改进：修复了 Qwen-7B s123 的 Immune 误分类问题，在所有参数组合下无回退。

---
