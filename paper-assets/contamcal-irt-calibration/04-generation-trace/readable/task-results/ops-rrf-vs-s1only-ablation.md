# ops rrf vs s1only ablation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rrf_vs_s1only_ablation_20260517T174924_result.json`
- **Structured JSON:** [`5dac6ee190b5a829350b.json`](../../sessions/5d/5dac6ee190b5a829350b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 benchmark 都完成。结果已保存到 `/root/autodl-tmp/exp006/s1_only_ablation/`。

## S1-only vs RRF 对比结果

| Bench | Method | τ | MAE | γ (mean) | 95% CI | PPP | R_hat | ESS |
|-------|--------|---|-----|----------|--------|-----|-------|-----|
| **MMLU** | RRF (baseline) | 0.731 | 0.0091 | 0.698 | [-0.42, 1.81] | 0.193 | 1.008 | 1708 |
| | **S1-only top300** | 0.674 | 0.098 | -1.934 | [-4.81, 5.80] | 0.750 | **1.532** | **7** |
| **ARC** | RRF (baseline) | 0.609 | 0.0196 | 0.727 | [0.02, 1.44] | — | — | — |
| | **S1-only top300** | 0.635 | 0.552 | **6.836** | [6.22, 7.45] | 0.000 | 1.008 | 1067 |

## 诊断

两个 S1-only 结果都不可信：

1. **MMLU**: R_hat=1.53, ESS=7 — 链未收敛。exposure 范围被压缩到 [0.749, 0.867]（top-300 by S1），变异太小导致 γ 不可识别。

2. **ARC**: 虽收敛，但 γ=6.84（饱和），MAE=0.552，PPP=0.000（完全不拟合）。exposure 范围 [0.672, 0.857] 同样过窄。

**根因**: top-300 by mean S1 把 exposure 限制在高分窄带，IRT 无法区分 θ（能力）和 γ×exposure（污染）。RRF baseline 的 random-300 subsample 保留了全 [0, 1] 的 exposure 方差，使得 γ 可识别。

这本身是有意义的 ablation 发现：RRF 融合的价值不仅在信号质量，更在于为 IRT 提供足够的 exposure 方差。

---
