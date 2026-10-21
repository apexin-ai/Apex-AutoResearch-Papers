# analysis loocv 5t model comparison

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loocv-5t-model-comparison_20260522T102815_result.json`
- **Structured JSON:** [`e2f42b5cbfb85c805e1a.json`](../../sessions/e2/e2f42b5cbfb85c805e1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### LOO-CV

| 版本 | Cells | MAE | 95% CI Coverage |
|------|-------|-----|-----------------|
| A (excl sync-dip) | 15 | 0.037 | **15/15** |
| B (含 sync-dip) | 20 | 0.203 | 16/20 |
| Seed-averaged A | 15 | 0.024 | **15/15** |

Version B 的 4 个 CI miss：2 个 sync-dip α=0.60 cell，2 个 T=10 fold（去掉 T=10 训练数据后模型低估 T=10 的检测率）。

### Model Comparison (AIC)

| 数据集 | M0 (constant) | M1 (linear) | **M2 (probit)** | M3 (exp) |
|--------|---------------|-------------|-----------------|----------|
| 16-cell | ΔAIC=66.2 | **ΔAIC=0** | ΔAIC=2.4 | **ΔAIC=0** |
| 20-cell | ΔAIC=92.5 | ΔAIC=4.2 | **ΔAIC=0** | ΔAIC=4.2 |

16-cell 上 M1/M2/M3 均 competitive（ΔAIC<4），20-cell 上 M2 胜出。M0 (无 T 依赖) 被淘汰。

### β Inference

- **Profile likelihood 95% CI: [0.24, 0.78]** — 固定 β=0.24 在 CI 内（ΔNLL=1.81 < 1.92 阈值，刚好在边界内）
- MLE: β=0.66, 对应 γ=0.76
- Bootstrap 95% CI: [0.59, 0.68]（偏窄，参数相关性导致 bootstrap 低估不确定性）

产出文件：
- `artifacts/alpha_c_theory/loocv_5t_results.json`
- `artifacts/alpha_c_theory/loocv_5t_analysis.py`
- `artifacts/alpha_c_theory/loocv_5t_summary.md`

---
