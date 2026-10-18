# analysis exp 008 bca gdn excluded

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008_bca_gdn_excluded_20260519T142112_result.json`
- **Structured JSON:** [`5f6659594c1712cfe784.json`](../../sessions/5f/5f6659594c1712cfe784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

### Part A: Bootstrap CI for LAMBADA ρ
- **Percentile 95% CI: [-1.0, -0.7]，不跨零**
- Architecture resampling (10000 次，8875 有效)，bootstrap 分布仅含两个值：ρ=-1.0 (49.4%) 和 ρ=-0.7 (50.6%)
- P(ρ > 0) = 0.000，100% 有效样本为负相关
- BCa 在 ρ=-1.0 边界退化（z0=-3.86），不适用，改用 percentile CI
- Jackknife: 排除任一架构后 ρ 仍为 -0.7 或 -1.0

### Part B: GDN-Excluded Sensitivity

| Benchmark | ρ (3 arch) | ρ (no GDN) | p (no GDN) | Direction |
|-----------|-----------|-----------|-----------|-----------|
| LAMBADA | -1.0 | -0.7 | 0.233 | WEAKER |
| HellaSwag | +0.3 | +0.5 | 0.450 | STRONGER |
| WinoGrande | +0.1 | +0.3 | 0.683 | STRONGER |
| **ARC-Easy** | **-0.7** | **-0.9** | **0.083** | **STRONGER** |
| ARC-Challenge | +0.6 | -0.2 | 0.783 | WEAKER |
| MMLU | -0.7 | +0.6 | 0.350 | WEAKER |

**ARC-Easy** 排除 GDN 后 ρ 从 -0.7 升至 -0.9（p=0.083），suggestive second anchor，但未达 0.05 显著性。LAMBADA 排除 GDN 后反而变弱（-1.0→-0.7），说明 GDN 对 LAMBADA convergence 贡献大。3 个 benchmark 变强，3 个变弱。

产出文件：
- `analysis/statistical_robustness_supplement.py`
- `analysis/robustness_supplement_summary.json`
- `analysis/robustness_supplement_gdn_excluded.csv`

---
