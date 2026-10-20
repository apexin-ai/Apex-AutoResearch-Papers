# analysis rho06 binding diagnostic

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho06_binding_diagnostic_20260516T020514_result.json`
- **Structured JSON:** [`00d0a24cfe40b26db8dc.json`](../../sessions/00/00d0a24cfe40b26db8dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

## A. Binding 比例

| 指标 | ρ=0.4 | ρ=0.6 |
|------|-------|-------|
| α_eff binding | 37.2% | 32.9% |
| ESS binding | 61.0% | 65.7% |
| b\*=0 | 1.8% | 1.3% |

## B. b\* 分布

| 统计量 | ρ=0.4 | ρ=0.6 |
|--------|-------|-------|
| mean | 1.393 | 1.390 |
| median | 0.867 | 0.860 |
| p25 | 0.540 | 0.540 |
| p75 | 1.505 | 1.480 |
| p90 | 2.660 | 2.580 |

## C. α_eff 分布

| 统计量 | ρ=0.4 | ρ=0.6 |
|--------|-------|-------|
| mean | 0.651 | 0.631 |
| median | 0.734 | 0.704 |
| ESS binding 时 mean | 0.554 | 0.542 |

## 关键洞察

1. **没有质变**。binding 比例仅移动 ~4-5pp，训练全程稳定无漂移。

2. **核心问题：b\* 对 contamination 完全不敏感。** contamination 增加 50%（0.4→0.6），但 b\* 分布几乎完全相同（mean 差 0.003）。ESS 约束占主导（~65%），而 ESS binding 时 b\* 只由 ESS≥n_min=2 决定，与 ρ 无关。

3. **grid b=0.5 胜出的原因**：adaptive 的 b\* 中位数 0.86、p90 达 2.58，高 b\* 尾部（~10% batch）导致梯度方差过大。grid b=0.5 提供稳定的温和降权，在高 contamination 下反而更优。

4. **改进方向**：提高 n_min（2→2.5-3）压缩 b\* 右尾；降低 τ（0.8 在 ρ=0.6 下 ESS binding 时 α_eff 只有 0.54，形同虚设）；或直接 clamp b\*≤1.0。

报告已注册为 artifact `binding_diagnosis_rho06_vs_04`。

---
