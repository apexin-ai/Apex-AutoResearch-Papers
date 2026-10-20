# analysis exp 017 llama conll n8 t07

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_017_llama_conll_n8_t07_20260515T154212_result.json`
- **Structured JSON:** [`95b2b3bd51f2f10a217a.json`](../../sessions/95/95b2b3bd51f2f10a217a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## exp_017_llama_conll_n8_t07 结果摘要

**基础指标**：greedy_f1=0.9266, oracle_f1=0.9407, n_valid=2756, parse_rate=100%

**核心发现 — correlation-selection gap 在低温下放大**：

| | rho delta (vs baseline) | AUROC delta (vs baseline) |
|---|---|---|
| 4 个 agreement 信号 (SJ/FK/VC/EM) | -0.09 | **-0.10** |
| LP | -0.02 | **-0.015** |

- Agreement 信号 AUROC 从 ~0.75 跌到 ~0.65（T=0.7 压缩了 agreement 分布，FK mean=0.956, SJ mean=0.983，区分度大幅下降）
- LP AUROC 从 0.766 仅跌到 0.751，对温度鲁棒
- LP 对 agreement 信号的 AUROC 优势从 ~0.02 扩大到 ~0.10

**结论**：**success**。Correlation-selection gap 在 T=0.7 N=8 条件下不仅存在而且放大，支持 gap 是 universal 的 claim（跨温度、样本数、模型）。Registry 已更新为 DONE，分析报告已注册为 artifact。

---
