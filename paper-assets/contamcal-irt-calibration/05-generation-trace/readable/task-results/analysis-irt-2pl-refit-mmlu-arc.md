# analysis irt 2pl refit mmlu arc

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt-2pl-refit-mmlu-arc_20260516T150541_result.json`
- **Structured JSON:** [`1d1ed87fe50c5575e1ab.json`](../../sessions/1d/1d1ed87fe50c5575e1ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果汇总：

**2PL+γ Refit 效果：**

| Benchmark | Model | PPP | cal_MAE | ΔMAE | 结论 |
|-----------|-------|-----|---------|------|------|
| GSM8K (N=16) | 4PL+γ | 0.398 | 0.035 | **+0.118** | 校准有效 |
| MMLU (N=8) | 4PL+γ→**2PL+γ** | 0.006→**0.426** | 0.021→**0.002** | -0.014→**+0.006** | 修复成功 |
| ARC (N=8) | 4PL+γ→**2PL+γ** | 0.000→0.002 | 0.086→0.036 | -0.077→-0.028 | 改善但仍不合格 |

**Domain Gamma N=24 核心发现：**
- STEM_Math γ=+0.97, STEM_Science γ=+0.84（exposure 提升分数）
- Social_Sciences γ=-0.50, Humanities γ=-0.41, Medical γ=-0.20（exposure 降低分数）
- Pooled MMLU γ≈-0.26 不显著，是正负 domain 效应的混合平均

报告已注册为 artifact `art_20260516_5bafe5`，输出路径：`/root/contamcal-irt-calibration/artifacts/analysis_2pl_gamma_refit_0516.md`

---
