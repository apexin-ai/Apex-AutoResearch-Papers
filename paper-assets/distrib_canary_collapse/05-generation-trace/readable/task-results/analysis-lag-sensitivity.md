# analysis lag sensitivity

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lag_sensitivity_20260519T042654_result.json`
- **Structured JSON:** [`4f3fa76772588dd93b67.json`](../../sessions/4f/4f3fa76772588dd93b67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。三个产出文件：

**核心结论：**

| alpha | lag=1 | lag=2 | lag=3 |
|-------|-------|-------|-------|
| 0.00 | 0.0% | 0.0% | infeasible |
| 0.25 | 0.0% | 0.0% | infeasible |
| 0.50 | 8.3% (2/24) | 12.5% (3/24) | infeasible |
| **0.75** | **83.3% (20/24)** | 0.0% | infeasible |
| **1.00** | **75.0% (6/8)** | 12.5% (1/8) | infeasible |

**三点发现：**

1. **Step function 仅存在于 lag=1**：α=0.75 在 lag=1 时 sig_rate=83.3%，lag=2 直接降为 0%。因果信号是单代传播：generation t 的 canary 退化预测 generation t+1 的多样性下降，无更深时间结构。

2. **lag=3 完全不可行**：T=11 差分后 T=10，lag=3 模型有 7 个参数 vs 7 个观测点，df_resid=0，F-statistic 无定义。

3. **Perplexity 对始终非显著**：即使 α=1.00 lag=1，canary→perplexity 的 raw_p=0.58/0.80，确认 perplexity divergence 遵循不同的时间动力学。

报告含 paper-ready 1-2 句结论，见 `artifacts/lag_sensitivity/lag_sensitivity_report.md`。

---
