# ssh trace plots ppc

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_trace_plots_ppc_20260522T213844_result.json`
- **Structured JSON:** [`a4b474b05e06e1b23dd9.json`](../../sessions/a4/a4b474b05e06e1b23dd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部生成成功。结果汇总：

**Trace plots (5 个)**
| 文件 | 大小 |
|------|------|
| `trace_cn.pdf` — 8 个模型的 $c_n$ | 6.2 MB |
| `trace_dj.pdf` — 9 个 judges 的 $d_j$ | 6.6 MB |
| `trace_sigma_c.pdf` — 全局参数 $\sigma_c$ | 757 KB |
| `trace_theta.pdf` — 4 个选定模型的 $\theta_n$ | 3.0 MB |
| `trace_b.pdf` — 6 个选定 items 的 $b_i$（高/中/低 difficulty） | 4.4 MB |

**Forest plots (2 个)**
| 文件 | 大小 |
|------|------|
| `forest_cn.pdf` — $c_n$ 排序 + 94% CI | 23 KB |
| `forest_dj.pdf` — $d_j$ 排序 + 94% CI | 25 KB |

**PPC**: 跳过，InferenceData 中无 `posterior_predictive` group（原始 MCMC 未保存 predictive samples）。

所有 PDF 保存在 `/root/gated_mfrm_judge_bias/artifacts/exp003b_diagnostics/`，总计 ~21 MB。每个 trace plot 包含左侧 4-chain trace 和右侧 KDE 密度图。

---
