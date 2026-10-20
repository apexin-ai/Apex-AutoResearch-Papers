# fix exp005 noise prop

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp005_noise_prop_20260515T165913_result.json`
- **Structured JSON:** [`6c815c24ca112348bab2.json`](../../sessions/6c/6c815c24ca112348bab2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断报告：exp-005 noise_propagation_analysis

### 实际完成状态：**COMPLETED（无需重跑）**

25/25 Stan fits 全部完成，所有 Rhat < 1.01，零 divergence。代码无 bug，数据无损坏。

### 为什么 conclusion=negative

**原实验测量了错误的结果变量。** `calibrated_score` 在 exposure=0 处计算：

```
calibrated_score[i] = (1/J) Σ_j [c_j + (d_j-c_j) · logit⁻¹(a_j(θ_i - b_j))]
```

gamma 项完全不出现——所以 CI width 在数学上不依赖 σ_e。0.0997-0.1000 的"无变化"是结构性必然，不是实验失败。

### 重分析：gamma 衰减（从已有数据提取）

| σ_e | ME γ̂ | ME bias | Simple γ̂ | Simple bias | ME 优势 |
|-----|-------|---------|-----------|-------------|---------|
| 0.1 | 0.492 | -1.5% | 0.491 | -1.8% | +0.3% |
| 0.3 | 0.306 | -38.9% | 0.281 | -43.9% | +5.0% |
| 0.5 | 0.185 | -62.9% | 0.148 | -70.4% | +7.4% |
| 0.7 | 0.123 | -75.4% | 0.082 | -83.6% | +8.2% |
| 1.0 | 0.075 | -85.1% | 0.038 | -92.4% | +7.3% |

- Gamma 衰减与 σ_e 完美单调（Spearman ρ=1.0, p=0.0）
- **ME 模型在 σ_e=1.0 时保留约 2 倍的 gamma 信号**（15% vs 8%）
- 确认 ME 校正对 gamma 估计有效

### 建议下一步

- **不需要重跑**。已从现有数据提取了正确指标。
- Registry 已更新 notes，重分析结果已注册为 artifact。
- 适合作为 **appendix robustness check**：展示 ME 模型在噪声环境下对 gamma 的衰减校正能力。
- 若要在正文引用，需额外讨论：两个模型在高 σ_e 下都严重低估 gamma，需配合 SIMEX 或 bootstrap 做 bias correction。

---
