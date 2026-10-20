# code exp 012 error propagation

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_012_error_propagation_20260521T223117_result.json`
- **Structured JSON:** [`0d6e38c306437339e26c.json`](../../sessions/0d/0d6e38c306437339e26c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，全流程通过。结果：

| σ | θ-RMSE | Δ% | c_n-RMSE | Δ% | θ-τ | c_n-corr |
|---|--------|-----|----------|-----|-----|----------|
| 0.0 | 0.2078 | baseline | 0.5832 | baseline | 0.884 | 0.832 |
| 0.5 | 0.3005 | +44.6% | 0.9393 | +61.1% | 0.814 | 0.624 |

**汇报：**

- **代码路径**: `/root/gated_mfrm_judge_bias/exp012/run_exp012.py`
- **行数**: ~230 行
- **文件列表**: `run_exp012.py`, `error_propagation.csv`, `summary.csv`, `error_propagation.png`, `cn_degradation.png`
- **Dry-run 输出**: 4 fits × ~25s = 110s 总时间，全部指标正常计算，summary 表和两张图正常生成
- **Dry-run 观察**: σ=0.5 导致 θ-RMSE 退化 +44.6%，c_n-RMSE 退化 +61.1%——噪声传播效应显著

**全量运行预估**:
- Dry-run (chains=2, warmup=200, samples=400): ~25s/fit
- 全量 (chains=4, warmup=2000, samples=4000): 约 10× 更长 → ~250s/fit
- 80 fits × 250s = ~5.6 小时 (CPU only)
- 如安装 CUDA jaxlib，预估可缩短到 1-2 小时

---
