# analysis pull round8 data for paper

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pull_round8_data_for_paper_20260515T155009_result.json`
- **Structured JSON:** [`d6f35f29bb6940452e03.json`](../../sessions/d6/d6f35f29bb6940452e03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据汇总已保存到 `artifacts/round8_analysis_data_summary.md`。关键发现：

**数据 1 — SJ Union vs Max：** 两种 normalizer 差异极小。SciERC Δρ=+0.005，CoNLL Δρ=+0.0004，可互换。

**数据 2 — Seed 456 LP Range：** seed456 median=0.040, IQR=[0.024, 0.073], tied=62.2%。与 seed42 (median=0.040, tied=60.3%) 高度一致，LP range 窄+tied fraction 高具有跨 seed 鲁棒性。

**数据 3 — Table 2 NER Selection F1 (2-seed)：** LP (+0.0020) > SJ (+0.0014) > FK (+0.0010) > Greedy > EM (−0.0077) > VC (−0.0218)。RE 部分 `selection_f1_table2.json` 仅有 NER，2-seed RE 尚未计算。已有单 seed RE 数据和 3-seed N=16 RE 数据可参考。

**RE seed 进度：** seed123 和 seed456 均已完成（May 15 23:45），但两组 RE ρ_SJ 仅 0.26-0.28，verdict 均为 FAIL。

---
