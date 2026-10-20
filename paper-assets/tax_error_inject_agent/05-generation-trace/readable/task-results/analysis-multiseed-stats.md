# analysis multiseed stats

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed-stats_20260514T214124_result.json`
- **Structured JSON:** [`81ad622a791110ec150c.json`](../../sessions/81/81ad622a791110ec150c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心数据摘要：

**Clean Eval（跨种子）**
- Vanilla: 65.3% ± 3.3% （最优）
- Random: 60.7% ± 7.6%
- TaxEI: 54.2% ± 10.5% （最差）

**统计检验**
- TaxEI vs Vanilla: **-11.0%, p=0.032**（显著更差）
- TaxEI vs Random: -6.4%, p=0.24（不显著）
- Random vs Vanilla: -4.6%, p=0.30（不显著）

**Recovery Eval（seed=42）**
- 三种方法恢复率相近（59.6%-63.8%），**检测率全部为 0%**

**对 negative paper 的支撑**：TaxEI 在所有维度被否定——不仅没有提升鲁棒性，还显著损害了基础性能（p<0.05）。高方差（±10.5% vs ±3.3%）表明错误注入训练增加了不稳定性。完整报告在 `artifacts/multiseed_analysis_report.md`。

---
