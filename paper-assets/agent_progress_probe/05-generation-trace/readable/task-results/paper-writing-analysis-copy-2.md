# paper writing analysis

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_analysis_20260514T215456_result.json`
- **Structured JSON:** [`e4c9681bfced07c72247.json`](../../sessions/e4/e4c9681bfced07c72247.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`analysis.tex` 已写入并注册。~500 词，4 个段落，所有数字追溯到 registry：

| 段落 | 关键数据 | Registry 来源 |
|------|----------|--------------|
| Circular evaluation | structural 0.9951, OH 0.967 | `non-nlp-baseline`, `cross-agent-structural` |
| TLM failure | TWV-MV 88.5%, flip 14.1%, downstream −2.57pp, σ narrow range | `temporal-label-model`, `tlm-probe-comparison`, `twv-ablation` |
| Error analysis | 131 errors (7.2%), 85 FP (64.9%), prob 0.922, conflict 39.7% vs 31% | `error-analysis` |
| OB holdout | 0.770±0.022 vs 0.847 (−7.7pp), coverage −33.5%, 100% agreement | `outcome-bp-3seed`, `train-without-ob` |

---
