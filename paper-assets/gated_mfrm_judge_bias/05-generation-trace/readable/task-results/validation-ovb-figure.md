# validation ovb figure

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validation_ovb-figure_20260525T205104_result.json`
- **Structured JSON:** [`2d429b894cf06455e1e6.json`](../../sessions/2d/2d429b894cf06455e1e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CPU run complete.

```
OVB r=0.86: MISMATCH  实际=0.7949 (CPU) / 0.7950 (GPU), 数据源=generate_paper_figures.py::generate_ovb_scatter_data(), 参数=N=50/I=100/J=8/rho=0.6/n_seeds=20
```

**结论**：

- CPU 和 GPU 后端结果一致：**r = 0.7949**（1000 个数据点，20 seeds）
- 论文 caption 标注 r = 0.86，**实际值偏离 0.065**
- 代码自初始提交以来未变更（仅 1 个 commit）
- `generate_paper_figures.py` 中 `plot_fig2_ovb_bias()` 调用 `generate_ovb_scatter_data()` 使用默认参数 `N=50, I=100, J=8, rho=0.6, n_seeds=20`
- 运行中的 r 值在 0.795-0.845 之间波动（依 seed 而定），最终收敛于 ~0.795

**可能原因**：caption 中的 0.86 可能来自早期某个版本的代码/参数（如更高的 rho 或不同的 n_seeds），但当前代码无法复现该值。需要更新 caption 为 r ≈ 0.79。

---
