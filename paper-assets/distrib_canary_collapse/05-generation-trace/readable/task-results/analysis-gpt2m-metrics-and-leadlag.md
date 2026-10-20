# analysis gpt2m metrics and leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2m_metrics_and_leadlag_20260515T221815_result.json`
- **Structured JSON:** [`754b3cb7f3f68337d3b7.json`](../../sessions/75/754b3cb7f3f68337d3b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。核心结果：

**Registry 已更新** — gen0/gen10 metrics + drift_pct（entropy −86.5%, ECE +4543%, perplexity +44703%, d1/d2/d3 −12~15%）。

**Lead-lag 分析关键发现：**

| | Full (T=11) | Sub (T=6) |
|---|---|---|
| Forward sig (FDR) | **6/6** | 0/6 |
| Reverse sig (FDR) | 3/6 (仅 diversity→ece) | 2/6 (不可靠, df_resid=1) |
| Forward mean f² | 66.15 | — |

- **Full window:** canary→diversity 全部显著，entropy 领先 diversity 1–2 代，ECE 领先 1 代。方向性清晰（forward f² 是 reverse 的 19×）。
- **Sub-window:** df_resid=1，Granger 完全无力。但 cross-correlation |r|>0.99，信号存在只是检验力不够。
- **GPT-2 Medium 复现了 Pythia 的 entropy-leads-diversity pattern**，支持跨架构泛化。
- Diversity 从 gen5 起 plateau（d1 从 0.0915 到 0.0914），印证 Reviewer 的判断。

报告和 JSON 结果已保存并注册（artifact `art_20260515_533dd2`）。

---
