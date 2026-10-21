# analysis gpt2m kappa

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2m_kappa_20260515T230642_result.json`
- **Structured JSON:** [`6bf2ca2003d5b2616127.json`](../../sessions/6b/6bf2ca2003d5b2616127.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| | Pythia-410M | GPT-2m |
|---|---|---|
| Fleiss' κ (all 12 pairs) | 0.185 | **0.091** |
| Mean Cohen's κ (all pairwise) | — | 0.200 |
| Interpretation | Slight | Slight |

两个架构都在 "slight agreement" 范围（κ < 0.20），确认低一致性是 5 方法面板在短时间序列下的结构性属性，非 Pythia 特定。

根因：Naive xcorr 永远判 sig（12/12），TY Granger 永远判 not-sig（0/12），这两个极端方法拉低了整体 κ。排除退化对后，3 个信息性方法（Diff、Onset、Perm.G）的平均 κ = 0.667（substantial agreement）。

报告已写入 `artifacts/gpt2m_kappa/kappa_report.md` 并注册。

---
