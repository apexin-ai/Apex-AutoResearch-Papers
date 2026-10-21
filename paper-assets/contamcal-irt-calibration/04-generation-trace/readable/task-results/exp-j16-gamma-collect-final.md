# exp j16 gamma collect final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_j16-gamma-collect-final_20260518T034149_result.json`
- **Structured JSON:** [`bba2d9a16338af2ab147.json`](../../sessions/bb/bba2d9a16338af2ab147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 8 个 domain 的 J=16 结果和 J=13 参考数据都已收集。以下是完整对比表。

## J=16 vs J=13 Domain γ 对比表

| Domain | n_items | J=13 γ | J=13 95%CI | J=13 P(γ<0)† | J=16 γ | J=16 95%CI | J=16 P(γ<0) | PPP | Rhat | 方向一致? |
|---|---|---|---|---|---|---|---|---|---|---|
| Social_Sciences | 2000* | -0.571 | [-1.054, -0.103] | ~99.1% | **-0.627** | [-1.073, -0.192] | **99.7%** | 0.722 | 1.006 | ✓ |
| Humanities | 2000* | -0.309 | [-0.852, 0.257] | ~86% | **-0.142** | [-0.662, 0.407] | **69.7%** | 0.416 | 1.007 | ✓ |
| Business_Law | 2000* | +0.044 | [-0.497, 0.579] | ~44% | **+0.080** | [-0.414, 0.579] | **37.8%** | 0.395 | 1.007 | ✓ |
| Medical | 1640 | +0.235 | [-0.421, 0.879] | ~24% | **+0.050** | [-0.527, 0.651] | **43.6%** | 0.268 | 1.008 | ✓ |
| Other | 883 | +0.127 | [-0.612, 0.885] | ~37% | **+0.318** | [-0.440, 1.104] | **20.4%** | 0.072 | 1.008 | ✓ |
| STEM_CS_Eng | 557 | +0.497 | [-0.425, 1.397] | ~15% | **+0.320** | [-0.556, 1.206] | **24.0%** | 0.503 | 1.006 | ✓ |
| STEM_Science | 1397 | +0.504 | [-0.189, 1.202] | ~8% | **+0.566** | [-0.071, 1.203] | **4.3%** | 0.197 | 1.007 | ✓ |
| STEM_Math | 1190 | +0.499 | [-0.213, 1.203] | ~8% | **+0.596** | [-0.076, 1.247] | **3.8%** | 0.305 | 1.007 | ✓ |

*subsampled from larger pool. †J=13 P(γ<0) 为正态近似估计。

**诊断**：所有 8 个 domain Rhat < 1.01，ESS > 1200，divergence = 0，MCMC 收敛良好。

**结论**：J=16 与 J=13 方向完全一致（8/8）。Social Sciences 仍为最显著的 anti-contamination 信号，且 J=16 下更强（γ: -0.571 → -0.627，P(γ<0): ~99.1% → 99.7%，95%CI 排除零）。STEM 三域的 pro-contamination 信号在 J=16 下也略有增强（STEM_Math P(γ<0) 从 ~8% 降至 3.8%）。中间四域（Medical, Business_Law, Other, Humanities）γ 置信区间仍跨零，无显著信号。

---
