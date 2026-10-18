# analysis exp003 p2 data check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp003-p2-data-check_20260520T022655_result.json`
- **Structured JSON:** [`0b91edf28283508da9b5.json`](../../sessions/0b/0b91edf28283508da9b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp003_p2_data_check.md`。

核心发现：
- **Pure 模型 log_samples**: 3/3 完整（GDN/RetNet/HGRN2，各 127MB）
- **H3-1 模型 log_samples**: 2/3 — RetNet 和 HGRN2 存在，**GDN h3-1 缺失**（只有 14K 的聚合 results，无 per-example 数据）
- **分析结果**: 完整，5153 examples 覆盖 LAMBADA 全集。但 `lambada_per_example.csv` 中 GDN 用的是 **h12-1**（非 h3-1）做 hybrid baseline，可能正是因为 h3-1 log_samples 缺失
- **统计结论不变**: 三个 arch 的 helped vs hurt perplexity 差异均不显著（p=0.21/0.66/0.25）

如果要求三个 arch 统一用 h3-1 对比，需补跑 GDN h3-1 的 `--log_samples` eval。

---
