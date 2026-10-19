# research bootstrap ci verification

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bootstrap-ci-verification_20260523T105029_result.json`
- **Structured JSON:** [`1ab170a525c0c51bef14.json`](../../sessions/1a/1ab170a525c0c51bef14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部关键数据已收集。以下是分析结论：

---

## Bootstrap CI 来源分析

### 1. Registry 值 [0.770, 0.859] 是对 `full_auroc` 做的

来自 `results/exp001/run_eval.py`（原始 eval 脚本）：
- 用 **全量数据** 计算 d_syc 方向，在全量数据上选最佳 layer/pos，得到 `full_auroc = 0.8159`
- Bootstrap 对这个 full_auroc 的 scores 重采样（**不是 CV**），n=2000, seed=42
- 得到 CI = **[0.7698, 0.8589]**，即 registry 中的 `[0.770, 0.859]`

**问题：** 这个 CI 有数据泄漏——方向和最佳层都在全量数据上选定，bootstrap 只对 scoring 做重采样，低估了不确定性。

### 2. 论文值 [0.795, 0.857] 是对 `cv_auroc_mean` 做的

来自 `analysis/bootstrap_auroc_ci.py`（后续更严格的分析脚本）：
- **Full CV bootstrap**：每次 bootstrap 重采样 181 对 pairs，重新跑完整 5-fold CV，n=2000, seed=42
- 得到 CI = **[0.7952, 0.8572]**，即论文中的 `[0.795, 0.857]`
- 这个 CI 围绕 `cv_auroc_mean = 0.827`（bootstrap mean = 0.825）

### 3. 差异原因总结

| | Registry | 论文 |
|---|---|---|
| CI | [0.770, 0.859] | [0.795, 0.857] |
| 来源指标 | full_auroc (0.816) | cv_auroc_mean (0.827) |
| Bootstrap 方法 | 重采样 scores（方向/层固定） | 重采样 pairs → 重跑整个 5-fold CV |
| n_bootstrap | 2000 | 2000 |
| 数据泄漏 | 有（train=test 选方向/层） | 无（CV 隔离） |

Registry CI 更宽（下界更低），因为 full_auroc 本身点估计更低（0.816 vs 0.827），且方向/层的 overfitting 增加了方差。

### 4. 论文应该报告哪个值

**论文值 [0.795, 0.857] 是正确的选择。** 它对应 5-fold CV AUROC，方法论上更严格（无数据泄漏），CI 通过 full CV bootstrap 计算。Registry 值应更新为 `bootstrap_ci_95: [0.795, 0.857]`，并标注 `method: full_cv_bootstrap`。

---
