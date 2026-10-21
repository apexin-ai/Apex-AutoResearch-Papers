# full_trace_256tok_seed42 实验分析

## Eval Metrics

| Metric | Value | 95% CI |
|--------|-------|--------|
| Accuracy | 78.82% | [76.4%, 81.0%] |
| Majority baseline | 71.5% | — |
| Lift over majority | +7.3pp | [+4.0pp, +10.7pp] |
| Pass P / R / F1 | 0.90 / 0.79 / 0.84 | — |
| Fail P / R / F1 | 0.60 / 0.79 / 0.68 | — |

## Training Summary

- Train loss: 0.1094 (3 epochs, 正常收敛)
- Training time: 3047s (~0.85h)
- Checkpoint: LoRA adapter, 154MB

## Baseline 对比 (Qwen-2.5-Coder-7B, seed42)

| Condition | Accuracy | Δ vs 256tok |
|-----------|----------|-------------|
| exception_only | 99.83% | +21.0pp |
| VOTA full | 99.41% | +20.6pp |
| full_trace (无截断) | 81.8% | +3.0pp |
| **full_trace_256tok** | **78.82%** | **baseline** |
| no_trace | 75.1% | -3.7pp |

## 结论

256 token 截断使 full_trace accuracy 从 81.8% 降至 78.82%（**-3.0pp**）。CI 上界 81.0% 未覆盖无截断的 81.8%，差异统计显著。

256tok 截断后 full_trace 仅比 no_trace (75.1%) 高 3.7pp，lift 大幅缩水（无截断时 lift 为 6.7pp）。这表明 256 tokens 不足以捕获 full_trace 中的有效信号——trace 的冗余信息被截掉的同时，关键诊断信息也丢失了。

对比 exception_only (99.83%) 的碾压性优势，进一步印证核心结论：exception events 是 verdict prediction 最高效的 trace component，full_trace 包含大量噪声，截断无法改善其 signal-to-noise ratio。

**判定: NEGATIVE** — accuracy 显著低于无截断 full_trace (81.8%)。