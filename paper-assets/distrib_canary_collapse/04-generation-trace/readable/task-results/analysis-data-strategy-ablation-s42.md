# analysis data strategy ablation s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_data_strategy_ablation_s42_20260520T083847_result.json`
- **Structured JSON:** [`41609cbfb9f0a1763c42.json`](../../sessions/41/41609cbfb9f0a1763c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

**data_strategy_ablation_s42 → DONE (success)**

| Method | accumulate | replace (baseline) | Δ |
|--------|-----------|-------------------|---|
| PermG_fwd | **0/8** | **6/8** | **-6** |
| PermG_rev | 0/8 | 0/8 | 0 |
| TY | 4/8 | 4/8 | 0 |
| K≥3 | **0/8** | **6/8** | **-6** |
| MMCT | 0.0 | 6/8 | -6 |

核心发现：accumulate 策略通过历代数据叠加将 canary drift 压平（entropy -2.4% vs -16.3%，ECE +89% vs +703%），但 downstream diversity 退化幅度不变（distinct_1 -27% vs -29%）。canary 信号被平滑→时序耦合断裂→lead-lag 检测全部失效。这证明 **数据策略是 canary early-warning 系统的关键设计选择**：replace 模式形成 Markov chain 信号放大使 canary 可检测，accumulate 模式虽减缓表观退化但掩盖了预警信号。

---
