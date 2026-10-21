# analysis 4method kappa

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4method_kappa_20260525T085442_result.json`
- **Structured JSON:** [`7b65b7a454d049df6f75.json`](../../sessions/7b/7b65b7a454d049df6f75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**Reference dataset (α=1.0 GPT-2M, 16 pairs, 复现 paper κ=0.185):**

| | 5-method | 4-method (−NaiveXCor) | Δ |
|---|---|---|---|
| Fleiss' κ | **0.187** | **0.167** | **−0.02** |

排除 NaiveXCor 后 κ **略降**而非改善。原因：在 α=1.0 下 NaiveXCor 与 PermG/DiffXCorr 高度一致（pairwise Cohen κ=0.47），去掉它减少了同质投票。低 κ 的根因是 Threshold（0/16=0%）和 TY（8/16=50%）与 DiffXCorr/PermG cluster（12/16=75%）之间的系统性分歧。

**Voting 对比 (alpha sweep, 5 null seeds + 3×detection seeds):**

| Threshold | FPR (null) | TPR (α=0.50) | TPR (α=0.75) |
|---|---|---|---|
| K≥3/5 (paper) | **5.0%** | 20.8% | **29.2%** |
| K≥2/4 (majority) | 17.5% | 29.2% | 54.2% |
| K≥3/4 (supermajority) | **2.5%** | 4.2% | 8.3% |

- K≥3/4 FPR 极好 (2.5%) 但 TPR 不可用 (4-8%)
- K≥2/4 TPR 有改善但 FPR 膨胀至 17.5%
- 两种 4-method threshold 都无法 dominate paper 的 K≥3/5

**结论**: MMCT K≥3/5 已自然边缘化 NaiveXCor（最多贡献 1/5 票，单独不能造成 false positive）。移除它不改善 κ，反而损失 voting 自由度。artifact 已保存到 `artifacts/4method_kappa_analysis.json`。

---
